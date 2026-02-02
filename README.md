```markdown
# ☁️ Mon Cloud Personnel

Une solution de cloud personnel auto-hébergé avec interface web moderne, développée en Python Flask.

## ✨ Fonctionnalités

- 📤 **Upload de fichiers** - Envoyez vos fichiers facilement
- 👁️ **Prévisualisation** - Visualisez images, PDF, vidéos, audio et texte directement dans le navigateur
- 📊 **Statistiques système** - Suivez CPU, RAM, disque, batterie en temps réel
- 👥 **Multi-utilisateurs** - Gestion des comptes avec interface d'administration
- 📱 **Design responsive** - Optimisé pour mobile, tablette et ordinateur
- 🔒 **Sécurisé** - Authentification par mot de passe hashé

## 📋 Prérequis

- **Linux/Ubuntu** : Python 3.5+
- **macOS** : Python 3.6+
- **Windows** : Python 3.6+

---

# 🐧 Installation sur Linux/Ubuntu

## 1. Installer les dépendances

```bash
# Mettre à jour les paquets
sudo apt-get update

# Installer Python et pip
sudo apt-get install python3 python3-pip

# Installer Flask et psutil
sudo apt-get install python3-flask python3-psutil
```

## 2. Créer la structure du projet

```bash
# Créer le dossier du projet
mkdir -p ~/mon-cloud
cd ~/mon-cloud

# Créer les dossiers nécessaires
mkdir templates uploads
```

## 3. Créer les fichiers

Créez les fichiers suivants :
- `app.py` - Application principale
- `templates/login.html` - Page de connexion
- `templates/index.html` - Page d'accueil
- `templates/preview.html` - Page de prévisualisation
- `templates/stats.html` - Page des statistiques
- `templates/users.html` - Gestion des utilisateurs

*(Copiez le contenu depuis les fichiers fournis)*

## 4. Lancer l'application

```bash
python3 app.py
```

Accédez à : `http://localhost:5000`

**Identifiants par défaut :**
- Utilisateur : `admin`
- Mot de passe : `admin123`

## 5. Démarrage automatique (Optionnel)

```bash
# Créer un service systemd
sudo nano /etc/systemd/system/mon-cloud.service
```

Ajoutez :

```ini
[Unit]
Description=Mon Cloud Personnel
After=network.target

[Service]
User=VOTRE_NOM_UTILISATEUR
WorkingDirectory=/home/VOTRE_NOM_UTILISATEUR/mon-cloud
ExecStart=/usr/bin/python3 /home/VOTRE_NOM_UTILISATEUR/mon-cloud/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Activez le service :

```bash
sudo systemctl daemon-reload
sudo systemctl enable mon-cloud
sudo systemctl start mon-cloud
```

---

# 🍎 Installation sur macOS

## 1. Installer Homebrew (si pas déjà installé)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 2. Installer Python 3

```bash
brew install python3
```

## 3. Installer les dépendances Python

```bash
pip3 install flask werkzeug psutil
```

## 4. Créer la structure du projet

```bash
# Créer le dossier
mkdir -p ~/mon-cloud
cd ~/mon-cloud

# Créer les sous-dossiers
mkdir templates uploads
```

## 5. Créer les fichiers

Créez tous les fichiers nécessaires (app.py et les templates)

## 6. Lancer l'application

```bash
python3 app.py
```

Accédez à : `http://localhost:5000`

## 7. Démarrage automatique (Optionnel)

Créez un LaunchAgent :

```bash
nano ~/Library/LaunchAgents/com.moncloud.app.plist
```

Ajoutez :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.moncloud.app</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/Users/VOTRE_NOM/mon-cloud/app.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

Chargez le service :

```bash
launchctl load ~/Library/LaunchAgents/com.moncloud.app.plist
```

---

# 🪟 Installation sur Windows

## 1. Installer Python

