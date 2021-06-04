#
# 관람객 객체에 관한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 01:12 created.
#


from typing import Optional

from bag import Bag


class Audience:
    """ 관람객을 의미하는 객체

    관람객은 가방을 소지하고 있다.

    """
    def __init__(self, bag: Bag):
        self._bag: Optional[Bag] = bag

    @property
    def bag(self):
        return self._bag
