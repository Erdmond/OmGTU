import streamlit as st
import requests
import time

st.set_page_config(page_title="Конституция РФ - Чат", layout="wide")
st.title("🤖 Конституция РФ - Поиск по статьям")

with st.sidebar:
    st.header("⚙️ Настройки")
    
    api_url = st.text_input("URL API", "http://localhost:8000")
    top_k = st.slider("Количество статей для ответа", 1, 10, 3)
    
    if st.button("🔄 Проверить соединение"):
        try:
            resp = requests.get(f"{api_url}/health", timeout=5)
            if resp.status_code == 200:
                st.success("✅ API работает")
            else:
                st.error(f"❌ Ошибка: {resp.status_code}")
        except:
            st.error("❌ API недоступен")
    
    st.markdown("---")
    st.markdown("**📋 Примеры вопросов:**")
    
    examples = [
        "Какие права есть у человека?",
        "Кто является главой государства?",
        "Что такое местное самоуправление?",
        "Какие виды собственности существуют?",
        "Кто осуществляет правосудие?",
        "Что гарантирует социальное государство?"
    ]
    
    for example in examples:
        if st.button(example, key=example):
            st.session_state.query = example

col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_input(
        "💬 Ваш вопрос по Конституции:",
        placeholder="Например: Какие права имеет гражданин РФ?",
        key="query_input"
    )

with col2:
    st.write("")
    st.write("")
    submit = st.button("🔍 Найти ответ", type="primary", use_container_width=True)

if submit or ('query' in st.session_state and st.session_state.query):
    if not query and 'query' in st.session_state:
        query = st.session_state.query
    
    if not query:
        st.warning("⚠️ Введите вопрос")
    else:
        with st.spinner("🔎 Ищем ответ в Конституции..."):
            try:
                start_time = time.time()
                
                response = requests.post(
                    f"{api_url}/ask",
                    json={"query": query, "top_k": top_k},
                    timeout=3000
                )
                
                if response.status_code == 200:
                    data = response.json()
                    elapsed = time.time() - start_time

                    st.success(f"✅ Ответ найден за {elapsed:.1f} сек")
                    st.markdown("---")
                    
                    st.subheader("📝 Ответ:")
                    st.markdown(f'<div style="padding:20px;border-radius:10px;border-left:5px solid #4CAF50;">{data["answer"]}</div>', 
                               unsafe_allow_html=True)

                    with st.expander(f"📚 Источники ({len(data['sources'])} статей)", expanded=True):
                        cols = st.columns(2)
                        
                        for idx, source in enumerate(data['sources']):
                            with cols[idx % 2]:
                                st.info(f"**{source}**")

                    with st.expander("🔍 Детали поиска"):
                        st.write(f"**Всего найдено статей:** {len(data['relevant_articles'])}")
                        
                        for article in data['relevant_articles']:
                            score = article.get('rerank_score', article.get('score', 0))
                            st.markdown(f"""
                            **Статья {article['article']}** (релевантность: `{score:.3f}`)
                            ```
                            {article['preview']}
                            ```
                            """)
                
                elif response.status_code == 404:
                    st.error("❌ Не найдено релевантных статей")
                else:
                    st.error(f"❌ Ошибка API: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Не удалось подключиться к API")
                st.info("Убедитесь, что API сервер запущен: `python API.py`")
            except requests.exceptions.Timeout:
                st.error("⏱️ Таймаут запроса. Попробуйте позже.")
            except Exception as e:
                st.error(f"❌ Ошибка: {str(e)}")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 14px;">
    Система использует RAG-архитектуру: поиск по статьям Конституции РФ → реранкинг → генерация ответа LLM
</div>
""", unsafe_allow_html=True)
