from shiny import reactive
from shiny.express import input, render, ui

ui.input_slider(
    'x',
    'Slider value',
    min=0, max=100,
    value=10
    )


@reactive.calc
def x2():
    return input.x() ** 2


@render.ui
def out1():
    return f"Render UI: {x2()}"


@render.text
def out2():
    return f'Render text: {x2()}'