Дана коротка інструкція допоможе встановити представлений проєкт локально у ОС Windows. Зверніть увагу кожен предсалений крок має бути виконано!
1. Для початку завантажте та розпакуйте архів SecureCloudAutoBackupProject.rar у локальну дикекторію. Ви отримаєте папку з якою будемо далі працювати.
2. Для того, щоб програма змогла отримати доступ до GoogleDrive необхідно отримати власний API ключ, врахуйте, що його назва має бути точно так "client_secrets.json".
3. Тепер даний файл необхідно залишити за адресою (відносно отриманої папки) SecureCloudAutoBackupProject/_internal/projPath.
4. (Опціонально) в паці projPath знаходиться ярлик-посилання "SC Auto Backup" на файл з графіним інтерфейсом, за допомогою якого ви зможете налаштовувати сценарії для копіювання.
5. Знову повертаємося до вмісту папки SecureCloudAutoBackupProject, а саме до файлу autoBackup.exe, його необхідно запускати у фоновому режимі під час запуску ОС.
Для цього необхідно відкрити командний рядок та виконати команду "reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v SCAutoBackup /t REG_SZ /d "C:\SecureCloudAutoBackupProject\autoBackup.exe" /f". Зверніть увагу, шлях до файлу необхідно задати власний, якщо він відрізняється від прикладу!

На цьому технічні налаштування закінчено, переходимо до налаштування сценаріїв!

1. Якщо ви виконали 4 крок та створили ярлик на робочому столі, то переходимо з цим посиланням на виконуваний файл.
Якщо ні, то переходимо за відносним шляхом SecureCloudAutoBackupProject/_internal/projPath та запускаємо файл guiPath.exe самостійно.
2. Буде представлено графіний інтерфейс, де необхідно слідвати логічним інструкціям та створити свій перший сценарій для резервного копіювання у хмару.
Коли сценарій налаштовано, перезавантажуємо систему, і маємо налаштоване резервне копіювання. При цьому не обов'язково перезавантажувати ОС кожний раз після створення сценарію, він автоматично буде врахований.

Зверніть увагу, при створенні сценарію вам буде видано унікальний ключ, якй буде шифрувати всі резервні копії в межах сценарію. Даний ключ необхідно надійно зберегти, у разі втрати ключа, шанс вилучити резервні копію буде втрачено.

Приємного досвіду!
