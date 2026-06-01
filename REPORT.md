# Лабораторная работа №?

Данная лабораторная работа посвящена изучению технологии работы с контейнерами.

Репозиторий:https://github.com/xkolyaa/lab_docker

### 1. Установка Docker и Git

Команда:```sudo apt-get update && sudo apt-get install -y git nano docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin```

### 2. Настройка Git и подготовка переменны

Команда:
```
export GITHUB_USERNAME="ИМЯ_ПОЛЬЗОВАТЕЛЯ"
alias edit=nano
```

### 3. Скачивание исходного кода лабораторной

Команда:
```
git clone https://github.com/tp-lessons/lab_docker temp_lab
cd temp_lab
```

Вывод:
```
Cloning into 'temp_lab'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 16 (delta 1), reused 13 (delta 1), pack-reused 0 (from 0)
Receiving objects: 100% (16/16), 5.01 KiB | 5.01 MiB/s, done.
Resolving deltas: 100% (1/1), done
```

### 4. Создание локального репозитория

Команда:
```
mkdir -p ~/projects/lab_docker
cp -r app db LICENSE README.md ~/projects/lab_docker/
cd ~/projects/lab_docker
git init
git add .
git commit -m "Initial commit from template"
```

Вывод:
```
Initialized empty Git repository in /home/codespace/projects/lab_docker/.git/
[main (root-commit) a561ae5] Initial commit from template
 7 files changed, 228 insertions(+)
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 app/app.py
 create mode 100644 app/models.py
 create mode 100644 app/requirements.txt
 create mode 100644 app/templates/index.html
 create mode 100644 db/init.sql
 ```
### 5. Связывание с GitHub

Команда:
```
git remote add origin https://github.com{GITHUB_USERNAME}/lab_docker.git
git branch -M main
git push -u origin main
```

Вывод:
```
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 2 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (12/12), 4.04 KiB | 4.04 MiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/xkolyaa/lab_docker.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'
```

### 6. Создание файлов main.py и requirements.tx

Команда:
```
cat > main.py << 'EOF'
print("Hello, Docker!")
EOF

cat > requirements.txt << 'EOF'
flask
requests
EOF
```

### 7. Создание Dockerfile

Команда:
```
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
EOF
```

### 8. Сборка и запуск Docker-контейнера

Команда:
```
docker build -t lab-docker .
docker run --rm -it lab-docker
```

Вывод:
```
[+] Building 52.6s (12/12) FINISHED                                                                                                         docker:default
 => [internal] load build definition from Dockerfile                                                                                                  0.0s
 => => transferring dockerfile: 253B                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                    1.1s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                         0.0s
 => [internal] load .dockerignore                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                       0.0s
 => [1/6] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              2.2s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              0.0s
 => => sha256:fc74430849022d13b0d44b8969a953f842f59c6e9d1a0c2c83d710affa286c08 13.88MB / 13.88MB                                                      0.4s
 => => sha256:b3ec39b36ae8c03a3e09854de4ec4aa08381dfed84a9daa075048c2e3df3881d 1.29MB / 1.29MB                                                        0.4s
 => => sha256:ea56f685404adf81680322f152d2cfec62115b30dda481c2c450078315beb508 251B / 251B                                                            0.4s
 => => sha256:38513bd7256313495cdd83b3b0915a633cfa475dc2a07072ab2c8d191020ca5d 29.78MB / 29.78MB                                                      0.7s
 => => extracting sha256:38513bd7256313495cdd83b3b0915a633cfa475dc2a07072ab2c8d191020ca5d                                                             0.8s
 => => extracting sha256:b3ec39b36ae8c03a3e09854de4ec4aa08381dfed84a9daa075048c2e3df3881d                                                             0.1s
 => => extracting sha256:fc74430849022d13b0d44b8969a953f842f59c6e9d1a0c2c83d710affa286c08                                                             0.5s
 => => extracting sha256:ea56f685404adf81680322f152d2cfec62115b30dda481c2c450078315beb508                                                             0.0s
 => [internal] load build context                                                                                                                     0.0s
 => => transferring context: 46.21kB                                                                                                                  0.0s
 => [2/6] WORKDIR /app                                                                                                                                1.5s
 => [3/6] RUN apt-get update && apt-get install -y     build-essential                                                                               19.0s
 => [4/6] COPY requirements.txt .                                                                                                                     0.1s 
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                          5.8s 
 => [6/6] COPY . .                                                                                                                                    0.1s 
 => exporting to image                                                                                                                               22.7s 
 => => exporting layers                                                                                                                              19.6s 
 => => exporting manifest sha256:caf63ca88e97ad5ebfb49a3fe248422a05e9fb19c27914da431c9f15dd569da3                                                     0.0s 
 => => exporting config sha256:9e914c98b993fc7bf57e16f6f507f275faae104b41eaeb3feb20351b8512f7c2                                                       0.0s 
 => => exporting attestation manifest sha256:e09e76d041ae6178dd819ade5b570999cca503e1de844b01f00661d8abd85e4a                                         0.0s 
 => => exporting manifest list sha256:df95a7d1610980c48506718b9ab701a37273ebb1c8eba29846cbde2d34953f4d                                                0.0s
 => => naming to docker.io/library/lab-docker:latest                                                                                                  0.0s
 => => unpacking to docker.io/library/lab-docker:latest                                                                                               3.0s
Hello, Docker!
```

