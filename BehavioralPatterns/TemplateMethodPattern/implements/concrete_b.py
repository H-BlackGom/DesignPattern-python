from BehavioralPatterns.TemplateMethodPattern.implements.template_method import TemplateMethod


class ConcreteB(TemplateMethod):
    def operation_1(self):
        print("ConcreteB says: Implemented Operation1")

    def operation_2(self):
        print("ConcreteB says: Implemented Operation2")
