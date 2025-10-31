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

## 🚀 Using the Source Code

### Installation and Setup

To use the project from source, refer to the compilation guides:

- 📗 **[Compilation guide (English)](COMPILATION_EN.md)** - Detailed instructions in English
- 📘 **[Guide de compilation (Français)](COMPILATION_FR.md)** - Instructions détaillées en français

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

Open-source project - Markdown Viewer & Editor

## 👤 Author

**Christophe Pelichet**

---

**Version** : v0.100  
**Date** : October 31, 2025  
**Status** : ✅ Operational