### 9. Настройка многоконтейнерной среды

Команда:
```
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  app:
    build: . 
    container_name: lab_docker
    depends_on:
      db:
        condition: service_healthy
    environment:
      - DB_HOST=db
      - DB_USER=db_user
      - DB_PASSWORD=secret
      - DB_NAME=lab_db

  db:
    image: mysql:8.0
    container_name: mysql_db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: secret_root_pass
      MYSQL_DATABASE: lab_db
      MYSQL_USER: db_user
      MYSQL_PASSWORD: secret
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  db_data:
EOF
```

### 10. Запуск Docker Compose

Команда:
```
docker compose up --build
```

Вывод:
```
WARN[0000] /home/codespace/projects/lab_docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 0.9s (14/14) FINISHED                                                                                                                         
 => [internal] load local bake definitions                                                                                                            0.0s
 => => reading from stdin 516B                                                                                                                        0.0s
 => [internal] load build definition from Dockerfile                                                                                                  0.0s
 => => transferring dockerfile: 253B                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                    0.5s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                         0.0s
 => [internal] load .dockerignore                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                       0.0s
 => [1/6] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              0.0s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              0.0s
 => [internal] load build context                                                                                                                     0.0s
 => => transferring context: 4.15kB                                                                                                                   0.0s
 => CACHED [2/6] WORKDIR /app                                                                                                                         0.0s
 => CACHED [3/6] RUN apt-get update && apt-get install -y     build-essential                                                                         0.0s
 => CACHED [4/6] COPY requirements.txt .                                                                                                              0.0s
 => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                   0.0s
 => [6/6] COPY . .                                                                                                                                    0.0s
 => exporting to image                                                                                                                                0.1s
 => => exporting layers                                                                                                                               0.0s
 => => exporting manifest sha256:857647b872db0deae89354762400438e9931ca95039c240bcd1319e83a951432                                                     0.0s
 => => exporting config sha256:b79f2e676ae20cbdca39cc44d1b00d58da524edab6e35279bfde5368baf12abe                                                       0.0s
 => => exporting attestation manifest sha256:d5ce35c2ff56daab3bdc920525e56e7f74098588054563be5d07803f6a5209b3                                         0.0s
 => => exporting manifest list sha256:69fc0480d57988d78e1d07067b0cd670cf18f5857639c039d68aef8d68c50d7d                                                0.0s
 => => naming to docker.io/library/lab_docker-app:latest                                                                                              0.0s
 => => unpacking to docker.io/library/lab_docker-app:latest                                                                                           0.0s
 => resolving provenance for metadata file                                                                                                            0.0s
[+] up 5/5
 ✔ Image lab_docker-app       Built                                                                                                                    0.9s
 ✔ Network lab_docker_default Created                                                                                                                  0.1s
 ✔ Volume lab_docker_db_data  Created                                                                                                                  0.0s
 ✔ Container mysql_db         Created                                                                                                                  0.1s
 ✔ Container lab_docker       Created                                                                                                                  0.1s
Attaching to lab_docker, mysql_db
Container mysql_db Waiting 
mysql_db  | 2026-06-01 14:01:04+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db  | 2026-06-01 14:01:04+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql_db  | 2026-06-01 14:01:04+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db  | 2026-06-01 14:01:04+00:00 [Note] [Entrypoint]: Initializing database files
mysql_db  | 2026-06-01T14:01:04.780077Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db  | 2026-06-01T14:01:04.781539Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.46) initializing of server in progress as process 79
mysql_db  | 2026-06-01T14:01:04.790181Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db  | 2026-06-01T14:01:05.753611Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db  | 2026-06-01T14:01:07.122917Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
mysql_db  | 2026-06-01 14:01:10+00:00 [Note] [Entrypoint]: Database files initialized
mysql_db  | 2026-06-01 14:01:10+00:00 [Note] [Entrypoint]: Starting temporary server
mysql_db  | 2026-06-01T14:01:10.521102Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db  | 2026-06-01T14:01:10.522941Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 121
mysql_db  | 2026-06-01T14:01:10.583713Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db  | 2026-06-01T14:01:10.921957Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db  | 2026-06-01T14:01:11.136082Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db  | 2026-06-01T14:01:11.136120Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db  | 2026-06-01T14:01:11.139543Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db  | 2026-06-01T14:01:11.158924Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: /var/run/mysqld/mysqlx.sock
mysql_db  | 2026-06-01T14:01:11.159610Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  MySQL Community Server - GPL.
mysql_db  | 2026-06-01 14:01:11+00:00 [Note] [Entrypoint]: Temporary server started.
mysql_db  | '/var/lib/mysql/mysql.sock' -> '/var/run/mysqld/mysqld.sock'
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/iso3166.tab' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/leapseconds' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/tzdata.zi' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/zone.tab' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/zone1970.tab' as time zone. Skipping it.
mysql_db  | 2026-06-01 14:01:13+00:00 [Note] [Entrypoint]: Creating database lab_db
mysql_db  | 2026-06-01 14:01:13+00:00 [Note] [Entrypoint]: Creating user db_user
mysql_db  | 2026-06-01 14:01:13+00:00 [Note] [Entrypoint]: Giving user db_user access to schema lab_db
mysql_db  | 
mysql_db  | 2026-06-01 14:01:13+00:00 [Note] [Entrypoint]: Stopping temporary server
mysql_db  | 2026-06-01T14:01:13.862113Z 13 [System] [MY-013172] [Server] Received SHUTDOWN from user root. Shutting down mysqld (Version: 8.0.46).
mysql_db  | 2026-06-01T14:01:14.995185Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.0.46)  MySQL Community Server - GPL.
mysql_db  | 2026-06-01 14:01:15+00:00 [Note] [Entrypoint]: Temporary server stopped
mysql_db  | 
mysql_db  | 2026-06-01 14:01:15+00:00 [Note] [Entrypoint]: MySQL init process done. Ready for start up.
mysql_db  | 
mysql_db  | 2026-06-01T14:01:16.113110Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db  | 2026-06-01T14:01:16.114552Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 1
mysql_db  | 2026-06-01T14:01:16.120307Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db  | 2026-06-01T14:01:19.860357Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db  | 2026-06-01T14:01:19.994836Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db  | 2026-06-01T14:01:19.994885Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db  | 2026-06-01T14:01:19.997983Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db  | 2026-06-01T14:01:20.016586Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
mysql_db  | 2026-06-01T14:01:20.016625Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
Container mysql_db Healthy 
lab_docker  | Hello, Docker!
lab_docker exited with code 0
```

