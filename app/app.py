from flask import Flask, render_template, request
import urllib.request
import json


app = Flask(__name__)


MEAL_ENUM = {
    'breakfast': 0,
    'lunch': 1,
    'dinner': 2,
}


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    '''
    Handles '/' routing for Flask app,
    returns an html page on a successful GET request

    if a POST request is recieved, returns an html page formatted with a list
    of menu item dictionaries  processed from the request data
    '''
    if request.method == 'POST':
        menu_items = None
        error = None
        try:
            menu_items = process_post(dict(request.form))
        except Exception as e:
            error = f'Error processing request: {e}'
        return render_template('index.html', menu_items=menu_items, error=error)
    return render_template('index.html')


@app.route('/about')
def about() -> str:
    '''
    Handles '/about' routing for Flask app,
    returns an html page on a succesful GET request
    '''
    return render_template('about.html')


### Helper functions ###


def process_post(form) -> list[dict[str, str]]:
    '''
    Processes a POST request from the index route,
    validates form input, queries data from ZotMeal API, and sorts the data
    by dri ratios

    returns a sorted list of dictionaries with menu item information

    raises ValueError if form data is invalid
    '''
    validate(form)

    menu_list: list[dict[str, str]] = query_zotmeal(form['location'], form['menu'])
    if not menu_list:
        raise ValueError('No menu data found from cache')

    bmr = calculate_bmr(form['sex'], int(form['age']), float(form['height']), float(form['weight']))

    dri = {
        'calories': bmr,
        'protein': bmr * .2,
        'totalFat': bmr * .3,
        'totalCarbohydrates': bmr * .55,
        'dietaryFiber': (bmr/1000) * 14
    }

    sorted_menu_list = sorted(menu_list, key=lambda x: get_dri_score(x, dri))
    return sorted_menu_list
    

def validate(form) -> None:
    '''
    Validates form input from the index route,
    raises ValueError if form data is invalid
    '''
    for item in form:
        if not form[item]:
            raise ValueError('Empty form field')
        if item == 'location' and form[item] not in ['anteatery', 'brandywine']:
            raise ValueError('Invalid location')
        if item == 'meal' and form[item] not in ['breakfast', 'lunch', 'dinner']:
            raise ValueError('Invalid meal')
        if item == 'sex' and form[item] not in ['male', 'female']:
            raise ValueError('Invalid sex')
        if item == 'age' and not form[item].isdigit():
            raise ValueError('Invalid age')
        if item in ['weight', 'height'] and not form[item].isnumeric():
            raise ValueError('Invalid weight/height')


def calculate_bmr(sex: str, age: int, height: float, weight: float) -> float:
    '''
    Calculates BMR from weight and height,
    uses harris-benedict bmr formula

    returns a float
    '''
    if sex == 'male':
        return (6.23762 * weight) + (12.7084 * height) - (6.755 * age) + 66.473
    elif sex == 'female':
        return (4.33789 * weight) + (4.69798 * height) - (4.6756 * age) + 655.0955 
    return -1.0


def get_dri_score(menu_item: dict[str, float], ideal: dict[str, float]) -> float:
    '''
    Calculates the % error of a menu item from the ideal DRI values (divided
    by 3 to account for 3 recommended meals per day), then returns the average
    of the % errors as a score for comparison
    '''
    total_percent_error = 0.0
    for key in ideal:
        if menu_item[key] == 'less than 1':
            menu_item[key] = 0.0
        percent_error = (float(menu_item[key]) - (ideal[key] / 3)) / (ideal[key] / 3)
        total_percent_error += abs(percent_error)
    return total_percent_error / 5
 

def query_zotmeal(location: str, meal: str) -> list[dict[str, str]]:
    '''
    Sends a query to the ZotMeal API and returns a list of menu items 
    as dictionaries
    '''
    menu = get_menu(location, meal)
    menu_list = parse_menu_data(menu)
    return menu_list


def get_menu(location: str, meal: str):
    '''
    Connects to the dinning api and returns back the alot of data for a given dinning hall
    '''
    base_url = "https://zotmeal-backend.vercel.app/"
    endpoint = f"api?location={location}&meal={MEAL_ENUM[meal]}"
    url = f"{base_url}{endpoint}"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.URLError as e:
        print(f"Failed to retrieve data: {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error {e.code}: {e.reason}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON response: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None


def parse_menu_data(menu_json) -> list[dict[str, str]]:
    '''
    Parses through to get the food and nutrition of Brandywine and Anteatery
    '''
    menu_list = []
    for station in menu_json["all"]:
        for category in station['menu']:
            for item in category["items"]:
                # bro wtf is this
                menu_item = {
                    'name': item["name"],
                    'calories': item['nutrition']["calories"] if 'calories' in item['nutrition'] else 0.0, 
                    'protein': item['nutrition']["protein"] if 'protein' in item['nutrition'] else 0.0,
                    'totalFat': item['nutrition']["totalFat"] if 'totalFat' in item['nutrition'] else 0.0,
                    'totalCarbohydrates': item['nutrition']["totalCarbohydrates"] if 'totalCarbohydrates' in item['nutrition'] else 0.0,
                    'dietaryFiber': item['nutrition']["dietaryFiber"] if 'dietaryFiber' in item['nutrition'] else 0.0,
                }
                menu_list.append(menu_item)
    return menu_list
 

if __name__ == '__main__':
    app.run(debug=True)
 
