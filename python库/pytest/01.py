class Result:
    test_timeout = None


def pytest_addoption(parser):
    parser.addoption("--test_timeout", action="store", default=30, help="open or save timeout")


def get_value(pytestconfig):
    value = pytestconfig.getoption("--test_timeout")
    print(value)

class Person:

    h = 175

    @classmethod
    def init(cls, age):
        cls.age = age

    def __init__(self, name):
        self.name = name

    def hello(self):
        self.kk = 584

if __name__ == '__main__':
    # Person.h
    # Person.init(26)
    # Person.kk
    p = Person("fff")
    p.h
    p.name
    p.age
    p.kk