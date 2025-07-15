import plotly.graph_objs as go
import plotly.io as pio
import os
import uuid

def generate_vitals_graph(vitals_data: list) -> str:
    visits = list(range(1, len(vitals_data) + 1))

    weight = [v['weight'] for v in vitals_data]
    sugar = [v['sugar'] for v in vitals_data]
    pressure = [v['pressure'] for v in vitals_data]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=visits, y=weight, mode='lines+markers', name='Weight (kg)'))
    fig.add_trace(go.Scatter(x=visits, y=sugar, mode='lines+markers', name='Sugar (mg/dL)'))
    fig.add_trace(go.Scatter(x=visits, y=pressure, mode='lines+markers', name='BP (mmHg)'))

    fig.update_layout(
        title="🩺 Vitals Trend Over 10 Visits",
        xaxis_title="Visit Number",
        yaxis_title="Values",
        template="plotly_white"
    )

    os.makedirs("charts", exist_ok=True)
    filename = f"vitals_{uuid.uuid4().hex[:6]}.html"
    path = os.path.join("charts", filename)

    pio.write_html(fig, file=path, auto_open=False)
    return path
