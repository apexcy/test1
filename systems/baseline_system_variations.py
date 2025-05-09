import os

from systems.baseline_system import BaselineLLMSystem, BaselineLLMSystemOllama

class BaselineLLMSystemGPT4oFewShot(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="gpt-4o", name="BaselineLLMSystemGPT4oFewShot", variance="few_shot", verbose=verbose, *args, **kwargs)

class BaselineLLMSystemGemma3(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="google/gemma-3-27b-it", name="BaselineLLMSystemGemini3", variance="few_shot", verbose=verbose, *args, **kwargs)


class BaselineLLMSystemDeepseekR1(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="deepseek-ai/DeepSeek-R1", name="BaselineLLMSystemDeepseekR1", variance="few_shot", verbose=verbose, *args, **kwargs)

class BaselineLLMSystemDeepseekCoder(BaselineLLMSystemOllama):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="deepseek-coder:33b", name="BaselineLLMSystemDeepseekCoder", variance="few_shot", verbose=verbose, *args, **kwargs)

class BaselineLLMSystemQwen2_5Coder(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="Qwen/Qwen2.5-Coder-32B-Instruct", name="BaselineLLMSystemQwen2_5Coder", variance="few_shot", verbose=verbose, *args, **kwargs)

class BaselineLLMSystemLlama3_3Intruct(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="meta-llama/Llama-3.3-70B-Instruct-Turbo", name="BaselineLLMSystemLlama3_3Intruct", variance="few_shot", verbose=verbose, *args, **kwargs)