"""Plotting bidding zones for the focus countries and interconnections

This script executes zones_no_se.py to obtain approximate Norwegian and
Swedish electricity market bidding zones from
tmrowco/electricitymap-contrib, and zones.py to obtain all other bidding
zones using nomenclature of territorial units for statistics (NUTS) data.
It then creates a plot of the bidding zones.
"""

# import libraries
from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource, CategoricalColorMapper
from bokeh.plotting import figure
from bokeh.palettes import viridis
from bokeh.tile_providers import get_provider, Vendors
from bokeh.embed import components

# import data
from zones import zones

# convert to Web Mercator projection
zones = zones.to_crs(crs='EPSG:3857')

# load data source
geo_source = GeoJSONDataSource(geojson=zones.to_json())

# generate unique colours for each bidding zone
zoneList = list(zones['zone'])
palette = viridis(len(zoneList))
color_map = CategoricalColorMapper(factors=zoneList, palette=palette)

# define map tooltips
TOOLTIPS = [('Zone', '@zone')]

# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
p = figure(title='Bidding zones. Data: tmrowco, Eurostat.',
    tooltips=TOOLTIPS, x_axis_type='mercator', y_axis_type='mercator')

# set OpenStreetMap / CartoDB overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data and configure plot
p.patches('xs', 'ys', fill_color={'field': 'zone', 'transform': color_map},
    source=geo_source, line_color='white', line_width=.5)

# # output the map and save to a custom path
# output_file('charts/bidding_zones/zones_plot.html')
# open the map
show(p)

# # to export script and div components
# script, div = components(p)
# # remove script HTML tags to save as JavaScript file
# script = script.replace('<script type="text/javascript">', '')
# script = script.replace('</script>', '')

# # export script as JavaScript file
# with open('charts/bidding_zones/zones.js', 'w') as f:
#     print(script, file=f)
# # export div as HTML file
# with open('charts/bidding_zones/zones-div.html', 'w') as f:
#     print(div, file=f)
# # export div as JavaScript file
# # (so that it can be read by zones.html)
# with open('charts/bidding_zones/zones-div.js', 'w') as f:
#     print('document.write(`' + div + '\n`);', file=f)