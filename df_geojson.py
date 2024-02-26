
import pandas as pd
import json

# サンプルデータフレーム
data = {
    'longitude': [longitude1, longitude2, longitude3],
    'latitude': [latitude1, latitude2, latitude3],
    'time': ['2024-02-26T12:30:00Z', '2024-02-26T13:15:00Z', '2024-02-26T14:00:00Z'],
    'content': ['Content 1', 'Content 2', 'Content 3']
}

df = pd.DataFrame(data)

# DataFrameをGeoJSONに変換する関数
def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    geojson = {'type': 'FeatureCollection', 'features': []}
    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'properties': {prop: row[prop] for prop in properties},
            'geometry': {
                'type': 'Point',
                'coordinates': [row[lon], row[lat]]
            }
        }
        geojson['features'].append(feature)
    return geojson

# GeoJSONに変換
geojson_data = df_to_geojson(df, properties=['time', 'content'])

# GeoJSONを表示
print(json.dumps(geojson_data, indent=2))
