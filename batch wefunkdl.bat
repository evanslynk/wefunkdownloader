@echo off
set /p min="Show number Min? "
set /p max="Show number Max? "

for /l %%i in (%min%,1,%max%) do (
    python wefunkdl.py %%i
)
pause