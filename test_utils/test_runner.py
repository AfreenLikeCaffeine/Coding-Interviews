"""
Test execution framework for LeetCode problems.

This module provides test runners to execute test cases and report results:
- TestRunner: For regular Solution methods
- ClassTestRunner: For class-based problems (e.g., MedianFinder)
- TestCase, TestResult: Data structures for test management
"""

from typing import List, Dict, Any, Callable, Optional
from enum import Enum


class TestResultStatus(Enum):
    """Status of a test result."""
    PASSED = "PASSED"
    FAILED = "FAILED"
    ERROR = "ERROR"


class TestCase:
    """Represents a single test case."""

    def __init__(self, name: str, inputs: Dict[str, Any], expected: Any,
                 comparator: Optional[Callable] = None):
        """
        Initialize a test case.

        Args:
            name: Descriptive name for the test case
            inputs: Dictionary of input parameters (keys match function args)
            expected: Expected output
            comparator: Optional custom comparison function
        """
        self.name = name
        self.inputs = inputs
        self.expected = expected
        self.comparator = comparator or (lambda a, e: a == e)


class TestResult:
    """Represents the result of running a test case."""

    def __init__(self, test_name: str, status: TestResultStatus,
                 actual=None, expected=None, error_msg: str = ""):
        self.test_name = test_name
        self.status = status
        self.actual = actual
        self.expected = expected
        self.error_msg = error_msg

    def __str__(self):
        if self.status == TestResultStatus.PASSED:
            return f"[PASS] {self.test_name}"
        elif self.status == TestResultStatus.FAILED:
            return f"[FAIL] {self.test_name}\n  Expected: {self.expected}\n  Got: {self.actual}"
        else:  # ERROR
            return f"[ERROR] {self.test_name}\n  Error: {self.error_msg}"


class TestRunner:
    """Runs test cases and reports results."""

    def __init__(self, solution_class, method_name: str):
        """
        Initialize test runner.

        Args:
            solution_class: The Solution class to test
            method_name: Name of the method to test
        """
        self.solution_class = solution_class
        self.method_name = method_name
        self.test_cases: List[TestCase] = []

    def add_test(self, name: str, inputs: Dict[str, Any], expected: Any,
                 comparator: Optional[Callable] = None):
        """
        Add a test case.

        Args:
            name: Descriptive name
            inputs: Dictionary of input parameters
            expected: Expected output
            comparator: Optional custom comparison function
        """
        self.test_cases.append(TestCase(name, inputs, expected, comparator))

    def run(self) -> bool:
        """
        Run all test cases.

        Returns:
            True if all tests passed, False otherwise
        """
        if not self.test_cases:
            print("No test cases defined.")
            return False

        results = []

        for test_case in self.test_cases:
            result = self._run_single_test(test_case)
            results.append(result)

        # Print results
        self._print_results(results)

        # Return overall status
        return all(r.status == TestResultStatus.PASSED for r in results)

    def _run_single_test(self, test_case: TestCase) -> TestResult:
        """Run a single test case and return result."""
        try:
            # Create solution instance
            solution = self.solution_class()
            method = getattr(solution, self.method_name)

            # Run the method with inputs
            actual = method(**test_case.inputs)

            # Compare result
            if test_case.comparator(actual, test_case.expected):
                return TestResult(test_case.name, TestResultStatus.PASSED)
            else:
                return TestResult(test_case.name, TestResultStatus.FAILED,
                                actual, test_case.expected)

        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            return TestResult(test_case.name, TestResultStatus.ERROR,
                            error_msg=error_msg)

    def _print_results(self, results: List[TestResult]):
        """Print formatted test results."""
        passed = sum(1 for r in results if r.status == TestResultStatus.PASSED)
        total = len(results)

        print(f"\n{'='*60}")
        print(f"Test Results: {passed}/{total} passed")
        print(f"{'='*60}\n")

        for result in results:
            print(result)

        print(f"\n{'='*60}")
        if passed == total:
            print("All tests passed!")
        else:
            print(f"{total - passed} test(s) failed.")
        print(f"{'='*60}\n")


class ClassTestRunner:
    """Test runner for class-based problems (e.g., MedianFinder)."""

    def __init__(self, solution_class):
        """
        Initialize class test runner.

        Args:
            solution_class: The class to test
        """
        self.solution_class = solution_class
        self.test_cases: List[Dict] = []

    def add_test(self, name: str, operations: List[str],
                 arguments: List[List[Any]], expected: List[Any]):
        """
        Add a test case for class-based problems.

        Args:
            name: Descriptive name
            operations: List of method names to call
            arguments: List of argument lists for each operation
            expected: List of expected outputs
        """
        self.test_cases.append({
            'name': name,
            'operations': operations,
            'arguments': arguments,
            'expected': expected
        })

    def run(self) -> bool:
        """Run all test cases."""
        if not self.test_cases:
            print("No test cases defined.")
            return False

        results = []

        for test_case in self.test_cases:
            result = self._run_single_test(test_case)
            results.append(result)

        # Print results
        self._print_results(results)

        return all(r.status == TestResultStatus.PASSED for r in results)

    def _run_single_test(self, test_case: Dict) -> TestResult:
        """Run a single test case for class-based problem."""
        try:
            obj = None
            actual_outputs = []

            for i, (op, args, expected_val) in enumerate(zip(
                test_case['operations'],
                test_case['arguments'],
                test_case['expected']
            )):
                if i == 0:
                    # Constructor call
                    obj = self.solution_class(*args)
                    actual_outputs.append(None)
                else:
                    # Method call
                    method = getattr(obj, op)
                    result = method(*args)
                    actual_outputs.append(result)

                    # Check individual result if not None
                    if expected_val is not None and result != expected_val:
                        return TestResult(
                            test_case['name'],
                            TestResultStatus.FAILED,
                            actual_outputs,
                            test_case['expected']
                        )

            return TestResult(test_case['name'], TestResultStatus.PASSED)

        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            return TestResult(test_case['name'], TestResultStatus.ERROR,
                            error_msg=error_msg)

    def _print_results(self, results: List[TestResult]):
        """Print formatted test results."""
        passed = sum(1 for r in results if r.status == TestResultStatus.PASSED)
        total = len(results)

        print(f"\n{'='*60}")
        print(f"Test Results: {passed}/{total} passed")
        print(f"{'='*60}\n")

        for result in results:
            print(result)

        print(f"\n{'='*60}")
        if passed == total:
            print("All tests passed!")
        else:
            print(f"{total - passed} test(s) failed.")
        print(f"{'='*60}\n")
