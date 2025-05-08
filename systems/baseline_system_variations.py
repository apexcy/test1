import os

from systems.baseline_system import BaselineLLMSystem, BaselineLLMSystemOllama

class BaselineLLMSystemGPT4oFewShot(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="gpt-4o", name="BaselineLLMSystemGPT4oFewShot", variance="few_shot", verbose=verbose, *args, **kwargs)

class BaselineLLMSystemGemma3(BaselineLLMSystemOllama):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="gemma3:27b", name="BaselineLLMSystemGemini3", variance="few_shot", verbose=verbose, *args, **kwargs)

class BaselineLLMSystemDeepseekCoder(BaselineLLMSystemOllama):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="deepseek-coder:33b", name="BaselineLLMSystemDeepseekCoder", variance="few_shot", verbose=verbose, *args, **kwargs)

class BaselineLLMSystemQwen2_5Coder(BaselineLLMSystemOllama):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(model="qwen2.5-coder:32b", name="BaselineLLMSystemQwen2_5Coder", variance="few_shot", verbose=verbose, *args, **kwargs)
