"""
Unit tests for MDSynthesis

"""

import unittest
import test_Core_Files


def suite():
    """Gather every test from package into a test suite.

    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_Core_Files.suite())

    return test_suite


if __name__ == '__main__':
    #so we can run tests from this package individually
    test_runner = unittest.TextTestRunner()
    test_suite = suite()
    test_runner.run(test_suite)
