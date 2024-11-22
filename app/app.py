# from flask import Flask, render_template, request, redirect


# app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def index() -> str:
#     if request.method == 'POST':
#         pass
#     return render_template('index.html')


# @app.route('/about')
# def about() -> str:
#     return render_template('about.html')


# # Helper functions
# def get_cached_data(location: str, meal) -> list[str]:
#     #TODO: query data from zotmeal-backend
#     return menu_list
from flask import Flask, request, render_template, jsonify, json

app = Flask(__name__)

@app.route('/')
def main_page():
    # Render the main page
    return render_template('web-page.html')

@app.route('/submit-health-data', methods=['POST'])
def submit_health_data():
    # TODO: Parse the JSON data sent by the client

    data = request.get_json()
    print(json.dumps(data, indent = 4)) # just printing out to terminal
    # Perform backend logic (e.g., process form data, save to DB)
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    # TODO: Item_list = some_function_here
    # TODO: return render_template('about.html', items = item_list)
    
    return render_template('about.html', items = [item() for _ in range(10)])

# currently just for testing 
class item():
    def __init__(self):
        self.f1 = 'hii'
        self.f2 = 'hii'
        self.f3 = 'hii'
        self.f4 = 'hii'
        self.f5 = 'hii'
    
    def __repr__(self):
        return f'Hi I am an item at {id(self)}'