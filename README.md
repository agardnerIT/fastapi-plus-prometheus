# fastapi-plus-prometheus

## Install Requirements
`pip install -r requirements.txt`

## Run Non-Prometheus Enabled Version

```
fastapi dev app1.py
```

Go to `http://127.0.0.1:8000`

## Run Prometheus Enabled Version

Stop the previous server.

Run the new version:
```
fastapi dev app2.py
```

Go to `http://127.0.0.1:8000` and see the same JSON. Refresh the page a few times to increment the `app_requests_total` counter.
Open a new tab and go to `http://127.0.0.1:8000/metrics`

At the end of the page you'll notice the metrics you created:

* `app_requests_total{endpoint="/"}`
* `app_random_number`
