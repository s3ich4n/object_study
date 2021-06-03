#
# 판매원 객체에 대한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 02:43 created.
#


from ticket_office import TicketOffice


class TicketSeller:
    def __init__(
            self,
            ticket_office: TicketOffice,
    ):
        self._ticket_office = ticket_office

    @property
    def ticket_office(self):
        return self._ticket_office
