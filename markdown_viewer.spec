# -*- mode: python ; coding: utf-8 -*-

# Exclusions to reduce size
excludes = [
    'tkinter',
    '_tkinter',
    'matplotlib',
    'numpy',
    'scipy',
    'pandas',
    'PIL',
    'Pillow',
    'wx',
    'PyQt5',
    'PyQt6',
    'unittest',
    'test',
    'pytest',
    'distutils',
    'setuptools',
    'pip',
    'email',
    'http',
    'urllib',
    'urllib3',
    # 'xml.dom',  # REMOVED - Required by markdown
    # 'xml.sax',  # REMOVED - Required by markdown
    # 'xml.etree',  # REMOVED - Required by markdown
    'xmlrpc',
    'pydoc',
    'doctest',
    # 'argparse',  # REMOVED - Required by PySide6
    'sqlite3',
    'bz2',
    'lzma',
    # '_ssl',  # May be needed
    # '_hashlib',  # May be needed
    'asyncio',
    'concurrent',
    'multiprocessing',
    'IPython',
    'jupyter',
    'notebook',
    'tornado',
]

a = Analysis(
    ['markdown_viewer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui', 
        'PySide6.QtWidgets',
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtWebEngineCore',
        'markdown',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
    optimize=2,  # Maximum optimization
)

# Keep all binaries and data for QtWebEngine stability

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='markdown_viewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,  # Strip not available on Windows
    upx=False,    # UPX disabled (not installed)
    console=False,  # Disable console now that it works
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
