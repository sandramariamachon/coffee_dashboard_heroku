import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State



# Define your variables
myheading ='Coffee Ranking by Origin'
tabtitle = 'Coffee Ranking by Origin'

# Read you data into Data Frames
coffee_data = pd.read_csv("http://raw.githubusercontent.com/sandramariamachon/coffee_dashboard_heroku/master/datasets_coffee/data.csv")
country_code = pd.read_csv("http://raw.githubusercontent.com/sandramariamachon/coffee_dashboard_heroku/master/datasets_coffee/code.csv")

# Merging the country codes and Coffee Ratings data frames on 'country'
coffee_data = coffee_data.rename(columns = {'Country.of.Origin': 'country'})
coffee_data= pd.merge(coffee_data, country_code, on = ['country'], how ='inner')
coffee_data = coffee_data.applymap(str)


# Set up the hoovering text contents for the map chart
text_hoover = coffee_data['country'] + '<br>'+ ('Aroma  ') + coffee_data['Aroma'] + '<br>' + ('Flavor  ') + coffee_data['Flavor'] + '<br>' + ('Aftertaste ') + coffee_data['Aftertaste'] + '<br>' + ('Acidity  ') + coffee_data["Acidity"] + '<br>' +('Body  ') + coffee_data["Body"] + '<br>' + ('Balance  ') + coffee_data["Balance"] + '<br>' + ('Uniformity  ') + coffee_data["Uniformity"] + '<br>' + ('Clean Cup  ') + coffee_data["Clean.Cup"] + '<br>' + ('Sweetness  ') 
+ coffee_data['Sweetness']

# Set up the World map chart  
fig = go.Figure(data = go.Choropleth(
    locations = coffee_data['code_3'],
    z =  coffee_data['Total.Cup.Points'],
    text = text_hoover,
    colorscale = 'brwnyl_r',
    autocolorscale = False,
    reversescale = True,
    marker_line_color = 'white',
    marker_line_width = 0.5,
    colorbar_title = 'Total Cup Points 0-100',
))

fig.update_layout(
    margin = {"r":5,"t":30,"l":5,"b":5},
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection_type = 'equirectangular'
    ),
    annotations = [dict(
        x = 0.55,
        y = 0.1,
        xref = 'paper',
        yref = 'paper',
        text = 'Source: <a href="https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi?select=merged_data_cleaned.csv">\
            Kaggle Dataset </a>',
        showarrow = False
        
    )] 
)

# Set up Table with coffee ranking
df = pd.read_csv('http://raw.githubusercontent.com/sandramariamachon/coffee_dashboard_heroku/master/datasets_coffee/table_board.csv')

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '5%',
    'margin-right': '5%',
    'top': 0,
    'padding': '20px 10px'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#704510',#title color
    'padding': '20px 10px'
}



# Set up the layout
title_map_chart = dbc.Col(
    [
        html.H2('The Map of Coffee Origins', style = {'textAlign': 'center','color': '#704510','padding': '40px 10px'})
        ]
        )

map_chart = dbc.Row(
    [
        dbc.Col(dcc.Graph(id = 'map-graph', figure = fig), align = 'centre', sm = 12, xs = 12)
        ]
        )

title_table = dbc.Col(
    [
        html.H2('Highest Rated Origins', style = {'textAlign': 'center','color': '#704510','padding': '40px 10px'})
        ]
        )

table = dbc.Col(
    [
        dbc.Table.from_dataframe(df.head(n = 5), striped = True, bordered = True, hover = True, responsive = True)
        ]
        ) #this is where I define the table - I need summed up characteristics for the country

