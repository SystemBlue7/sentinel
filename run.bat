@echo off
cd /d %~dp0

echo ===============================
echo      INICIANDO SENTINEL
echo ===============================

python -m app.main

pause