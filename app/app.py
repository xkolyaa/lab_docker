from flask import Flask, request, render_template_string
import mysql.connector
import os

app = Flask(__name__)

HTML = """
<h2>Tasks</h2>
<form method="post">
  <input name="task" placeholder="Enter task">
  <button type="submit">Add</button>
</form>
<ul>
{% for t in tasks %}
  <li>{{ t[1] }}</li>
{% endfor %}
</ul>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    db = mysql.connector.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    if request.method == 'POST':
        cur.execute("INSERT INTO tasks (name) VALUES (%s)", (request.form['task'],))
        db.commit()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    db.close()
    return render_template_string(HTML, tasks=tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
