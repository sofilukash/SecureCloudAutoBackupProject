import os
import sys
import time
import json
import shutil
import base64
import threading
from datetime import datetime

import schedule
from cryptography.fernet import Fernet

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def zip_folder(folder_path, zip_name):
    current_date = datetime.now().strftime('%Y-%m-%d__%H-%M-%S')
    zip_name_with_date = f"{zip_name}_{current_date}"
    shutil.make_archive(zip_name_with_date, 'zip', folder_path)
    return zip_name_with_date + '.zip'

def authenticate_google_drive(user_email):
    try:
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        _internal_dir = os.path.join(project_dir, 'projPath', '_internal')
        user_dir = os.path.join(_internal_dir, 'root', user_email)
        token_path = os.path.join(user_dir, 'token.json')

        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/drive.file'])

            if creds and creds.valid:
                print(f"Користувач {user_email} успішно автентифікований.")
                return build('drive', 'v3', credentials=creds)

            elif creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                with open(token_path, 'w') as token_file:
                    token_file.write(creds.to_json())
                print(f"Користувач {user_email} успішно автентифікований після оновлення токену.")
                return build('drive', 'v3', credentials=creds)
            else:
                print(f"Токен користувача {user_email} не дійсний і не можна оновити.")
        else:
            print(f"Файл {token_path} не знайдено для {user_email}.")
    except Exception as e:
        print(f'Помилка автентифікації для {user_email}:', e)

    return None

def encrypt_folder(folder_path, key):
    fernet = Fernet(key)
    encrypted_folder_path = folder_path + "_encrypted"

    # Копіюємо вміст папки для шифрування
    shutil.copytree(folder_path, encrypted_folder_path)

    # Шифруємо файли
    for root, dirs, files in os.walk(encrypted_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                original_data = f.read()
            encrypted_data = fernet.encrypt(original_data)
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)

    return encrypted_folder_path

def upload_to_drive(drive_service, file_path, main_folder_name, folder_name):
    query = f"mimeType = 'application/vnd.google-apps.folder' and name = '{main_folder_name}'"
    results = drive_service.files().list(q=query).execute()
    items = results.get('files', [])

    if not items:
        file_metadata = {'name': main_folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
        folder = drive_service.files().create(body=file_metadata, fields='id').execute()
        main_folder_id = folder.get('id')
        print(f"Основна папка '{main_folder_name}' була створена. ID: {main_folder_id}")
    else:
        main_folder_id = items[0]['id']
        print(f"Основна папка '{main_folder_name}' знайдена. ID: {main_folder_id}")

    query = f"mimeType = 'application/vnd.google-apps.folder' and name = '{folder_name}' and '{main_folder_id}' in parents"
    results = drive_service.files().list(q=query).execute()
    items = results.get('files', [])

    if not items:
        file_metadata = {'name': folder_name, 'mimeType': 'application/vnd.google-apps.folder',
                         'parents': [main_folder_id]}
        folder = drive_service.files().create(body=file_metadata, fields='id').execute()
        subfolder_id = folder.get('id')
        print(f"Підпапка '{folder_name}' була створена в папці '{main_folder_name}'. ID: {subfolder_id}")
    else:
        subfolder_id = items[0]['id']
        print(f"Підпапка '{folder_name}' знайдена в папці '{main_folder_name}'. ID: {subfolder_id}")

    file_metadata = {'name': os.path.basename(file_path), 'parents': [subfolder_id]}  # Вказуємо ID підпапки в 'parents'
    media = MediaFileUpload(file_path, mimetype='application/zip')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print(f"Файл завантажено в підпапку '{folder_name}' у папці '{main_folder_name}'. ID файлу: {file.get('id')}")
    return file.get('id')

def load_tasks():
    project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    _internal_dir = os.path.join(project_dir, 'projPath', '_internal')
    root_dir = os.path.join(_internal_dir, 'root')
    tasks = []
    for user_folder in os.listdir(root_dir):
        user_folder_path = os.path.join(root_dir, user_folder)
        if os.path.isdir(user_folder_path):
            backup_file_path = os.path.join(user_folder_path, 'backup.json')
            if os.path.exists(backup_file_path):
                with open(backup_file_path, 'r') as backup_file:
                    data = json.load(backup_file)
                    print(f"Знайдено завдання: {data}")
                    tasks.extend(data)
    return tasks

def run_task(task):
    print(f"Запуск резервного копіювання для {task['user_email']} в папку {task['backup_folder']}")
    project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    main_dir = os.path.join(project_dir, 'projPath')
    _internal_dir = os.path.join(main_dir, '_internal')
    root_dir = os.path.join(_internal_dir, 'root')
    backups_dir = os.path.join(_internal_dir, 'backups')

    os.makedirs(backups_dir, exist_ok=True)
    user_email = task['user_email']
    print({user_email})
    user_folder_path = os.path.join(root_dir, user_email)
    if os.path.isdir(user_folder_path):
        credentials_file_path = os.path.join(main_dir, 'client_secrets.json')
        if os.path.exists(credentials_file_path):
            user_email = task['user_email']
            file_path = task['backup_folder']
            days = task['schedule_days']
            backup_time = task['schedule_time']
            encoded_key = task.get('password_hash', '')
            key = base64.urlsafe_b64decode(encoded_key.encode()) if encoded_key else None
            if os.path.exists(file_path):
                folder_name = os.path.basename(file_path)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                destination_path = os.path.join(backups_dir, f"{folder_name}_{timestamp}")
                shutil.copytree(file_path, destination_path)
                encrypted_folder = encrypt_folder(destination_path, key)
                zip_file = zip_folder(encrypted_folder, os.path.join(backups_dir, folder_name))
                drive_service = authenticate_google_drive(user_email)
                if drive_service:
                    drive_folder_name = f"{folder_name}_{''.join([d[0] for d in days])}_{backup_time}"
                    upload_to_drive(drive_service, zip_file, 'backups', drive_folder_name)
                    shutil.rmtree(encrypted_folder)
                    os.remove(zip_file)
                    shutil.rmtree(destination_path)

                    print(f"Завдання для {user_email}, резервне копіювання в {file_path} за розкладом: {days} о {backup_time}")

def check_schedule(tasks):
    today_day = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M')

    print(f"Сьогодні {today_day}, поточний час: {current_time}")

    for task in tasks:
        task_time = task['schedule_time'][:5]
        print(f"Перевіряю завдання: {task}")
        print(f"Заплановані дні: {task['schedule_days']}, Запланований час: {task_time}")

        if today_day in task['schedule_days'] and current_time == task_time:
            print(f"Виконую завдання для {task['user_email']} у новому потоці")
            backup_thread = threading.Thread(target=run_task, args=(task,))
            backup_thread.start()
def scheduled_task():
    print("Перевірка розкладу...")
    tasks = load_tasks()
    check_schedule(tasks)


if __name__ == "__main__":
    schedule.every(60).seconds.do(scheduled_task)
    while True:
        schedule.run_pending()
        time.sleep(20)
