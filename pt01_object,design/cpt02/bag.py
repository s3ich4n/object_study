#
# 가방 객체에 대한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/03 23:56 created.
#


from typing import Optional

from invitation import Invitation
from ticket import Ticket


class Bag:
    """ 관람객의 소지품을 보관할 가방.

    초대장, 티켓, 현금을 들고있다.

    """

    # amount에 대해 강제성이 있다
    # invitation, ticket은 강제성이 없다
    def __init__(
        self,
        amount: int,
        invitation: Optional[Invitation] = None,
        ticket: Optional[Ticket] = None,
    ):
        self.amount = amount
        self.invitation = invitation
        self.ticket = ticket

    def __getattr__(self, item):
        try:
            value = super().__getattribute__(item)
            return value
        except AttributeError:
            print(f"No attribute named {item}")

    def __setattr__(self, key, value):
        try:
            super().__setattr__(key, value)
        except AttributeError:
            print(
                f"Cannot see key and value... "
                f"key: {key}, value: {value}"
            )

    def hold(
            self,
            ticket: Ticket,
    ):
        """

        "가방" 이 무엇을 한다. 하는 관점에서 보자.
        객체지향적 패러다임에서는 모든 객체는 무엇이든 할 수 있다.

        사물을 객체화 하면, 사물이 '기능' 하는 것을 행위로 풀어쓴다고 생각하라.

        예를들어, 가방에 '담는다' 라는 것도 코드로 풀어야 된다 정도로...

        :param ticket:
        :return:
        """
        if self.invitation:
            self.ticket = ticket
        else:
            self.ticket = ticket
            self.minus_amount(ticket.fee)
            return ticket.fee

    def plus_amount(self, amount):
        self.amount += amount

    def minus_amount(self, amount):
        self.amount -= amount
