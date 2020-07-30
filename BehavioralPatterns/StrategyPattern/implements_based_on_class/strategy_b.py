from BehavioralPatterns.StrategyPattern.implements_based_on_class.strategy import Strategy


class StrategyB(Strategy):
    def do_algorithm(self, data):
        return sorted(data)
