"""Plotting NUTS 3 boundaries for DE

This script obtains nomenclature of territorial units for
statistics (NUTS) data at level 3 from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background) for DE. It then
creates a plot of the these boundaries.
"""

# import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd
from os import path

# import data
if path.isfile('data/geography/polygons/nuts3_DE.geojson'):
    nuts3 = gpd.read_file('data/geography/polygons/nuts3_DE.geojson')
else:
    from nuts3 import nuts3

# convert to Web Mercator projection
nuts3 = nuts3.to_crs(crs='EPSG:3857')

# ## Matplotlib plot
# plot styles
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']

# configure plot
fig, ax = plt.subplots(1, figsize=(13, 13))
nuts3.plot(
    column='CNTR_CODE', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'loc': 'lower right'})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
plt.show()

"""Bokeh plot

# import libraries
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, CategoricalColorMapper
from bokeh.plotting import figure
from bokeh.palettes import viridis
from bokeh.tile_providers import get_provider, Vendors
from bokeh.embed import components

# load data source
geo_source = GeoJSONDataSource(geojson=nuts3.to_json())

# generate unique colours for each country
countries = list(set(nuts3['CNTR_CODE']))
palette = viridis(len(countries))
color_map = CategoricalColorMapper(factors=countries, palette=palette)

# define map tooltips
TOOLTIPS = [('NUTS', '@NUTS_ID: @NUTS_NAME')]

# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
p = figure(
    title='NUTS 3 boundaries. Data: Eurostat.',
    tooltips=TOOLTIPS, x_axis_type='mercator', y_axis_type='mercator')

# set OpenStreetMap / CartoDB overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data and configure plot
p.patches(
    'xs', 'ys', fill_color={'field': 'CNTR_CODE', 'transform': color_map},
    source=geo_source, line_color='white', line_width=.5)

# open the map
show(p)
"""
