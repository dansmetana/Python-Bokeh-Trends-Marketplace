# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:08:09 2020

@author: dsmet
"""

#import the necessary libraries
import pandas as pd
import bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, HoverTool, CategoricalColorMapper

#create the dataframe
ex_df = pd.read_csv("datasource_name.csv")

#create an output file
output_file('example.html', title = "Example Title")

#store the data in a ColumnDataSource
ex_cds = ColumnDataSource(ex_df)


