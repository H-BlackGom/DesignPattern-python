from BehavioralPatterns.TemplateMethodPattern.implements.template_method import TemplateMethod


class ConcreteA(TemplateMethod):
    def operation_1(self):
        print("ConcreteA says: Implemented Operation1")

    def operation_2(self):
        print("ConcreteA says: Implemented Operation2")