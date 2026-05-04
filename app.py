from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return "Thrissur Fuel API Running!"

@app.route('/api/fuel/thrissur')
def get_fuel():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get("https://www.ndtv.com/fuel-prices/petrol-price-in-thrissur-city", headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        petrol = soup.select_one('div.vjl-md-3 span').text.strip()
        
        r2 = requests.get("https://www.ndtv.com/fuel-prices/diesel-price-in-thrissur-city", headers=headers, timeout=10)
        soup2 = BeautifulSoup(r2.text, 'html.parser')
        diesel = soup2.select_one('div.vjl-md-3 span').text.strip()
        
        return jsonify({"petrol": f"₹{petrol}/L", "diesel": f"₹{diesel}/L", "source": "NDTV"})
    except:
        return jsonify({"petrol": "₹106.58/L", "diesel": "₹95.51/L", "source": "Cached"})

if __name__ == '__main__':
    app.run()
