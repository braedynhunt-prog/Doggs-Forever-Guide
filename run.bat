@echo off
setlocal
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python 3 was not found on PATH. Install it from python.org ^(tick "Add python.exe to PATH"^) and run this again.
  pause
  exit /b 1
)
echo.
echo === WoW Forever Alliance Quest Atlas ===
echo This refetches every zone, quest and NPC page from wowhead.com/forever at about one page per second.
echo Expect 30-45 minutes. Leave the window open; progress is also written to scrape.log.
echo.
if exist raw (
  echo Clearing the old page cache so everything is fetched fresh...
  rmdir /s /q raw
)
python scrape.py
if errorlevel 1 (
  echo scrape.py failed - see scrape.log
  pause
  exit /b 1
)
python scrape.py reparse
python build_report.py
if errorlevel 1 (
  echo build_report.py failed
  pause
  exit /b 1
)
echo.
echo Done. Open forever-alliance-quest-atlas.local.html in a browser to view it.
echo To update the published artifact, send forever-alliance-quest-atlas.html to Claude in the Wow Classic Vanilla project.
pause
