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
    # Parse the JSON data sent by the client

    data = request.get_json()
    print(json.dumps(data, indent = 4))
    # Perform backend logic (e.g., process form data, save to DB)
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    # Example: Return an HTML snippet based on data
    # processed_data = "Processed: " + str(data.get('health_metric', 'unknown'))
    return render_template('about.html')
