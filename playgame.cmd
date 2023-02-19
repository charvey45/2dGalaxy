@echo off

REM Set the virtual environment name
set VENV_NAME=myenv

REM Activate the virtual environment
echo Activating virtual environment %VENV_NAME%...
call %VENV_NAME%\Scripts\activate.bat

REM Start the game
echo Starting game...
python main.py

REM Deactivate the virtual environment
echo Game finished.
deactivate
