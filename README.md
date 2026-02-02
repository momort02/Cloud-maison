# ☁️ Mon Cloud Personnel

Solution de **cloud personnel auto-hébergé**, simple et sécurisée, avec **interface web moderne**, développée en **Python (Flask)**.

Idéal pour stocker, prévisualiser et gérer vos fichiers depuis votre propre machine, sans dépendre de services tiers.

---

## 📌 Sommaire

- ✨ Fonctionnalités  
- 📋 Prérequis  
- 🐧 Installation Linux / Ubuntu  
- 🍎 Installation macOS  
- 🪟 Installation Windows  
- 🌐 Accès réseau local  
- 🔧 Configuration  
- 🔒 Sécurité  
- 📱 Utilisation  
- 🐛 Dépannage  
- 🤝 Contribution  
- 📄 Licence  

---

## ✨ Fonctionnalités

- 📤 **Upload de fichiers** via interface web
- 👁️ **Prévisualisation intégrée**
  - Images (JPG, PNG, GIF, WebP)
  - PDF
  - Vidéos (MP4, WebM)
  - Audio (MP3, WAV)
  - Fichiers texte
- 📊 **Statistiques système en temps réel**
  - CPU, RAM, disque
  - Batterie (si disponible)
  - Temps de fonctionnement
- 👥 **Multi-utilisateurs** avec interface d'administration
- 📱 **Design responsive** (mobile, tablette, PC)
- 🔒 **Sécurité** avec mots de passe hashés

---

## 📋 Prérequis

| Système | Version Python |
|-------|----------------|
| Linux / Ubuntu | Python 3.5+ |
| macOS | Python 3.6+ |
| Windows | Python 3.6+ |

---

## 🐧 Installation Linux / Ubuntu

### 1️⃣ Installer les dépendances


sudo apt update
sudo apt install python3 python3-pip python3-flask python3-psutil

2️⃣ Créer la structure du projet

mkdir -p ~/mon-cloud/{templates,uploads}
cd ~/mon-cloud

3️⃣ Créer les fichiers

app.py
templates/login.html
templates/index.html
templates/preview.html
templates/stats.html
templates/users.html

4️⃣ Lancer l'application

python3 app.py

Accès :

http://localhost:5000

Identifiants par défaut :

Utilisateur : admin
Mot de passe : admin123


---

🍎 Installation macOS

1️⃣ Installer Homebrew (si nécessaire)

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2️⃣ Installer Python

brew install python3

3️⃣ Installer les dépendances

pip3 install flask werkzeug psutil

4️⃣ Lancer l'application

python3 app.py

Accès :

http://localhost:5000


---

🪟 Installation Windows

1️⃣ Installer Python

Télécharger depuis https://www.python.org
Cocher "Add Python to PATH"

2️⃣ Installer les dépendances

pip install flask werkzeug psutil

3️⃣ Créer la structure du projet

mkdir C:\mon-cloud\templates
mkdir C:\mon-cloud\uploads
cd C:\mon-cloud

4️⃣ Créer les fichiers

app.py
templates\login.html
templates\index.html
templates\preview.html
templates\stats.html
templates\users.html

⚠️ Sauvegardez les fichiers en UTF-8 sans BOM

5️⃣ Lancer l'application

python app.py


---

🌐 Accès réseau local

Trouver votre adresse IP

ip addr     # Linux
ifconfig    # macOS

ipconfig    # Windows

Accès depuis un autre appareil

http://VOTRE_IP:5000

Exemple :

http://192.168.1.42:5000


---

# 🔧 Configuration

Changer le port

app.run(host="0.0.0.0", port=8080, debug=False)

Ajouter des utilisateurs

USERS = {
    "admin": generate_password_hash("admin123"),
    "user1": generate_password_hash("motdepasse")
}

Modifier la taille maximale des fichiers

app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024  # 1 Go


---

# 🔒 Sécurité

Recommandations importantes :

- Modifier la clé secrète Flask
- Changer le mot de passe admin
- Utiliser HTTPS (Nginx / Apache)
- Ne pas exposer directement sur Internet


---

# 📱 Utilisation

1. Se connecter
2. Choisir un fichier
3. Envoyer
4. Prévisualiser ou télécharger


---

# 🐛 Dépannage

## Port déjà utilisé

Changer le port ou arrêter l'application conflictuelle

## Module introuvable

pip install flask werkzeug psutil

## Problème de permissions Linux

chmod 755 uploads


---

# 🤝 Contribution

- Bugs
- Améliorations
- Nouvelles fonctionnalités


---

# 📄 Licence

Projet libre pour un usage personnel et éducatif.


---

# 🎉 Bon cloud personnel !

Créez votre propre solution de stockage locale et sécurisée ☁️
