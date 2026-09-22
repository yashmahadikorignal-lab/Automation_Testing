@echo off

cd /d "%~dp0"

Framework\Scripts\python.exe -m pytest -v -s Test_cases --browser=edge --headless

pause