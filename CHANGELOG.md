# 📋 Version History (CHANGELOG)

**Project:** Markdown Viewer & Editor  
**Author:** Christophe Pelichet  
**Current Version:** v1.0.1

---

## [1.0.1] - December 2, 2025

### 🐛 Bug Fixes
- **Preview Scroll Position** : Fixed issue where preview window would scroll to top after each edit
  - Preview now maintains scroll position when editing content
  - Implemented JavaScript-based scroll position saving and restoration
  - Improves editing experience when working on long documents
- **Emoji Display** : Fixed emoji rendering in preview window
  - Added Segoe UI Emoji font support
  - Converted HTML emojis to numeric entities for better compatibility
  - Ensures consistent emoji display across all Windows versions

### ⚡ Performance Improvements
- **Executable Size Optimization** : Optimized compiled .exe size (~200MB)
  - Extended module exclusion list (asyncio, jupyter, tornado, etc.)
  - Enhanced Qt binaries filtering (removed unused Qt modules)
  - Optimized QtWebEngine locales (EN-US and FR-FR only)
  - Filtered redundant Windows API sets and MSVC libraries
  - Aggressive DLL filtering to remove unnecessary dependencies

---

## [1.0] - December 1, 2025

### 🎉 First Production Release

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
- **Remember Last Directory** : Application remembers the last folder used for file operations

#### 🎨 User Interface
- **Modern Theme** : Fusion interface with professional styling
- **Complete Toolbar** : Quick access to main functions
- **Status Bar** : Display of status information
- **Professional CSS** : Markdown rendering with GitHub-like style
- **View Modes** : Switch between split, editor only, or preview only

#### 📚 Documentation
- **Built-in Markdown Help** : Quick guide to Markdown syntax

---

**Symbol Legend:**
- ✨ New feature
- 🛠️ Improvement
- 🐛 Bug fix
- 🔒 Security
- 📚 Documentation
- ⚙️ Technical
- 🎨 User interface
