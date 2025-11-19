from tensorflow.keras.models import load_model as keras_load_model
from catboost import CatBoostRegressor
import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

feature_ranges = {
    'carat': (0.2, 5.01),
    'cut': (0,4),
    'color': (0,6),
    'clarity': (0,7),
    'depth': (43.0,79.0),
    'table': (43.0,95.0),
    'x': (3.73,10.74),
    'y': (3.68,58.9),
    'z': (1.07,31.8)
}

@st.cache_data
def load_data(dataset_path):
    return pd.read_csv(dataset_path)

def validate_input(values):
    for feature, (min_val, max_val) in feature_ranges.items():
        if not (min_val <= values[feature] <= max_val):
            return False, f"Некорректное значение для {feature}"
    return True, ""

cut_mapping = {'Ideal':0, 'Premium':1, 'Very Good':2, 'Good':3, 'Fair':4}
color_mapping = {'D':0, 'E':1, 'F':2, 'G':3, 'H':4, 'I':5, 'J':6}
clarity_mapping = {'I1':7, 'SI2':6, 'SI1':5, 'VS2':4, 'VS1':3, 'VVS2':2, 'VVS1':1, 'IF':0}

def load_model(model_name):
    try:
        if 'Cat' in model_name:
            model_path = MODELS_DIR / f"{model_name}.cbm"
            return CatBoostRegressor().load_model(str(model_path))
        elif 'Neural' in model_name:
            model_path = MODELS_DIR / f"{model_name}.keras"
            return keras_load_model(str(model_path))
        else:
            model_path = MODELS_DIR / f"{model_name}.pkl"
            with open(model_path, "rb") as f:
                return pickle.load(f)
    except Exception as e:
        st.error(f"Ошибка загрузки модели {model_name}: {str(e)}")
        return None
    

# Страница 1: О разработчике
def page_developer():
    st.title("Информация о разработчике")
    col1, col2 = st.columns([1,3])
    
    with col1:
        st.image(str(DATA_DIR / "photo.jpg"), width=200)
    
    with col2:
        st.header("Изгородин Илья Юрьевич")
        st.subheader("Группа: ФИТ-232")
        st.write("Тема РГР: Разработка Web-приложения")


# Страница 2: О наборе данных
def page_dataset():
    st.title("Описание набора данных")
    st.header("Предметная область")
    st.write("""Набор данных содержит информацию о характеристиках алмазов и их рыночной стоимости.
Используется для построения моделей машинного обучения, предсказывающих цену алмазов.""")
    
    st.header("Описание признаков")
    features = pd.DataFrame([
        ["carat", "Вес алмаза (1 карат = 0.2 г)", "числовой"],
        ["cut", "Качество огранки", "категориальный"],
        ["color", "Цвет алмаза", "категориальный"],
        ["clarity", "Чистота алмаза", "категориальный"],
        ["depth", "Глубина алмаза", "числовой"],
        ["table", "Ширина площадки", "числовой"],
        ["price", "Цена в долларах", "числовой"],
        ["x", "Длина (мм)", "числовой"],
        ["y", "Ширина (мм)", "числовой"],
        ["z", "Высота (мм)", "числовой"]
    ], columns=["Признак", "Описание", "Тип"])
    
    st.table(features)
    
    st.header("Предобработка данных")
    st.write("""1. Удаление нулевых значений в x, y, z
2. Замена пропусков модой
3. Преобразование категориальных признаков
4. Обработка выбросов
5. Корректировка типов данных""")


# Страница 3: Визуализации
def page_visualizations():
    st.title("Визуализации данных")

    # Диаграмма рассеяния
    st.subheader("Диаграмма рассеяния")
    st.image(str(DATA_DIR / "plot_2.png"), 
            caption="Зависимость цены алмаза от веса (карат)",
            use_container_width=True)
    st.write("""
    **Анализ:** Четко прослеживается положительная зависимость между весом алмаза (карат) и его ценой. 
    При этом видно несколько кластеров, что может указывать на разные ценовые категории 
    в зависимости от других характеристик (огранки, чистоты и цвета).
    """)

    # Матрица корреляций
    st.subheader("Матрица корреляций")
    st.image(str(DATA_DIR / "plot_1.png"), 
            caption="Тепловая карта корреляций между параметрами алмазов",
            use_container_width=True)
    st.write("""
    **Анализ:** Наибольшая корреляция наблюдается между:
    - Весом (карат) и физическими размерами (x, y, z)
    - Весом и ценой (ожидаемо)
    - Размерами между собой (x, y, z)

    Слабая корреляция между остальными признаками указывает на их меньшую линейную значимость для ценообразования.
    """)

    # 3D визуализация данных
    st.subheader("3D представление: Карат vs Размеры vs Ширина площадки")
    st.image(str(DATA_DIR / "plot_4.png"), 
            caption="3D зависимость между весом (карат), длиной (x) и шириной площадки (table)",
            use_container_width=True)
    st.write("""
    **Анализ:** На 3D-графике четко прослеживается:
    1. Основная масса алмазов сосредоточена в области:
    - Вес: 0.2-2.5 карата
    - Длина (x): 3-8 мм
    - Ширина площадки: 50-65%

    2. Крупные алмазы (свыше 3 карат) демонстрируют:
    - Нелинейный рост физических размеров
    - Больший разброс параметра table (ширины площадки)

    3. Наблюдаются редкие выбросы среди небольших алмазов с аномально высокими значениями table.
    """)

    # Распределение цены
    st.subheader("Распределение цены")
    st.image(str(DATA_DIR / "plot_3.png"), 
            caption="Гистограмма распределения цен на алмазы",
            use_container_width=True)
    st.write("""
    **Анализ:** Распределение цен имеет правостороннюю асимметрию с большим количеством алмазов 
    в диапазоне 0-1000$ и постепенным уменьшением частоты для более дорогих экземпляров. 
    Это типично для рынка драгоценных камней, где крупные высококачественные алмазы встречаются редко.
    """)

