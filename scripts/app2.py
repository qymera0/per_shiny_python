from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_text("text", label="Enter some text"),
    ui.output_text("text_out")
)

def server(input):
    @render.text
    def text_out():
        return f"Input text: {input.text()}"

app = App(app_ui, server)