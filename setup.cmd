@echo off

REM Set the virtual environment name and Python version
set VENV_NAME=myenv
set PYTHON_VERSION=3.9.0

REM Create and activate the virtual environment
echo Creating virtual environment %VENV_NAME%...
python -m venv %VENV_NAME%
call %VENV_NAME%\Scripts\activate.bat

REM Update pip and install necessary modules
echo Installing Pygame...
python -m pip install --upgrade pip
python -m pip install pygame

REM Deactivate the virtual environment
echo Done installing modules.
deactivate
