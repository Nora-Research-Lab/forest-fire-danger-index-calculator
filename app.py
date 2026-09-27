import gradio as gr
from forest_fire_danger_index_calculator import calculate_ffdi


def run_calculator(temperature, relative_humidity, wind_speed, drought_factor):
    result = calculate_ffdi(
        temperature=temperature,
        relative_humidity=relative_humidity,
        wind_speed=wind_speed,
        drought_factor=drought_factor,
    )

    if result["success"]:
        return (
            result["ffdi"],
            result["badge_html"],
            result["gauge_html"],
            "",
        )

    return (
        None,
        '<span style="color:#d32f2f;font-weight:bold;">Invalid input</span>',
        "",
        result["error"],
    )


with gr.Blocks(title="Forest Fire Danger Index Calculator") as demo:
    gr.Markdown(
        """
        # Forest Fire Danger Index Calculator
        Estimate the McArthur Forest Fire Danger Index (FFDI) from weather and drought inputs.
        """
    )

    with gr.Row():
        temperature = gr.Slider(
            minimum=-10,
            maximum=50,
            value=30,
            step=0.1,
            label="Temperature (°C)",
        )
        relative_humidity = gr.Slider(
            minimum=0,
            maximum=100,
            value=40,
            step=0.1,
            label="Relative Humidity (%)",
        )

    with gr.Row():
        wind_speed = gr.Slider(
            minimum=0,
            maximum=200,
            value=20,
            step=0.1,
            label="Wind Speed (km/h)",
        )
        drought_factor = gr.Slider(
            minimum=0,
            maximum=10,
            value=5,
            step=0.1,
            label="Drought Factor",
        )

    calculate_button = gr.Button("Calculate FFDI", variant="primary")

    ffdi_output = gr.Number(label="Forest Fire Danger Index (FFDI)", precision=2)
    classification_output = gr.HTML(label="FFDI Classification")
    gauge_output = gr.HTML(label="FFDI Gauge")
    error_output = gr.Textbox(label="Input Error", interactive=False)

    inputs = [temperature, relative_humidity, wind_speed, drought_factor]
    outputs = [ffdi_output, classification_output, gauge_output, error_output]

    calculate_button.click(fn=run_calculator, inputs=inputs, outputs=outputs)
    demo.load(fn=run_calculator, inputs=inputs, outputs=outputs)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
