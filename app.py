# -*- coding: cp1250 -*-
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






########### Define your variables
'''
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='lightblue'
color2='darkgreen'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Test'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'
'''
myheading='Coffee Ranking by Origin'
tabtitle= 'Coffee Ranking by Origin'
data_coffee = pd.DataFrame(pd.read_csv('C:/Users/macho/Desktop/Coffee_Dashboard_Herkou/arabica_data_cleaned - arabica_data_cleaned.csv'))
code = pd.DataFrame(pd.read_csv('C:/Users/macho/Desktop/Coffee_Dashboard_Herkou/code.csv'))
data_coffee= data_coffee.rename(columns={'Country.of.Origin': 'country'})
data_coffee = pd.merge(data_coffee,code, on= ['country'], how='inner')
data_coffee = data_coffee.drop([ 'altitude_high_meters','altitude_low_meters', 'unit_of_measurement', 'Certification.Contact','Certification.Address', 'Expiration','Certification.Body','Quakers','Bag.Weight','ICO.Number'], axis=1)
test = data_coffee.groupby(['country','code_3'])[["Total.Cup.Points",'Aroma','Flavor','Aftertaste','Acidity','Body','Balance','Uniformity','Sweetness','Clean.Cup','Cupper.Points']].mean()
test.reset_index(inplace=True)
test = test.round(decimals=2)
'''
Brazil = test.loc[0]
Brazil.apply(pd.to_numeric, errors='ignore')

'''
########### Set up the chart
'''
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)
'''
for col in test.columns:
    test[col] = test[col].astype(str)
    
test["text"] = test["country"] + '<br>' + ('Aroma  ') + test['Aroma'] + '<br>' + ('Flavor  ') + test['Flavor'] + '<br>' + ('Aftertaste ') + test['Aftertaste'] + '<br>' + ('Acidity  ') + test["Acidity"] + '<br>' +('Body  ')+ test["Body"] + '<br>' + ('Balance  ') + test["Balance"] + '<br>' + ('Uniformity  ') + test["Uniformity"] + '<br>' + ('Clean Cup  ') + test["Clean.Cup"] + '<br>' + ('Sweetness  ') + test['Sweetness']

selected_country= 'Brazil'

fig = go.Figure(data= go.Choropleth(
    locations = test['code_3'],
    z =  test['Total.Cup.Points'],
    text = test["text"],
    colorscale = 'brwnyl_r',
    autocolorscale= False,
    reversescale=True,
    marker_line_color='white',
    marker_line_width=0.5,
    colorbar_title = 'Total Cup Points 0-100',
))

fig.update_layout(
    margin={"r":5,"t":30,"l":5,"b":5},
    #title_text='Coffee Origins and Taste Ranking',
    #width = 1000,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi?select=merged_data_cleaned.csv">\
            Kaggle Dataset </a>',
        showarrow = False
        
    )] 
)

#########Table
df = pd.read_csv('C:/Users/macho/Desktop/Coffee_Dashboard_Herkou/table_board.csv')
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

#########Flavour Radar Chart
##test
countries = df['Country'].unique()

characteristics = df.columns[1:]

#Brazil = pd.DataFrame(dict(
    #r=[7.55,7.57,7.44,7.51,7.54,7.53,9.88,9.95,9.85,7.56],
    #theta=['Aroma','Flavour','Aftertaste','Acidity', 'Body','Balance','Uniformity','Sweetness','Clean.Cup','Cupper.Points']))

#fig2 = px.line_polar(Brazil ,r='r', theta ='theta', line_close=True, color_discrete_sequence=px.colors.sequential.solar)

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '5%',
    'margin-right': '5%',
    'top': 0,
    'padding': '20px 10px'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#704510',#tittle color
    'padding': '20px 10px'
}



########### Set up the layout
'''
The layout is composed of a tree of "components" like html.Div and dcc.Graph.
The dash_html_components library has a component for every HTML tag.
The html.H1(children='Hello Dash')component generates
a <h1>Hello Dash</h1> HTML element in your application.

The children property is special. By convention,
it's always the first attribute which means that you can omit it:
html.H1(children='Hello Dash') is the same as html.H1('Hello Dash').
Also, it can contain a string, a number, a single component, or a list of components.
'''
'''
app.layout = html.Div(children=[
html.H1(myheading),

dcc.Graph(
        id='example-graph',
        figure=fig),


html.Div(children=[html.H4(children='10 Top Coffee Origins'),
    generate_table(df)]),


dcc.Dropdown(
        id='country_name',
        options=[{'label': i, 'value': i} for i in countries],
        value='Country'),

dcc.Graph(id='radar_graph'),

])
'''

title1 = dbc.Col([html.H2('The Map of Coffee Origins', style={
            'textAlign': 'center','color': '#704510','padding': '40px 10px'})])

map_chart = dbc.Row(
   [
        dbc.Col(dcc.Graph(id='example-graph-', figure=fig), align='centre')])

title2 = dbc.Col([html.H2('Highest Rated Origins', style={
            'textAlign': 'center','color': '#704510','padding': '40px 10px'})])

table = dbc.Col([dbc.Table.from_dataframe(df.head(n=5), striped=True, bordered=True, hover=True, responsive=True)])


'''
dbc.Row(
    [
        dbc.Col(
        html.Div(children=[html.H2(children='10 Top Coffee Origins', style={
            'textAlign': 'center','color': '#191950'
        },),
        generate_table(df)]), md=12)])

'''


