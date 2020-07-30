from BehavioralPatterns.TemplateMethodPattern.implements.concrete_a import ConcreteA
from BehavioralPatterns.TemplateMethodPattern.implements.concrete_b import ConcreteB


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    obj = ConcreteA()
    obj.template()
    print("")

    print("Same client code can work with different subclasses:")
    obj = ConcreteB()
    obj.template()
