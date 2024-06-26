from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

main = Blueprint('main', __name__)

# Load dataset
#file_path = '/workspaces/tv_market_analysis_2024/data/raw/tv_cleaned_data.csv'
#data = pd.read_csv(file_path)

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the relative path to the dataset
file_path = os.path.join(current_dir, '..', 'tv_cleaned_data.csv')

# Load dataset
data = pd.read_csv(file_path)

@main.route('/')
def index():
    # Key metrics
    total_tvs = data.shape[0]
    average_price = round(data['Price'].mean(), 2)

    # Price Distribution of Top 6 Brands
    top_6_brands = data['Brand'].value_counts().nlargest(6).index
    top_6_brands_data = data[data['Brand'].isin(top_6_brands)]
    fig_price_dist_brand = px.box(top_6_brands_data, x='Brand', y='Price', title='Price Distribution of Top 6 Brands')
    price_dist_brand_plot = pio.to_html(fig_price_dist_brand, full_html=False)


    # Market Share by Display Type
    display_type_counts = data['DisplayType'].value_counts()
    fig_display_type = px.pie(values=display_type_counts.values, names=display_type_counts.index, title='Market Share by Display Type')
    display_type_plot = pio.to_html(fig_display_type, full_html=False)

    # Price vs. Screen Size
    fig_price_vs_size = px.scatter(data, x='Inches', y='Price', title='Price vs. Screen Size')
    price_vs_size_plot = pio.to_html(fig_price_vs_size, full_html=False)

    # Average Price by Price Category
    avg_price_category = data.groupby('Price_Category')['Price'].mean().reset_index()
    fig_avg_price_category = px.bar(avg_price_category, x='Price_Category', y='Price', title='Average Price by Price Category')
    avg_price_category_plot = pio.to_html(fig_avg_price_category, full_html=False)

    # Pie Chart for Price Category
    price_category_counts = data['Price_Category'].value_counts()
    fig_price_category = px.pie(values=price_category_counts.values, names=price_category_counts.index, title='Market Share by Price Category')
    price_category_plot = pio.to_html(fig_price_category, full_html=False)


    # Table for Price Range by Price Category
    price_range_category = data.groupby('Price_Category')['Price'].agg([min, max]).reset_index()
    fig_price_range_category = go.Figure(data=[go.Table(
        header=dict(values=['Price Category', 'Min Price', 'Max Price'],
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[price_range_category['Price_Category'], price_range_category['min'], price_range_category['max']],
                   fill_color='lavender',
                   align='left'))
    ])
    price_range_category_table = pio.to_html(fig_price_range_category, full_html=False)

    return render_template('index.html', total_tvs=total_tvs, average_price=average_price, 
                           price_dist_brand_plot=price_dist_brand_plot, 
                           display_type_plot=display_type_plot, 
                           price_vs_size_plot=price_vs_size_plot, 
                           avg_price_category_plot=avg_price_category_plot, 
                           price_category_plot=price_category_plot, 
                           price_range_category_table=price_range_category_table)


@main.route('/brand-analysis')
def brand_analysis():

    # Key metrics
    total_brands = data['Brand'].nunique()
    most_popular_brand = data['Brand'].value_counts().idxmax()

    # Bar chart: Number of TVs per brand (top 15)
    brand_counts = data['Brand'].value_counts().nlargest(15)
    fig_brand_counts = px.bar(brand_counts, x=brand_counts.index, y=brand_counts.values, title='Number of TVs per Brand (Top 15)', labels={'x': 'Brand', 'y': 'Number of TVs'})
    brand_counts_plot = pio.to_html(fig_brand_counts, full_html=False)

    # Bar chart: Average price per brand
    avg_price_brand = data.groupby('Brand')['Price'].mean().sort_values(ascending=False)
    fig_avg_price_brand = px.bar(avg_price_brand, x=avg_price_brand.index, y=avg_price_brand.values, title='Average Price per Brand', labels={'x': 'Brand', 'y': 'Average Price'})
    avg_price_brand_plot = pio.to_html(fig_avg_price_brand, full_html=False)

    # Box plot: Screen size distribution per brand
    fig_screen_size_dist_brand = px.box(data, x='Brand', y='Inches', title='Screen Size Distribution per Brand')
    screen_size_dist_brand_plot = pio.to_html(fig_screen_size_dist_brand, full_html=False)

    # Box plot: Price distribution per brand
    fig_price_dist_brand = px.box(data, x='Brand', y='Price', title='Price Distribution per Brand')
    price_dist_brand_plot = pio.to_html(fig_price_dist_brand, full_html=False)

    # Pie chart: Market share by brand (top 5)
    top_5_brands = data['Brand'].value_counts().nlargest(5)
    fig_market_share_brand = px.pie(values=top_5_brands.values, names=top_5_brands.index, title='Market Share by Brand (Top 5)')
    market_share_brand_plot = pio.to_html(fig_market_share_brand, full_html=False)

    return render_template('brand_analysis.html', total_brands=total_brands, most_popular_brand=most_popular_brand, 
                           brand_counts_plot=brand_counts_plot, 
                           avg_price_brand_plot=avg_price_brand_plot, 
                           screen_size_dist_brand_plot=screen_size_dist_brand_plot, 
                           price_dist_brand_plot=price_dist_brand_plot, 
                           market_share_brand_plot=market_share_brand_plot)



