from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Главная страница с формой
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        user_input = request.form['user_input']

        # Проверяем, что пользователь ввел что-то
        if user_input:
            return redirect(url_for('result', user_input=user_input))
        else:
            # Если поле пустое, возвращаем ошибку
            return render_template('index.html', error="Пожалуйста, введите текст.")

    return render_template('index.html')


# Страница, которая отображает результат
@app.route('/result')
def result():
    user_input = request.args.get('user_input')
    return render_template('result.html', user_input=user_input)


if __name__ == '__main__':
    app.run(debug=True)
