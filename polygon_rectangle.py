def calculate_bbox(points):
    x_values, y_values = zip(*points)
    xmin = min(x_values)
    xmax = max(x_values)
    ymin = min(y_values)
    ymax = max(y_values)
    return xmin, xmax, ymin, ymax

data2[['xmin','xmax','ymin','ymax']]=data2['points'].apply(lambda x: pd.Series(calculate_bbox(x)))
data2['label2']=data2['label'].apply(lambda x:reverse_mapping[x])
data2['Xcent']=(data2['xmin']+data2['xmax'])/(2*data2['width'])
data2['Ycent']=(data2['ymin']+data2['ymax'])/(2*data2['height'])
data2['boxW']=(data2['xmax']-data2['xmin'])/data2['width']
data2['boxH']=(data2['ymax']-data2['ymin'])/data2['height']