## Часть I (Docker)

### 1. Создание Dockerfile для приложения

Команда:
```
cat > Dockerfile << 'EOF'
FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
CMD ["python", "main.py"]
EOF
```

### 2. Сборка и запуск контейнера с приложением

Команда:
```
docker build -t lab-docker-app .
docker run -d --name my_web_app -p 5000:5000 lab-docker-app
```

Вывод:
```
[+] Building 50.6s (11/11) FINISHED                                                                                                         docker:default
 => [internal] load build definition from Dockerfile                                                                                                  0.0s
 => => transferring dockerfile: 247B                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                    0.3s
 => [internal] load .dockerignore                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                       0.0s
 => [1/6] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              0.0s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              0.0s
 => [internal] load build context                                                                                                                     0.0s
 => => transferring context: 204B                                                                                                                     0.0s
 => CACHED [2/6] WORKDIR /app                                                                                                                         0.0s
 => [3/6] RUN apt-get update && apt-get install -y build-essential                                                                                   20.2s
 => [4/6] COPY app/requirements.txt .                                                                                                                 0.1s 
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                          6.0s 
 => [6/6] COPY app/ .                                                                                                                                 0.1s 
 => exporting to image                                                                                                                               23.7s 
 => => exporting layers                                                                                                                              19.9s 
 => => exporting manifest sha256:b275d991a8d8957205bcad4fadf2a6ee1ac749035ab28be4c54a0ea4adbf71c2                                                     0.0s 
 => => exporting config sha256:643da1d4a6aad29b269bf33beba72e8b83164868442e6b1a304dc897ab663923                                                       0.0s 
 => => exporting attestation manifest sha256:abb6eb3449ae3025a0ad7362208b9b6dbb972bea21712d819face95a45a6da68                                         0.0s 
 => => exporting manifest list sha256:3a350611885810848573ed36de12e9a9454db35b456b6a46b3860f1fb76f97e2                                                0.0s
 => => naming to docker.io/library/lab-docker-app:latest                                                                                              0.0s
 => => unpacking to docker.io/library/lab-docker-app:latest                                                                                           3.7s
1c4792fb912f38624c13695ca182964855faacb8aefb0166c2d31b2ae2562205
```

