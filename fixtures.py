from systems.baseline_example import ExampleBaselineSystem


def sut_factory(cls, sut: str = None):
        if sut == "baseline-gpt-4o-mini":
            return ExampleBaselineSystem("gpt-4o-mini")
        elif sut == "baseline-gpt-4o":
            return ExampleBaselineSystem("gpt-4o")
        elif sut == "baseline-mixtral":
            return ExampleBaselineSystem("mixtral")
        elif sut == "baseline-llama3":
            return ExampleBaselineSystem("llama3")
        else:
            raise ValueError(f"System {sut} not found")
