#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import psutil
import platform
import time

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_changez_moi'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024

USERS = {
    'admin': generate_password_hash('admin123')
}

def get_file_size(filepath):
    size = os.path.getsize(filepath)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return "{:.1f} {}".format(size, unit)
        size = size / 1024.0
    return "{:.1f} {}".format(size, unit)

def get_file_icon(filename):
    if '.' in filename:
        ext = filename.split('.')[-1].lower()
    else:
        ext = ''
    
    icons = {
        'pdf': '📕', 'doc': '📘', 'docx': '📘', 'xls': '📗', 'xlsx': '📗',
        'ppt': '📙', 'pptx': '📙', 'txt': '📝',
        'jpg': '🖼️', 'jpeg': '🖼️', 'png': '🖼️', 'gif': '🖼️', 'webp': '🖼️',
        'mp4': '🎬', 'avi': '🎬', 'mkv': '🎬', 'mov': '🎬',
        'mp3': '🎵', 'wav': '🎵', 'flac': '🎵',
        'zip': '📦', 'rar': '📦', '7z': '📦',
        'py': '🐍', 'js': '📜', 'html': '🌐', 'css': '🎨'
    }
    return icons.get(ext, '📄')

def can_preview(filename):
    if '.' in filename:
        ext = filename.split('.')[-1].lower()
    else:
        ext = ''
    
    preview_exts = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'pdf', 'txt', 'mp4', 'webm', 'mp3', 'wav']
    return ext in preview_exts

@app.route('/')
@app.route('/folder/<path:folder_path>')
def index(folder_path=''):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    files = []
    folders = []
    current_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_path)
    
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    
    for item in os.listdir(current_path):
        item_path = os.path.join(current_path, item)
        
        if os.path.isdir(item_path):
            folders.append({
                'name': item,
                'path': os.path.join(folder_path, item) if folder_path else item
            })
        elif os.path.isfile(item_path):
            files.append({
                'name': item,
                'size': get_file_size(item_path),
                'date': datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%d/%m/%Y %H:%M'),
                'icon': get_file_icon(item),
                'can_preview': can_preview(item),
                'path': folder_path
            })
    
    folders.sort(key=lambda x: x['name'])
    files.sort(key=lambda x: x['date'], reverse=True)
    
    breadcrumb = []
    if folder_path:
        parts = folder_path.split('/')
        path = ''
        for part in parts:
            path = os.path.join(path, part) if path else part
            breadcrumb.append({'name': part, 'path': path})
    
    return render_template('index.html', 
        files=files, 
        folders=folders,
        current_folder=folder_path,
        breadcrumb=breadcrumb,
        username=session['username']
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in USERS and check_password_hash(USERS[username], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Identifiants incorrects')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/upload', methods=['POST'])
def upload():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if 'file' not in request.files:
        flash('Aucun fichier selectionne')
        return redirect(url_for('index'))
    
    files = request.files.getlist('file')
    current_folder = request.form.get('current_folder', '')
    
    if not files or files[0].filename == '':
        flash('Aucun fichier selectionne')
        return redirect(url_for('index', folder_path=current_folder))
    
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], current_folder)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    uploaded_count = 0
    for file in files:
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_path, filename))
            uploaded_count = uploaded_count + 1
    
    if uploaded_count == 1:
        flash('1 fichier uploade avec succes')
    else:
        flash(str(uploaded_count) + ' fichiers uploades avec succes')
    
    return redirect(url_for('index', folder_path=current_folder))

@app.route('/view/<path:filepath>')
def view(filepath):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filepath)

@app.route('/download/<path:filepath>')
def download(filepath):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filepath, as_attachment=True)

@app.route('/preview/<path:filepath>')
def preview(filepath):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    filename = os.path.basename(filepath)
    if '.' in filename:
        ext = filename.split('.')[-1].lower()
    else:
        ext = ''
    
    return render_template('preview.html', filename=filename, filepath=filepath, extension=ext)

