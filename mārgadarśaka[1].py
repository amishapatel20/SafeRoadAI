!pip install osmnx

import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt


place_name = "Delhi, India"


road_graph = ox.graph_from_place(place_name, network_type='all')

road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)

fig, ax = plt.subplots(figsize=(10, 10))
road_gdf.plot(ax=ax, linewidth=0.8, color='blue')
plt.title(f"Road Network for {place_name}")
plt.show()

import random
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString


road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)

num_points = 500
gnss_data = []

for _ in range(num_points):
    random_road = road_gdf.sample(n=1)
    road_coords = list(random_road.geometry.values[0].coords)


    start_point, end_point = random.sample(road_coords, 2)
    random_point = Point(
        [
            random.uniform(start_point[0], end_point[0]),
            random.uniform(start_point[1], end_point[1]),
        ]
    )
    gnss_data.append({
        'latitude': random_point.y,
        'longitude': random_point.x,
        'timestamp': pd.Timestamp.now(),
        'speed': random.uniform(10, 60)
    })


gnss_df = pd.DataFrame(gnss_data)
geometry = [Point(xy) for xy in zip(gnss_df.longitude, gnss_df.latitude)]
gnss_gdf = gpd.GeoDataFrame(gnss_df, geometry=geometry, crs='EPSG:4326')

gnss_gdf.to_csv('simulated_gnss_data_delhi.csv', index=False)
print("Simulated GNSS data saved to 'simulated_gnss_data_delhi.csv'.")

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

gnss_data_path = '/content/simulated_gnss_data_delhi.csv'
gnss_data = pd.read_csv(gnss_data_path)

print(gnss_data.head())


geometry = [Point(xy) for xy in zip(gnss_data['longitude'], gnss_data['latitude'])]
gnss_gdf = gpd.GeoDataFrame(gnss_data, geometry=geometry, crs='EPSG:4326')

