from plotly.express import scatter_geo
scatter_geo(data_frame=df[df['year'] == 2021], lat='Latitude of the center', lon='Longitude of the center', color='Name of the storm', fitbounds='locations',
           opacity=0.5, title='2021 Typhoon season', hover_data=['Time of analysis'], size='Maximum sustained wind speed')
