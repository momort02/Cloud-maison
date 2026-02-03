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
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    files = []
    upload_path = app.config['UPLOAD_FOLDER']
    
    if os.path.exists(upload_path):
        for filename in os.listdir(upload_path):
            filepath = os.path.join(upload_path, filename)
            if os.path.isfile(filepath):
                files.append({
                    'name': filename,
                    'size': get_file_size(filepath),
                    'date': datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%d/%m/%Y %H:%M'),
                    'icon': get_file_icon(filename),
                    'can_preview': can_preview(filename)
                })
    
    files.sort(key=lambda x: x['date'], reverse=True)
    
    return render_template('index.html', files=files, username=session['username'])

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
    
    file = request.files['file']
    
    if file.filename == '':
        flash('Aucun fichier selectionne')
        return redirect(url_for('index'))
    
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Fichier uploade avec succes')
    
    return redirect(url_for('index'))

@app.route('/view/<filename>')
def view(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/download/<filename>')
def download(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/preview/<filename>')
def preview(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if '.' in filename:
        ext = filename.split('.')[-1].lower()
    else:
        ext = ''
    
    return render_template('preview.html', filename=filename, extension=ext)

@app.route('/delete/<filename>')
def delete(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash('Fichier supprime')
    
    return redirect(url_for('index'))

@app.route('/stats')
def stats():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # RAM
    memory = psutil.virtual_memory()
    memory_total = memory.total / (1024**3)
    memory_used = memory.used / (1024**3)
    memory_percent = memory.percent
    
    # Disque
    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024**3)
    disk_used = disk.used / (1024**3)
    disk_free = disk.free / (1024**3)
    disk_percent = disk.percent
    
    # Espace uploads
    upload_size = 0
    upload_count = 0
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(filepath):
                upload_size = upload_size + os.path.getsize(filepath)
                upload_count = upload_count + 1
    upload_size_gb = upload_size / (1024**3)
    
    # Batterie (avec gestion d'erreur pour anciennes versions de psutil)
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
    
    # Uptime
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    
    # Info système
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

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=5000, debug=True)