@REM
@REM MHD visualization running in windows.
@REM

@REM local env setting
setlocal
set "VISIT_PATH=C:\\Users\\hinhi\\AppData\\VisIt\\LLNL\\VisIt 3.0.2\\lib\\site-packages"
set "VISIT_EXEC_PATH=C:\\Users\\hinhi\\AppData\\VisIt\\LLNL\\VisIt 3.0.2"
set "PLOTS_PATH=.\plots"
set "CAMERA_PATH=.\camera"

set PATH=%PATH%;%VISIT_PATH%;%VISIT_EXEC_PATH%;%PLOTS_PATH%;%CAMERA_PATH%
set PYTHONPATH=%PYTHONPATH%;%VISIT_PATH%;%VISIT_EXEC_PATH%;%PLOTS_PATH%;%CAMERA_PATH%

@REM run the script.
python ./src/main.py