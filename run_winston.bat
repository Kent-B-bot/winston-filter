@echo off
title Winston Filter Dashboard Launcher
start cmd /k "uvicorn main:app --reload"
timeout /t 3 /nobreak >nul
start cmd /k "python -m streamlit run app.py"
start http://localhost:8501