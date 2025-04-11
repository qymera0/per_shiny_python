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
async def result():
    input.compute() # Take a dependecy on the button
    await asyncio.sleep(2)
    with reactive.isolate():
        # Read input.n() without taking a dependency on it
        return f"Result:{input.n()}"