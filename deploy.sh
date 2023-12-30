#!/bin/bash

# update requirements file to reflect latest packages
pipenv run pip freeze > requirements.txt

# format python files
black .

# create docker image and store it in 
gcloud builds submit --tag gcr.io/<PROJECT_NAME>/streamlit-data-tools --project=<PROJECT_NAME>

# deploy to cloud run
gcloud run deploy streamlit-data-tools --image gcr.io/<PROJECT_NAME>/streamlit-data-tools --platform managed  --project=<PROJECT_NAME> --allow-unauthenticated --region australia-southeast1 --memory 2Gi