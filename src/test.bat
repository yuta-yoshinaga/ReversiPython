@echo off
echo UNIT TEST RUN
echo.
echo ReversiAnzTest
python -m test.ReversiAnzTest
echo.
echo ReversiHistoryTest
python -m test.ReversiHistoryTest
echo.
echo ReversiPointTest
python -m test.ReversiPointTest
echo.
echo ReversiSettingTest
python -m test.ReversiSettingTest
echo.
echo ReversiTest
python -m test.ReversiTest
echo.
echo ReversiPlayTest
python -m test.ReversiPlayTest
echo.
pause
