import unittest
from Home.HomeTest import HomeTest
from Login.RegisterTest import RegisterTest
from Login.Login import LoginTest


def runTests(testClasses):
    loader = unittest.TestLoader()
    suitesList = []
    for testClass in testClasses:
        suite = loader.loadTestsFromTestCase(testClass)
        suitesList.append(suite)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(unittest.TestSuite(suitesList))


def main():
    runTests([RegisterTest])
    runTests([LoginTest])
    runTests([HomeTest])


if __name__ == '__main__':
    main()