### 3. Копирование файла README.md внутрь контейнера

Команда:
```
docker run -d --name my_web_app lab-docker-app sleep infinity
docker cp README.md my_web_app:/home/
```

Вывод:
```
Successfully copied 4.44kB (transferred 6.14kB) to my_web_app:/home/
```

### 4. Подключение к терминалу контейнера в интерактивном режиме

Команда:
```
$ docker exec -it my_web_app sh
```

### 5. Проверка наличия скопированного айла

Команда:
```
ls -la /home/
```

Вывод:
```
total 16
drwxr-xr-x 1 root root 4096 Jun  1 14:08 .
drwxr-xr-x 1 root root 4096 Jun  1 14:08 ..
-rw-r--r-- 1 1000 1000 4442 Jun  1 13:40 README.md
```

### 6. Выход из контейнера и его остановка

Команда: ```exit```

Команда: ```docker stop my_web_app && docker rm my_web_app```


## Часть II. Настройка многоконтейнерной среды

### 1. Создание файла docker-compose.yml

Команда:
```
cat > docker-compose.yml << 'EOF'
services:
  app:
    build: . 
    container_name: lab_docker_app_container
    restart: on-failure
    ports:
      - "5000:5000"
    depends_on:
      db:
        condition: service_healthy
    environment:
      - DB_HOST=db
      - DB_USER=db_user
      - DB_PASSWORD=secret
      - DB_NAME=lab_db

  db:
    image: mysql:8.0
    container_name: mysql_db_container
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: secret_root_pass
      MYSQL_DATABASE: lab_db
      MYSQL_USER: db_user
      MYSQL_PASSWORD: secret
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
      - ./db:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 2s
      retries: 10

volumes:
  db_data:
EOF
```

