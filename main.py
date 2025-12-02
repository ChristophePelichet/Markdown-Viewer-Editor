"""
Markdown Viewer & Editor - Markdown file viewer and editor tool
Version: v1.0.1
Author: Christophe Pelichet
"""

import sys
import os
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QSplitter, QFileDialog, QMessageBox,
    QLabel, QComboBox, QToolBar, QStatusBar
)
from PySide6.QtCore import Qt, QSize, QSettings
from PySide6.QtGui import QIcon, QFont, QTextCursor, QAction
from PySide6.QtWebEngineWidgets import QWebEngineView

try:
    import markdown
    from markdown.extensions import tables, fenced_code, toc, codehilite
    MARKDOWN_AVAILABLE = True
except ImportError:
    MARKDOWN_AVAILABLE = False
    print("⚠️ Module 'markdown' non installé. Installez-le avec: pip install markdown")


class MarkdownViewer(QMainWindow):
    """Main window for Markdown viewer/editor"""
    
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.modified = False
        
        # Configuration to remember preferences (works even when compiled)
        self.settings = QSettings("ChristophePelichet", "MarkdownViewerEditor")
        
        # Timer for automatic refresh (avoids refreshing on every keystroke)
        from PySide6.QtCore import QTimer
        self.refresh_timer = QTimer()
        self.refresh_timer.setSingleShot(True)
        self.refresh_timer.setInterval(500)  # 500ms delay
        self.refresh_timer.timeout.connect(self.refresh_preview)
        
        self.init_ui()
        self.load_quick_files()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("📝 Markdown Viewer & Editor - v1.0.1")
        self.setMinimumSize(1200, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Quick selection bar
        quick_layout = QHBoxLayout()
        quick_label = QLabel("📂 Fichier rapide :")
        quick_label.setStyleSheet("font-weight: bold;")
        quick_layout.addWidget(quick_label)
        
        self.quick_combo = QComboBox()
        self.quick_combo.setMinimumWidth(300)
        self.quick_combo.currentTextChanged.connect(self.load_quick_file)
        quick_layout.addWidget(self.quick_combo)
        
        quick_layout.addStretch()
        
        # View buttons
        view_label = QLabel("📐 Vue :")
        view_label.setStyleSheet("font-weight: bold; margin-left: 20px;")
        quick_layout.addWidget(view_label)
        
        split_btn = QPushButton("⬌ Split")
        split_btn.setToolTip("Vue divisée (éditeur + prévisualisation)")
        split_btn.clicked.connect(lambda: self.splitter.setSizes([600, 600]))
        quick_layout.addWidget(split_btn)
        
        editor_btn = QPushButton("✏️ Éditeur")
        editor_btn.setToolTip("Vue éditeur uniquement")
        editor_btn.clicked.connect(lambda: self.splitter.setSizes([1200, 0]))
        quick_layout.addWidget(editor_btn)
        
        preview_btn = QPushButton("👁️ Aperçu")
        preview_btn.setToolTip("Vue prévisualisation uniquement")
        preview_btn.clicked.connect(lambda: self.splitter.setSizes([0, 1200]))
        quick_layout.addWidget(preview_btn)
        
        quick_layout.addSpacing(20)
        
        # Refresh button
        refresh_btn = QPushButton("🔄 Actualiser")
        refresh_btn.clicked.connect(self.refresh_preview)
        quick_layout.addWidget(refresh_btn)
        
        layout.addLayout(quick_layout)
        
        # Main splitter (editor | preview)
        self.splitter = QSplitter(Qt.Horizontal)
        
        # Editor area
        editor_widget = QWidget()
        editor_layout = QVBoxLayout(editor_widget)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        
        self.editor = QTextEdit()
        self.editor.setFont(QFont("Consolas", 11))
        self.editor.setLineWrapMode(QTextEdit.WidgetWidth)
        self.editor.setPlaceholderText("✏️ Editor - Type or open a Markdown file...")
        self.editor.textChanged.connect(self.on_text_changed)
        editor_layout.addWidget(self.editor)
        
        self.splitter.addWidget(editor_widget)
        
        # Preview area
        preview_widget = QWidget()
        preview_layout = QVBoxLayout(preview_widget)
        preview_layout.setContentsMargins(0, 0, 0, 0)
        
        if MARKDOWN_AVAILABLE:
            self.preview = QWebEngineView()
            
            # Connecter le signal loadFinished pour restaurer la position de scroll
            self.preview.loadFinished.connect(self.on_load_finished)
            self.saved_scroll_pos = 0
            
            # Initialiser avec une page d'accueil
            welcome_html = """
            <html>
            <head>
                <style>
                    body {
                        font-family: 'Segoe UI', 'Segoe UI Emoji', Tahoma, Geneva, Verdana, sans-serif;
                        padding: 40px;
                        text-align: center;
                        color: #666;
                        background: #ffffff;
                        margin: 0;
                        height: 100vh;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                    }
                    h1 { 
                        color: #333; 
                        margin-bottom: 20px;
                        font-size: 2em;
                    }
                    p { 
                        margin: 10px 0; 
                        line-height: 1.6;
                        font-size: 1.1em;
                    }
                    .hint { 
                        background: #e8f4f8; 
                        padding: 20px; 
                        border-radius: 8px; 
                        margin-top: 30px;
                        border: 2px solid #0366d6;
                    }
                    .hint strong {
                        color: #0366d6;
                        font-size: 1.2em;
                    }
                </style>
            </head>
            <body>
                <div>
                    <h1>&#128196; Prévisualisation Markdown</h1>
                    <p>Ouvrez un fichier Markdown ou sélectionnez un fichier rapide ci-dessus.</p>
                    <p>La prévisualisation s'affichera automatiquement ici.</p>
                    <div class="hint">
                        <p><strong>&#9000; Raccourcis clavier :</strong></p>
                        <p>Ctrl+O : Ouvrir | Ctrl+S : Sauvegarder | Ctrl+F : Rechercher</p>
                    </div>
                </div>
            </body>
            </html>
            """
            self.preview.setHtml(welcome_html)
            # Forcer le fond blanc du widget
            self.preview.setStyleSheet("background-color: white;")
        else:
            self.preview = QTextEdit()
            self.preview.setReadOnly(True)
            self.preview.setPlainText("Module 'markdown' non installé. Installez-le avec: pip install markdown")
            
        preview_layout.addWidget(self.preview)
        
        self.splitter.addWidget(preview_widget)
        
        # 50/50 ratio
        self.splitter.setSizes([600, 600])
        
        layout.addWidget(self.splitter)
        
        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.update_status("Ready")
        
        # Toolbar (after editor creation)
        self.create_toolbar()
        
    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = QToolBar("Outils")
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)
        
        # Open
        open_action = QAction("📂 Ouvrir", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)
        
        # Save
        save_action = QAction("💾 Sauvegarder", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)
        
        toolbar.addSeparator()
        
        # Undo
        undo_action = QAction("↶ Annuler", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.editor.undo)
        toolbar.addAction(undo_action)
        
        # Redo
        redo_action = QAction("↷ Refaire", self)
        redo_action.setShortcut("Ctrl+Y")
        redo_action.triggered.connect(self.editor.redo)
        toolbar.addAction(redo_action)
        
        toolbar.addSeparator()
        
        # Find
        find_action = QAction("🔍 Rechercher", self)
        find_action.setShortcut("Ctrl+F")
        find_action.triggered.connect(self.find_text)
        toolbar.addAction(find_action)
        
        toolbar.addSeparator()
        
        # Markdown help
        help_action = QAction("❓ Aide Markdown", self)
        help_action.triggered.connect(self.show_markdown_help)
        toolbar.addAction(help_action)
        
    def load_quick_files(self):
        """Load the list of quick files (CHANGELOG, README)"""
        base_path = Path(__file__).parent
        
        quick_files = []
        
        # Search for CHANGELOG and README files
        patterns = ['CHANGELOG*.md', 'README*.md']
        folders = [
            base_path / 'Documentation',
            base_path,
        ]
        
        for folder in folders:
            if folder.exists():
                for pattern in patterns:
                    for file in folder.glob(pattern):
                        rel_path = file.relative_to(base_path)
                        quick_files.append((str(rel_path), str(file)))
        
        # Trier par nom
        quick_files.sort(key=lambda x: x[0])
        
        # Add to combo
        self.quick_combo.addItem("-- Sélectionnez un fichier --", "")
        for display, full_path in quick_files:
            self.quick_combo.addItem(display, full_path)
            
    def load_quick_file(self, text):
        """Load a file from quick selection"""
        if text == "-- Sélectionnez un fichier --":
            return
            
        file_path = self.quick_combo.currentData()
        if file_path:
            self.load_file(file_path)
            
    def open_file(self):
        """Open a Markdown file"""
        if self.modified:
            reply = QMessageBox.question(
                self,
                "Fichier modifié",
                "Le fichier a été modifié. Voulez-vous sauvegarder avant d'ouvrir un autre fichier ?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            
            if reply == QMessageBox.Yes:
                self.save_file()
            elif reply == QMessageBox.Cancel:
                return
        
        # Get last used path or use Documents directory as default
        default_path = str(Path.home() / "Documents")
        last_path = self.settings.value("last_directory", default_path)
        
        # Debug: display retrieved path
        print(f"[DEBUG] Last path: {last_path}")
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Ouvrir un fichier Markdown",
            last_path,
            "Markdown Files (*.md);;All Files (*.*)"
        )
        
        if file_path:
            # Sauvegarder le répertoire du fichier ouvert
            new_dir = str(Path(file_path).parent)
            print(f"[DEBUG] Sauvegarde du chemin: {new_dir}")
            self.settings.setValue("last_directory", new_dir)
            self.settings.sync()  # Forcer la synchronisation
            self.load_file(file_path)
            
    def load_file(self, file_path):
        """Load file content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            self.editor.setPlainText(content)
            self.current_file = file_path
            self.modified = False
            
            # Sauvegarder le répertoire du fichier chargé
            new_dir = str(Path(file_path).parent)
            print(f"[DEBUG] load_file - Sauvegarde du chemin: {new_dir}")
            self.settings.setValue("last_directory", new_dir)
            self.settings.sync()  # Forcer la synchronisation
            
            self.update_title()
            self.update_status(f"Fichier chargé : {Path(file_path).name}")
            self.refresh_preview()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Erreur de lecture",
                f"Impossible de lire le fichier :\n{str(e)}"
            )
            
    def save_file(self):
        """Save the current file"""
        if not self.current_file:
            self.save_file_as()
            return
            
        try:
            with open(self.current_file, 'w', encoding='utf-8') as f:
                f.write(self.editor.toPlainText())
                
            self.modified = False
            self.update_title()
            self.update_status(f"Fichier sauvegardé : {Path(self.current_file).name}")
            
            QMessageBox.information(
                self,
                "Sauvegarde réussie",
                f"Le fichier a été sauvegardé :\n{self.current_file}"
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Erreur de sauvegarde",
                f"Impossible de sauvegarder le fichier :\n{str(e)}"
            )
            
    def save_file_as(self):
        """Save with a new name"""
        # Récupérer le dernier chemin utilisé ou utiliser le répertoire Documents par défaut
        default_path = str(Path.home() / "Documents")
        last_path = self.settings.value("last_directory", default_path)
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Sauvegarder sous",
            last_path,
            "Markdown Files (*.md);;All Files (*.*)"
        )
        
        if file_path:
            # Sauvegarder le répertoire du fichier sauvegardé
            self.settings.setValue("last_directory", str(Path(file_path).parent))
            self.current_file = file_path
            self.save_file()
            
    def on_text_changed(self):
        """Called when text is modified"""
        self.modified = True
        self.update_title()
        # Restart timer for automatic refresh (with delay)
        self.refresh_timer.start()
        
    def refresh_preview(self):
        """Refresh the preview"""
        if not MARKDOWN_AVAILABLE:
            self.preview.setPlainText(self.editor.toPlainText())
            return
            
        content = self.editor.toPlainText()
        
        # Save scroll position before refreshing
        def save_scroll_position():
            scroll_js = "document.documentElement.scrollTop || document.body.scrollTop;"
            self.preview.page().runJavaScript(scroll_js, self.on_scroll_saved)
        
        save_scroll_position()
        
        # Convert Markdown to HTML
        html = markdown.markdown(
            content,
            extensions=[
                'tables',
                'fenced_code',
                'toc',
                'codehilite',
                'nl2br'
            ]
        )
        
        # CSS for rendering
        css = """
        <style>
            body {
                font-family: 'Segoe UI', 'Segoe UI Emoji', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                padding: 20px;
                max-width: 900px;
                margin: 0 auto;
                background: #ffffff;
                color: #333;
            }
            h1, h2, h3, h4, h5, h6 {
                margin-top: 24px;
                margin-bottom: 16px;
                font-weight: 600;
                line-height: 1.25;
            }
            h1 { font-size: 2em; border-bottom: 2px solid #eaecef; padding-bottom: 0.3em; }
            h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
            h3 { font-size: 1.25em; }
            h4 { font-size: 1em; }
            code {
                background: #f6f8fa;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 0.9em;
            }
            pre {
                background: #f6f8fa;
                padding: 16px;
                border-radius: 6px;
                overflow-x: auto;
            }
            pre code {
                background: none;
                padding: 0;
            }
            blockquote {
                border-left: 4px solid #0366d6;
                padding-left: 16px;
                margin-left: 0;
                color: #6a737d;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                margin: 16px 0;
            }
            table th, table td {
                border: 1px solid #dfe2e5;
                padding: 8px 13px;
            }
            table th {
                background: #f6f8fa;
                font-weight: 600;
            }
            table tr:nth-child(2n) {
                background: #f6f8fa;
            }
            ul, ol {
                padding-left: 2em;
            }
            li {
                margin: 0.25em 0;
            }
            a {
                color: #0366d6;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            hr {
                border: none;
                border-top: 2px solid #eaecef;
                margin: 24px 0;
            }
        </style>
        """
        
        full_html = f"<html><head>{css}</head><body>{html}</body></html>"
        self.preview.setHtml(full_html)
    
    def on_scroll_saved(self, scroll_pos):
        """Callback after saving scroll position"""
        self.saved_scroll_pos = scroll_pos if scroll_pos else 0
        
    def on_load_finished(self, ok):
        """Called when page is loaded - restores scroll position"""
        if ok and hasattr(self, 'saved_scroll_pos') and self.saved_scroll_pos > 0:
            restore_js = f"window.scrollTo(0, {self.saved_scroll_pos});"
            self.preview.page().runJavaScript(restore_js)
        
    def find_text(self):
        """Simple text search"""
        from PySide6.QtWidgets import QInputDialog
        
        text, ok = QInputDialog.getText(
            self,
            "Rechercher",
            "Texte à rechercher :"
        )
        
        if ok and text:
            cursor = self.editor.textCursor()
            cursor.movePosition(QTextCursor.Start)
            self.editor.setTextCursor(cursor)
            
            if self.editor.find(text):
                self.update_status(f"Texte trouvé : {text}")
            else:
                self.update_status(f"Texte non trouvé : {text}")
                QMessageBox.information(
                    self,
                    "Recherche",
                    f"Le texte '{text}' n'a pas été trouvé."
                )
                
    def show_markdown_help(self):
        """Display Markdown help"""
        help_text = """
<h2>📝 Guide rapide Markdown</h2>

<h3>Titres</h3>
<pre>
# Titre 1
## Titre 2
### Titre 3
</pre>

<h3>Formatage du texte</h3>
<pre>
**gras** ou __gras__
*italique* ou _italique_
***gras et italique***
`code inline`
~~barré~~
</pre>

<h3>Listes</h3>
<pre>
- Élément 1
- Élément 2
  - Sous-élément
  
1. Premier
2. Deuxième
3. Troisième
</pre>

<h3>Liens et images</h3>
<pre>
[Texte du lien](https://example.com)
![Texte alternatif](image.png)
</pre>

<h3>Citations</h3>
<pre>
> Ceci est une citation
> Sur plusieurs lignes
</pre>

<h3>Code</h3>
<pre>
```python
def hello():
    print("Hello World!")
```
</pre>

<h3>Tableaux</h3>
<pre>
| Colonne 1 | Colonne 2 |
|-----------|-----------|
| Données 1 | Données 2 |
</pre>

<h3>Séparateur</h3>
<pre>
---
</pre>

<h3>Emojis</h3>
<pre>
✅ ❌ ⚠️ 📝 🔧 🌐 📚 🎯
</pre>
        """
        
        msg = QMessageBox(self)
        msg.setWindowTitle("Aide Markdown")
        msg.setTextFormat(Qt.RichText)
        msg.setText(help_text)
        msg.exec()
        
    def update_title(self):
        """Met à jour le titre de la fenêtre"""
        title = "📝 Markdown Viewer & Editor"
        if self.current_file:
            title += f" - {Path(self.current_file).name}"
        if self.modified:
            title += " *"
        self.setWindowTitle(title)
        
    def update_status(self, message):
        """Met à jour la barre d'état"""
        self.statusBar.showMessage(message)
        
    def closeEvent(self, event):
        """Appelé à la fermeture de la fenêtre"""
        if self.modified:
            reply = QMessageBox.question(
                self,
                "Fichier modifié",
                "Le fichier a été modifié. Voulez-vous sauvegarder avant de quitter ?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            
            if reply == QMessageBox.Yes:
                self.save_file()
                event.accept()
            elif reply == QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    
    # Modern style
    app.setStyle('Fusion')
    
    viewer = MarkdownViewer()
    viewer.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
