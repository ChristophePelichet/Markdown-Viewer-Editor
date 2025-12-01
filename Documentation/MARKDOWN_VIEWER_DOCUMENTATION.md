# 📘 Markdown Viewer & Editor - Complete Documentation

**Project:** Markdown Viewer & Editor  
**Version:** v0.100  
**Author:** Christophe Pelichet  
**Date:** December 1, 2025

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Installation & Setup](#installation--setup)
4. [Building & Compilation](#building--compilation)
5. [Development Workflow](#development-workflow)
6. [Technical Details](#technical-details)
7. [Troubleshooting](#troubleshooting)

---

## Project Overview

Markdown Viewer & Editor is a desktop application for viewing and editing Markdown files with real-time HTML preview. Built with Python and PySide6 (Qt6), it provides a professional Markdown editing experience with a split-view interface.

### Key Features

- ✅ **Real-time preview** : HTML rendering with professional CSS
- ✅ **Split view** : Editor and preview side-by-side
- ✅ **Full Markdown support** : Tables, code, blockquotes, lists, links, images
- ✅ **Syntax highlighting** : For code blocks
- ✅ **Quick files** : Dropdown list of CHANGELOG and README files
- ✅ **Persistent preferences** : Remembers last used directory
- ✅ **Keyboard shortcuts** : Standard shortcuts (Ctrl+O, Ctrl+S, etc.)

### Target Audience

- Technical writers
- Developers writing documentation
- Anyone working with Markdown files
- GitHub/GitLab users

---

## Project Structure

### File Tree

```
Markdown-Viewer-Editor/
├── .gitignore                          # Git ignore configuration
├── .venv/                              # Python virtual environment
│   ├── Scripts/                        # Executables (python, pip, activate)
│   └── Lib/                            # Installed Python libraries
├── Documentation/                      # Project documentation
│   ├── BUILD_INSTRUCTIONS_EN.md       # Build instructions
│   ├── COMPILATION_EN.md              # Compilation guide
│   └── PROJECT_STRUCTURE.md           # Project structure (this file)
├── markdown_viewer.py                 # Main source code (651 lines)
├── markdown_viewer.spec               # PyInstaller configuration
├── README.md                          # Main documentation
├── CHANGELOG.md                       # Version history
└── requirements.txt                   # Python dependencies

After compilation:
├── build/                              # Temporary build files
└── dist/                               # Final executable
    └── markdown_viewer.exe            # Compiled application (~150-250 MB)
```

### Main Files Description

#### `markdown_viewer.py`
**Type:** Python source code  
**Lines:** 651  
**Description:** Main application with PySide6 interface  

**Key Components:**
- `MarkdownViewer` class : Main window (QMainWindow)
- `init_ui()` : UI initialization
- `create_toolbar()` : Toolbar creation
- `load_quick_files()` : Auto-detect CHANGELOG/README files
- `open_file()` : File opening with directory persistence
- `load_file()` : File loading
- `save_file()` / `save_file_as()` : File saving
- `refresh_preview()` : Markdown to HTML conversion
- `find_text()` : Text search
- `show_markdown_help()` : Built-in Markdown guide

#### `requirements.txt`
**Type:** Dependency list  
**Content:**
```
PySide6>=6.10.0        # Qt6 GUI framework
markdown>=3.9.0        # Markdown to HTML conversion
pyinstaller>=6.16.0    # Executable compilation
```

#### `markdown_viewer.spec`
**Type:** PyInstaller configuration  
**Mode:** OneFile (single portable executable)  
**Options:**
- `console=False` : No console window (GUI only)
- Excluded modules to reduce size
- UPX compression enabled
- Windows version information

### Code Statistics

| Component | Lines | Size | Description |
|-----------|-------|------|-------------|
| Python code | 651 | ~30 KB | Main application |
| Spec file | 36 | ~1 KB | Build configuration |
| Documentation | ~1500 | ~100 KB | All docs combined |

### Dependencies

| Module | Version | Size | Purpose |
|--------|---------|------|---------|
| PySide6 | 6.10.0 | ~240 MB | Qt6 GUI framework |
| markdown | 3.9 | ~107 KB | Markdown conversion |
| PyInstaller | 6.16.0 | ~1.4 MB | Executable compilation |

---

## Installation & Setup

### Prerequisites

- **Python** : 3.8 or higher (tested with 3.13)
- **Operating System** : Windows 10/11 (64-bit)
- **Git** : For cloning the repository

### Step 1: Clone the Repository

```bash
git clone https://github.com/ChristophePelichet/Markdown-Viewer-Editor.git
cd Markdown-Viewer-Editor
```

### Step 2: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate environment (PowerShell)
.venv\Scripts\Activate.ps1

# Or activate (cmd)
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```powershell
# Install all requirements
pip install -r requirements.txt

# Verify installation
pip list
```

Expected output:
```
Package      Version
------------ -------
PySide6      6.10.0
markdown     3.9
PyInstaller  6.16.0
```

### Step 4: Run the Application

```powershell
# Make sure virtual environment is activated
python markdown_viewer.py
```

---

## Building & Compilation

### Method 1: Using the .spec File (Recommended)

```powershell
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Compile with the .spec file
pyinstaller markdown_viewer.spec --clean
```

The executable will be generated in: `dist\markdown_viewer.exe`

### Method 2: Direct Command Line

```powershell
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Compile in onefile mode
pyinstaller --onefile --noconsole --name="markdown_viewer" markdown_viewer.py
```

### Build Options

#### OneFile Mode (Current Configuration)
- ✅ **Advantage** : Single .exe file, easy to distribute
- ⚠️ **Disadvantage** : Slightly slower startup (~2-3 seconds)
- 📦 **Size** : ~150-250 MB (due to Qt6 and WebEngine)

#### OneDir Mode (Alternative)
- ✅ **Advantage** : Faster startup
- ⚠️ **Disadvantage** : Complete folder structure to distribute
- 📦 **Size** : Same total size, but spread across multiple files

To switch to OneDir mode, modify the `.spec` file:
```python
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,  # Change to True for OneDir
    # ... rest of configuration
)
```

### Size Optimization

#### 1. UPX Compression
UPX is already enabled in the .spec file. To install UPX:

```powershell
# Download UPX from https://upx.github.io/
# Extract to a folder
# Add to system PATH
```

#### 2. Excluding Unnecessary Modules
The .spec file already excludes common large modules that aren't needed.

#### 3. Reducing Dependencies
Only essential modules are imported. The application uses:
- PySide6 (required for GUI)
- markdown (required for conversion)
- Standard library modules only

### Testing the Executable

#### Before Distribution

1. **Functional Test**:
   ```powershell
   .\dist\markdown_viewer.exe
   ```

2. **Verification Checklist**:
   - [ ] Application launches without errors
   - [ ] File opening works and remembers directory
   - [ ] Saving works
   - [ ] Markdown preview displays correctly
   - [ ] Quick files are detected (CHANGELOG, README)
   - [ ] All toolbar buttons work
   - [ ] Keyboard shortcuts work (Ctrl+O, Ctrl+S, etc.)
   - [ ] Search function works (Ctrl+F)
   - [ ] Undo/Redo works (Ctrl+Z, Ctrl+Y)
   - [ ] Help dialog displays

3. **Clean Machine Test**:
   - Test on a machine **without Python installed**
   - Verify all dependencies are embedded
   - Check that preferences persist (QSettings)

### Pre-Release Checklist

- [ ] Version number updated in all files
- [ ] CHANGELOG.md updated with latest changes
- [ ] README.md reflects current features
- [ ] All functional tests passed
- [ ] OneFile compilation successful
- [ ] Executable size is acceptable
- [ ] Clean machine test passed
- [ ] Documentation up to date
- [ ] Debug messages removed or disabled

---

## Development Workflow

### Initial Setup

```powershell
# 1. Clone repository
git clone https://github.com/ChristophePelichet/Markdown-Viewer-Editor.git
cd Markdown-Viewer-Editor

# 2. Create virtual environment
python -m venv .venv

# 3. Activate environment
.venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt
```

### Daily Development

```powershell
# 1. Activate environment
.venv\Scripts\Activate.ps1

# 2. Create feature branch
git checkout -b feature/your-feature-name

# 3. Run in development mode
python markdown_viewer.py

# 4. Make changes and test
# Edit code, test frequently

# 5. Commit changes
git add .
git commit -m "feat: Your feature description"

# 6. Push to GitHub
git push origin feature/your-feature-name
```

### Testing Cycle

1. **Development Testing**:
   ```powershell
   python markdown_viewer.py
   ```

2. **Build Testing**:
   ```powershell
   pyinstaller markdown_viewer.spec --clean
   .\dist\markdown_viewer.exe
   ```

3. **Feature Testing**:
   - Test all existing features still work
   - Test new features thoroughly
   - Test edge cases and error handling

### Code Style

- **PEP 8** compliance for Python code
- **Docstrings** for all classes and methods
- **Type hints** where beneficial
- **Comments** for complex logic
- **Meaningful variable names**

---

## Technical Details

### Architecture

```
┌─────────────────────────────────────┐
│   QMainWindow (MarkdownViewer)      │
├─────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  │
│  │   QTextEdit │  │ QWebEngineView│ │
│  │   (Editor)  │  │  (Preview)    │ │
│  └─────────────┘  └──────────────┘  │
│                                     │
│  ┌─────────────────────────────┐   │
│  │      QToolBar               │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │      QStatusBar             │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### Key Technologies

1. **PySide6 (Qt6)**
   - Cross-platform GUI framework
   - Native look and feel
   - Rich widget set
   - Excellent documentation

2. **QtWebEngine**
   - Chromium-based web engine
   - Full HTML/CSS rendering
   - Supports modern web standards

3. **Python Markdown**
   - Pure Python Markdown parser
   - Extensible architecture
   - Extensions: tables, fenced_code, toc, codehilite

4. **QSettings**
   - Cross-platform settings storage
   - Windows: Registry (HKEY_CURRENT_USER)
   - Automatic persistence

### Data Flow

```
User Input → QTextEdit → Markdown Parser → HTML → QWebEngineView → Display
                ↓
            QSettings (remember directory)
```

### File Operations

1. **Open File**:
   - Retrieve last directory from QSettings
   - Show QFileDialog with last directory
   - Load file content
   - Save new directory to QSettings
   - Update preview

2. **Save File**:
   - Check if file path exists
   - If not, show Save As dialog
   - Write content to file
   - Update window title

### Compatibility

- **Windows** : 10, 11 (64-bit)
- **Python** : 3.8+ (tested with 3.13)
- **Qt** : PySide6 6.10.0 (Qt 6.x)

---

## Troubleshooting

### Common Issues

#### 1. Module Not Found Error

**Error:**
```
ModuleNotFoundError: No module named 'PySide6'
```

**Solution:**
```powershell
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### 2. QtWebEngine Not Working

**Error:**
```
QWebEngineView shows blank page or crashes
```

**Solution:**
```powershell
# Reinstall PySide6 with WebEngine
pip uninstall PySide6
pip install PySide6>=6.10.0
```

#### 3. Executable Too Large

**Issue:** `markdown_viewer.exe` is over 250 MB

**Solutions:**
1. UPX is already enabled - verify it's installed
2. Consider OneDir mode for faster startup
3. Size is normal due to Qt6 + WebEngine

#### 4. Application Doesn't Launch

**Issue:** Double-clicking .exe does nothing

**Solutions:**
1. Compile with `console=True` temporarily to see errors:
   ```python
   # In markdown_viewer.spec
   console=True,  # Enable console
   ```

2. Check Windows Event Viewer for errors
3. Test on different machine
4. Verify all DLLs are included

#### 5. Last Directory Not Remembered

**Issue:** Application always opens in Documents folder

**Solutions:**
1. Check QSettings is initialized:
   ```python
   self.settings = QSettings("ChristophePelichet", "MarkdownViewerEditor")
   ```

2. Verify sync() is called:
   ```python
   self.settings.setValue("last_directory", path)
   self.settings.sync()
   ```

3. Check Windows Registry:
   ```
   HKEY_CURRENT_USER\Software\ChristophePelichet\MarkdownViewerEditor
   ```

### Build Issues

#### PyInstaller Fails

**Error:**
```
Fatal error in launcher: Unable to create process
```

**Solution:**
```powershell
# Reinstall PyInstaller
pip uninstall pyinstaller
pip install pyinstaller>=6.16.0

# Clear cache
pyinstaller --clean markdown_viewer.spec
```

#### Missing Modules in Executable

**Error:** Application works in dev but not in .exe

**Solution:**
Add to `hiddenimports` in `.spec` file:
```python
hiddenimports=[
    'PySide6.QtCore',
    'PySide6.QtWidgets',
    'markdown.extensions.tables',
    # Add missing module here
],
```

### Debug Mode

To enable debug output:

```powershell
# Compile with debug
pyinstaller --debug=all markdown_viewer.spec

# Run and check console output
.\dist\markdown_viewer.exe
```

### Getting Help

1. **Check documentation**: Review this file and README.md
2. **Check issues**: Search GitHub issues for similar problems
3. **Create issue**: Open a new issue with detailed information
4. **Contact author**: Christophe Pelichet via GitHub

---

## Version History

See [CHANGELOG.md](../CHANGELOG.md) for complete version history.

**Current Version:** v0.100 (December 1, 2025)

---

**Last Updated:** December 1, 2025  
**Status:** ✅ Production Ready  
**Maintained By:** Christophe Pelichet
