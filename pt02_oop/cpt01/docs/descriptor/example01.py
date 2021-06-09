#
# 데코레이터를 쓴 예시
#


# class Foo():
#     @property
#     def attribute1(self) -> object:
#         print("accessing the attribute to get the value")
#         return 42
#
#     @attribute1.setter
#     def attribute1(self, value) -> None:
#         print("accessing the attribute to set the value")
#         raise AttributeError("Cannot change the value")
#
#
# my_foo_object = Foo()
# x = my_foo_object.attribute1
# print(x)


# class Foo():
#     def getter(self) -> object:
#         print("accessing the attribute to get the value")
#         return 42
#
#     def setter(self, value) -> None:
#         print("accessing the attribute to set the value")
#         raise AttributeError("Cannot change the value")
#
#     # property() returns a property object
#     # that implements the descriptor protocol.
#     attribute1 = property(getter, setter)
#
#
# my_foo_object = Foo()
# x = my_foo_object.attribute1
# print(x)

# lazy_properties.py
# import time
#
# class LazyProperty:
#     def __init__(self, function):
#         self.function = function
#         self.name = function.__name__
#
#     def __get__(self, obj, type=None) -> object:
#         obj.__dict__[self.name] = self.function(obj)
#         return obj.__dict__[self.name]
#
# class DeepThought:
#     @LazyProperty
#     def meaning_of_life(self):
#         time.sleep(3)
#         return 42
#
# my_deep_thought_instance = DeepThought()
# print(my_deep_thought_instance.meaning_of_life)
# print(my_deep_thought_instance.meaning_of_life)
# print(my_deep_thought_instance.meaning_of_life)


# # wrong_lazy_properties.py
# import time
#
# class LazyProperty:
#     def __init__(self, function):
#         self.function = function
#         self.name = function.__name__
#
#     def __get__(self, obj, type=None) -> object:
#         obj.__dict__[self.name] = self.function(obj)
#         return obj.__dict__[self.name]
#
#     def __set__(self, obj, value):
#         pass
#
# class DeepThought:
#     @LazyProperty
#     def meaning_of_life(self):
#         time.sleep(3)
#         return 42
#
# my_deep_thought_instance = DeepThought()
# print(my_deep_thought_instance.meaning_of_life)
# print(my_deep_thought_instance.meaning_of_life)
# print(my_deep_thought_instance.meaning_of_life)


# properties2.py
class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()


my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)
