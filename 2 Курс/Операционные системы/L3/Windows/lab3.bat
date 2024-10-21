@echo off

set program="program.exe"

start "" %program%
timeout /t 3 /nobreak >nul

start "" %program%
timeout /t 3 /nobreak >nul

start "" %program%

