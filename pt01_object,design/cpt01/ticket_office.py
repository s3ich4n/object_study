#
# 매표소 객체에 대한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 02:27 created.
#


from typing import List

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

    def plus_amount(self, amount):
        self.amount += amount

    def minus_amount(self, amount):
        self.amount -= amount
