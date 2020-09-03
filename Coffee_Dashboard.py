#!/usr/bin/env python
# coding: utf-8

# # Coffee Dashboard
# 

# In[1]:


import plotly
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


data_coffee = pd.DataFrame(pd.read_csv('arabica_data_cleaned - arabica_data_cleaned.csv'))
code = pd.DataFrame(pd.read_csv('code.csv'))



data_coffee= data_coffee.rename(columns={'Country.of.Origin': 'country'})




data_coffee = pd.merge(data_coffee,code, on= ['country'], how='inner')





print (data_coffee.info())





data_coffee = data_coffee.drop([ 'altitude_high_meters','altitude_low_meters', 'unit_of_measurement', 'Certification.Contact','Certification.Address', 'Expiration','Certification.Body','Quakers','Bag.Weight','ICO.Number'], axis=1)





#data_coffee.isnull().sum()





#df[] = df[list("ABCD")].astype(int)



test = data_coffee.groupby(['country','code_3'])[["Total.Cup.Points",'Aroma','Flavor','Aftertaste','Acidity','Body','Balance','Uniformity','Sweetness','Clean.Cup','Cupper.Points']].mean()
print(test)





test.reset_index(inplace=True)  


test = test.round(decimals=2)


test.dtypes




for col in test.columns:
    test[col] = test[col].astype(str)
    
test["text"] = test["country"] + '<br>' + ('Aroma  ') + test['Aroma'] + '<br>' + ('Flavor  ') + test['Flavor'] + '<br>' + ('Aftertaste ') + test['Aftertaste'] + '<br>' + ('Acidity  ') + test["Acidity"] + '<br>' +('Body  ')+ test["Body"] + '<br>' + ('Balance  ') + test["Balance"] + '<br>' + ('Uniformity  ') + test["Uniformity"] + '<br>' + ('Clean Cup  ') + test["Clean.Cup"] + '<br>' + ('Sweetness  ') + test['Sweetness']


fig = go.Figure(data= go.Choropleth(
    locations = test['code_3'],
    z =  test['Total.Cup.Points'],
    #zmin= 'Bad',
    #text =  data_coffee['country'],
    text = test["text"],
    #colorscale = ['brown', 'yellow','beige'],
    # colorscale = 'solar',
    colorscale = 'brwnyl_r',
    #color_continuous_midpoint=avg_CupTasteGrade,
    autocolorscale= False,
    reversescale=True,
    marker_line_color='white',
    marker_line_width=0.5,
    #colorbar_tickprefix = '',
    colorbar_title = 'Total Cup Points 0-100',
    
))

fig.update_layout(
    title_text='Coffee Origins and Taste Ranking',
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

fig.show()


# In[15]:


Brazil = test.loc[0]
Brazil.apply(pd.to_numeric, errors='ignore')



# In[16]:



Brazil = pd.DataFrame(dict(
    r=[7.55,7.57,7.44,7.51,7.54,7.53,9.88,9.95,9.85,7.56],
    theta=['Aroma','Flavour','Aftertaste','Acidity', 'Body','Balance','Uniformity','Sweetness','Clean.Cup','Cupper.Points']))

fig = px.line_polar(Brazil ,r='r', theta ='theta', line_close=True, color_discrete_sequence=px.colors.sequential.solar)
fig.show()


# In[18]:


fig = px.line_polar(Brazil, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself', line_color='brown')
fig.show()


# In[19]:


fig = px.bar_polar(Brazil, r="r", theta="theta", template="plotly_dark",
            color_discrete_sequence= px.colors.sequential.solar)
fig.show()


# In[20]:


data = data_coffee.groupby(['country','code_3'])[["Total.Cup.Points","altitude_mean_meters","Processing.Method", "Variety", "Region"]].mean()
print(data)


# In[ ]:


correlation.reset_index(inplace=True)  


# In[ ]:





# In[ ]:




