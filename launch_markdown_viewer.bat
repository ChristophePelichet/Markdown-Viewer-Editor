@echo off
REM Lanceur pour le Markdown Viewer & Editor
REM Version: v0.100
REM Auteur: Christophe Pelichet

echo ========================================
echo  Markdown Viewer ^& Editor - v0.100
echo ========================================
echo.

REM Activer l'environnement virtuel
if exist ".venv\Scripts\activate.bat" (
    echo Activation de l'environnement virtuel...
    call .venv\Scripts\activate.bat
) else (
    echo ERREUR: Environnement virtuel non trouve!
    pause
    exit /b 1
)

REM Vérifier si markdown est installé
python -c "import markdown" 2>nul
if errorlevel 1 (
    echo.
    echo Le module 'markdown' n'est pas installe.
    echo Installation en cours...
    echo.
    python -m pip install markdown
    echo.
)

REM Lancer l'application
echo Lancement du Markdown Viewer...
echo.
python markdown_viewer.py

pause
