# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:08:09 2020

@author: dsmet
"""

#import the necessary libraries
import pandas as pd
import bokeh

#create the dataframe
nfl_data = pd.read_csv("2019projections_fantasy.csv")

#import key bokeh functionality 
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import gridplot

#create sub-data frames
week1_nfl = nfl_data[nfl_data['Week'] == 1]
week10_nfl = nfl_data[nfl_data['Week'] == 10]

#create output file
output_file('nflweek_proj_v_actual.html', title = "NFL Week 2 Player Fantasy Projections vs. Actual Points")

#store the data in a ColumnDataSources
week1_nfl_cds = ColumnDataSource(week1_nfl)
week10_nfl_cds = ColumnDataSource(week10_nfl)

#select tools
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

#Create the figures
fig = figure(plot_height=600,
             plot_width=600,
             x_axis_label='Projected Player Fantasy Output',
             y_axis_label='Actual Player Fantasy Output',
             title='NFL Week 1 Player Fantasy Projections vs. Actual Points',
             toolbar_location='below',
             tools=select_tools)

fig2 = figure(plot_height=600,
             plot_width=600,
             x_axis_label='Projected Player Fantasy Output',
             y_axis_label='Actual Player Fantasy Output',
             title='NFL Week 10 Player Fantasy Projections vs. Actual Points',
             toolbar_location='below',
             tools=select_tools)

#Add a circle for each player
fig.circle(x = 'Proj', 
           y = 'Actual',
           source = week1_nfl_cds,
           color = '#Fb4F4F',
           selection_color = "#AD0909",
           nonselection_color = '#D0D0D0',
           nonselection_alpha = 0.3,
           size = 5)

fig2.circle(x = 'Proj', 
           y = 'Actual',
           source = week10_nfl_cds,
           color = '#01D3D0',
           selection_color = "#032D7A",
           nonselection_color = '#D0D0D0',
           nonselection_alpha = 0.3,
           size = 5)

#format tooltip for Hover functionality, list of tuples
tooltips = [('Player', '@Player'), ('Projected Points', '@Proj'), ('Actual Points', '@Actual')]

#add the hover functionality to the figures
fig.add_tools(HoverTool(tooltips = tooltips))
fig2.add_tools(HoverTool(tooltips = tooltips))

#create a side-by-side gride
grid = gridplot([[fig, fig2]])

#show the visual
show(grid)
