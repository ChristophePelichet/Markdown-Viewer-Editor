# 📝 Markdown Viewer & Editor

> 🇫🇷 **Version française** | **[🇬🇧 English version](Documentation/README_EN.md)**

Outil de visualisation et d'édition de fichiers Markdown avec prévisualisation en temps réel.

## 🎯 Fonctionnalités

### Visualisation
- ✅ **Prévisualisation en temps réel** : Rendu HTML du Markdown avec CSS professionnel
- ✅ **Split view** : Éditeur à gauche, prévisualisation à droite
- ✅ **Support complet Markdown** : Tables, code, citations, listes, liens, images
- ✅ **Coloration syntaxique** : Pour les blocs de code
- ✅ **Emojis** : Support complet des emojis Unicode

### Édition
- ✅ **Éditeur monospace** : Police Consolas pour une meilleure lisibilité
- ✅ **Annuler/Refaire** : Ctrl+Z / Ctrl+Y
- ✅ **Recherche** : Ctrl+F pour rechercher du texte
- ✅ **Détection de modifications** : Astérisque (*) dans le titre si modifié
- ✅ **Confirmation avant fermeture** : Si le fichier a été modifié

### Fichiers rapides
- ✅ **Sélection rapide** : Liste déroulante des CHANGELOG et README
- ✅ **Auto-détection** : Recherche automatique dans Documentation/ et racine
- ✅ **Affichage relatif** : Chemins relatifs pour une meilleure lisibilité

## 🚀 Utilisation

### Méthode 1 : Lanceur batch (Recommandé)
```batch
launch_markdown_viewer.bat
```

Le script :
1. Active automatiquement l'environnement virtuel
2. Installe le module `markdown` si nécessaire
3. Lance l'application

### Méthode 2 : Ligne de commande
```bash
# Activer l'environnement virtuel
.venv\Scripts\activate

# Installer markdown si nécessaire
pip install markdown

# Lancer l'application
python markdown_viewer.py
```

## 📋 Interface

```
┌─────────────────────────────────────────────────────────────────────┐
│ 📂 Ouvrir  💾 Sauvegarder  ↶ Annuler  ↷ Refaire  🔍 Rechercher     │
├─────────────────────────────────────────────────────────────────────┤
│ 📂 Fichier rapide: [CHANGELOG_FR.md ▼]           🔄 Actualiser     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────────────┬───────────────────────────────────────┐  │
│  │  ✏️ Éditeur          │  👁️ Prévisualisation                 │  │
│  ├──────────────────────┼───────────────────────────────────────┤  │
│  │ # Titre              │  Titre                                 │  │
│  │                      │  ═════                                 │  │
│  │ **Gras** *Italique*  │  Gras Italique                        │  │
│  │                      │                                        │  │
│  │ - Liste 1            │  • Liste 1                            │  │
│  │ - Liste 2            │  • Liste 2                            │  │
│  │                      │                                        │  │
│  │ ```python            │  def hello():                         │  │
│  │ def hello():         │      print("Hello!")                  │  │
│  │     print("Hello!")  │                                        │  │
│  │ ```                  │                                        │  │
│  │                      │                                        │  │
│  └──────────────────────┴───────────────────────────────────────┘  │
│                                                                       │
├─────────────────────────────────────────────────────────────────────┤
│ Fichier chargé : CHANGELOG_FR.md                                    │
└─────────────────────────────────────────────────────────────────────┘
```

## ⌨️ Raccourcis clavier

| Raccourci | Action |
|-----------|--------|
| **Ctrl+O** | Ouvrir un fichier |
| **Ctrl+S** | Sauvegarder |
| **Ctrl+Z** | Annuler |
| **Ctrl+Y** | Refaire |
| **Ctrl+F** | Rechercher |

## 📚 Aide Markdown intégrée

L'application inclut un guide rapide Markdown accessible via le bouton "❓ Aide Markdown" :

### Exemples de syntaxe
- **Titres** : `# H1`, `## H2`, `### H3`
- **Gras** : `**texte**` ou `__texte__`
- **Italique** : `*texte*` ou `_texte_`
- **Code** : `` `code inline` ``
- **Listes** : `- item` ou `1. item`
- **Liens** : `[texte](url)`
- **Citations** : `> citation`
- **Tableaux** : `| Col 1 | Col 2 |`