@app.route('/delete/<path:filepath>')
def delete(filepath):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], filepath)
    if os.path.exists(full_path):
        os.remove(full_path)
        flash('Fichier supprime')
    
    folder_path = os.path.dirname(filepath)
    return redirect(url_for('index', folder_path=folder_path))

@app.route('/stats')
def stats():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    memory = psutil.virtual_memory()
    memory_total = memory.total / (1024**3)
    memory_used = memory.used / (1024**3)
    memory_percent = memory.percent
    
    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024**3)
    disk_used = disk.used / (1024**3)
    disk_free = disk.free / (1024**3)
    disk_percent = disk.percent
    
    upload_size = 0
    upload_count = 0
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(filepath):
                upload_size = upload_size + os.path.getsize(filepath)
                upload_count = upload_count + 1
    upload_size_gb = upload_size / (1024**3)
    
    battery_info = None
    try:
        if hasattr(psutil, 'sensors_battery'):
            battery = psutil.sensors_battery()
            if battery:
                battery_info = {
                    'percent': battery.percent,
                    'plugged': battery.power_plugged,
                    'time_left': battery.secsleft if battery.secsleft != -1 else None
                }
    except Exception:
        pass
    
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    
    system_info = {
        'os': platform.system(),
        'os_version': platform.release(),
        'hostname': platform.node(),
        'architecture': platform.machine()
    }
    
    return render_template('stats.html', 
        cpu_percent=cpu_percent,
        cpu_count=cpu_count,
        memory_total=memory_total,
        memory_used=memory_used,
        memory_percent=memory_percent,
        disk_total=disk_total,
        disk_used=disk_used,
        disk_free=disk_free,
        disk_percent=disk_percent,
        upload_size_gb=upload_size_gb,
        upload_count=upload_count,
        battery=battery_info,
        uptime_hours=uptime_hours,
        uptime_minutes=uptime_minutes,
        system_info=system_info,
        username=session['username']
    )

@app.route('/create_folder', methods=['POST'])
def create_folder():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    folder_name = request.form.get('folder_name', '').strip()
    current_folder = request.form.get('current_folder', '')
    
    if not folder_name:
        flash('Nom de dossier requis')
        return redirect(url_for('index', folder_path=current_folder))
    
    folder_name = secure_filename(folder_name)
    new_folder_path = os.path.join(app.config['UPLOAD_FOLDER'], current_folder, folder_name)
    
    if os.path.exists(new_folder_path):
        flash('Ce dossier existe deja')
    else:
        os.makedirs(new_folder_path)
        flash('Dossier ' + folder_name + ' cree avec succes')
    
    return redirect(url_for('index', folder_path=current_folder))

@app.route('/delete_folder/<path:folder_path>')
def delete_folder(folder_path):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    folder_full_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_path)
    
    if os.path.exists(folder_full_path) and os.path.isdir(folder_full_path):
        import shutil
        shutil.rmtree(folder_full_path)
        flash('Dossier supprime')
    
    parent_folder = os.path.dirname(folder_path)
    return redirect(url_for('index', folder_path=parent_folder))

@app.route('/users', methods=['GET', 'POST'])
def users():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if session['username'] != 'admin':
        flash('Acces refuse. Reserve a l\'administrateur.')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        new_user = request.form['username']
        new_pass = request.form['password']
        
        if new_user and new_pass:
            if new_user in USERS:
                flash('Cet utilisateur existe deja')
            else:
                USERS[new_user] = generate_password_hash(new_pass)
                flash('Utilisateur ' + new_user + ' ajoute avec succes')
        else:
            flash('Nom d\'utilisateur et mot de passe requis')
    
    return render_template('users.html', users=list(USERS.keys()), username=session['username'])

@app.route('/delete_user/<username>')
def delete_user(username):
    if 'username' not in session or session['username'] != 'admin':
        return redirect(url_for('login'))
    
    if username == 'admin':
        flash('Impossible de supprimer l\'administrateur')
    elif username in USERS:
        del USERS[username]
        flash('Utilisateur ' + username + ' supprime')
    
    return redirect(url_for('users'))

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=5000, debug=True)