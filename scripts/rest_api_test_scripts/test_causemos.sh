#!/usr/bin/env bash

# CauseMos-Delphi integration QA script

# Exit immediately if there is an error.

set -e

# Set the host 

host=localhost:5000

base_url=$host/delphi

# Test model listing
curl $base_url/models

# Test model creation
curl -X POST -d @create-model.json -H "Content-Type:application/json" $base_url/create-model
echo "Model creation successful."

# Get the model id
model_id=`curl -s ${base_url}/models | head -n 2 | tail -n 1 | cut -d '"' -f 2`

# Test projection
experiment_id=`curl -X POST -d @projection-input.json \
  -H "Content-Type:application/json" ${base_url}/models/${model_id}/projection \
  | head -n 2 \
  | tail -n 1 \
  | cut -d '"' -f 4`

# Get experiment results
seconds_to_wait=5
echo "Waiting ${seconds_to_wait} seconds..."
sleep $seconds_to_wait
results=`curl -s ${base_url}/models/${model_id}/experiment/${experiment_id}`
echo $results | python test_causemos.py 
