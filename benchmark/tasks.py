import json
import os
from typing import Any, Dict, List

from benchmark_api import System

class Executor:
    def __init__(
            self,
            system: System,
            workload_path: str | os.PathLike,
            results_directory: str | os.PathLike,
            verbose=False
        ):
        """
        `workload_path` is a json file containing workloads.
        """
        self.system = system
        if self.system.dataset_directory is None:
            raise Exception("Executor __init__ error: System.process_dataset was not called.")
        with open(workload_path) as f:
            self.workload = json.load(f)
        self.num_queries = len(self.workload)
        self.cur_query_id = 0
        self.results_directory = results_directory
        self.workload_path = workload_path
        self.verbose = verbose
    
    def run_task(self, task: Dict[str, Any]) -> Dict[str, str | Dict | List]:
        """
        Takes a task entry and runs it on the test subject System
        See `workload/` for examples of the input.
        The output is formatted as follows
        {
            "task_id": str
            "model_output": text or json - the content directly outputed by test System
            "subresponses": [ ... {"model_output": ..., "subresponses": ... } ... ]
        }
        """
        if self.verbose:
            print(f"task_id: {task["id"]}")
            print(f"query: {task["query"]}")
        model_output = self.system.serve_query(task["query"])
        response = {}
        response["task_id"] = task["id"]
        response["model_output"] = model_output
        response["subresponses"] = []
        for subtask in task["subtasks"]:
            subresponse = self.run_task(subtask)
            response["subresponse"].append(subresponse)
        return response
    
    def run_next_task(self):
        """
        Iterator model to run all tasks in this test workload.
        """
        if self.cur_query_id >= self.num_queries:
            return None
        result = self.run_task(self.workload[self.cur_query_id])
        self.cur_query_id += 1
        return result
    
    def reset_task_iterator(self):
        self.cur_query_id = 0
    
    def run_workload(self, cache_system_output: bool = True):
        """
        Runs all the tasks in the given workload.
        Results are cached under self.results_directory/output_cache.
        Note that the cache content here are the raw response dicts, not
        evaluation results.
        """
        if self.verbose:
            print(f"------------- Running workload at {self.workload_path} ----------------")
        results = []
        while True:
            result = self.run_next_task()
            if result is None:
                break
            results.append(result)
        
        if cache_system_output:
            # TODO(SylviaZiyuZhang): implement me
            pass

        return results

class Evaluator:
    def __init__(
            self,
            workload_path: str | os.PathLike,
            task_fixture_directory: str | os.PathLike,
            results_directory: str | os.PathLike
        ):
        """
        `task_fixtures_directory` contains the tasks fixtures for finding valid
        evaluation methods of each type of task and response.
        """
        self.workload_path = workload_path
        self.task_fixture_directory = task_fixture_directory
        self.results_directory = results_directory
        with open(workload_path) as f:
            self.workload = json.load(f)
        with open(task_fixture_directory/'task_fixtures.json') as f:
            self.task_fixtures = json.load(f)
        with open(task_fixture_directory/'input_type_fixtures.json') as f:
            self.input_type_fixtures = json.load(f)
        with open(task_fixture_directory/'output_type_fixtures.json') as f:
            self.output_type_fixtures = json.load(f)
    
    def evaluate_results_on_metric(responses: List[Dict[str, Any]], metric_name: str):
        # TODO: implement me
        pass

    def evaluat_results(responses: List[Dict[str, Any]]):
        """
        Evaluate results on all applicable metrics as specified in the task fixtures.
        """
        # TODO: implement me
        pass

class Benchmark:
    def __init__ (
            self,
            system_name: str,
            task_fixture_directory: str | os.PathLike,
            cache_system_output: bool = False,
    ):
        system_module = __import__("system")
        system_class_ = getattr(system_module, system_name)
        self.system = system_class_()
        self.cache_system_output = cache_system_output
        self.task_fixture_directory = task_fixture_directory
    
    def run_benchmark(
            self,
            dataset_directory: str | os.PathLike,
            results_directory: str | os.PathLike,
            workload_path: str | os.PathLike,
            verbose: bool = False
        ):
        self.system.process_dataset(dataset_directory)
        executor = Executor(
            system=self.system,
            workload_path=workload_path,
            results_directory=results_directory,
            verbose=verbose
        )
        results = executor.run_workload(cache_system_output=self.cache_system_output)
        evaluator = Evaluator(
            workload_path=workload_path,
            task_fixture_directory=self.task_fixture_directory,
            results_directory=results_directory
        )
        evaluator.evaluat_results(results)

