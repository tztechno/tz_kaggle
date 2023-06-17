###############################################
df[['Latitude', 'Longitude']] = df['GPS'].str.split(', ', expand=True).astype(float)

# Create the USA map plot
fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', hover_name='Supercharger',
                        hover_data=['Street Address', 'City', 'State', 'Zip'],
                        color_discrete_sequence=['blue'], zoom=3, height=600)

fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(title_text='Supercharger Locations in the USA')
fig.update_layout(margin={'r': 0, 't': 30, 'l': 0, 'b': 0})

# Display the plot
fig.show()
###############################################
