#
# 티켓 객체에 대한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/03 23:55 created.
#


from typing import Optional


class Ticket:
    """ 공연을 관람하려는 사람이 소지해야하는 티켓에 대한 객체

    """
    def __init__(
            self,
            fee: Optional[int] = None
    ):
        self._fee = fee

    @property
    def fee(self):
        return self._fee
