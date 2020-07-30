from BehavioralPatterns.StrategyPattern.implements_based_on_class.context import Context
from BehavioralPatterns.StrategyPattern.implements_based_on_class.strategy_a import StrategyA
from BehavioralPatterns.StrategyPattern.implements_based_on_class.strategy_b import StrategyB


if __name__ == '__main__':
    context = Context(StrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = StrategyB()
    context.do_some_business_logic()
