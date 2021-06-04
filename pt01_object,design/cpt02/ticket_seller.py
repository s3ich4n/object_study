#
# 판매원 객체에 대한 코드: 개선된 버전
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 02:43 created.
#


from audience import Audience

from ticket_office import TicketOffice


class TicketSeller:
    def __init__(
            self,
            ticket_office: TicketOffice,
    ):
        self._ticket_office = ticket_office

    #
    # 메소드 getter를 삭제하였음에 유의!
    # 다른 객체에서 TicketOffice에 대해 직접 접근할 수 없게 만듦
    # 이 객체의 세부사항을 숨김 -> 캡슐화
    #

    def sell_to(
            self,
            audience: Audience,
    ):
        """ 극장에 관객이 입장하는 경우를 처리하는 메소드.

        Theatre가 관리하는 것이 아니라, 판매원이 자율적으로 처리한다.

        Bag과 TicketOffice를 직접 관리한다

        :param audience:
        :return:
        """
        self._ticket_office.sell_ticket_to(audience)