### 2. Обновление списка зависимостей приложения

Команда:
```
cat > app/requirements.txt << 'EOF'
flask
requests
mysql-connector-python
EOF
```

### 3. Интеграция Flask с базой данных

Команда:
```
cat > app/main.py << 'EOF'
import os
import time
from flask import Flask, request, render_template_string, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'db'),
                database=os.getenv('DB_NAME', 'lab_db'),
                user=os.getenv('DB_USER', 'db_user'),
                password=os.getenv('DB_PASSWORD', 'secret')
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}. Retrying...")
            time.sleep(2)
            retries -= 1
    return None

def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Database initialized successfully.")

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    if not conn:
        return "Ошибка подключения к базе данных!", 500
    
    cursor = conn.cursor()
    
    if request.method == 'POST':
        task_name = request.form.get('task')
        if task_name:
            try:
                cursor.execute("INSERT INTO tasks (name) VALUES (%s)", (task_name,))
                conn.commit()
            except Error as e:
                print(f"Failed to insert record: {e}")
            return redirect(url_for('index'))
            
    try:
        cursor.execute("SELECT name FROM tasks")
        tasks = [item[0] for item in cursor.fetchall()]
    except Error as e:
        print(f"Error fetching tasks: {e}")
        tasks = []
        
    cursor.close()
    conn.close()

    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lab Docker</title>
        <meta charset="utf-8">
    </head>
    <body style="font-family: Arial; margin: 40px; background-color: #f4f4f9;">
        <h2>Список задач (Лабораторная Docker)</h2>
        <form method="POST" style="margin-bottom: 20px;">
            <input type="text" name="task" placeholder="Новая задача" required style="padding: 8px; width: 250px;">
            <button type="submit" style="padding: 8px 15px; background-color: #007bff; color: white; border: none; cursor: pointer;">Добавить</button>
        </form>
        <h3>Текущие задачи в БД:</h3>
        <ul>
        {% for task in tasks %}
            <li style="margin: 5px 0; font-size: 16px;"><b>{{ task }}</b></li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''
    return render_template_string(html, tasks=tasks)

if __name__ == '__main__':
    time.sleep(3)
    init_db()
    app.run(host='0.0.0.0', port=5000)
EOF
```

### 4. Сборка и запуск многоконтейнерной среды

Команда:
```
docker compose down -v
docker compose build --no-cache
docker compose up
```

