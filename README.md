# BigQuery Table Health Checker & Google Chat Alerts

This sample shows how to automatically monitor BigQuery table health (freshness, null checks, etc.) and send alerts to a Google Chat space using a webhook and a Cloud Function.

## Architecture

- **BigQuery** scheduled query checks table health and writes results to an `alerts` table.
- **Cloud Scheduler** (or Pub/Sub) triggers a **Cloud Function** after each run.
- The **Cloud Function** sends an alert message to a Google Chat webhook if issues are detected.

See `/diagrams/architecture.txt` for a diagram.

---

## Quick Start

### 1. Google Chat: Create a Webhook

- In your Google Chat space, go to *Apps & Integrations* > *Webhooks*.
- Add a webhook (e.g. `BigQuery Alerts`) and copy the webhook URL.

### 2. BigQuery: Schedule a Health Check

- Edit `/bigquery/health_check_example.sql` for your table/logic.
- Schedule the query to write results to an `alerts` table.

### 3. Deploy Cloud Function

- Fill in your webhook URL in `/cloud-function/main.py`.
- Deploy the function to Google Cloud.

### 4. Connect Everything

- Trigger the function from Cloud Scheduler, Pub/Sub, or directly from BigQuery.

---

## Files

- `cloud-function/` — Python code for Google Cloud Function.
- `bigquery/` — Example SQL health check.
- `diagrams/` — ASCII architecture diagram.

## License

MIT
  
