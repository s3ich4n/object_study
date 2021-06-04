#
# 구동 테스트
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/06/04 18:09 created.
#

import datetime

from audience import Audience
from bag import Bag
from invitation import Invitation
from theatre import Theatre
from ticket import Ticket
from ticket_seller import TicketSeller
from ticket_office import TicketOffice


new_audience = Audience(
    Bag(10000)
)

two_days_b4 = datetime.datetime.now() - datetime.timedelta(days=2)

new_audience_with_invitation = Audience(
    Bag(10000, Invitation(two_days_b4)),
)

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
print(f"관객의 경우 (초대장 x): {new_audience.bag.__dict__}")
print(f"관객의 경우 (초대장 O): {new_audience_with_invitation.bag.__dict__}")


print("")
theatre.enter(new_audience)

print("판매 후 상황")
print(f"극장의 경우: {theatre.ticket_seller.ticket_office.__dict__}")
print(f"관객의 경우 (초대장 x): {new_audience.bag.__dict__}")
print(f"관객의 경우 (초대장 O): {new_audience_with_invitation.bag.__dict__}")


print("")
theatre.enter(new_audience_with_invitation)

print("판매 후 상황")
print(f"극장의 경우: {theatre.ticket_seller.ticket_office.__dict__}")
print(f"관객의 경우 (초대장 x): {new_audience.bag.__dict__}")
print(f"관객의 경우 (초대장 O): {new_audience_with_invitation.bag.__dict__}")