Вывод:
```
[+] down 4/4
 ✔ Container lab_docker_app_container Removed                                                                                                          0.0s
 ✔ Container mysql_db_container       Removed                                                                                                          0.0s
 ✔ Volume lab_docker_db_data          Removed                                                                                                          0.0s
 ✔ Network lab_docker_default         Removed                                                                                                          0.1s
[+] Building 65.6s (14/14) FINISHED                                                                                                                        
 => [internal] load local bake definitions                                                                                                            0.0s
 => => reading from stdin 540B                                                                                                                        0.0s
 => [internal] load build definition from Dockerfile                                                                                                  0.0s
 => => transferring dockerfile: 247B                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                    0.5s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                         0.0s
 => [internal] load .dockerignore                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                       0.0s
 => [1/6] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              0.0s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                              0.0s
 => [internal] load build context                                                                                                                     0.0s
 => => transferring context: 235B                                                                                                                     0.0s
 => CACHED [2/6] WORKDIR /app                                                                                                                         0.0s
 => [3/6] RUN apt-get update && apt-get install -y build-essential                                                                                   22.2s
 => [4/6] COPY app/requirements.txt .                                                                                                                 0.1s 
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                          8.6s 
 => [6/6] COPY app/ .                                                                                                                                 0.1s 
 => exporting to image                                                                                                                               33.6s 
 => => exporting layers                                                                                                                              22.9s 
 => => exporting manifest sha256:5f8b213476c47a2c065de97b99f4367495a8022f41bc719c8d4e062901a1cacd                                                     0.0s 
 => => exporting config sha256:e31c27221d1d753eabbf9d145e077b93eea48562e6f1b23a794a6ebd83ff62bf                                                       0.0s 
 => => exporting attestation manifest sha256:ebcf6009f8a659c20cd43edbc951738b5c5b4aa79e44b5cbb1af98fae8d81944                                         0.0s 
 => => exporting manifest list sha256:b0b51c0605de584ff02c3126c435ce4d7400b3fbb3128caf53bc023aea3f2563                                                0.0s
 => => naming to docker.io/library/lab_docker-app:latest                                                                                              0.0s
 => => unpacking to docker.io/library/lab_docker-app:latest                                                                                          10.5s
 => resolving provenance for metadata file                                                                                                            0.1s
[+] build 1/1
 ✔ Image lab_docker-app Built                                                                                                                         65.7s
[+] up 4/4
 ✔ Network lab_docker_default         Created                                                                                                          0.1s
 ✔ Volume lab_docker_db_data          Created                                                                                                          0.0s
 ✔ Container mysql_db_container       Created                                                                                                          0.1s
 ✔ Container lab_docker_app_container Created                                                                                                          0.1s
Attaching to lab_docker_app_container, mysql_db_container
Container mysql_db_container Waiting 
mysql_db_container  | 2026-06-01 14:38:45+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db_container  | 2026-06-01 14:38:47+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql_db_container  | 2026-06-01 14:38:47+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db_container  | 2026-06-01 14:38:48+00:00 [Note] [Entrypoint]: Initializing database files
mysql_db_container  | 2026-06-01T14:38:48.172674Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db_container  | 2026-06-01T14:38:48.172913Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.46) initializing of server in progress as process 79
mysql_db_container  | 2026-06-01T14:38:48.185630Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db_container  | 2026-06-01T14:38:49.197847Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db_container  | 2026-06-01T14:38:50.628136Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
mysql_db_container  | 2026-06-01 14:38:53+00:00 [Note] [Entrypoint]: Database files initialized
mysql_db_container  | 2026-06-01 14:38:53+00:00 [Note] [Entrypoint]: Starting temporary server
mysql_db_container  | 2026-06-01T14:38:54.284489Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db_container  | 2026-06-01T14:38:54.285917Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 127
mysql_db_container  | 2026-06-01T14:38:54.305523Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db_container  | 2026-06-01T14:38:54.669327Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db_container  | 2026-06-01T14:38:54.904845Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db_container  | 2026-06-01T14:38:54.905198Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db_container  | 2026-06-01T14:38:54.908706Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db_container  | 2026-06-01T14:38:54.966839Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: /var/run/mysqld/mysqlx.sock
mysql_db_container  | 2026-06-01T14:38:54.966928Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  MySQL Community Server - GPL.
mysql_db_container  | 2026-06-01 14:38:54+00:00 [Note] [Entrypoint]: Temporary server started.
mysql_db_container  | '/var/lib/mysql/mysql.sock' -> '/var/run/mysqld/mysqld.sock'
Container mysql_db_container Healthy 
mysql_db_container  | Warning: Unable to load '/usr/share/zoneinfo/iso3166.tab' as time zone. Skipping it.
mysql_db_container  | Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
mysql_db_container  | Warning: Unable to load '/usr/share/zoneinfo/leapseconds' as time zone. Skipping it.
mysql_db_container  | Warning: Unable to load '/usr/share/zoneinfo/tzdata.zi' as time zone. Skipping it.
mysql_db_container  | Warning: Unable to load '/usr/share/zoneinfo/zone.tab' as time zone. Skipping it.
mysql_db_container  | Warning: Unable to load '/usr/share/zoneinfo/zone1970.tab' as time zone. Skipping it.
mysql_db_container  | 2026-06-01 14:38:58+00:00 [Note] [Entrypoint]: Creating database lab_db
mysql_db_container  | 2026-06-01 14:38:58+00:00 [Note] [Entrypoint]: Creating user db_user
mysql_db_container  | 2026-06-01 14:38:58+00:00 [Note] [Entrypoint]: Giving user db_user access to schema lab_db
mysql_db_container  | 
mysql_db_container  | 2026-06-01 14:38:58+00:00 [Note] [Entrypoint]: /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init.sql
mysql_db_container  | 
mysql_db_container  | 
mysql_db_container  | 2026-06-01 14:38:58+00:00 [Note] [Entrypoint]: Stopping temporary server
mysql_db_container  | 2026-06-01T14:38:58.627915Z 15 [System] [MY-013172] [Server] Received SHUTDOWN from user root. Shutting down mysqld (Version: 8.0.46).
mysql_db_container  | 2026-06-01T14:38:59.894006Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.0.46)  MySQL Community Server - GPL.
mysql_db_container  | 2026-06-01 14:39:00+00:00 [Note] [Entrypoint]: Temporary server stopped
mysql_db_container  | 
mysql_db_container  | 2026-06-01 14:39:00+00:00 [Note] [Entrypoint]: MySQL init process done. Ready for start up.
mysql_db_container  | 
mysql_db_container  | 2026-06-01T14:39:00.892025Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db_container  | 2026-06-01T14:39:00.893909Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 1
mysql_db_container  | 2026-06-01T14:39:00.902753Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db_container  | 2026-06-01T14:39:03.011482Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db_container  | 2026-06-01T14:39:03.216432Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db_container  | 2026-06-01T14:39:03.216466Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db_container  | 2026-06-01T14:39:03.219298Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db_container  | 2026-06-01T14:39:03.250435Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
mysql_db_container  | 2026-06-01T14:39:03.250677Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
lab_docker_app_container  | Error connecting to MySQL: 2003 (HY000): Can't connect to MySQL server on 'db:3306' (111). Retrying...
lab_docker_app_container  | Error connecting to MySQL: 2003 (HY000): Can't connect to MySQL server on 'db:3306' (111). Retrying...
lab_docker_app_container  | Database initialized successfully.
lab_docker_app_container  |  * Serving Flask app 'main'
lab_docker_app_container  |  * Debug mode: off
lab_docker_app_container  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
lab_docker_app_container  |  * Running on all addresses (0.0.0.0)
lab_docker_app_container  |  * Running on http://127.0.0.1:5000
lab_docker_app_container  |  * Running on http://172.18.0.3:5000
lab_docker_app_container  | Press CTRL+C to quit
```

