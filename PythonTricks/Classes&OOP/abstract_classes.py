from abc import ABCMeta, abstractclassmethod


class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()


class Concrete(Base):
    def foo(self):
        return 'foo() called'

    # def bar(self):
    #    return "bar() called"


b = Base()
# b.foo()
c = Concrete()
print(c.foo())
print(c.bar())


class Base(metaclass=ABCMeta):
    @abstractclassmethod
    def foo(self):
        pass

    @abstractclassmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass


assert issubclass(Concrete, Base)
