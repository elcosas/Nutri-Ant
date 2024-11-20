from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        try: 
        except:
    return render_template('index.html')


@app.route('/about')
def about() -> str:
    return render_template('about.html')


# Helper functions
def get_cached_data(location: str, meal) -> list[str]:
    #TODO: query data from zotmeal-backend
    return menu_list
