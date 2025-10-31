# 🔧 Instructions de Compilation et Déploiement

**Projet :** Markdown Viewer & Editor  
**Version :** v0.100  
**Auteur :** Christophe Pelichet

---

## 📦 Compilation avec PyInstaller

### Prérequis
- Environnement virtuel activé
- Tous les modules installés (voir `requirements.txt`)
- PyInstaller installé

### Méthode 1 : Utiliser le fichier .spec (Recommandé)

```powershell
# Activer l'environnement virtuel
.venv\Scripts\activate

# Compiler avec le fichier .spec
pyinstaller markdown_viewer.spec
```

L'exécutable sera généré dans : `dist\MarkdownViewer.exe`

### Méthode 2 : Ligne de commande directe

```powershell
# Activer l'environnement virtuel
.venv\Scripts\activate

# Compiler en mode onefile
pyinstaller --onefile --noconsole --name="MarkdownViewer" markdown_viewer.py
```

---

## 🎯 Options de compilation

### Mode OnFile (Portable)
- **Avantage** : Un seul fichier .exe, facile à distribuer
- **Inconvénient** : Démarrage légèrement plus lent
- **Taille** : ~150-250 MB (en raison de Qt6)

```powershell
pyinstaller --onefile markdown_viewer.spec
```

### Mode OneDir (Plus rapide)
- **Avantage** : Démarrage plus rapide
- **Inconvénient** : Dossier complet à distribuer
- **Modification** : Dans le .spec, remplacer `EXE()` par mode onedir

---

## 🔍 Optimisation de la taille

### 1. UPX (Compression)
UPX est déjà activé dans le fichier .spec. Pour l'installer :

```powershell
# Télécharger UPX depuis https://upx.github.io/
# Ajouter UPX au PATH
```

### 2. Exclusion de modules inutiles
Le fichier .spec exclut déjà :
- tkinter
- matplotlib
- numpy
- scipy
- PIL
- wx

### 3. Réduire les imports
Vérifier que seuls les modules nécessaires sont importés dans le code.

---

## 🧪 Test de l'exécutable

### Avant de distribuer

1. **Test fonctionnel** :
   ```powershell
   dist\MarkdownViewer.exe
   ```

2. **Vérifier** :
   - [ ] L'application se lance sans erreur
   - [ ] L'ouverture de fichiers fonctionne
   - [ ] La sauvegarde fonctionne
   - [ ] La prévisualisation Markdown s'affiche
   - [ ] Les fichiers rapides sont détectés
   - [ ] Tous les boutons sont fonctionnels

3. **Test sur machine propre** :
   - Tester sur une machine sans Python installé
   - Vérifier que toutes les dépendances sont embarquées

---

## 📋 Checklist avant release

- [ ] Version mise à jour dans tous les fichiers
- [ ] CHANGELOG à jour
- [ ] README à jour
- [ ] Tests fonctionnels réussis
- [ ] Compilation onefile sans erreur
- [ ] Taille de l'exécutable acceptable
- [ ] Test sur machine propre réussi
- [ ] Documentation à jour

---

## 🐛 Résolution de problèmes

### Erreur : Module non trouvé
**Solution** : Ajouter le module dans `hiddenimports` du fichier .spec

### Erreur : QtWebEngine ne fonctionne pas
**Solution** : Vérifier que PySide6_Addons est installé

### Exécutable trop volumineux
**Solutions** :
1. Installer et activer UPX
2. Vérifier les exclusions dans le .spec
3. Utiliser le mode OneDir au lieu de OnFile

### L'application ne se lance pas
**Solutions** :
1. Compiler avec `--debug=all` pour voir les erreurs
2. Vérifier les logs dans le dossier temporaire
3. Tester avec `console=True` dans le .spec

---

## 📦 Distribution

### Fichiers à inclure

**Pour utilisateurs finaux** :
- `MarkdownViewer.exe` (exécutable compilé)
- `README.md` (documentation)
- `Documentation/` (dossier complet)

**Pour développeurs** :
- Tous les fichiers sources
- `requirements.txt`
- `.venv/` (créer avec les instructions)
- `markdown_viewer.spec`

### Méthodes de distribution

1. **Archive ZIP** :
   ```powershell
   # Créer une archive avec l'exe et la doc
   Compress-Archive -Path dist\MarkdownViewer.exe, README.md, Documentation -DestinationPath MarkdownViewer-v0.100.zip
   ```

2. **Installeur** (avancé) :
   - Utiliser Inno Setup
   - Utiliser NSIS
   - Créer un MSI

---

## 🔄 Mise à jour de version

### Fichiers à modifier

1. `markdown_viewer.py` : En-tête du fichier
2. `markdown_viewer.spec` : Version info
3. `requirements.txt` : En-tête
4. `launch_markdown_viewer.bat` : En-tête et echo
5. `README.md` : Section version
6. `Documentation/README_EN.md` : Section version
7. `Documentation/CHANGELOG_FR.md` : Nouvelle entrée
8. `Documentation/CHANGELOG_EN.md` : Nouvelle entrée

### Script de mise à jour (à créer)

```powershell
# update_version.ps1
$oldVersion = "0.100"
$newVersion = "0.200"

# Remplacer dans tous les fichiers
(Get-Content file.txt) -replace $oldVersion, $newVersion | Set-Content file.txt
```

---

## 📊 Informations techniques

### Dépendances principales
- **PySide6** : 6.10.0 (Qt6 pour Python)
- **Markdown** : 3.9 (Conversion MD → HTML)
- **PyInstaller** : 6.16.0 (Compilation)

### Taille des composants
- **PySide6_Essentials** : ~74 MB
- **PySide6_Addons** : ~165 MB (inclut QtWebEngine)
- **Markdown** : ~107 KB
- **Code source** : ~20 KB

### Compatibilité
- **Windows** : 10, 11 (64-bit)
- **Python** : 3.13+ (3.9+ avec versions antérieures de PySide6)

---

**Dernière mise à jour** : 31 octobre 2025  
**Statut** : ✅ Production Ready
