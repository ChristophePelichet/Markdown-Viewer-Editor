# 🔧 Build and Deployment Instructions

**Project:** Markdown Viewer & Editor  
**Version:** v0.100  
**Author:** Christophe Pelichet

---

## 📦 Building with PyInstaller

### Prerequisites
- Activated virtual environment
- All modules installed (see `requirements.txt`)
- PyInstaller installed

### Method 1: Using the .spec file (Recommended)

```powershell
# Activate virtual environment
.venv\Scripts\activate

# Compile with the .spec file
pyinstaller markdown_viewer.spec
```

The executable will be generated in: `dist\MarkdownViewer.exe`

### Method 2: Direct command line

```powershell
# Activate virtual environment
.venv\Scripts\activate

# Compile in onefile mode
pyinstaller --onefile --noconsole --name="MarkdownViewer" markdown_viewer.py
```

---

## 🎯 Build Options

### OneFile Mode (Portable)
- **Advantage**: Single .exe file, easy to distribute
- **Disadvantage**: Slightly slower startup
- **Size**: ~150-250 MB (due to Qt6)

```powershell
pyinstaller --onefile markdown_viewer.spec
```

### OneDir Mode (Faster)
- **Advantage**: Faster startup
- **Disadvantage**: Complete folder to distribute
- **Modification**: In the .spec, replace `EXE()` with onedir mode

---

## 🔍 Size Optimization

### 1. UPX (Compression)
UPX is already enabled in the .spec file. To install it:

```powershell
# Download UPX from https://upx.github.io/
# Add UPX to PATH
```

### 2. Excluding Unnecessary Modules
The .spec file already excludes:
- tkinter
- matplotlib
- numpy
- scipy
- PIL
- wx

### 3. Reducing Imports
Verify that only necessary modules are imported in the code.

---

## 🧪 Testing the Executable

### Before Distribution

1. **Functional test**:
   ```powershell
   dist\MarkdownViewer.exe
   ```

2. **Verify**:
   - [ ] Application launches without errors
   - [ ] File opening works
   - [ ] Saving works
   - [ ] Markdown preview displays
   - [ ] Quick files are detected
   - [ ] All buttons are functional

3. **Test on clean machine**:
   - Test on a machine without Python installed
   - Verify all dependencies are embedded

---

## 📋 Pre-Release Checklist

- [ ] Version updated in all files
- [ ] CHANGELOG up to date
- [ ] README up to date
- [ ] Functional tests passed
- [ ] Onefile compilation successful
- [ ] Executable size acceptable
- [ ] Clean machine test passed
- [ ] Documentation up to date

---

## 🐛 Troubleshooting

### Error: Module not found
**Solution**: Add the module to `hiddenimports` in the .spec file

### Error: QtWebEngine not working
**Solution**: Verify that PySide6_Addons is installed

### Executable too large
**Solutions**:
1. Install and enable UPX
2. Check exclusions in the .spec
3. Use OneDir mode instead of OneFile

### Application doesn't launch
**Solutions**:
1. Compile with `--debug=all` to see errors
2. Check logs in temporary folder
3. Test with `console=True` in the .spec

---

## 📦 Distribution

### Files to Include

**For end users**:
- `MarkdownViewer.exe` (compiled executable)
- `README.md` (documentation)
- `Documentation/` (complete folder)

**For developers**:
- All source files
- `requirements.txt`
- `.venv/` (create with instructions)
- `markdown_viewer.spec`

### Distribution Methods

1. **ZIP Archive**:
   ```powershell
   # Create archive with exe and docs
   Compress-Archive -Path dist\MarkdownViewer.exe, README.md, Documentation -DestinationPath MarkdownViewer-v0.100.zip
   ```

2. **Installer** (advanced):
   - Use Inno Setup
   - Use NSIS
   - Create an MSI

---

## 🔄 Version Update

### Files to Modify

1. `markdown_viewer.py`: File header
2. `markdown_viewer.spec`: Version info
3. `requirements.txt`: Header
4. `launch_markdown_viewer.bat`: Header and echo
5. `README.md`: Version section
6. `Documentation/README_EN.md`: Version section
7. `Documentation/CHANGELOG_FR.md`: New entry
8. `Documentation/CHANGELOG_EN.md`: New entry

### Update Script (to create)

```powershell
# update_version.ps1
$oldVersion = "0.100"
$newVersion = "0.200"

# Replace in all files
(Get-Content file.txt) -replace $oldVersion, $newVersion | Set-Content file.txt
```

---

## 📊 Technical Information

### Main Dependencies
- **PySide6**: 6.10.0 (Qt6 for Python)
- **Markdown**: 3.9 (MD → HTML conversion)
- **PyInstaller**: 6.16.0 (Compilation)

### Component Sizes
- **PySide6_Essentials**: ~74 MB
- **PySide6_Addons**: ~165 MB (includes QtWebEngine)
- **Markdown**: ~107 KB
- **Source code**: ~20 KB

### Compatibility
- **Windows**: 10, 11 (64-bit)
- **Python**: 3.13+ (3.9+ with earlier PySide6 versions)

---

**Last update**: October 31, 2025  
**Status**: ✅ Production Ready
