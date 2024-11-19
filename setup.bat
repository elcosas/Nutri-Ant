@echo off
setlocal enabledelayedexpansion
python -m venv .venv
call .venv\Scripts\activate.bat
.venv\Scripts\python -m pip install -r requirements.txt
endlocal
