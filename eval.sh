#!/bin/bash

module load anaconda/Python-ML-2025a
source .venv/bin/activate

# Run the script
datasets=("archeology")

for ds in "${datasets[@]}"; do
  echo "Running benchmark on dataset: $ds"
  python evaluate.py --sut BaselineLLMSystemGPTo3FewShot --dataset_name "$ds" --workload_filename "$ds.json" --use_truth_subset --run_subtasks
done