from Algorithms.UnitTestOrchestrator import TestRunner

import argparse
import pathlib
import os

"""
Argument parser
"""

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--all", help="test all components", action="store_true")

parser.add_argument(
    "-p",
    "--pedantic",
    help="allow for output of tests to be pedantic",
    action="store_true",
)
parser.add_argument(
    "-t", "--test", help="test certain components, comma separated", type=str
)

parser.add_argument(
    "-s",
    "--sub-component",
    help="test certain sub-component, given the direct path",
    type=str,
)
arguments = parser.parse_args()

R = TestRunner(parent_dir=pathlib.Path("UnitTests/"), pedantic=True)

pedantic = arguments.pedantic

if test := arguments.test:
    for valid_test in test.split(","):
        R.test_certain_class(valid_test)

if arguments.all:
    R.run_all_tests()

if arguments.sub_component:
    path = pathlib.Path(arguments.sub_component)
    if path.is_file():
        result = R.conduct_test(path)
        R.print_resultant_message(result)
    else:
        print(f"[ERROR] Could not load test at pah {path}, no such file")
