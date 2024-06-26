from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/brand-analysis')
def brand_analysis():
    return render_template('brand_analysis.html')

@main.route('/price-analysis')
def price_analysis():
    return render_template('price_analysis.html')

@main.route('/screen-size-analysis')
def screen_size_analysis():
    return render_template('screen_size_analysis.html')

@main.route('/display-type-analysis')
def display_type_analysis():
    return render_template('display_type_analysis.html')

@main.route('/outliers-analysis')
def outliers_analysis():
    return render_template('outliers_analysis.html')
