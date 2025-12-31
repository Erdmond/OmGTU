@echo off
chcp 65001 >nul
call ..\..\venv\Scripts\activate.bat
start "API" cmd /k "py API.py"
timeout /t 3 /nobreak >nul
start "Web" cmd /k "streamlit run app.py"