### 5. Фиксация изменений

Команда:
```
git add .
git commit -m "Complete Part 2 of Docker lab: integrate Flask with MySQL via compose"
git push origin main
```

Вывод:
```
[main b8a6e7f] Complete Part 1 and Part 2 of Docker lab
 4 files changed, 143 insertions(+)
 create mode 100644 Dockerfile
 create mode 100644 app/main.py
 create mode 100644 docker-compose.yml
 Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 2 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 2.65 KiB | 2.65 MiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/xkolyaa/lab_docker.git
   a561ae5..b8a6e7f  main -> main
```
### 6. Тестирование работы связки "Пользователь — Приложение — БД"

1. После успешного запуска команды docker compose up интерфейс приложения стал доступен на порту 5000. 
При первом обращении база данных успешно инициализировалась, отображая пустой список задач:

<img width="1521" height="996" alt="image" src="https://gist.github.com/user-attachments/assets/1a755de6-aa3f-4aaa-8fb2-5cf70bb53fc0" />

2. Проверка отправки данных пользователем. После ввода новой задачи и нажатия «Добавить», Flask отправило запрос в контейнер MySQL. 
Данные были успешно записаны, извлечены и выведены на экран:

<img width="1521" height="989" alt="image" src="https://gist.github.com/user-attachments/assets/7c035399-27b4-4249-a007-4f94c20d292c" />