fig, ax = plt.subplots(figsize=(10, 10))
```python
!pip install osmnx

import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt


place_name = "Delhi, India"


road_graph = ox.graph_from_place(place_name, network_type='all')

road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)

fig, ax = plt.subplots(figsize=(10, 10))
road_gdf.plot(ax=ax, linewidth=0.8, color='blue')
plt.title(f"Road Network for {place_name}")
plt.show()

import random
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString


road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)

num_points = 500
gnss_data = []

for _ in range(num_points):
    random_road = road_gdf.sample(n=1)
    road_coords = list(random_road.geometry.values[0].coords)


    start_point, end_point = random.sample(road_coords, 2)
    random_point = Point(
        [
            random.uniform(start_point[0], end_point[0]),
            random.uniform(start_point[1], end_point[1]),
        ]
    )
    gnss_data.append({
        'latitude': random_point.y,
        'longitude': random_point.x,
        'timestamp': pd.Timestamp.now(),
        'speed': random.uniform(10, 60)
    })


gnss_df = pd.DataFrame(gnss_data)
geometry = [Point(xy) for xy in zip(gnss_df.longitude, gnss_df.latitude)]
gnss_gdf = gpd.GeoDataFrame(gnss_df, geometry=geometry, crs='EPSG:4326')

gnss_gdf.to_csv('simulated_gnss_data_delhi.csv', index=False)
print("Simulated GNSS data saved to 'simulated_gnss_data_delhi.csv'.")

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

gnss_data_path = '/content/simulated_gnss_data_delhi.csv'
gnss_data = pd.read_csv(gnss_data_path)

print(gnss_data.head())


geometry = [Point(xy) for xy in zip(gnss_data['longitude'], gnss_data['latitude'])]
gnss_gdf = gpd.GeoDataFrame(gnss_data, geometry=geometry, crs='EPSG:4326')

fig, ax = plt.subplots(figsize=(10, 10))
gnss_gdf.plot(ax=ax, markersize=5, color='red')
plt.title("GNSS Data Points")
plt.show()

!pip install osmnx geopandas scikit-learn numpy pandas

!pip install pandas numpy geopandas osmnx hmmlearn scikit-learn geopy

import pandas as pd
import numpy as np
from geopy.distance import geodesic

np.random.seed(0)
n_points = 500

center_lat, center_lon = 28.6139, 77.2090
lat_noise = np.random.normal(loc=0, scale=0.001, size=n_points)
lon_noise = np.random.normal(loc=0, scale=0.001, size=n_points)
timestamps = pd.date_range(start='2023-01-01', periods=n_points, freq='5s')

gnss_data = pd.DataFrame({
    'latitude': center_lat + lat_noise,
    'longitude': center_lon + lon_noise,
    'timestamp': timestamps,
    'speed': np.abs(np.random.normal(loc=30, scale=5, size=n_points)),
    'heading': np.random.uniform(0, 360, size=n_points)
})

print(gnss_data.head())

import osmnx as ox
import networkx as nx
from hmmlearn import hmm
from shapely.geometry import Point, LineString


place_name = "Delhi, India"
road_graph = ox.graph_from_place(place_name, network_type='drive')


road_graph = ox.project_graph(road_graph)


import geopandas as gpd

geometry = [Point(xy) for xy in zip(gnss_data.longitude, gnss_data.latitude)]
gnss_gdf = gpd.GeoDataFrame(gnss_data, geometry=geometry, crs='EPSG:4326')
gnss_gdf = gnss_gdf.to_crs(ox.graph_to_gdfs(road_graph, nodes=False).crs)


def map_matching_hmm(gnss_gdf, road_graph):

    model = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)


    X = np.column_stack([gnss_gdf.geometry.x, gnss_gdf.geometry.y])


    model.fit(X)

    states = model.predict(X)
    gnss_gdf['road_type'] = states
    return gnss_gdf

gnss_gdf = map_matching_hmm(gnss_gdf, road_graph)
print(gnss_gdf.head())

from geopy.distance import geodesic

def feature_engineering(gnss_gdf):
    
    road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)
    gnss_gdf['nearest_road'] = gnss_gdf.apply(
        lambda row: road_gdf.distance(row.geometry).min(), axis=1
    )

    gnss_gdf['heading_change'] = gnss_gdf['heading'].diff().fillna(0)


    return gnss_gdf

gnss_gdf = feature_engineering(gnss_gdf)
print(gnss_gdf[['nearest_road', 'heading_change']].head())

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


X = gnss_gdf[['speed', 'heading_change', 'nearest_road']]
y = gnss_gdf['road_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report


X = gnss_gdf[['speed', 'heading_change', 'nearest_road']]
y = gnss_gdf['road_type']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [50, 100, 150, 200], 
    'max_depth': [None, 10, 20, 30],      
    'min_samples_split': [2, 5, 10],      
    'min_samples_leaf': [1, 2, 4],        
    'bootstrap': [True, False]            
}


rf = RandomForestClassifier(random_state=42)


grid_search = GridSearchCV(estimator=rf, param_grid=param_grid,
                           cv=5,  
                           n_jobs=-1,  
                           verbose=2) 


grid_search.fit(X_train, y_train)


best_rf = grid_search.best_estimator_

y_pred = best_rf.predict(X_test)
print("Best Parameters:", grid_search.best_params_)
print(classification_report(y_test, y_pred))

!pip install xgboost

import xgboost as xgb
import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt


place_name = "Delhi, India"


road_graph = ox.graph_from_place(place_name, network_type='all')

road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)

fig, ax = plt.subplots(figsize=(10, 10))
road_gdf.plot(ax=ax, linewidth=0.8, color='blue')
plt.title(f"Road Network for {place_name}")
plt.show()

import random
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString


road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)

num_points = 500
gnss_data = []

for _ in range(num_points):
    random_road = road_gdf.sample(n=1)
    road_coords = list(random_road.geometry.values[0].coords)


    start_point, end_point = random.sample(road_coords, 2)
    random_point = Point(
        [
            random.uniform(start_point[0], end_point[0]),
            random.uniform(start_point[1], end_point[1]),
        ]
    )
    gnss_data.append({
        'latitude': random_point.y,
        'longitude': random_point.x,
        'timestamp': pd.Timestamp.now(),
        'speed': random.uniform(10, 60)
    })


gnss_df = pd.DataFrame(gnss_data)
geometry = [Point(xy) for xy in zip(gnss_df.longitude, gnss_df.latitude)]
gnss_gdf = gpd.GeoDataFrame(gnss_df, geometry=geometry, crs='EPSG:4326')

gnss_gdf.to_csv('simulated_gnss_data_delhi.csv', index=False)
print("Simulated GNSS data saved to 'simulated_gnss_data_delhi.csv'.")

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

gnss_data_path = '/content/simulated_gnss_data_delhi.csv'
gnss_data = pd.read_csv(gnss_data_path)

print(gnss_data.head())


geometry = [Point(xy) for xy in zip(gnss_data['longitude'], gnss_data['latitude'])]
gnss_gdf = gpd.GeoDataFrame(gnss_data, geometry=geometry, crs='EPSG:4326')

fig, ax = plt.subplots(figsize=(10, 10))
gnss_gdf.plot(ax=ax, markersize=5, color='red')
plt.title("GNSS Data Points")
plt.show()

!pip install osmnx geopandas scikit-learn numpy pandas

!pip install pandas numpy geopandas osmnx hmmlearn scikit-learn geopy

import pandas as pd
import numpy as np
from geopy.distance import geodesic

np.random.seed(0)
n_points = 500

center_lat, center_lon = 28.6139, 77.2090
lat_noise = np.random.normal(loc=0, scale=0.001, size=n_points)
lon_noise = np.random.normal(loc=0, scale=0.001, size=n_points)
timestamps = pd.date_range(start='2023-01-01', periods=n_points, freq='5s')

gnss_data = pd.DataFrame({
    'latitude': center_lat + lat_noise,
    'longitude': center_lon + lon_noise,
    'timestamp': timestamps,
    'speed': np.abs(np.random.normal(loc=30, scale=5, size=n_points)),
    'heading': np.random.uniform(0, 360, size=n_points)
})

print(gnss_data.head())

import osmnx as ox
import networkx as nx
from hmmlearn import hmm
from shapely.geometry import Point, LineString


place_name = "Delhi, India"
road_graph = ox.graph_from_place(place_name, network_type='drive')


road_graph = ox.project_graph(road_graph)


import geopandas as gpd

geometry = [Point(xy) for xy in zip(gnss_data.longitude, gnss_data.latitude)]
gnss_gdf = gpd.GeoDataFrame(gnss_data, geometry=geometry, crs='EPSG:4326')
gnss_gdf = gnss_gdf.to_crs(ox.graph_to_gdfs(road_graph, nodes=False).crs)


def map_matching_hmm(gnss_gdf, road_graph):

    model = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)


    X = np.column_stack([gnss_gdf.geometry.x, gnss_gdf.geometry.y])


    model.fit(X)

    states = model.predict(X)
    gnss_gdf['road_type'] = states
    return gnss_gdf

gnss_gdf = map_matching_hmm(gnss_gdf, road_graph)
print(gnss_gdf.head())

from geopy.distance import geodesic

def feature_engineering(gnss_gdf):
    
    road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)
    gnss_gdf['nearest_road'] = gnss_gdf.apply(
        lambda row: road_gdf.distance(row.geometry).min(), axis=1
    )

    gnss_gdf['heading_change'] = gnss_gdf['heading'].diff().fillna(0)


    return gnss_gdf

gnss_gdf = feature_engineering(gnss_gdf)
print(gnss_gdf[['nearest_road', 'heading_change']].head())

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


X = gnss_gdf[['speed', 'heading_change', 'nearest_road']]
y = gnss_gdf['road_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report


X = gnss_gdf[['speed', 'heading_change', 'nearest_road']]
y = gnss_gdf['road_type']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [50, 100, 150, 200], 
    'max_depth': [None, 10, 20, 30],      
    'min_samples_split': [2, 5, 10],      
    'min_samples_leaf': [1, 2, 4],        
    'bootstrap': [True, False]            
}


rf = RandomForestClassifier(random_state=42)


grid_search = GridSearchCV(estimator=rf, param_grid=param_grid,
                           cv=5,  
                           n_jobs=-1,  
                           verbose=2) 


grid_search.fit(X_train, y_train)


best_rf = grid_search.best_estimator_

y_pred = best_rf.predict(X_test)
print("Best Parameters:", grid_search.best_params_)
print(classification_report(y_test, y_pred))

!pip install xgboost

import xgboost as xgb

import pandas as pd
import numpy as np
from geopy.distance import geodesic

np.random.seed(0)
n_points = 500

center_lat, center_lon = 28.6139, 77.2090
lat_noise = np.random.normal(loc=0, scale=0.001, size=n_points)
lon_noise = np.random.normal(loc=0, scale=0.001, size=n_points)
timestamps = pd.date_range(start='2023-01-01', periods=n_points, freq='5s')

gnss_data = pd.DataFrame({
    'latitude': center_lat + lat_noise,
    'longitude': center_lon + lon_noise,
    'timestamp': timestamps,
    'speed': np.abs(np.random.normal(loc=30, scale=5, size=n_points)),
    'heading': np.random.uniform(0, 360, size=n_points)
})

print(gnss_data.head())

import osmnx as ox
import networkx as nx
from hmmlearn import hmm
from shapely.geometry import Point, LineString


place_name = "Delhi, India"
road_graph = ox.graph_from_place(place_name, network_type='drive')


road_graph = ox.project_graph(road_graph)


import geopandas as gpd

geometry = [Point(xy) for xy in zip(gnss_data.longitude, gnss_data.latitude)]
gnss_gdf = gpd.GeoDataFrame(gnss_data, geometry=geometry, crs='EPSG:4326')
gnss_gdf = gnss_gdf.to_crs(ox.graph_to_gdfs(road_graph, nodes=False).crs)


def map_matching_hmm(gnss_gdf, road_graph):

    model = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)


    X = np.column_stack([gnss_gdf.geometry.x, gnss_gdf.geometry.y])


    model.fit(X)

    states = model.predict(X)
    gnss_gdf['road_type'] = states
    return gnss_gdf

gnss_gdf = map_matching_hmm(gnss_gdf, road_graph)
print(gnss_gdf.head())

from geopy.distance import geodesic

def feature_engineering(gnss_gdf):
    
    road_gdf = ox.graph_to_gdfs(road_graph, nodes=False)
    gnss_gdf['nearest_road'] = gnss_gdf.apply(
        lambda row: road_gdf.distance(row.geometry).min(), axis=1
    )

    gnss_gdf['heading_change'] = gnss_gdf['heading'].diff().fillna(0)


    return gnss_gdf

gnss_gdf = feature_engineering(gnss_gdf)
print(gnss_gdf[['nearest_road', 'heading_change']].head())

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


X = gnss_gdf[['speed', 'heading_change', 'nearest_road']]
y = gnss_gdf['road_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report


X = gnss_gdf[['speed', 'heading_change', 'nearest_road']]
y = gnss_gdf['road_type']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [50, 100, 150, 200], 
    'max_depth': [None, 10, 20, 30],      
    'min_samples_split': [2, 5, 10],      
    'min_samples_leaf': [1, 2, 4],        
    'bootstrap': [True, False]            
}


rf = RandomForestClassifier(random_state=42)


grid_search = GridSearchCV(estimator=rf, param_grid=param_grid,
                           cv=5,  
                           n_jobs=-1,  
                           verbose=2) 


grid_search.fit(X_train, y_train)


best_rf = grid_search.best_estimator_

y_pred = best_rf.predict(X_test)
print("Best Parameters:", grid_search.best_params_)
print(classification_report(y_test, y_pred))

pip install xgboost

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


X = gnss_gdf[['speed', 'heading_change', 'nearest_road']]
y = gnss_gdf['road_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

xgb_model = xgb.XGBClassifier(
    n_estimators=100,      
    learning_rate=0.1,     
    max_depth=5,           
    subsample=0.8,         
    colsample_bytree=0.8,  
    random_state=42        
)

xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)
print(classification_report(y_test, y_pred))


accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)

import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


data = load_iris()
X = data.data
y = data.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model saved successfully.")

from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

     
        df = pd.DataFrame(data)



        features = df.to_numpy()

        
        predictions = model.predict(features)

        response = {'predictions': predictions.tolist()}

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

