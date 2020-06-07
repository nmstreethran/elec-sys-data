"""Plotting bidding zones in Norway and Sweden

This script executes zones_no_se.py to obtain approximate Norwegian and
Swedish electricity market bidding zones from
tmrowco/electricitymap-contrib. It then creates a plot of the bidding zones.
"""

# import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
# import contextily as ctx

# import data
from zones_no_se import bzn

# convert to Web Mercator projection
bzn = bzn.to_crs(crs='EPSG:3857')

# plot the zones
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']
fig, ax = plt.subplots(1, figsize=(10, 9.5))
bzn.plot(column='zone', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'bbox_to_anchor': (0, 0, .99, .37)})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
# ctx.add_basemap(ax, crs=bzn.crs.to_string())
