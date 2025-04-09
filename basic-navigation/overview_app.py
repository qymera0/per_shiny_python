import plotly.express as px

from shiny.express import input, render, ui
from shinywidgets import render_plotly

# Data

tips = px.data.tips()

with ui.layout_columns():
    
    @render_plotly
    def plot1():
        p = px.histogram(tips, x = input.var1())
        p.update_layout(height = 200, xaxis_title = None)
        return p
    
    @render_plotly
    def plot2():
        p = px.histogram(tips, x = input.var2())
        p.update_layout(height = 200, xaxis_title = None)
        return p
    
with ui.layout_columns():
    ui.input_select(
        'var1',
        None,
        choices = ["total_bill", "tip"],
        width = '100%'
    )
    ui.input_select(
        'var2',
        None,
        choices = ['tip', "total_bill"],
        width = '100%'
    )