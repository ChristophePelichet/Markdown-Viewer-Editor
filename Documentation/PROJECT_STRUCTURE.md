# 📁 Structure du Projet - Markdown Viewer & Editor

**Version :** v0.100  
**Auteur :** Christophe Pelichet  
**Date :** 31 octobre 2025

---

## 🌳 Arborescence du projet

```
Markedown - Editor/
├── .gitignore                          # Fichiers à ignorer par Git
├── .venv/                              # Environnement virtuel Python
│   ├── Scripts/                        # Exécutables (python, pip, activate)
│   └── Lib/                            # Bibliothèques Python installées
├── Documentation/                      # Documentation du projet
│   ├── BUILD_INSTRUCTIONS.md          # Instructions de compilation
│   ├── CHANGELOG_EN.md                # Historique des versions (Anglais)
│   ├── CHANGELOG_FR.md                # Historique des versions (Français)
│   └── README_EN.md                   # Documentation principale (Anglais)
├── launch_markdown_viewer.bat         # Lanceur batch Windows
├── markdown_viewer.py                 # Code source principal (633 lignes)
├── markdown_viewer.spec               # Configuration PyInstaller
├── README.md                          # Documentation principale (Français)
└── requirements.txt                   # Dépendances Python

Après compilation :
├── build/                              # Fichiers temporaires de compilation
└── dist/                               # Exécutable final
    └── MarkdownViewer.exe             # Application compilée (~150-250 MB)
```

---

## 📄 Description des fichiers

### Fichiers principaux

#### `markdown_viewer.py`
**Type :** Code source Python  
**Lignes :** 633  
**Description :** Application principale avec interface PySide6  
**Fonctionnalités :**
- Interface graphique Qt6
- Éditeur de texte Markdown
- Prévisualisation HTML en temps réel
- Gestion de fichiers (ouvrir, sauvegarder)
- Fichiers rapides (CHANGELOG, README)
- Recherche de texte
- Aide Markdown intégrée

#### `requirements.txt`
**Type :** Liste de dépendances  
**Description :** Modules Python requis  
**Contenu :**
```
PySide6>=6.10.0        # Interface graphique Qt6
markdown>=3.9.0        # Conversion Markdown → HTML
pyinstaller>=6.16.0    # Compilation en exécutable
```

#### `markdown_viewer.spec`
**Type :** Configuration PyInstaller  
**Description :** Paramètres de compilation  
**Mode :** OnFile (exécutable unique portable)  
**Options :**
- Console désactivée (GUI pur)
- Modules exclus pour réduire la taille
- Informations de version Windows
- UPX activé (compression)

### Fichiers de lancement

#### `launch_markdown_viewer.bat`
**Type :** Script batch Windows  
**Description :** Lanceur automatique  
**Actions :**
1. Active l'environnement virtuel (.venv)
2. Vérifie et installe markdown si nécessaire
3. Lance l'application Python

### Documentation

#### `README.md` (Français)
**Contenu :**
- Guide d'utilisation complet
- Description des fonctionnalités
- Instructions d'installation
- Raccourcis clavier
- Guide Markdown
- Dépannage

#### `Documentation/README_EN.md` (Anglais)
**Contenu :** Version anglaise du README principal

#### `Documentation/CHANGELOG_FR.md`
**Contenu :**
- Historique des versions (Français)
- Version actuelle : v0.100
- Nouvelles fonctionnalités
- Corrections de bugs
- Notes de version

#### `Documentation/CHANGELOG_EN.md`
**Contenu :** Version anglaise du CHANGELOG

#### `Documentation/BUILD_INSTRUCTIONS.md`
**Contenu :**
- Instructions de compilation PyInstaller
- Options de compilation
- Optimisation de la taille
- Tests et déploiement
- Résolution de problèmes
- Mise à jour de version

### Configuration

