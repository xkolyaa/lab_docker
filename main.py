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
    # Ждем пару секунд для гарантированного аптайма базы перед авто-созданием таблиц
    time.sleep(3)
    init_db()
    app.run(host='0.0.0.0', port=5000)
