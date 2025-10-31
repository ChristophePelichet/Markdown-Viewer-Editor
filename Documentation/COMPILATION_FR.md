### Cloner le dépôt
git clone https://github.com/ChristophePelichet/markdown-viewer-editor.git
cd markdown-viewer-editor

### Installation
```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### Utilisation
```bash
# Méthode 1 : Lanceur batch (recommandé)
launch_markdown_viewer.bat

# Méthode 2 : Ligne de commande
python markdown_viewer.py
```

### Compilation en exécutable

Pour compiler l'application en exécutable portable :

```bash
# Activer l'environnement virtuel
.venv\Scripts\activate

# Compiler avec PyInstaller
pyinstaller markdown_viewer.spec

# L'exécutable sera dans : dist\MarkdownViewer.exe
```

Pour plus de détails sur la compilation, consultez **[BUILD_INSTRUCTIONS.md](Documentation/BUILD_INSTRUCTIONS.md)**