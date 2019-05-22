import os, sys

curr_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.join(curr_path, "..")
if root_path not in sys.path:
    sys.path.insert(0, root_path)

import unittest
import inspect


class_test_count = {} # count the number of test already taken by a TestCase class

class TestBase(unittest.TestCase):

    def log(self):
        stack = inspect.stack()
        class_name = self.__class__.__name__
        func_name = stack[1][3]
        if class_name not in class_test_count:
            class_test_count[class_name] = 1
        else:
            class_test_count[class_name] += 1
        print ("{} - {}: {}".format(class_name,
                                    class_test_count[class_name],
                                    func_name))
