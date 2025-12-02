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
    'xml.dom',
    'xml.sax',
    'xml.etree',
    'xmlrpc',
    'pydoc',
    'doctest',
    'argparse',
    'sqlite3',
    'bz2',
    'lzma',
    '_ssl',
    '_hashlib',
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
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.toc',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
    optimize=2,  # Maximum optimization
)

# Filter unused Qt binaries to reduce size
a.binaries = [x for x in a.binaries if not any([
    x[0].startswith('opengl'),
    x[0].startswith('d3d'),
    'Qt6Sql' in x[0],
    'Qt6Test' in x[0],
    'Qt6Designer' in x[0],
    'Qt6Network' in x[0],
    'Qt6Qml' in x[0],
    'Qt6Quick' in x[0],
    'Qt6Bluetooth' in x[0],
    'Qt6Multimedia' in x[0],
    'Qt6Positioning' in x[0],
    'Qt6Sensors' in x[0],
    'Qt6SerialPort' in x[0],
    'Qt6Svg' in x[0],
    'Qt6PrintSupport' in x[0],
    'Qt6Xml' in x[0],
    'Qt63D' in x[0],
    'Qt6Charts' in x[0],
    'Qt6DataVisualization' in x[0],
    'api-ms-win' in x[0],  # Redundant Windows API sets
    'msvcp' in x[0] and not 'msvcp140' in x[0],  # Keep only MSVC 2015+
])]

# Filtrer les données Qt inutiles (locales, traductions, etc.)
a.datas = [x for x in a.datas if not any([
    'qtwebengine_locales' in x[0].lower() and not any(loc in x[0].lower() for loc in ['en-us', 'fr-fr']),
    'translations' in x[0].lower() and not any(lang in x[0].lower() for lang in ['qt_en', 'qt_fr', 'qtwebengine_en', 'qtwebengine_fr']),
])]

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
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
