# -*- mode: python ; coding: utf-8 -*-
# =============================================================================
# PyInstaller spec file pour Markdown Viewer & Editor
# Version: v0.100
# Auteur: Christophe Pelichet
# 
# Compilation:
#   pyinstaller markdown_viewer.spec
#
# L'exécutable sera généré dans le dossier dist/
# =============================================================================

block_cipher = None

a = Analysis(
    ['markdown_viewer.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Ajouter les fichiers de documentation si nécessaire
        # ('Documentation', 'Documentation'),
    ],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtWebEngineCore',
        'markdown',
        'markdown.extensions',
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.toc',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'scipy',
        'PIL',
        'wx',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MarkdownViewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Pas de fenêtre console (GUI uniquement)
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Ajouter 'icon.ico' si vous avez une icône
    # Informations sur le fichier Windows
    version_info={
        'FileVersion': '0.100.0.0',
        'ProductVersion': '0.100.0.0',
        'FileDescription': 'Markdown Viewer & Editor',
        'CompanyName': 'Christophe Pelichet',
        'LegalCopyright': 'Copyright (c) 2025 Christophe Pelichet',
        'ProductName': 'Markdown Viewer & Editor',
        'InternalName': 'MarkdownViewer',
        'OriginalFilename': 'MarkdownViewer.exe',
    },
)

# =============================================================================
# Notes de compilation:
# =============================================================================
# 
# 1. Compilation en mode onefile (portable):
#    L'exécutable contient tous les fichiers nécessaires et peut être 
#    distribué seul sans dépendances externes.
#
# 2. Modules exclus:
#    Les modules inutilisés (tkinter, matplotlib, etc.) sont exclus pour 
#    réduire la taille de l'exécutable.
#
# 3. Console désactivée:
#    console=False désactive la fenêtre de console au lancement (GUI pur).
#
# 4. UPX activé:
#    UPX compresse l'exécutable pour réduire sa taille (nécessite UPX installé).
#
# 5. Pour ajouter une icône:
#    Décommentez la ligne icon= et ajoutez le chemin vers votre fichier .ico
#
# 6. Taille estimée de l'exécutable:
#    ~ 150-250 MB (en raison de Qt6 et QtWebEngine)
#
# =============================================================================
