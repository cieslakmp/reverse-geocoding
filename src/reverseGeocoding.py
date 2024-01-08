import pandas as pd
import geopandas as gpd
import geopy

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt
import tqdm
from tqdm import tqdm


import plotly_express as px
import plotly.io as pio
pio.renderers.default = "vscode"
import panel as pn
pn.extension()

locator = Nominatim(user_agent="myGeocoder")
coordinates = "53.480837, -2.244914"
location = locator.reverse(coordinates)
print(location.address)

# sample of a dataset containting lats and lons

url = "https://www.dropbox.com/s/15gisj8hx218rn1/street-pole-sample.csv?dl=1"

df = pd.read_csv(url)
print(df.head())

#px.scatter_mapbox(df, lat = "Y", lon="X", zoom = 15)

df["geom"] = df["Y"].map(str) + ',' + df["X"].map(str)
print(df["geom"][0])

locator = Nominatim(user_agent="myGeocoder", timeout=10)
rgeocode = RateLimiter(locator.reverse, min_delay_seconds=0.001)

tqdm.pandas()
df['address'] = df['geom'].progress_apply(rgeocode)
print(df.head())
# testing git