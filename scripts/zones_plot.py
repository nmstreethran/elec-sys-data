"""Plotting bidding zones for DE and its interconnections

This script plots approximate SE electricity market bidding zones
from Tomorrow's electricityMap
(https://github.com/tmrowco/electricitymap-contrib), and bidding zones for
DE, AT, CH, CZ, DK, FR, LU, NL, PL using nomenclature of territorial units
for statistics (NUTS) data from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background).
"""

# import libraries
import geopandas as gpd

# import data
zones = gpd.read_file(
    'https://gitlab.com/api/v4/projects/19753809/repository/files/' +
    'geography%2Fpolygons%2Fbidding_zones.geojson/raw?ref=master')

# Bokeh plot

# import libraries
from bokeh.io import show # output_file
from bokeh.models import GeoJSONDataSource, CategoricalColorMapper, Plot
from bokeh.plotting import figure
from bokeh.palettes import viridis
# from bokeh.tile_providers import get_provider, Vendors

# load data source
geo_source = GeoJSONDataSource(geojson=zones.to_json())

# generate unique colours for each bidding zone
zoneList = list(zones['zone'])
palette = viridis(len(zoneList))
color_map = CategoricalColorMapper(factors=zoneList, palette=palette)

# define map tooltips
TOOLTIPS = [('Zone', '@zone'), ('(Lon, Lat)', '($x, $y)')]

# set output backend for the glyph API
p = Plot(output_backend='webgl')

# set figure tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
# set output backend for the plotting API
p = figure(
    # x_axis_type='mercator', y_axis_type='mercator',
    tooltips=TOOLTIPS, output_backend='webgl', tools='save, hover',
    plot_width=400)

# # set OpenStreetMap / CartoDB overlay
# p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# hover settings
p.hover.point_policy = 'follow_mouse'

# add data and configure plot
p.patches(
    'xs', 'ys', fill_color={'field': 'zone', 'transform': color_map},
    source=geo_source, line_color='white', line_width=.5)

# open the map
show(p)

# Bokeh components

"""

# output the map and save to a custom path
output_file('charts/zones_plot.html')

# import libraries
from bokeh.embed import components

# to export script and div components
script, div = components(p)
# remove script HTML tags to save as JavaScript file
script = script.replace('<script type="text/javascript">', '')
script = script.replace('</script>', '')

# export script as JavaScript file
with open('charts/bidding_zones/zones.js', 'w') as f:
    print(script, file=f)
# export div as HTML file
with open('charts/bidding_zones/zones-div.html', 'w') as f:
    print(div, file=f)
# export div as JavaScript file
# (so that it can be read by zones.html)
with open('charts/bidding_zones/zones-div.js', 'w') as f:
    print('document.write(`' + div + '\n`);', file=f)
"""

# Matplotlib plot

"""

# import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt

# convert to Web Mercator projection
zones = zones.to_crs(crs='EPSG:3857')

# plot styles
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']

# configure plot
fig, ax = plt.subplots(1, figsize=(13, 13))
zones.plot(
    column='zone', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'loc': 'lower right'})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
plt.show()
"""
