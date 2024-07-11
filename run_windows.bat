@echo off
REM Check if wt.exe exists in the path
where wt.exe >nul 2>&1

IF %ERRORLEVEL% EQU 0 (
    REM wt.exe found, run the Python script using wt.exe
    wt.exe python jubilant_formatter.py
) ELSE (
    REM wt.exe not found, fallback to cmd.exe
    cmd.exe /c python jubilant_formatter.py
)
pause