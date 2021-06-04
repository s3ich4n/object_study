#
# 매표소 객체에 대한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 02:27 created.
#


from typing import List

from audience import Audience
from ticket import Ticket


class TicketOffice:
    """ 매표소에 대한 객체

    판매한 총 금액과 티켓에 대한 객체를 가지고 있다.
    """
    def __init__(
            self,
            amount: int,
            tickets: List[Ticket],
    ):
        self.amount = amount
        self.tickets = tickets

    @property
    def ticket(self):
        return self.tickets.pop()

    def _plus_amount(self, amount):
        self.amount += amount

    def minus_amount(self, amount):
        self.amount -= amount

    def sell_ticket_to(
            self,
            audience: Audience,
    ):
        """ 매표소는 Audience 에게 표를 '판매' 한다.

        기존 판매원은 아래의 두가지 매표소 행동을 침해했다
            + 매표소의 티켓을 자기멋대로 꺼내서 팔음
            + Audience 에게 받은 금액을 매표소에 자기멋대로 넣음

        따라서, 관련 작업을 위임했다.

        :return:
        """
        self._plus_amount(audience.buy(self.ticket))
