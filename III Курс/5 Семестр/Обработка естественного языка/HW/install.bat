@echo off
chcp 65001 >nul
call ..\..\venv\Scripts\Activate
call pip install -r requirements.txt
pause
