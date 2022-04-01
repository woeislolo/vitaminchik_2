from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException

from nutrition import nutrition, resource_of_nutrients


app = Flask(__name__)


@app.route('/')
def entry_page() -> 'html':

    return render_template('entry.html.j2', the_title='Health App')

@app.route('/result', methods=['POST'])
def data() -> 'html':

    food = request.form['food']
    suppl = request.form.getlist('suppl')

    not_found, nutrient_dict, calorii = nutrition(food, suppl)

    recommend_amount = {'Магний': 300, 'Цинк': 12, 'B6': 2, 'C': 120, 'P': 30, 
                        'Селен': 55, 'Йод': 150, 'B1': 1.5, 'B2': 1.8, 'B5': 5, 'B9': 200, 'B12': 2,
                        'N': 30, 'PP': 10, 'Марганец': 3.8, 'Медь': 2, 'Омега3': 1100,
                        'Железо': 18, 'Калий': 2500, 'Фосфор': 1000,
                        'Кальций': 1000, 'E': 15, 'D': 5, 'A': 750, 'K': 120, 'Лютеин': 5000}

    nutrient_lack_list = []
    for k, v in recommend_amount.items():
        if nutrient_dict[k] < v * 0.9:
            nutrient_lack_list.append(k)
    
    nutrient_resource = dict(resource_of_nutrients(nutrient_lack_list))


    return render_template('results.html.j2', 
                            not_found=not_found,
                            nutrient_dict=nutrient_dict,
                            recommend_amount=recommend_amount,
                            nutrient_resource=nutrient_resource,
                            protein=nutrient_dict['Белки'],
                            fat=nutrient_dict['Жиры'], 
                            carbs=nutrient_dict['Углеводы'],
                            kkal=calorii)

@app.errorhandler(Exception) 
def handle_exception(error) -> 'html':
    """При ошибках редиректит на главную страницу"""
    if isinstance(error, HTTPException):
        return entry_page()

if __name__ == '__main__':
    app.run()
