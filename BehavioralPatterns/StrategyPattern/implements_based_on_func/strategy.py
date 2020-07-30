import types


class Strategy:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'

        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = Strategy()
    strat1 = Strategy(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = Strategy(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()