1. Téléchargez Python depuis [python.org](https://www.python.org/downloads/)
2. **Important** : Cochez "Add Python to PATH" pendant l'installation
3. Installez Python

## 2. Installer les dépendances

Ouvrez **PowerShell** ou **Invite de commandes** :

```powershell
pip install flask werkzeug psutil
```

## 3. Créer la structure du projet

```powershell
# Créer le dossier
mkdir C:\mon-cloud
cd C:\mon-cloud

# Créer les sous-dossiers
mkdir templates
mkdir uploads
```

## 4. Créer les fichiers

Utilisez Notepad++ ou Visual Studio Code pour créer :
- `app.py`
- `templates\login.html`
- `templates\index.html`
- `templates\preview.html`
- `templates\stats.html`
- `templates\users.html`

**⚠️ Important** : Sauvegardez en UTF-8 sans BOM

## 5. Lancer l'application

```powershell
python app.py
```

Accédez à : `http://localhost:5000`

## 6. Démarrage automatique (Optionnel)

### Méthode 1 : Créer un raccourci dans le dossier de démarrage

1. Créez un fichier `start-cloud.bat` :

```batch
@echo off
cd C:\mon-cloud
python app.py
```

2. Appuyez sur `Win+R`, tapez `shell:startup`
3. Créez un raccourci vers `start-cloud.bat` dans ce dossier

### Méthode 2 : Service Windows (avancé)

Utilisez NSSM (Non-Sucking Service Manager) :

1. Téléchargez [NSSM](https://nssm.cc/download)
2. Exécutez :

```powershell
nssm install MonCloud "C:\Python39\python.exe" "C:\mon-cloud\app.py"
nssm start MonCloud
```

---

# 🌐 Accès depuis le réseau local

## Trouver votre adresse IP

**Linux/macOS :**
```bash
ip addr show  # Linux
ifconfig      # macOS
```

**Windows :**
```powershell
ipconfig
```

Cherchez une adresse comme `192.168.x.x`

## Accéder depuis d'autres appareils

Sur le même réseau WiFi, accédez à :
```
http://VOTRE_IP:5000
```

Exemple : `http://192.168.1.100:5000`

---

# 🔧 Configuration

## Changer le port

Dans `app.py`, ligne finale :

```python
app.run(host='0.0.0.0', port=8080, debug=True)  # Changez 5000 en 8080
```

## Ajouter des utilisateurs

**Méthode 1 : Interface web**
1. Connectez-vous en tant qu'admin
2. Allez sur "👥 Utilisateurs"
3. Ajoutez un nouvel utilisateur

**Méthode 2 : Modifier le code**

Dans `app.py`, modifiez :

```python
USERS = {
    'admin': generate_password_hash('admin123'),
    'marie': generate_password_hash('motdepasse123'),
    'jean': generate_password_hash('autremotdepasse')
}
```

## Désactiver le debug (production)

```python
app.run(host='0.0.0.0', port=5000, debug=False)
```

## Modifier la taille max des fichiers

Dans `app.py` :

```python
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1024 * 1024  # 1GB au lieu de 500MB
```

---

# 🔒 Sécurité

## Recommandations

1. **Changez la clé secrète** dans `app.py` :
   ```python
   app.secret_key = 'VOTRE_CLE_SECRETE_UNIQUE_ET_LONGUE'
   ```

2. **Changez le mot de passe admin** par défaut

3. **Utilisez HTTPS** en production (avec nginx/apache)

4. **Pare-feu** : Autorisez uniquement le port 5000 sur votre réseau local

5. **N'exposez PAS** directement sur Internet sans reverse proxy et HTTPS

---

# 📱 Utilisation

## Upload de fichiers

1. Connectez-vous
2. Cliquez sur "Choisir un fichier"
3. Sélectionnez votre fichier
4. Cliquez sur "Envoyer"

## Prévisualisation

Cliquez sur "👁️ Voir" pour :
- Images (JPG, PNG, GIF, WebP)
- PDF
- Vidéos (MP4, WebM)
- Audio (MP3, WAV)
- Fichiers texte

## Téléchargement

Cliquez sur "↓" pour télécharger un fichier

## Statistiques

Accédez à "📊 Stats" pour voir :
- Utilisation CPU
- Utilisation RAM
- Espace disque
- Espace cloud utilisé
- État de la batterie
- Temps de fonctionnement

---

# 🐛 Dépannage

## "Port already in use"

Le port 5000 est déjà utilisé. Changez le port dans `app.py` ou arrêtez l'autre application.

## "Module not found: flask"

```bash
pip3 install flask werkzeug psutil
```

## "Permission denied" sur Linux

```bash
sudo python3 app.py
# ou changez le port en >1024 (ex: 8080)
```

## Les fichiers uploadés disparaissent

Vérifiez que le dossier `uploads/` existe et a les bonnes permissions :

```bash
mkdir -p uploads
chmod 755 uploads
```

## Erreur "Invalid syntax" avec Python 3.5

Les f-strings ne sont pas supportées. Utilisez la version fournie qui utilise `.format()` à la place.

---

# 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter des fonctionnalités

---

# 📄 Licence

Ce projet est libre d'utilisation pour un usage personnel.

---

# 📞 Support

Pour toute question ou problème, créez une issue sur GitHub.

---

# 🎉 Bon cloud personnel !

Profitez de votre solution de stockage maison ! 
```

Sauvegardez avec `Ctrl+O`, `Entrée`, `Ctrl+X`.

Ce README complet couvre :
- ✅ Installation sur Linux/Ubuntu, macOS et Windows
- ✅ Configuration
- ✅ Démarrage automatique
- ✅ Accès réseau
- ✅ Sécurité
- ✅ Dépannage
- ✅ Utilisation

Vous pouvez le personnaliser selon vos besoins ! 📚
