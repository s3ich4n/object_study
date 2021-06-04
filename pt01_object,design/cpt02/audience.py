#
# 관람객 객체에 관한 코드: 개선된 버전
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 01:12 created.
#


from typing import Optional

from bag import Bag
from ticket import Ticket


class Audience:
    """ 관람객을 의미하는 객체

    관람객은 가방을 소지하고 있다.

    """
    def __init__(self, bag: Bag):
        self._bag: Optional[Bag] = bag

    @property
    def bag(self):
        return self._bag

    def buy(
            self,
            ticket: Ticket,
    ):
        """ 관람객이 가방에서 초대장, 돈을 가지고 표를 구매한다

        이 때, Audience 객체가 스스로 '가방' 을 처리함에 유의힌다.

        :param ticket:
        :return:
        """
        return self.bag.hold(ticket)
