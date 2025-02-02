# SecureCloudAutoBackupProject

![logo](https://github.com/user-attachments/assets/c3e8294d-9bcb-4547-b68d-49c42827bf31)

## Опис
SecureCloudAutoBackupProject — це рішення для автоматичного резервного копіювання файлів у хмарне сховище Google Drive. Проєкт передбачає просту установку та зручний графічний інтерфейс для керування сценаріями копіювання.

## Встановлення

### 1. Завантаження та підготовка файлів
1. Завантажте та розпакуйте архів `SecureCloudAutoBackupProject.rar` у локальну директорію.
2. Ви отримаєте папку `SecureCloudAutoBackupProject`, з якою будемо працювати.

### 2. Отримання API ключа
1. Для доступу до Google Drive необхідно отримати власний API ключ.
2. Назвіть файл ключа **точно** `client_secrets.json`.
3. Помістіть його у папку: `SecureCloudAutoBackupProject/_internal/projPath`.

### 3. Запуск програми
1. У директорії `SecureCloudAutoBackupProject` знайдіть файл `autoBackup.exe`.
2. Його необхідно запускати у фоновому режимі під час старту ОС. Для цього відкрийте **Командний рядок** та виконайте команду:
   ```sh
   reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v SCAutoBackup /t REG_SZ /d "C:\SecureCloudAutoBackupProject\autoBackup.exe" /f
   ```
   ⚠ **Зверніть увагу!** Якщо шлях до файлу відрізняється, вкажіть його власноруч.

## Налаштування сценаріїв

### 1. Запуск графічного інтерфейсу
- Якщо ви скористалися ярликом `SC Auto Backup`, відкрийте його.
- Або ж відкрийте `SecureCloudAutoBackupProject/_internal/projPath` та запустіть `guiPath.exe` вручну.

### 2. Створення сценарію
1. Виконуйте логічні інструкції у графічному інтерфейсі.
2. Після створення сценарію перезавантажте систему для активації автоматичного резервного копіювання.
3. Подальші зміни у сценаріях будуть застосовуватися автоматично без перезапуску ОС.

## Важлива інформація
🔑 Під час створення сценарію ви отримаєте **унікальний ключ** для шифрування резервних копій.
- **Збережіть цей ключ!** У разі його втрати розшифрувати резервні копії буде неможливо.

---

✨ **Приємного користування!**
