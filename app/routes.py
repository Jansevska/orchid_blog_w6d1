from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/TopFive')
def topfive():
    img_ttl_txt = {"https://www.orchidsinfo.eu/wp-content/uploads/2022/05/pexels-carissa-bongalosa-1047814-scaled.jpg": ['Phalaenopsis', 'This plant originates from South-East Asia, the Philipines and Australia.'], "https://www.orchidsinfo.eu/wp-content/uploads/2022/05/raw_c6833a9494d4232b333f10785d5e5b93.jpg": ['Zygopetalum', 'Zygopetalum originates from South America.'], "https://www.orchidsinfo.eu/wp-content/uploads/2022/05/raw_b216aecdfd5b924ed514cc3317af1a52.jpg": ['Cattleya', 'Cattleyas originate from Central and South America.'], "https://www.orchidsinfo.eu/wp-content/uploads/2022/05/raw_f42c1244762dbf85c9b771cd5573ea0b.jpg": ['Cymbidium', "Most of the ancestors of today’s cymbidiums originated from the forests of the Himalayas."], "https://www.orchidsinfo.eu/wp-content/uploads/2022/05/raw_d76fd9db88827737b2fc2e8bca5782bd.jpg":['Vanda', 'The Vanda is an orchid which is widespread in nature, from India and Sri Lanka to Northern Australia.']}
    
    return render_template('topfive.html', img_ttl_txt=img_ttl_txt)