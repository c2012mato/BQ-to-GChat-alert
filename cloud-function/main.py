import requests
import functions_framework
import os

WEBHOOK_URL = os.getenv("GCHAT_WEBHOOK_URL", "YOUR_WEBHOOK_HERE")

@functions_framework.http
def bigquery_alert(request):
    """HTTP Cloud Function to send alerts from BigQuery to Google Chat."""
    data = request.get_json(silent=True)
    alert_msg = f"BigQuery Alert: {data.get('description', 'Check your table!')}"
    payload = {"text": alert_msg}
    resp = requests.post(WEBHOOK_URL, json=payload)
    if resp.status_code != 200:
        return f"Failed to send alert: {resp.text}", 500
    return 'OK', 200