@main.route('/price-analysis')
def price_analysis():
    

    # Key metrics
    total_price_categories = data['Price_Category'].nunique()
    average_price = round(data['Price'].mean(), 2)
    min_price = data['Price'].min()
    max_price = data['Price'].max()

    # Histogram: Price distribution
    fig_price_dist = px.histogram(data, x='Price', nbins=50, title='Price Distribution')
    price_dist_plot = pio.to_html(fig_price_dist, full_html=False)

    # Box plot: Price distribution by price category
    fig_price_dist_category = px.box(data, x='Price_Category', y='Price', title='Price Distribution by Price Category')
    price_dist_category_plot = pio.to_html(fig_price_dist_category, full_html=False)

    # Box plot: Price distribution by display type
    fig_price_dist_display = px.box(data, x='DisplayType', y='Price', title='Price Distribution by Display Type')
    price_dist_display_plot = pio.to_html(fig_price_dist_display, full_html=False)

    # Bar chart: Average price by price category
    avg_price_category = data.groupby('Price_Category')['Price'].mean().reset_index()
    fig_avg_price_category = px.bar(avg_price_category, x='Price_Category', y='Price', title='Average Price by Price Category')
    avg_price_category_plot = pio.to_html(fig_avg_price_category, full_html=False)

    # Scatter plot: Price vs. screen size
    fig_price_vs_size = px.scatter(data, x='Inches', y='Price', title='Price vs. Screen Size')
    price_vs_size_plot = pio.to_html(fig_price_vs_size, full_html=False)

    return render_template('price_analysis.html', total_price_categories=total_price_categories, average_price=average_price, 
                           min_price=min_price, max_price=max_price, price_dist_plot=price_dist_plot, 
                           price_dist_category_plot=price_dist_category_plot, 
                           price_dist_display_plot=price_dist_display_plot, 
                           avg_price_category_plot=avg_price_category_plot, 
                           price_vs_size_plot=price_vs_size_plot)



@main.route('/screen-size-analysis')
def screen_size_analysis():

    # Key metrics
    total_screen_sizes = data['Inches'].nunique()
    most_common_screen_size = data['Inches'].mode()[0]
    average_screen_size = round(data['Inches'].mean(), 2)

    # Histogram: Screen size distribution
    fig_screen_size_dist = px.histogram(data, x='Inches', nbins=20, title='Screen Size Distribution')
    screen_size_dist_plot = pio.to_html(fig_screen_size_dist, full_html=False)

    # Box plot: Screen size distribution by price category
    fig_screen_size_dist_category = px.box(data, x='Price_Category', y='Inches', title='Screen Size Distribution by Price Category')
    screen_size_dist_category_plot = pio.to_html(fig_screen_size_dist_category, full_html=False)

    # Box plot: Screen size distribution by brand
    fig_screen_size_dist_brand = px.box(data, x='Brand', y='Inches', title='Screen Size Distribution by Brand')
    screen_size_dist_brand_plot = pio.to_html(fig_screen_size_dist_brand, full_html=False)

    # Bar chart: Average screen size by price category
    avg_screen_size_category = data.groupby('Price_Category')['Inches'].mean().reset_index()
    fig_avg_screen_size_category = px.bar(avg_screen_size_category, x='Price_Category', y='Inches', title='Average Screen Size by Price Category')
    avg_screen_size_category_plot = pio.to_html(fig_avg_screen_size_category, full_html=False)

    # Scatter plot: Price vs. screen size
    fig_price_vs_size = px.scatter(data, x='Inches', y='Price', title='Price vs. Screen Size')
    fig_price_vs_size.update_traces(marker=dict(size=12, opacity=0.5))
    price_vs_size_plot = pio.to_html(fig_price_vs_size, full_html=False)

    return render_template('screen_size_analysis.html', total_screen_sizes=total_screen_sizes, most_common_screen_size=most_common_screen_size, 
                           average_screen_size=average_screen_size, screen_size_dist_plot=screen_size_dist_plot, 
                           screen_size_dist_category_plot=screen_size_dist_category_plot, 
                           screen_size_dist_brand_plot=screen_size_dist_brand_plot, 
                           avg_screen_size_category_plot=avg_screen_size_category_plot, 
                           price_vs_size_plot=price_vs_size_plot)



