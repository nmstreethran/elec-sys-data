"""Plotting national boundaries for DE and its interconnections

This script obtains national borders based on nomenclature of
territorial units for statistics (NUTS) from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background) for the following
countries: DE, DK, SE, AT, CH, CZ, FR, LU, NL, PL.
It then creates a plot of the these boundaries.
"""

# import libraries
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt

# import data
cntr = gpd.read_file(
    'https://gitlab.com/api/v4/projects/19753809/repository/files/' +
    'geography%2Fpolygons%2Fcountries%2Egeojson/raw?ref=master')

# plot styles
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']

# configure plot
fig, ax = plt.subplots(1, figsize=(13, 13))
cntr.plot(
    column='CNTR_CODE', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'loc': 'lower right'})
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.show()

"""Bokeh plot

# import libraries
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, CategoricalColorMapper, Plot
from bokeh.plotting import figure
from bokeh.palettes import viridis

# load data source
geo_source = GeoJSONDataSource(geojson=cntr.to_json())

# generate unique colours for each country
countries = list(set(cntr['CNTR_CODE']))
palette = viridis(len(countries))
color_map = CategoricalColorMapper(factors=countries, palette=palette)

# define map tooltips
TOOLTIPS = [('Country', '@CNTR), ('(Lon, Lat)', '($x, $y)')]

# set output backend for the glyph API
p = Plot(output_backend='webgl')

# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
p = figure(
    tooltips=TOOLTIPS, output_backend='webgl', tools='save, hover',
    plot_width=4, plot_height=6)

# hover settings
p.hover.point_policy = 'follow_mouse'

# add data and configure plot
p.patches(
    'xs', 'ys', fill_color={'field': 'CNTR_CODE', 'transform': color_map},
    source=geo_source, line_color='white', line_width=.5)

# open the map
show(p)
"""
