import requests
from flask import Flask, render_template, request

api_key = "4510f9ba2f0fcabc19cb3c233afa75f9"
json_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + api_key
app = Flask(__name__)


# response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

dic = {
    "Thunderstorm" : "https://media.giphy.com/media/j69Ma1PlscvTO/giphy.gif",
    "Drizzle": "https://i.gifer.com/Rhhw.gif",
    "Rain" : "https://i.gifer.com/fyDi.gif",
    "Snow" : "https://i.gifer.com/wn.gif",
    "Clear" : "https://i.gifer.com/XFbw.gif",
    "Clouds" : "https://i.gifer.com/7RtV.gif"
}

def get_weather(location):
    response = requests.get(json_url + "&q=" + location).json()
    return response 

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/location", methods=['GET', 'POST'])
def weather():
    faren = None
    f = None
    location = request.args.get('text')
    temp = get_weather(location)
    try:
        faren = round((temp["main"]["temp"] - 273.15) * 9/5 + 32, 1)
        temp["weather"][0]["description"] = temp["weather"][0]["description"].upper()
    except:
        return render_template('error.html')
    return render_template('search.html', location = temp, f = faren)

if __name__ == "__main__":
    app.run(debug=True)
    # temp = input()
    # print(get_weather(temp))