from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
from prometheus_client import Counter, Gauge, make_asgi_app

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Define Prometheus metrics
REQUEST_COUNTER = Counter(
    "app_requests_total",  # Metric name
    "Total number of requests to the app",  # Metric description
    ["endpoint"],  # Labels (e.g., endpoint name)
)

RANDOM_NUMBER_GAUGE = Gauge(
    "app_random_number",  # Metric name
    "Current value of the random number",  # Metric description
)

@app.get("/", response_class=JSONResponse)
def get_homepage():
    # Increment the request counter
    REQUEST_COUNTER.labels(endpoint="/").inc()

    random_number = random.randint(a=0, b=100)

     # Set the random number gauge
    RANDOM_NUMBER_GAUGE.set(random_number)

    return {"status": "ok", "random_number": random_number}
