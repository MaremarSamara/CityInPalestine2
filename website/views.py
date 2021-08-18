from flask import Blueprint, render_template,request
import requests
import json 
from flask_login import login_required,current_user
views = Blueprint("views", __name__)



@views.route('/')
@login_required  
def home():  
    return render_template('index.html');  
    

        
@views.route('/palestine City/Jerusalem')  
def AlAqsaMosque():  
    return render_template('AlAqsaMosque.html')

@views.route('/palestine City/jericho')  
def jericho():  
    return render_template('jericho.html')

@views.route('/palestine City/Gaza')  
def gaza():  
    return render_template('gaza.html')

@views.route('/palestine City/safed')  
def safed():  
    return render_template('safed.html')

@views.route('/palestine City/yafa')  
def yafa():  
    return render_template('yafa.html')

@views.route('/{city_name}/weather')
def weather():
    return render_template('weather.html')


def get_weather_data(city_name):
    raw_data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=bc368fbffb0d27697c1822903f154f03')
    return raw_data.json()
 

@views.route('/city', methods=['POST'])
def city():
    name = request.form['city_name']
    data = get_weather_data(name)
    
    weather_main = data['weather'][0]['main']
    weather_description = data['weather'][0]['description']
    temp = data['main']['temp']
    c_temp = format(float(float(temp) - 273.15), '.2f')
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    return render_template('city.html', city_name=name, weather=weather_main,
                           weather_description=weather_description, temperature=c_temp,
                           pressure=pressure, humidity=humidity)    

@views.route('/AddCity')  
def addCity():
    render_template('add_city.html')                         