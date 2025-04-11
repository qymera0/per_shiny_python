from shiny import reactive
from shiny.express import input, render, ui

ui.input_slider(
    'x',
    'Slider value',
    min=0, max=100,
    value=10
    )

@reactive.effect
def _():
    ui.insert_ui(
        ui.p(input.x()),
        selector='#x',
        where='afterEnd'
        )