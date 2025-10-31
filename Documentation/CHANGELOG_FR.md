# 📋 Historique des Versions (CHANGELOG)

**Projet :** Markdown Viewer & Editor  
**Auteur :** Christophe Pelichet  
**Version actuelle :** v0.100

---

## [0.100] - 31 octobre 2025

### 🎉 Version initiale

#### ✨ Nouvelles fonctionnalités
- **Visualisation Markdown** : Prévisualisation en temps réel avec rendu HTML professionnel
- **Éditeur intégré** : Éditeur de texte avec police monospace (Consolas)
- **Vue divisée** : Affichage simultané de l'éditeur et de la prévisualisation
- **Fichiers rapides** : Sélection rapide des fichiers CHANGELOG et README
- **Support Markdown complet** :
  - Titres (H1 à H6)
  - Formatage (gras, italique, barré)
  - Listes (ordonnées et non ordonnées)
  - Tables avec formatage
  - Blocs de code avec coloration syntaxique
  - Citations
  - Liens et images
  - Emojis Unicode
  - Séparateurs horizontaux

#### 🛠️ Fonctionnalités d'édition
- **Annuler/Refaire** : Support complet de l'historique (Ctrl+Z / Ctrl+Y)
- **Recherche de texte** : Fonction de recherche intégrée (Ctrl+F)
- **Détection des modifications** : Indicateur visuel (*) dans le titre
- **Sauvegarde intelligente** : Confirmation avant fermeture si modifications non sauvegardées
- **Raccourcis clavier** : Support complet des raccourcis clavier standards

#### 🎨 Interface utilisateur
- **Thème moderne** : Interface Fusion avec style professionnel
- **Barre d'outils complète** : Accès rapide aux fonctions principales
- **Barre d'état** : Affichage des informations de statut
- **CSS professionnel** : Rendu Markdown avec style GitHub-like
- **Modes de vue** : Basculement entre split, éditeur seul, ou aperçu seul

#### 📚 Documentation
- **Aide Markdown intégrée** : Guide rapide de la syntaxe Markdown
- **README complet** : Documentation utilisateur détaillée
- **Lanceur batch** : Script de lancement automatique avec gestion de l'environnement

#### ⚙️ Technique
- **Python 3.x** : Développé avec Python moderne
- **PySide6** : Interface graphique Qt6
- **markdown** : Conversion Markdown vers HTML
- **Extensions Markdown** : Support des tables, code fencé, TOC, coloration syntaxique
- **Environnement virtuel** : Isolation des dépendances

---

## 📝 Notes de version

### Configuration requise
- Python 3.8 ou supérieur
- PySide6 (Qt6 pour Python)
- Module markdown avec extensions

### Installation
```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### Utilisation
```bash
# Méthode 1 : Lanceur batch (recommandé)
launch_markdown_viewer.bat

# Méthode 2 : Ligne de commande
python markdown_viewer.py
```

---

## 🔮 Prochaines versions

### Version 0.2 (planifiée)
- [ ] Export HTML
- [ ] Export PDF
- [ ] Thèmes de couleurs
- [ ] Préférences utilisateur
- [ ] Historique des fichiers récents

### Version 0.3 (planifiée)
- [ ] Support des plugins Markdown
- [ ] Auto-complétion Markdown
- [ ] Aperçu des images
- [ ] Support du drag & drop

---

**Légende des symboles :**
- ✨ Nouvelle fonctionnalité
- 🛠️ Amélioration
- 🐛 Correction de bug
- 🔒 Sécurité
- 📚 Documentation
- ⚙️ Technique
- 🎨 Interface utilisateur
