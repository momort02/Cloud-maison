# ☁️ Mon Cloud Personnel

Solution de **cloud personnel auto-hébergé**, simple et sécurisée, avec **interface web moderne**, développée en **Python (Flask)**.

Idéal pour stocker, prévisualiser et gérer vos fichiers depuis votre propre machine, sans dépendre de services tiers.

---

## 📌 Sommaire

* ✨ Fonctionnalités
* 📋 Prérequis
* 🐧 Installation Linux / Ubuntu
* 🍎 Installation macOS
* 🪟 Installation Windows
* 🌐 Accès réseau local
* 🔧 Configuration
* 🔒 Sécurité
* 📱 Utilisation
* 🐛 Dépannage
* 🤝 Contribution
* 📄 Licence

---

## ✨ Fonctionnalités

* 📤 **Upload de fichiers** via interface web
* 👁️ **Prévisualisation intégrée**

  * Images (JPG, PNG, GIF, WebP)
  * PDF
  * Vidéos (MP4, WebM)
  * Audio (MP3, WAV)
  * Fichiers texte
* 📊 **Statistiques système en temps réel**

  * CPU, RAM, disque
  * Batterie (si disponible)
  * Temps de fonctionnement
* 👥 **Multi-utilisateurs** avec interface d'administration
* 📱 **Design responsive** (mobile, tablette, PC)
* 🔒 **Sécurité** avec mots de passe hashés

---

## 📋 Prérequis

| Système        | Version Python |
| -------------- | -------------- |
| Linux / Ubuntu | Python 3.5+    |
| macOS          | Python 3.6+    |
| Windows        | Python 3.5+    |

---

## 🐧 Installation Linux / Ubuntu

### 1️⃣ Installer les dépendances système

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
```

### 2️⃣ Créer la structure du projet

```bash
mkdir -p ~/serveur
cd ~/serveur
```

### 3️⃣ Télécharger le dépôt

```bash
git clone https://github.com/momort02/Cloud-maison.git mon-cloud
cd mon-cloud
```

### 4️⃣ Installer les dépendances Python

```bash
pip3 install -r requirements.txt || pip3 install flask werkzeug psutil
```

### 5️⃣ Lancer l'application

```bash
python3 app.py
```

➡️ Accès : [http://localhost:5000](http://localhost:5000)

Identifiants par défaut :

* Utilisateur : **admin**
* Mot de passe : **admin123**

---

## 🍎 Installation macOS

### 1️⃣ Installer Homebrew (si nécessaire)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2️⃣ Installer Python 3

```bash
brew update
brew install python
```

Vérifier :

```bash
python3 --version
pip3 --version
```

### 3️⃣ Télécharger le projet

```bash
mkdir -p ~/serveur
cd ~/serveur
git clone https://github.com/momort02/Cloud-maison.git mon-cloud
cd mon-cloud
```

### 4️⃣ Installer les dépendances Python

```bash
pip3 install -r requirements.txt || pip3 install flask werkzeug psutil
```

### 5️⃣ Lancer l'application

```bash
python3 app.py
```

➡️ Accès : [http://localhost:5000](http://localhost:5000)

ℹ️ macOS demandera parfois une autorisation réseau au premier lancement.

---

## 🪟 Installation Windows

### 1️⃣ Installer Python

* Télécharger Python depuis le site officiel
* **Cocher impérativement** : `Add Python to PATH`

Vérifier dans l’invite de commandes (cmd) :

```bat
python --version
pip --version
```

### 2️⃣ Télécharger le projet

Option A – via Git :

```bat
cd %USERPROFILE%
mkdir serveur
cd serveur
git clone https://github.com/momort02/Cloud-maison.git mon-cloud
cd mon-cloud
```

Option B – ZIP :

* Télécharger l’archive GitHub
* Extraire dans `C:\Users\VotreNom\serveur\mon-cloud`

### 3️⃣ Installer les dépendances Python

```bat
pip install -r requirements.txt
```

Si `requirements.txt` n’existe pas :

```bat
pip install flask werkzeug psutil
```

### 4️⃣ Lancer l'application

```bat
python app.py
```

➡️ Accès : [http://localhost:5000](http://localhost:5000)

⚠️ Autoriser Python dans le pare-feu Windows si demandé.

---

## 🌐 Accès réseau local

Trouver votre adresse IP :

```bash
ip addr      # Linux
ifconfig     # macOS
ipconfig     # Windows
```

Depuis un autre appareil sur le même réseau :

```
http://VOTRE_IP:5000
```

Exemple : `http://192.168.1.42:5000`

---

## 🔧 Configuration

### Changer le port

```python
app.run(host="0.0.0.0", port=8080, debug=False)
```

### Ajouter des utilisateurs

```python
USERS = {
    "admin": generate_password_hash("admin123"),
    "user1": generate_password_hash("motdepasse")
}
```

### Modifier la taille maximale des fichiers

```python
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024  # 1 Go
```

---

## 🔒 Sécurité

Recommandations importantes :

* Modifier la `SECRET_KEY` Flask
* Changer le mot de passe admin
* Mettre Flask derrière **Nginx / Apache**
* Activer **HTTPS**
* Ne pas exposer directement le port 5000 sur Internet

---

## 📱 Utilisation

1. Ouvrir l’interface web
2. Se connecter
3. Uploader un fichier
4. Prévisualiser ou télécharger

---

## 🐛 Dépannage

### Port déjà utilisé

Changer le port ou arrêter le service concerné.

### Module introuvable

```bash
pip install flask werkzeug psutil
```

### Problème de permissions (Linux/macOS)

```bash
chmod -R 755 uploads
```

---

## 🤝 Contribution

* Signalement de bugs
* Propositions d’améliorations
* Ajout de nouvelles fonctionnalités

---

## 📄 Licence

Projet libre pour un usage **personnel et éducatif**.

---

## 🎉 Bon cloud personnel !

Créez votre propre solution de stockage locale et sécurisée ☁️
