from .baseline_system import BaselineLLMSystem

class BaselineLLMSystemGPT4oFewShot(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model="gpt-4o",
            name="BaselineLLMSystemGPT4oFewShot",
            variance="few_shot",
            verbose=verbose,
            supply_data_snippet=True,
            *args, **kwargs
        )

class BaselineLLMSystemGPT4oOneShot(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model="gpt-4o",
            name="BaselineLLMSystemGPT4oOneShot",
            variance="one_shot",
            verbose=verbose,
            supply_data_snipper=True,
            *args, **kwargs
        )

class BaselineLLMSystemGPT4oNaive(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model="gpt-4o",
            name="BaselineLLMSystemGPT4oOneShot",
            variance="one_shot",
            verbose=verbose,
            supply_data_snipper=False,
            *args, **kwargs
        )