# 📋 Version History (CHANGELOG)

**Project:** Markdown Viewer & Editor  
**Author:** Christophe Pelichet  
**Current Version:** v0.100

---

## [0.100] - October 31, 2025

### 🎉 Initial Release

#### ✨ New Features
- **Markdown Viewer** : Real-time preview with professional HTML rendering
- **Integrated Editor** : Text editor with monospace font (Consolas)
- **Split View** : Simultaneous display of editor and preview
- **Quick Files** : Fast selection of CHANGELOG and README files
- **Complete Markdown Support** :
  - Headings (H1 to H6)
  - Formatting (bold, italic, strikethrough)
  - Lists (ordered and unordered)
  - Tables with formatting
  - Code blocks with syntax highlighting
  - Blockquotes
  - Links and images
  - Unicode emojis
  - Horizontal rules

#### 🛠️ Editing Features
- **Undo/Redo** : Complete history support (Ctrl+Z / Ctrl+Y)
- **Text Search** : Built-in search function (Ctrl+F)
- **Modification Detection** : Visual indicator (*) in title
- **Smart Save** : Confirmation before closing if unsaved changes
- **Keyboard Shortcuts** : Full support for standard keyboard shortcuts

#### 🎨 User Interface
- **Modern Theme** : Fusion interface with professional styling
- **Complete Toolbar** : Quick access to main functions
- **Status Bar** : Display of status information
- **Professional CSS** : Markdown rendering with GitHub-like style
- **View Modes** : Switch between split, editor only, or preview only

#### 📚 Documentation
- **Built-in Markdown Help** : Quick guide to Markdown syntax
- **Complete README** : Detailed user documentation
- **Batch Launcher** : Automatic launch script with environment management

#### ⚙️ Technical
- **Python 3.x** : Developed with modern Python
- **PySide6** : Qt6 graphical interface
- **markdown** : Markdown to HTML conversion
- **Markdown Extensions** : Support for tables, fenced code, TOC, syntax highlighting
- **Virtual Environment** : Dependency isolation

---

## 📝 Release Notes

### Requirements
- Python 3.8 or higher
- PySide6 (Qt6 for Python)
- markdown module with extensions

### Installation
```bash
# Create virtual environment
python -m venv .venv

# Activate environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage
```bash
# Method 1: Batch launcher (recommended)
launch_markdown_viewer.bat

# Method 2: Command line
python markdown_viewer.py
```

---

## 🔮 Future Versions

### Version 0.2 (planned)
- [ ] HTML export
- [ ] PDF export
- [ ] Color themes
- [ ] User preferences
- [ ] Recent files history

### Version 0.3 (planned)
- [ ] Markdown plugins support
- [ ] Markdown auto-completion
- [ ] Image preview
- [ ] Drag & drop support

---

**Symbol Legend:**
- ✨ New feature
- 🛠️ Improvement
- 🐛 Bug fix
- 🔒 Security
- 📚 Documentation
- ⚙️ Technical
- 🎨 User interface
