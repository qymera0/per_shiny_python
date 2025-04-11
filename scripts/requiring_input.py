import pandas as pd
from shiny import reactive, req
from shiny.express import input, render, ui

ui.input_file(
    'file',
    'Upload a csv file',
    accept='.csv'
    )

@reactive.calc
def df():
    # req() stops execution until input.file() is truthy
    f = req(input.file())
    return pd.read_csv(f[0]['datapath'])

@render.data_frame
def table():
    # Output won´t render until input.file() is truthy
    return render.DataGrid(df())