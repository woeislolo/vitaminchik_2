from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException

from nutrition import nutrition


app = Flask(__name__)

@app.route('/')
def entry_page() -> 'html':
    """Выводит HTML-форму"""
    return render_template('entry.html.j2', the_title='Health App')

@app.route('/result', methods=['POST'])
def data() -> 'html':
    """Извлекает данные из запроса, записывает в эксель, возвращает результаты""" 

    food = request.form['food']
    suppl = request.form.getlist('suppl')

    not_found, lack, resource_of_lack = nutrition(food, suppl)

    resource = []
    for k, v in resource_of_lack.items():
        v = ', '.join(v)
        resource.append(f'{k}: {v}.')


    return render_template('results.html.j2', 
                            not_found=not_found,
                            lack=lack,
                            resource=resource)

@app.errorhandler(Exception) 
def handle_exception(error) -> 'html':
    """При ошибках редиректит на главную страницу"""
    if isinstance(error, HTTPException):
        return entry_page()

if __name__ == '__main__':
    app.run()
