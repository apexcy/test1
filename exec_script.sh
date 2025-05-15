#!/bin/bash
for workload in "archeology" "astronomy" "biomedical" "environment" "legal" "wildfire"; do

for sut_name in "BaselineLLMSystemDeepseekR1" "BaselineLLMSystemLlama3_3Instruct" "BaselineLLMSystemQwen2_5Coder"; do
 for config in "Naive" "OneShot" "FewShot"; do
    echo "Running workload: $workload with SUT: $sut_name$config"
    "python evaluate.py --sut $sut_name$config --workload $workload.json --dataset_name $workload

done
done
done
