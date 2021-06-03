#
# 소극장 객체에 대한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 02:46 created.
#


from audience import Audience
from bag import Bag
from ticket import Ticket
from ticket_seller import TicketSeller
from ticket_office import TicketOffice


class Theatre:
    """ 소극장에서 수행하는 관련 로직을 모아둔 클래스

    """
    def __init__(
            self,
            ticket_seller: TicketSeller,
    ):
        self._ticket_seller = ticket_seller

    @property
    def ticket_seller(self):
        return self._ticket_seller

    def enter(
            self,
            audience: Audience,
    ):
        """ 극장에 관객이 입장하는 경우를 처리하는 메소드.

        1. 관람객의 가방 안에 초대장이 들어있는지 확인한다.
            1. 초대장이 들어있다면 티켓으로 교환하여 가방에 넣어준다.
            2. 초대장이 없다면 아래 과정을 거친다
                1. 관람객의 가방에서 돈을 꺼내고
                2. 매표소의 금액을 증가시킨다
                3. 관람객의 가방안에 티켓을 넣어준다.

        :param audience:
        :return:
        """
        if audience.bag.invitation is not None:
            ticket = self.ticket_seller.ticket_office.ticket
            audience.bag.ticket = ticket
        else:
            ticket = self._ticket_seller.ticket_office.ticket
            audience.bag.minus_amount(ticket.fee)
            self.ticket_seller.ticket_office.plus_amount(ticket.fee)
            audience.bag.ticket = ticket


if __name__ == '__main__':
    new_audience = Audience(Bag(10000))

    theatre = Theatre(
        TicketSeller(
            TicketOffice(
                100000,
                [Ticket(1000), Ticket(1000)]
            )
        )
    )

    print("판매 전 상황")
    print(f"극장의 경우: {theatre.ticket_seller.ticket_office.__dict__}")
    print(f"관객의 경우: {new_audience.bag.__dict__}")

    print("")
    theatre.enter(new_audience)

    print("판매 후 상황")
    print(f"극장의 경우: {theatre.ticket_seller.ticket_office.__dict__}")
    print(f"관객의 경우: {new_audience.bag.__dict__}")
