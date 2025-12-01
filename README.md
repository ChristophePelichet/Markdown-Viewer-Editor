# 📝 Markdown Viewer & Editor

**📥 [Download version v0.100](https://github.com/ChristophePelichet/Markdown-Viewer-Editor/releases/tag/v0.100)**

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
- ✅ **Remember last directory** : Automatically opens the last folder you used

### Quick Files
- ✅ **Quick selection** : Dropdown list of CHANGELOG and README files
- ✅ **Auto-detection** : Automatic search in Documentation/ and root
- ✅ **Relative display** : Relative paths for better readability

## 🚀 Installation & Usage

### Using the Compiled Executable

1. Download the latest release from GitHub
2. Extract the archive
3. Run `markdown_viewer.exe`

### Using the Source Code

For detailed compilation and setup instructions, see:
- 📗 **[Build Instructions](Documentation/BUILD_INSTRUCTIONS_EN.md)** - Complete setup guide
- 📗 **[Compilation Guide](Documentation/COMPILATION_EN.md)** - Detailed compilation steps

**Quick start:**
```bash
# Clone the repository
git clone https://github.com/ChristophePelichet/Markdown-Viewer-Editor.git
cd Markdown-Viewer-Editor

# Create virtual environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python markdown_viewer.py
```

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+O** | Open file |
| **Ctrl+S** | Save |
| **Ctrl+Z** | Undo |
| **Ctrl+Y** | Redo |
| **Ctrl+F** | Search |

## 📚 Built-in Markdown Help

The application includes a quick Markdown guide accessible via the "❓ Markdown Help" button:

### Syntax Examples
- **Headings** : `# H1`, `## H2`, `### H3`
- **Bold** : `**text**` or `__text__`
- **Italic** : `*text*` or `_text_`
- **Code** : `` `inline code` ``
- **Lists** : `- item` or `1. item`
- **Links** : `[text](url)`
- **Blockquotes** : `> quote`
- **Tables** : `| Col 1 | Col 2 |`

## 💾 Saving

### Automatic Confirmation
- ✅ Before opening another file
- ✅ Before closing the application
- ✅ Clear message with options: Yes / No / Cancel

### Modification Indicator
- The window title displays an asterisk (*) if the file is modified
- Example: `📝 Markdown Viewer & Editor - README.md *`

## 🎨 Preview Style

HTML rendering uses a professional style inspired by GitHub:

- ✅ **Typography** : Segoe UI, 1.6 line height
- ✅ **Headings** : With bottom borders (H1, H2)
- ✅ **Code** : Light gray background, monospace font
- ✅ **Tables** : Borders, alternating rows
- ✅ **Blockquotes** : Blue left border
- ✅ **Links** : GitHub blue color (#0366d6)
- ✅ **Max width** : 900px for optimal reading

## 🔧 Technical Details

### Built With
- **Python 3.13**
- **PySide6 6.10.0** - Qt6 for Python (GUI framework)
- **Markdown 3.9** - Markdown to HTML conversion
- **PyInstaller 6.16.0** - Executable compilation

### Architecture
- Modern Qt6-based GUI application
- Real-time Markdown to HTML conversion
- QSettings for persistent preferences
- WebEngine for professional HTML rendering

## 🔮 Roadmap

### Planned Features
- [ ] HTML/PDF export
- [ ] Markdown toolbar (bold, italic buttons, etc.)
- [ ] Dark/light mode themes
- [ ] Search and replace
- [ ] Multiple open files (tabs)
- [ ] Local image preview
- [ ] Spell checking
- [ ] Automatic table of contents
- [ ] User preferences dialog
- [ ] Recent files history
- [ ] Markdown plugins support
- [ ] Auto-completion
- [ ] Drag & drop support

## 📄 License

Open-source project - Markdown Viewer & Editor

## 👤 Author

**Christophe Pelichet**

GitHub: [@ChristophePelichet](https://github.com/ChristophePelichet)

---

**Version** : v0.100  
**Date** : October 31, 2025  
**Status** : ✅ Operational
