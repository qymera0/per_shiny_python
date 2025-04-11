from shiny import reactive
from shiny.express import input, render, ui

ui.input_slider(
    'x',
    'Slider value',
    min=0, max=100,
    value=10
    )

# Starts with a empty list

vals = reactive.value([])

# Track the history of the slider


@reactive.effect
@reactive.event(input.x)
def _():
    vals.set([input.x()] + vals())

@render.ui
def out():
    return [ui.p(x) for x in vals()]

