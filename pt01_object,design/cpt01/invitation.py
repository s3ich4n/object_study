#
# 초대장 객체에 대한 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/03 23:54 created.
#


from typing import Optional

import datetime


class Invitation:
    """ 초대장을 구현한 객체

    """
    def __init__(
            self,
            when: Optional[datetime.datetime] = None
    ):
        self._when = when
