#
# 소극장 객체에 대한 코드: 개선된 버전
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 02:46 created.
#

from audience import Audience

from ticket_seller import TicketSeller


class Theatre:
    """ 소극장에서 수행하는 관련 로직을 모아둔 클래스

    수정된 Theatre 객체에서는 ticket_office에 '직접' 접근하지 않는다!

    """
    def __init__(
            self,
            ticket_seller: TicketSeller,
    ):
        self._ticket_seller = ticket_seller

    def enter(
            self,
            audience: Audience,
    ):
        """ 극장에 손님이 입장하며, 판매원이 이를 처리한다.

        Theatre는 판매원이 일을 할 수 있는갑다 정도만 알고있다.

        :param audience:
        :return:
        """
        self._ticket_seller.sell_to(audience)
