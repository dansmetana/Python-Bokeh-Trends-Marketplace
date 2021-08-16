# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:25:58 2020

@author: dsmet
"""

#import the necessary libraries
import pandas as pd
import bokeh

#create the dataframe
gdp_data = pd.read_csv("world_gdpPerCapita.csv")

#import key bokeh functionality 
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Tabs, Panel

#create sub-data frames
gdp_americas = gdp_data[(gdp_data['Country Name'] == 'United States') | (gdp_data['Country Name'] == 'Canada') | 
                        (gdp_data['Country Name'] == 'Brazil') | (gdp_data['Country Name'] == 'Mexico')]
gdp_europe = gdp_data[(gdp_data['Country Name'] == 'France') | (gdp_data['Country Name'] == 'Italy') |
                      (gdp_data['Country Name'] == 'Spain') | (gdp_data['Country Name'] == 'United Kingdom')] 
gdp_asia = gdp_data[(gdp_data['Country Name'] == 'China') | (gdp_data['Country Name'] == 'India') |
                    (gdp_data['Country Name'] == 'Japan') | (gdp_data['Country Name'] == 'Singapore')]
gdp_world = pd.concat([gdp_americas, gdp_europe, gdp_asia])


#create output file
output_file('gpd_per_capita.html', title = "GDP Per Capita")

#Create the ColumnDataSource objects
#americas
us_cds = ColumnDataSource(gdp_americas[gdp_americas['Country Name'] == "United States"])
canada_cds = ColumnDataSource(gdp_americas[gdp_americas['Country Name'] == "Canada"])
mexico_cds = ColumnDataSource(gdp_americas[gdp_americas['Country Name'] == "Mexico"])
brazil_cds = ColumnDataSource(gdp_americas[gdp_americas['Country Name'] == "Brazil"])

#europe
france_cds = ColumnDataSource(gdp_europe[gdp_europe['Country Name'] == 'France'])
italy_cds = ColumnDataSource(gdp_europe[gdp_europe['Country Name'] == 'Italy'])
spain_cds = ColumnDataSource(gdp_europe[gdp_europe['Country Name'] == 'Spain'])
uk_cds = ColumnDataSource(gdp_europe[gdp_europe['Country Name'] == 'United Kingdom'])

#asia
china_cds = ColumnDataSource(gdp_asia[gdp_asia['Country Name'] == 'China'])
india_cds = ColumnDataSource(gdp_asia[gdp_asia['Country Name'] == 'India'])
japan_cds = ColumnDataSource(gdp_asia[gdp_asia['Country Name'] == 'Japan'])
singapore_cds = ColumnDataSource(gdp_asia[gdp_asia['Country Name'] == 'Singapore'])

#select tools
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

#Create figures
#americas
fig_americas = figure(plot_height=700, plot_width=1000,
             title='GDP Per Capita',
             x_axis_label='Year', y_axis_label='GDP Per Capita',
             toolbar_location='below',
             tools=select_tools)

fig_americas.line('Year', 'GDP Per Capita', 
         color='#D3011B', legend='United States', 
         source=us_cds)
fig_americas.line('Year', 'GDP Per Capita', 
         color='#0041D5', legend='Canada', 
         source=canada_cds)
fig_americas.line('Year', 'GDP Per Capita', 
         color='#148704', legend='Mexico', 
         source=mexico_cds)
fig_americas.line('Year', 'GDP Per Capita', 
         color='#430679', legend='Brazil', 
         source=brazil_cds)
fig_americas.legend.location = "top_left"

#europe
fig_europe = figure(plot_height=700, plot_width=1000,
             title='GDP Per Capita',
             x_axis_label='Year', y_axis_label='GDP Per Capita',
             toolbar_location='below',
             tools=select_tools)

fig_europe.line( 'Year', 'GDP Per Capita', 
         color='#08E2BE', legend='France',
         source=france_cds)
fig_europe.line( 'Year', 'GDP Per Capita', 
         color='#E27F08', legend='Italy',
         source=italy_cds)
fig_europe.line( 'Year', 'GDP Per Capita', 
         color='#000000', legend='United Kingdom',
         source=uk_cds)
fig_europe.line( 'Year', 'GDP Per Capita', 
         color='#A908D4', legend='Spain',
         source=spain_cds)
fig_europe.legend.location = "top_left"

#asia
fig_asia = figure(plot_height=700, plot_width=1000,
             title='GDP Per Capita',
             x_axis_label='Year', y_axis_label='GDP Per Capita',
             toolbar_location='below',
             tools=select_tools)

fig_asia.line( 'Year', 'GDP Per Capita', 
         color='#924646', legend='China',
         source=china_cds)
fig_asia.line( 'Year', 'GDP Per Capita', 
         color='#CA07DA', legend='India',
         source=india_cds)
fig_asia.line( 'Year', 'GDP Per Capita', 
         color='#A38357', legend='Japan',
         source=japan_cds)
fig_asia.line( 'Year', 'GDP Per Capita', 
         color='#916ED4', legend='Singapore',
         source=singapore_cds)
fig_asia.legend.location = 'top_left'

#world
fig_world = figure(plot_height=700, plot_width=1000,
             title='GDP Per Capita',
             x_axis_label='Year', y_axis_label='GDP Per Capita',
             toolbar_location='below',
             tools=select_tools)

fig_world.line('Year', 'GDP Per Capita', 
         color='#D3011B', legend='United States', 
         source=us_cds)
fig_world.line('Year', 'GDP Per Capita', 
         color='#0041D5', legend='Canada', 
         source=canada_cds)
fig_world.line('Year', 'GDP Per Capita', 
         color='#148704', legend='Mexico', 
         source=mexico_cds)
fig_world.line('Year', 'GDP Per Capita', 
         color='#430679', legend='Brazil', 
         source=brazil_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#08E2BE', legend='France',
         source=france_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#E27F08', legend='Italy',
         source=italy_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#000000', legend='United Kingdom',
         source=uk_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#A908D4', legend='Spain',
         source=spain_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#924646', legend='China',
         source=china_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#CA07DA', legend='India',
         source=india_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#A38357', legend='Japan',
         source=japan_cds)
fig_world.line( 'Year', 'GDP Per Capita', 
         color='#916ED4', legend='Singapore',
         source=singapore_cds)
fig_world.legend.location = 'top_left'


#Create panels for each figure
americas_panel = Panel(child = fig_americas, title = "Americas")
europe_panel = Panel(child = fig_europe, title = 'Europe')
asia_panel = Panel(child = fig_asia, title = 'Asia')
world_panel = Panel(child = fig_world, title = 'World')

#tabs
final_graph = Tabs(tabs = [americas_panel, europe_panel, asia_panel, world_panel])
                   
#Show the new layout 
show(final_graph)
