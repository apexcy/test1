#!/bin/bash

module load anaconda/Python-ML-2025a
source .venv/bin/activate

# Run the script
datasets=("archeology" "astronomy" "biomedical" "environment" "legal" "wildfire")
systems=(
  "BaselineLLMSystemGPT4oNaive"
  "BaselineLLMSystemGPTo3Naive"
  "BaselineLLMSystemClaude35Naive"
  "BaselineLLMSystemLlama3_3InstructNaive"
  "BaselineLLMSystemDeepSeekR1Naive"
  "BaselineLLMSystemQwen2_5CoderNaive"
  "BaselineLLMSystemGPT4oOneShot"
  "BaselineLLMSystemGPTo3OneShot"
  "BaselineLLMSystemClaude35OneShot"
  "BaselineLLMSystemLlama3_3InstructOneShot"
  "BaselineLLMSystemDeepSeekR1OneShot"
  "BaselineLLMSystemQwen2_5CoderOneShot"
  "BaselineLLMSystemGPT4oFewShot"
  "BaselineLLMSystemGPTo3FewShot"
  "BaselineLLMSystemClaude35FewShot"
  "BaselineLLMSystemLlama3_3InstructFewShot"
  "BaselineLLMSystemDeepSeekR1FewShot"
  "BaselineLLMSystemQwen2_5CoderFewShot"
  
  # add more systems here if needed
)

for ds in "${datasets[@]}"; do
  for sut in "${systems[@]}"; do
    echo "==============================================="
    echo "Dataset: $ds | System: $sut"
    echo "==============================================="

    # Run evaluate.py
    # Remove 'tee' if you don't want logs saved to files
    python evaluate.py \
      --sut "$sut" \
      --dataset_name "$ds" \
      --workload_filename "${ds}.json" \
      --run_subtasks \
      --use_evaluation_cache
  done
done