## 🔧 Dépendances

### Requises
- **PySide6** : Interface graphique Qt
- **PySide6-WebEngine** : Affichage HTML dans Qt
- **markdown** : Conversion Markdown → HTML

### Installation
```bash
pip install PySide6 PySide6-WebEngine markdown
```

Ou via `requirements.txt` :
```bash
pip install -r requirements.txt
```

## 📁 Fichiers détectés automatiquement

L'outil recherche automatiquement ces fichiers :

### Documentation/
- `CHANGELOG_FR.md`
- `CHANGELOG_EN.md`
- `CHANGELOG_DE.md`
- `README_FR.md`
- `README_EN.md`
- `README_DE.md`
- Tous les fichiers `*.md`

### Racine du projet
- `CHANGELOG.md`
- `README.md`
- Tous les fichiers `*.md`

## 💾 Sauvegarde

### Confirmation automatique
- ✅ Avant d'ouvrir un autre fichier
- ✅ Avant de quitter l'application
- ✅ Message clair avec options : Oui / Non / Annuler

### Indicateur de modification
- Le titre de la fenêtre affiche un astérisque (*) si le fichier est modifié
- Exemple : `📝 Markdown Viewer & Editor - CHANGELOG_FR.md *`

## 🎨 Style de prévisualisation

Le rendu HTML utilise un style professionnel inspiré de GitHub :

- ✅ **Typographie** : Segoe UI, ligne de 1.6
- ✅ **Titres** : Avec bordures inférieures (H1, H2)
- ✅ **Code** : Fond gris clair, police monospace
- ✅ **Tableaux** : Bordures, lignes alternées
- ✅ **Citations** : Bordure bleue à gauche
- ✅ **Liens** : Couleur bleue GitHub (#0366d6)
- ✅ **Largeur max** : 900px pour une lecture optimale

## 🐛 Dépannage

### Le module 'markdown' n'est pas installé
```bash
pip install markdown
```

### Erreur d'encodage
Le fichier utilise UTF-8 par défaut. Vérifiez que vos fichiers Markdown sont en UTF-8.

### La prévisualisation ne s'affiche pas
1. Vérifiez que `PySide6-WebEngine` est installé
2. Vérifiez que le module `markdown` est installé
3. Cliquez sur "🔄 Actualiser" pour forcer le rendu

### L'environnement virtuel n'est pas trouvé
Assurez-vous que le fichier `.venv/Scripts/activate.bat` existe :
```bash
python -m venv .venv
```

## 📝 Utilisation typique

### 1. Éditer le CHANGELOG
1. Lancer l'outil : `launch_markdown_viewer.bat`
2. Sélectionner "CHANGELOG_FR.md" dans la liste déroulante
3. Éditer le contenu dans le panneau de gauche
4. Voir le rendu en temps réel à droite
5. Sauvegarder : **Ctrl+S** ou bouton "💾 Sauvegarder"

### 2. Créer un nouveau document
1. Écrire le contenu Markdown dans l'éditeur
2. Sauvegarder sous un nouveau nom : Menu → Sauvegarder sous
3. Le fichier est ajouté automatiquement à la liste rapide (si CHANGELOG ou README)

### 3. Rechercher dans le document
1. **Ctrl+F** ou bouton "🔍 Rechercher"
2. Entrer le texte à rechercher
3. L'éditeur se positionne sur la première occurrence

## 🔮 Améliorations futures possibles

- [ ] Export PDF depuis la prévisualisation
- [ ] Barre d'outils Markdown (boutons gras, italique, etc.)
- [ ] Mode sombre / clair
- [ ] Rechercher et remplacer
- [ ] Support de multiples fichiers ouverts (onglets)
- [ ] Prévisualisation des images locales
- [ ] Vérification orthographique
- [ ] Génération automatique de table des matières

## 📄 Licence

Projet open-source - Markdown Viewer & Editor

## 👤 Auteur

**Christophe Pelichet**

---

**Version** : v0.100  
**Date** : 31 octobre 2025  
**Statut** : ✅ Opérationnel
