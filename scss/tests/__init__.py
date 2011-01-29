import unittest


def all_tests_suite():
    return unittest.TestLoader().loadTestsFromNames([
        'scss.tests.test_for',
        'scss.tests.test_variables',
        'scss.tests.test_nesting',
        'scss.tests.test_files',
        'scss.tests.test_scss',
    ])


def main():
    runner = unittest.TextTestRunner()
    suite = all_tests_suite()
    runner.run(suite)


if __name__ == '__main__':
    import os.path
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()