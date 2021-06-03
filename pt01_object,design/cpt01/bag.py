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

    def plus_amount(self, amount):
        self.amount += amount

    def minus_amount(self, amount):
        self.amount -= amount


if __name__ == "__main__":
    a = Bag(10000)
    a.invitation = Invitation()
    a.ticket = Ticket()

    print(a.__dict__)
    print(a.invitation is not None)
    print(a.ticket is not None)

    # TODO
    #   이걸 막으려면?
    # a.asdf = 1234

    b = Bag(10000, Invitation(), Ticket())

    print(b.__dict__)
    print(b.invitation is not None)
    print(b.ticket is not None)
