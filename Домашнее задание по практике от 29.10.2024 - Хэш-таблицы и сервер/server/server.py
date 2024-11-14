from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    # Получение JSON-данных из запроса
    data = request.get_json()
    
    # Извлечение параметров a и b
    a = data.get('a', 0)
    b = data.get('b', 0)
    
    # Сложение
    result = a + b
    
    # Формирование ответа
    response = {
        'action': 'Сложение',
        'parameters': {
            'a': a,
            'b': b
        },
        'result': result
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
