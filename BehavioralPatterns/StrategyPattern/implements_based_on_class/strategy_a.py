from BehavioralPatterns.StrategyPattern.implements_based_on_class.strategy import Strategy


class StrategyA(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))