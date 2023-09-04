@echo off
setlocal

set "current_dir=%~dp0"
set "bot_script=%current_dir%bot.py"
set "python_exe=%current_dir%venv\Scripts\python.exe"
%python_exe% %bot_script%

endlocal