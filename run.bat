@echo off
echo Starting Raster to Lucide Converter...

:: Check if the virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo [!] Error: Virtual environment not found. 
    echo Please make sure the 'venv' folder exists in this directory.
    pause
    exit /b
)

:: Activate the environment
call venv\Scripts\activate.bat

:: Run the Python script
python main.py

:: Keep the window open if the app crashes or is closed
pause