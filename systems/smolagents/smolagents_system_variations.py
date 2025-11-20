from .deepresearch import SmolagentsDeepResearch
from .reflexion import SmolagentsReflexion
from .pdt import SmolagentsPDT

class SmolagentsDeepResearchClaude37Sonnet(SmolagentsDeepResearch):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model="claude-3-7-sonnet-latest",
            name="SmolagentsDeepResearchClaude37Sonnet",
            verbose=verbose,
            supply_data_snippet=True,
            *args, **kwargs
        )

class SmolagentsReflexionClaude37Sonnet(SmolagentsReflexion):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model="claude-3-7-sonnet-latest",
            name="SmolagentsReflexionClaude37Sonnet",
            verbose=verbose,
            supply_data_snippet=True,
            *args, **kwargs
        )

class SmolagentsPDTClaude37Sonnet(SmolagentsPDT):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model="claude-3-7-sonnet-latest",
            name="SmolagentsPDTClaude37Sonnet",
            verbose=verbose,
            supply_data_snippet=True,
            *args, **kwargs
        )