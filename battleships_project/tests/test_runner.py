import traceback
import sys

__DEFAULT_EQ_FN = lambda x,y: x == y

def assert_eq(expected, actual, eq_fn=__DEFAULT_EQ_FN):
    assert eq_fn(expected, actual), "Assertion failed [expected] %s [actual] %s" % (str(expected), str(actual))

class TestStatus:

    PASSED = 1
    FAILED = 2
    EXCEPTION = 3

class Tester:

    def __init__(self, before_each=lambda: None):
        self.__before_each = before_each
        self.__tests = dict()

    def __run_test(self, test_name):
        test_fn = self.__tests[test_name]['fn']
        self.__before_each()
        try:
            test_fn()
            return TestStatus.PASSED, None
        except AssertionError as ae:
            return TestStatus.FAILED, str(ae)
        except Exception as e:
            return TestStatus.EXCEPTION, e.__traceback__

    def create_test(self, test_fn, msg=""):
        if test_fn.__name__ in self.__tests:
            raise KeyError("%s already a test", (test_fn.__name__))
        self.__tests[test_fn.__name__] = {
            'fn' : test_fn,
            'msg' : msg,
            'enabled' : True
        }

    def disable_test(self, test_fn):
        if test_fn.__name__ in self.__tests:
            self.__tests[test_fn.__name__]['enabled'] = False

    def run_all_tests(self, show_all=False):
        num_passed = 0
        for name in self.__tests:
            if not self.__tests[name]['enabled']:
                continue

            self.__before_each()
            try:
                self.__tests[name]['fn']()
                num_passed += 1
                if show_all:
                    print("\n TEST [%s] PASSED" % (name))
            except AssertionError as ae:
                print("\nTEST [%s] FAILED [%s] %s" % (name, str(ae), self.__tests[name]['msg']), file=sys.stderr)
            except Exception as e:
                print("\nTEST [%s] RAISED EXCEPTION [%s]\nTRACEBACK: " % (name, self.__tests[name]['msg']), file=sys.stderr)
                traceback.print_exc()

        print("\n--- SUMMARY ---\n%d/%d tests passed." % (num_passed, len(self.__tests)),file=sys.stderr)

            

    
        