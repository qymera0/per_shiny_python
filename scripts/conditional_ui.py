from shiny.express import input, render, ui

ui.input_text('message', 'Message', value='Hello, world!')

ui.input_checkbox_group(
    'styles', 'Styles',
    choices=['Bold', 'Italic'],
    selected=['Bold'],
    inline='True'
    )

@render.ui

def result():
    x = input.message()
    if 'Bold' in input.styles():
        x = ui.strong(x)
    if 'Italic' in input.styles():
        x = ui.em(x)
    return x



