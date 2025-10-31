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

## 🚀 Utilisation des sources

### Installation et configuration

Pour utiliser le projet à partir des sources, consultez les guides de compilation :

- 📘 **[Guide de compilation (Français)](Documentation/COMPILATION_FR.md)** - Instructions détaillées en français
- 📗 **[Compilation guide (English)](Documentation/COMPILATION_EN.md)** - Detailed instructions in English

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

## 🔮 Améliorations futures possibles

- [ ] Export PDF depuis la prévisualisation
- [ ] Export HTML / PDF
- [ ] Barre d'outils Markdown (boutons gras, italique, etc.)
- [ ] Mode sombre / clair
- [ ] Rechercher et remplacer
- [ ] Support de multiples fichiers ouverts (onglets)
- [ ] Prévisualisation des images locales
- [ ] Vérification orthographique
- [ ] Génération automatique de table des matières
- [ ] Thèmes de couleurs
- [ ] Préférences utilisateur
- [ ] Historique des fichiers récents
- [ ] Support des plugins Markdown
- [ ] Auto-complétion Markdown
- [ ] Aperçu des images
- [ ] Support du drag & drop

## 📄 Licence

Projet open-source - Markdown Viewer & Editor

## 👤 Auteur

**Christophe Pelichet**

---

**Version** : v0.100  
**Date** : 31 octobre 2025  
**Statut** : ✅ Opérationnel