legend_table = dbc.Jumbotron(
    [
        html.H1("Welcome to the Coffee Origins interactive dashboard!", style={'color': '#704510'}, className="display-3"),
        html.P("Here you can explore taste profiles of various coffee origins. This dashboard is a synthesis of over 1300 coffee reviews"
               "gathered by the Coffee Quality Institute in January 2018.", className = "lead"),
        html.P(dbc.Button("Kaggle Dataset", outline = True, color = "warning", className = "mr-1",href = "https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi?select=merged_data_cleaned.csv")),
        dbc.ListGroup(
             [
        dbc.ListGroupItem("As measures of coffee quality, tasters used: ", active = True),
        dbc.ListGroupItem("Aroma - the fragrance of the coffee before and after brewing"),
        dbc.ListGroupItem("Flavour - the combination of taste (sweet, sour, bitter, salty and pungent)"),
        dbc.ListGroupItem("Aftertaste - Aftertaste is the lingering feeling or flavour after the coffee has been swallowed."
                          " Aftertaste can make it or break it for a coffee. If the aftertaste is super sweet and lingering",
                          "it is good. If it disappears immediately, it is not good. "),
        dbc.ListGroupItem("Acidity - The acidity is really important in coffee. Same with wine, it is what give the coffee a backbone, structures it. Balances out the sweetest."),
        dbc.ListGroupItem("Body - Representing the tactile feeling of a coffee. How does it feel in your mouth?  Is it dense? How is the texture?"),
        dbc.ListGroupItem("Balance - The balance represents complexity. How do all the different attributes play together, and does it deepen the coffee?"),
        dbc.ListGroupItem("Uniformity - Uniformity refers to the consistency of flavour of the different cups of the sample tasted. "),
        dbc.ListGroupItem("Sweetness - Sweetness refers to a pleasing fullness of flavour as well as any obvious sweetness and its perception is the result of the presence of certain carbohydrates."),
        dbc.ListGroupItem("Clean Cup - Clean Cup refers to a lack of interfering negative impressions from first ingestion to final aftertaste, a transparency of cup")]),
        html.P(
            "The Final Score is calculated by summing the individual scores given for each of the primary attributes in the box marked Total Cup Points.", style = {'color': '#704510', 'padding': '20px 10px'})
        
])

dropdown = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H2('Taste profile by Origin', style = {'textAlign': 'center','color': '#704510','padding': '40px 10px'}))),align ="center",),
        dbc.Row(dbc.Col(html.Div(dcc.Dropdown(id ='country_name',options = [{'label': i,'value': i} for i in coffee_data['country'].unique()],value = 'Hawaii'))),align = "center",),
        dbc.Row(dbc.Col(html.Div(dcc.Graph(id ='radar_graph'))),align = "center",)

])

quality_bar_chart = html.Div(
            [
            dbc.Row(dbc.Col(html.Div(html.H2('Quality Measures Bar Chart', style = {'textAlign': 'center','color': '#704510','padding': '40px 10px'}))), align ="center",),
            dbc.Row(dbc.Col(html.Div(dcc.Dropdown(id = 'characteristic_name',options = [{'label': i,'value': i} for i in coffee_data.columns[20:30]],value = 'Total Cup Points'))), align ="center",),
            dbc.Row(dbc.Col(html.Div(dcc.Graph(id = 'taste_graph'))), align = "center",)

])


content = html.Div(
    [
        html.H2('Coffee Origins Dashboard', style = TEXT_STYLE),
        html.Hr(),
        legend_table,
        title_map_chart,
        map_chart,
        title_table,
        table,
        dropdown,
        quality_bar_chart
    ],
    style = CONTENT_STYLE
)

########### Initiate the app
app = dash.Dash(external_stylesheets = [dbc.themes.SKETCHY])
app.layout = html.Div(content)
server = app.server
app.title = tabtitle 


# app_callbacks radar graph, taste profile graph 
@app.callback(
    Output('radar_graph', 'figure'),
    [Input('country_name', 'value')])

def update_graph(_country):
    count = df.index.size
    i = 0
    countryIndex = 0
    while (i < count):
        if(df.iloc[i][0] == _country):
            countryIndex = i 
        i = i + 1
     
    data = pd.DataFrame(dict(
    r = [df.iloc[countryIndex][2],df.iloc[countryIndex][3],df.iloc[countryIndex][4],
    df.iloc[countryIndex][5],df.iloc[countryIndex][6],df.iloc[countryIndex][7]
    ,df.iloc[countryIndex][8], df.iloc[countryIndex][9]],
    theta = ['Aroma','Flavor','Aftertaste','Acidity', 'Body','Balance','Uniformity','Sweetness']))
    fig2 = px.line_polar(data ,r = 'r', theta = 'theta', range_r = [0,10], line_close = True, color_discrete_sequence = px.colors.sequential.solar)
    return fig2

@app.callback(
    Output('taste_graph', 'figure'),
    [Input('characteristic_name', 'value')])
def update_graph(_character): 
    b = _character
    graph = px.bar(df.sort_values(by = b, ascending = False), x = 'Country', y = b,
    hover_data = [b], color = b,
    labels = {'pop':b}, height = 450, color_continuous_scale = 'Brwnyl_r') 
    return graph




if __name__ == '__main__':
    app.run_server(debug=True)
    