jumbotron = dbc.Jumbotron(
    [
        html.H1("Welcome to the Coffee Origins interactive dashboard!", style={'color': '#704510'}, className="display-3"),
        html.P(
            "Here you can explore taste profiles of various coffee origins. This dashboard is a synthesis of over 1300 coffee reviews"
            " gathered by the Coffee Quality Institute in January 2018.", className="lead"),
        #dbc.NavItem(dbc.NavLink("Kaggle Dataset", active=True,href="https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi?select=merged_data_cleaned.csv")),
        html.P(dbc.Button("Kaggle Dataset", outline=True, color="warning", className="mr-1",href="https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi?select=merged_data_cleaned.csv")),
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
        dbc.ListGroupItem("Clean Cup - Clean Cup refers to a lack of interfering negative impressions from first ingestion to final aftertaste, a “transparency” of cup")]),
        html.P(
            "The Final Score is calculated by summing the individual scores given for each of the primary attributes in the box marked “Total Cup Points.”", style={'color': '#704510', 'padding': '20px 10px'})
        
])

#title3 = dbc.Col([html.H2('Taste profile by Origin', style={
            #'textAlign': 'center','color': '#704510','padding': '40px 10px'})])

titles= html.Div(
    dbc.Row(
            [
            dbc.Col(html.Div(html.H2('Taste profile by Origin', style={
            'textAlign': 'center','color': '#704510','padding': '40px 10px'})),width=True),
            dbc.Col(html.Div(html.H2('Quality Measures Bar Chart', style={
            'textAlign': 'center','color': '#704510','padding': '40px 10px'})),width = True)], align="center",))




dropdown = html.Div(
    dbc.Row(
            [
            dbc.Col(html.Div(dcc.Dropdown(id='country_name',options=[{'label': i,'value': i} for i in countries],value = 'Hawaii'))),
            dbc.Col(html.Div(dcc.Dropdown(id='characteristic_name',options=[{'label': i,'value': i} for i in characteristics],value = 'Total Cup Points')))], align="center",))

'''
controls= dbc.FormGroup(
    [
        dcc.Dropdown(
            id='country_name',
            options=[{
                'label': i,
                'value': i} for i in countries],value = 'Hawaii')])
'''
row = html.Div(
    dbc.Row(
            [
            dbc.Col(html.Div(dcc.Graph(id='radar_graph')),width=True),
            dbc.Col(html.Div(dcc.Graph(id='taste_graph')),width = True)], align="center",))

#radar_graph = dbc.Row([dbc.Col(dcc.Graph(id='radar_graph'), width={"size": 4, "offset": 3})])


#title4 = dbc.Col([html.H2('Quality Measures Bar Chart', style={
            #'textAlign': 'center','color': '#704510','padding': '40px 10px'})])
'''
dropdown= dbc.FormGroup(
    [
        dcc.Dropdown(
            id='characteristic_name',
            options=[{
                'label': i,
                'value': i} for i in characteristics],value = 'Total Cup Points')])
'''
#taste_graph = dbc.Row([dbc.Col(dcc.Graph(id='taste_graph'), width={"size": 10, "offset": 1})])

content = html.Div(
    [
        html.H2('Coffee Origins Dashboard', style=TEXT_STYLE),
        html.Hr(),
        jumbotron,
        title1,
        map_chart,
        title2,
        table,
        #title3,
        #controls,
        #radar_graph,
        #title4 ,
        titles,
        dropdown,
        #taste_graph,
        row
    ],
    style=CONTENT_STYLE
)

########### Initiate the app
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])
app.layout = html.Div(content)
server = app.server
app.title=tabtitle 

'''
#style sheets:
 CERULEAN, COSMO, CYBORG, DARKLY,
 FLATLY, JOURNAL, LITERA, LUMEN, LUX,
 MATERIA, MINTY, PULSE, SANDSTONE, SIMPLEX,
 SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI
 '''
#############app_callbacks_radar graph
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
          
    Zorg = pd.DataFrame(dict(
    r=[df.iloc[countryIndex][2],df.iloc[countryIndex][3],df.iloc[countryIndex][4],df.iloc[countryIndex][5],df.iloc[countryIndex][6],df.iloc[countryIndex][7],df.iloc[countryIndex][8],df.iloc[countryIndex][9]],
    theta=["Aroma",'Flavor','Aftertaste','Acidity', 'Body','Balance','Uniformity','Sweetness']))
    fig2 = px.line_polar(Zorg ,r='r', theta ='theta', range_r = [0,10], line_close=True, color_discrete_sequence=px.colors.sequential.solar)
    #please rewrite this so you don't hardcode anything!

    #fig2 = px.line_polar(df['Country'],
                     #r='r', theta='theta',
                     #line_close=True, color_discrete_sequence=px.colors.sequential.solar)

    #fig2.update_layout(margin={'l': 60, 'b': 60, 't': 10, 'r': 0}, hovermode='closest')


    return fig2

@app.callback(
    Output('taste_graph', 'figure'),
    [Input('characteristic_name', 'value')])
def update_graph(_character): 
    b= _character
    graph = px.bar(df.sort_values(by=b, ascending=False), x='Country', y=b,
    hover_data= [b], color=b,
    labels={'pop':b}, height=450, color_continuous_scale='Brwnyl_r') 
    return graph








if __name__ == '__main__':
    app.run_server(debug=True)
    
