from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException, BadRequest, InternalServerError

from nutrition import nutrition, resource_of_nutrients


app = Flask(__name__)


@app.route('/')
def entry_page() -> 'html':

    return render_template('entry.html.j2', the_title='Health App')

@app.route('/result', methods=['POST'])
def data() -> 'html':

    food = request.form['food']
    suppl = request.form.getlist('suppl')

    nutrition_res = nutrition(food, suppl)
    if nutrition_res == False:
        return render_template('error.html.j2')
    else:
        not_found, nutrient_dict, calorii = nutrition_res

    recommend_amount = {'Магний': 320, 'Цинк': 12, 'B6': 2, 'C': 120, 'P': 30, 
                        'Селен': 55, 'Йод': 150, 'B1': 1.5, 'B2': 1.8, 'B5': 5, 'B9': 200, 'B12': 2,
                        'N': 30, 'PP': 10, 'Марганец': 3.8, 'Медь': 2, 'Омега3': 1100,
                        'Железо': 18, 'Калий': 2500, 'Фосфор': 1000,
                        'Кальций': 1000, 'E': 15, 'D': 5, 'A': 750, 'K': 120, 'Лютеин': 5000,
                        'Белки': 113, 'Жиры': 51, 'Углеводы': 170, }

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
    if isinstance(error, BadRequest):
        return render_template('error400.html.j2'), 400 
    elif isinstance(error, InternalServerError):
        return render_template('error500.html.j2'), 500
    elif isinstance(error, HTTPException):
        return render_template('errorhttp.html.j2')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