#### `.gitignore`
**Type :** Configuration Git  
**Description :** Fichiers à exclure du versionnement  
**Ignore :**
- Environnement virtuel (.venv/)
- Fichiers compilés (__pycache__/, *.pyc)
- Builds (build/, dist/)
- Fichiers IDE (.vscode/, .idea/)
- Fichiers temporaires (*.tmp, *.log)

---

## 🔧 Environnement virtuel

### Structure de .venv/

```
.venv/
├── Scripts/
│   ├── activate.bat           # Activation (cmd)
│   ├── activate.ps1           # Activation (PowerShell)
│   ├── python.exe             # Interpréteur Python
│   └── pip.exe                # Gestionnaire de packages
├── Lib/
│   └── site-packages/         # Modules installés
│       ├── PySide6/           # Qt6 pour Python
│       ├── markdown/          # Conversion Markdown
│       └── pyinstaller/       # Compilateur
└── pyvenv.cfg                 # Configuration venv
```

### Modules installés

| Module | Version | Taille | Description |
|--------|---------|--------|-------------|
| PySide6 | 6.10.0 | ~240 MB | Interface Qt6 |
| markdown | 3.9 | ~107 KB | Conversion MD→HTML |
| pyinstaller | 6.16.0 | ~1.4 MB | Compilation |

---

## 📊 Statistiques du projet

### Lignes de code
- **Python** : 633 lignes (markdown_viewer.py)
- **Batch** : 35 lignes (launch_markdown_viewer.bat)
- **Spec** : 120 lignes (markdown_viewer.spec)
- **Total** : ~788 lignes de code

### Documentation
- **Français** : ~500 lignes (README.md + CHANGELOG_FR.md)
- **Anglais** : ~500 lignes (README_EN.md + CHANGELOG_EN.md)
- **Technique** : ~400 lignes (BUILD_INSTRUCTIONS.md)
- **Total** : ~1400 lignes de documentation

### Taille des fichiers
- **Code source** : ~30 KB
- **Documentation** : ~100 KB
- **Environnement virtuel** : ~400 MB
- **Exécutable compilé** : ~150-250 MB

---

## 🎯 Points d'entrée

### Pour les utilisateurs

1. **Exécutable compilé** :
   ```
   dist\MarkdownViewer.exe
   ```

2. **Script batch** :
   ```
   launch_markdown_viewer.bat
   ```

### Pour les développeurs

1. **Ligne de commande** :
   ```powershell
   .venv\Scripts\activate
   python markdown_viewer.py
   ```

2. **Compilation** :
   ```powershell
   .venv\Scripts\activate
   pyinstaller markdown_viewer.spec
   ```

---

## 🔄 Workflow de développement

### 1. Installation initiale
```powershell
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Développement
```powershell
# Activer l'environnement
.venv\Scripts\activate

# Lancer en mode développement
python markdown_viewer.py

# Éditer le code
# Tester les modifications
```

### 3. Tests
```powershell
# Lancer l'application
python markdown_viewer.py

# Tester toutes les fonctionnalités
# Vérifier les fichiers rapides
# Tester la prévisualisation
```

### 4. Compilation
```powershell
# Compiler avec PyInstaller
pyinstaller markdown_viewer.spec

# L'exécutable est dans dist/
```

### 5. Distribution
```powershell
# Créer une archive
Compress-Archive -Path dist\MarkdownViewer.exe, README.md, Documentation -DestinationPath Release.zip
```

---

## 📝 Notes importantes

### Version
- Tous les fichiers utilisent la version **v0.100**
- Auteur : **Christophe Pelichet**
- Date : **31 octobre 2025**

### Compatibilité
- **OS** : Windows 10/11 (64-bit)
- **Python** : 3.13+ (3.9+ pour versions antérieures)
- **Qt** : PySide6 6.10.0 (Qt 6.x)

### Nettoyage effectué
- ✅ Toutes les références à "DAOC" supprimées
- ✅ Version mise à jour partout en v0.100
- ✅ Auteur "Christophe Pelichet" partout
- ✅ Code nettoyé et organisé

---

**Dernière mise à jour** : 31 octobre 2025  
**Statut** : ✅ Production Ready
