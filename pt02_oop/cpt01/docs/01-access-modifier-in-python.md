# 파이썬에서의 접근 수정자

## 파이썬 애트리뷰트의 가시성

+ 객체지향 프로그래밍을 지원하는 프로그래밍 언어는 보통 아래 접근 수정자는 쓴다
  + `public`, `protected`, `private`
+ 파이썬에서는 아래 문법과 같다
  + 심지어 키워드도 아님

```python
class ObjTest:
    def __init__(self):
        self.public = 5
        self._protected = 10
        self.__private = 15

    def get_private_field(self):
        return self.__private

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private
```

+ 클래스 내부의 메소드에서는 접근할 수 있고 클래스 외부에서는 접근할 수 없다

```python
a = ObjTest()

assert a.get_private_field() == 15
assert a.__private == 15

>>>
Traceback ...
AttributeError: 'ObjTest' object has no attribute '__private'
```

+ 클래스 메소드는 `class` 블록 안에 있어서 접근할 수 있다

```python

b = ObjTest()

assert ObjTest.get_private_field_of_instance(b) == 15
```

+ 하위 클래스는 부모클래스의 비공개 필드에 접근할 수 없다

```python
class ParentObj:
    def __init__(self):
        self.__private = 15

class ChildObj(ParentObj):
    def get_private_object(self):
        return self.__private

c = ChildObj()
assert c.get_private_object() == 15

>>>
Traceback ...
AttributeError: 'ChildObj' object has no attribute '_ChildObj__private'
```

+ `private` 으로 쓰는 값은 사실 컴파일러 단에서 이름을 변경하기 때문에 그런 것이다
+ `c` 변수 내의 값을보면 다음 방식으로 이름이 바뀌어 담겨있음을 알 수 있다
  + `c._<부모클래스명>__<private값>`

```python
c.__dict__
>>> {'_ParentObj__private': 15}
c._ParentObj__private
>>> 15
```

+ 접근제한자가 사실 엄격하게 제한하지는 않는다.
+ 이러는 이유는 쓰는 사람이 제대로 쓸 것이라고 믿기 때문이다.
  + [After all, we're all consenting adults here.](https://mail.python.org/pipermail/tutor/2003-October/025932.html)
+ 그리고, 파이썬은 애트리뷰트 접근에 대해 `__getattr__`, `__setattr__` 을 쓸 수 있다
  + 저걸 쓰면 객체 내부의 값을 `a.foobar` 이런식으로 바로 접근할 수 있게 된다
+ 차라리, `protected` 형식을 쓰고, 객체에 쓰면 immutable 하게 쓰도록 docstring 을 풍부하게 쓰자
  + 어떤 필드는 하위 클래스에서 변경해도 되고, 어떤 필든 안되는지...
+ 이름 충돌이 날 까봐 걱정될 때만 `private` 형식을 쓰도록 하자
  + 상위 클래스의 변수 이름과 하위 클래스의 변수 이름이 같을지도 모를 때..
