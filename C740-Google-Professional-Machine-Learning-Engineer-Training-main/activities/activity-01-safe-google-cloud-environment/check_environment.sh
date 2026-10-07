#!/usr/bin/env bash
set -euo pipefail
gcloud config get-value project
gcloud config get-value ai/region
gcloud services list --enabled --filter='name:(aiplatform.googleapis.com OR bigquery.googleapis.com OR run.googleapis.com)' --format='value(name)'