@main.route('/display-type-analysis')
def display_type_analysis():
    

    # Key metrics
    total_display_types = data['DisplayType'].nunique()
    most_common_display_type = data['DisplayType'].mode()[0]
    avg_price_per_display_type = data.groupby('DisplayType')['Price'].mean().round(2).reset_index()

    # Pie chart: Display type distribution
    display_type_counts = data['DisplayType'].value_counts()
    fig_display_type_dist = px.pie(values=display_type_counts.values, names=display_type_counts.index, title='Display Type Distribution')
    display_type_dist_plot = pio.to_html(fig_display_type_dist, full_html=False)

    # Box plot: Price distribution by display type
    fig_price_dist_display = px.box(data, x='DisplayType', y='Price', title='Price Distribution by Display Type')
    price_dist_display_plot = pio.to_html(fig_price_dist_display, full_html=False)

    # Bar chart: Average price by display type
    fig_avg_price_display = px.bar(avg_price_per_display_type, x='DisplayType', y='Price', title='Average Price by Display Type')
    avg_price_display_plot = pio.to_html(fig_avg_price_display, full_html=False)

    # Box plot: Screen size distribution by display type
    fig_screen_size_dist_display = px.box(data, x='DisplayType', y='Inches', title='Screen Size Distribution by Display Type')
    screen_size_dist_display_plot = pio.to_html(fig_screen_size_dist_display, full_html=False)

    # Scatter plot: Price vs. screen size by display type
    fig_price_vs_size_display = px.scatter(data, x='Inches', y='Price', color='DisplayType', title='Price vs. Screen Size by Display Type')
    fig_price_vs_size_display.update_traces(marker=dict(size=12, opacity=0.5))
    price_vs_size_display_plot = pio.to_html(fig_price_vs_size_display, full_html=False)

    return render_template('display_type_analysis.html', total_display_types=total_display_types, 
                           most_common_display_type=most_common_display_type, 
                           display_type_dist_plot=display_type_dist_plot, 
                           price_dist_display_plot=price_dist_display_plot, 
                           avg_price_display_plot=avg_price_display_plot, 
                           screen_size_dist_display_plot=screen_size_dist_display_plot, 
                           price_vs_size_display_plot=price_vs_size_display_plot)





@main.route('/outliers-analysis')
def outliers_analysis():
    
    # Key metrics
    total_outliers = data['outlier_flag'].sum()
    percentage_outliers = round((total_outliers / data.shape[0]) * 100, 2)

    # Filter outliers
    outliers = data[data['outlier_flag'] == 1]

    # Box plot: Outliers by price
    fig_outliers_price = px.box(data, y='Price', title='Outliers by Price', points='all')
    outliers_price_plot = pio.to_html(fig_outliers_price, full_html=False)

    # Box plot: Outliers by screen size
    fig_outliers_size = px.box(data, y='Inches', title='Outliers by Screen Size', points='all')
    outliers_size_plot = pio.to_html(fig_outliers_size, full_html=False)

    # Box plot: Outliers by price category
    fig_outliers_price_category = px.box(data, x='Price_Category', y='Price', title='Outliers by Price Category', points='all')
    outliers_price_category_plot = pio.to_html(fig_outliers_price_category, full_html=False)

    # Scatter plot: Outliers by price and screen size
    fig_outliers_scatter = px.scatter(outliers, x='Inches', y='Price', title='Outliers by Price and Screen Size', color='Price_Category')
    outliers_scatter_plot = pio.to_html(fig_outliers_scatter, full_html=False)

    return render_template('outliers_analysis.html', total_outliers=total_outliers, percentage_outliers=percentage_outliers, 
                           outliers_price_plot=outliers_price_plot, outliers_size_plot=outliers_size_plot, 
                           outliers_price_category_plot=outliers_price_category_plot, outliers_scatter_plot=outliers_scatter_plot)


