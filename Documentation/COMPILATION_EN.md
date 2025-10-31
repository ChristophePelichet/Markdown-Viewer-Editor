### Clone the Repository
git clone https://github.com/ChristophePelichet/markdown-viewer-editor.git
cd markdown-viewer-editor

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

### Compiling to Executable

To compile the application into a portable executable:

```bash
# Activate virtual environment
.venv\Scripts\activate

# Compile with PyInstaller
pyinstaller markdown_viewer.spec

# The executable will be in: dist\MarkdownViewer.exe
```

For more details on compilation, see **[BUILD_INSTRUCTIONS_EN.md](BUILD_INSTRUCTIONS_EN.md)**
