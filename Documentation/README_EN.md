# 📝 Markdown Viewer & Editor

> **[🇫🇷 Version française](../README.md)** | 🇬🇧 English version

Markdown file viewing and editing tool with real-time preview.

## 🎯 Features

### Viewing
- ✅ **Real-time preview** : HTML rendering of Markdown with professional CSS
- ✅ **Split view** : Editor on the left, preview on the right
- ✅ **Full Markdown support** : Tables, code, blockquotes, lists, links, images
- ✅ **Syntax highlighting** : For code blocks
- ✅ **Emojis** : Full Unicode emoji support

### Editing
- ✅ **Monospace editor** : Consolas font for better readability
- ✅ **Undo/Redo** : Ctrl+Z / Ctrl+Y
- ✅ **Search** : Ctrl+F to search text
- ✅ **Change detection** : Asterisk (*) in title if modified
- ✅ **Confirmation before closing** : If the file has been modified

### Quick Files
- ✅ **Quick selection** : Dropdown list of CHANGELOG and README files
- ✅ **Auto-detection** : Automatic search in Documentation/ and root
- ✅ **Relative display** : Relative paths for better readability

## 🚀 Usage

### Method 1: Batch launcher (Recommended)
```batch
launch_markdown_viewer.bat
```

The script:
1. Automatically activates the virtual environment
2. Installs the `markdown` module if necessary
3. Launches the application

### Method 2: Command line
```bash
# Activate virtual environment
.venv\Scripts\activate

# Install markdown if necessary
pip install markdown

# Launch application
python markdown_viewer.py
```

## 📋 Interface

```
┌─────────────────────────────────────────────────────────────────────┐
│ 📂 Open  💾 Save  ↶ Undo  ↷ Redo  🔍 Search                        │
├─────────────────────────────────────────────────────────────────────┤
│ 📂 Quick file: [CHANGELOG_FR.md ▼]               🔄 Refresh        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────────────┬───────────────────────────────────────┐  │
│  │  ✏️ Editor            │  👁️ Preview                          │  │
│  ├──────────────────────┼───────────────────────────────────────┤  │
│  │ # Title              │  Title                                 │  │
│  │                      │  ═════                                 │  │
│  │ **Bold** *Italic*    │  Bold Italic                          │  │
│  │                      │                                        │  │
│  │ - List 1             │  • List 1                             │  │
│  │ - List 2             │  • List 2                             │  │
│  │                      │                                        │  │
│  │ ```python            │  def hello():                         │  │
│  │ def hello():         │      print("Hello!")                  │  │
│  │     print("Hello!")  │                                        │  │
│  │ ```                  │                                        │  │
│  │                      │                                        │  │
│  └──────────────────────┴───────────────────────────────────────┘  │
│                                                                       │
├─────────────────────────────────────────────────────────────────────┤
│ File loaded: CHANGELOG_FR.md                                        │
└─────────────────────────────────────────────────────────────────────┘
```

## ⌨️ Keyboard shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+O** | Open file |
| **Ctrl+S** | Save |
| **Ctrl+Z** | Undo |
| **Ctrl+Y** | Redo |
| **Ctrl+F** | Search |

## 📚 Built-in Markdown help

The application includes a quick Markdown guide accessible via the "❓ Markdown Help" button:

### Syntax examples
- **Headings** : `# H1`, `## H2`, `### H3`
- **Bold** : `**text**` or `__text__`
- **Italic** : `*text*` or `_text_`
- **Code** : `` `inline code` ``
- **Lists** : `- item` or `1. item`
- **Links** : `[text](url)`
- **Blockquotes** : `> quote`
- **Tables** : `| Col 1 | Col 2 |`

## 🔧 Dependencies

### Required
- **PySide6** : Qt graphical interface
- **PySide6-WebEngine** : HTML display in Qt
- **markdown** : Markdown → HTML conversion

### Installation
```bash
pip install PySide6 PySide6-WebEngine markdown
```

Or via `requirements.txt`:
```bash
pip install -r requirements.txt
```

## 📁 Automatically detected files

The tool automatically searches for these files:

### Documentation/
- `CHANGELOG_FR.md`
- `CHANGELOG_EN.md`
- `CHANGELOG_DE.md`
- `README_FR.md`
- `README_EN.md`
- `README_DE.md`
- All `*.md` files

### Project root
- `CHANGELOG.md`
- `README.md`
- All `*.md` files

## 💾 Saving

### Automatic confirmation
- ✅ Before opening another file
- ✅ Before closing the application
- ✅ Clear message with options: Yes / No / Cancel

### Modification indicator
- The window title displays an asterisk (*) if the file is modified
- Example: `📝 Markdown Viewer & Editor - CHANGELOG_FR.md *`

## 🎨 Preview style

HTML rendering uses a professional style inspired by GitHub:

- ✅ **Typography** : Segoe UI, 1.6 line height
- ✅ **Headings** : With bottom borders (H1, H2)
- ✅ **Code** : Light gray background, monospace font
- ✅ **Tables** : Borders, alternating rows
- ✅ **Blockquotes** : Blue left border
- ✅ **Links** : GitHub blue color (#0366d6)
- ✅ **Max width** : 900px for optimal reading

## 🐛 Troubleshooting

### Module 'markdown' not installed
```bash
pip install markdown
```

### Encoding error
The file uses UTF-8 by default. Make sure your Markdown files are in UTF-8.

### Preview not displaying
1. Check that `PySide6-WebEngine` is installed
2. Check that the `markdown` module is installed
3. Click "🔄 Refresh" to force rendering

### Virtual environment not found
Make sure the `.venv/Scripts/activate.bat` file exists:
```bash
python -m venv .venv
```

## 📝 Typical usage

### 1. Edit CHANGELOG
1. Launch tool: `launch_markdown_viewer.bat`
2. Select "CHANGELOG_FR.md" from dropdown
3. Edit content in left panel
4. See real-time rendering on the right
5. Save: **Ctrl+S** or "💾 Save" button

### 2. Create new document
1. Write Markdown content in editor
2. Save with new name: Menu → Save as
3. File is automatically added to quick list (if CHANGELOG or README)

### 3. Search in document
1. **Ctrl+F** or "🔍 Search" button
2. Enter text to search
3. Editor positions at first occurrence

## 🔮 Possible future improvements

- [ ] PDF export from preview
- [ ] Markdown toolbar (bold, italic buttons, etc.)
- [ ] Dark / light mode
- [ ] Search and replace
- [ ] Multiple open files support (tabs)
- [ ] Local image preview
- [ ] Spell checking
- [ ] Automatic table of contents generation

## 📄 License

Part of the Markdown Viewer & Editor project.

## 👤 Author

**Christophe Pelichet**

---

**Version** : v0.100  
**Date** : October 31, 2025  
**Status** : ✅ Operational