# Страница 4: Предсказание
def page_prediction():
    st.title("Предсказание стоимости алмаза")

    available_models = {
        "Decision Tree": "DecisionTree",
        "Gradient Boosting": "GradientBoost", 
        "CatBoost": "CatBoost",
        "Bagging": "Bagging",
        "Stacking": "Stacking",
        "Neural Network": "NeuralNet"
    }

    st.header("1. Выбор модели")
    selected_model_name = st.selectbox(
        "Выберите модель для предсказания",
        options=list(available_models.keys()))

    st.header("2. Загрузка данных")
    input_method = st.radio(
        "Способ ввода данных",
        ["Загрузка CSV-файла", "Ручной ввод параметров"])
    
    if input_method == "Загрузка CSV-файла":
        uploaded_file = st.file_uploader("Загрузите CSV-файл с данными алмазов", type="csv")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.write("Первые 5 строк файла:")
            st.dataframe(df.head())
            
            if st.button("Предсказать для файла"):
                try:
                    model = load_model(available_models[selected_model_name])
                    predictions = model.predict(df)
                    df['predicted_price'] = predictions
                    
                    st.success("Предсказание выполнено успешно!")
                    st.dataframe(df[['predicted_price']].style.format({'predicted_price': "${:,.2f}"}))

                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Скачать результаты",
                        data=csv,
                        file_name='diamond_predictions.csv',
                        mime='text/csv')
                    
                except Exception as e:
                    st.error(f"Ошибка при предсказании: {str(e)}")
    
    else:
        st.subheader("Введите параметры алмаза")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            carat = st.number_input("Карат", min_value=0.2, max_value=5.01, value=1.0)
            depth = st.number_input("Глубина", min_value=43.0, max_value=79.0, value=60.0)
            table = st.number_input("Ширина площадки", min_value=43.0, max_value=95.0, value=55.0)
        
        with col2:
            cut = st.selectbox("Огранка", options=list(cut_mapping.keys()))
            color = st.selectbox("Цвет", options=list(color_mapping.keys()))
            clarity = st.selectbox("Чистота", options=list(clarity_mapping.keys()))
        
        with col3:
            x = st.number_input("Длина (x)", min_value=3.73, max_value=10.74, value=5.0)
            y = st.number_input("Ширина (y)", min_value=3.68, max_value=58.9, value=5.0)
            z = st.number_input("Высота (z)", min_value=1.07, max_value=31.8, value=3.0)
        
        if st.button("Рассчитать стоимость"):
            try:
                input_data = {
                    'carat': carat,
                    'cut': cut_mapping[cut],
                    'color': color_mapping[color],
                    'clarity': clarity_mapping[clarity],
                    'depth': depth,
                    'table': table,
                    'x': x,
                    'y': y,
                    'z': z
                }

                is_valid, message = validate_input(input_data)
                if not is_valid:
                    st.error(message)
                    return

                model = load_model(available_models[selected_model_name])

                input_df = pd.DataFrame([input_data])

                prediction = model.predict(input_df)
                if selected_model_name=="Neural Network":
                    price = float(prediction[0][0])
                else:
                    price = float(prediction[0])

                st.success(f"Прогнозируемая стоимость алмаза ({selected_model_name}): ${price:,.2f}")

                with st.expander("Показать сырые данные"):
                    st.json(input_data)
                
            except Exception as e:
                st.error(f"Ошибка при предсказании: {str(e)}")
                st.error("Убедитесь, что все модели существуют")


# Конфигурация страницы
st.set_page_config(page_title="Diamond Price Prediction", layout="wide")

pages = {
    "О разработчике": page_developer,
    "О наборе данных": page_dataset,
    "Визуализации": page_visualizations,
    "Предсказание цены": page_prediction
}

st.sidebar.title("Навигация")
page = st.sidebar.radio("Выберите страницу:", list(pages.keys()))
pages[page]()
