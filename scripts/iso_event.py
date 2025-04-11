import asyncio
from shiny import reactive
from shiny.express import input, render, ui

ui.input_slider(
    'n',
    'N',
    min=1, max=100, value=1
    )

ui.input_action_button('compute', 'Compute!')

@render.text

@reactive.event(input.compute) # Take a dependency on the button

async def result():
    # Any reactive dependencies inside this function are ignored
    await asyncio.sleep(2) # Simulate a long computaion
    return f"Result: {input.n()}"