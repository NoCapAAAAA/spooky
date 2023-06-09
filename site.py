import pyodbc
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

connection_string = r'Driver={SQL Server};Server=WIN-SPFE3KCRJES;Database=test;Trusted_Connection=yes;'

def create_connection():
    return pyodbc.connect(connection_string)

@app.route('/submit', methods=['POST'])
def submit():
    # Получение данных из формы
    data = request.form
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    parking_date = data.get('parking_date')
    phone_number = data.get('phone_number')
    comment = data.get('comment')

    # Создание подключения к базе данных
    with create_connection() as connection:
        cursor = connection.cursor()

        # Выполнение SQL-запроса для записи данных в таблицу
        query = "INSERT INTO ApplicationOfOrder (first_name, last_name, parking_date, phone_number, comment) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (first_name, last_name, parking_date, phone_number, comment))
        connection.commit()

    return redirect(url_for('index', modal=True))

@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
# Back it stu', I mean it, 808-ой толкает волну
# (У, я) Hello, мир, Манера крутит мир
# В дабл капе мои заны, а другой держу свой bean
# (У, я) Погоди, I’m swervin' shit один
# И мне так похуй, я застрял среди этих паутин (М-м)