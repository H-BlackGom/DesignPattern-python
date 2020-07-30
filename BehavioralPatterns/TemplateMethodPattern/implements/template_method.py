from abc import ABC, abstractmethod


class TemplateMethod(ABC):
    def template(self):
        print("AbstractClass says: I am doing the bulk of the work")
        self.operation_1()
        print("AbstractClass says: But I let subclasses override some operations")
        self.operation_2()
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def operation_1(self):
        pass

    @abstractmethod
    def operation_2(self):
        pass