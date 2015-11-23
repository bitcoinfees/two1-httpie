"""The 21 BC functionality."""
import requests.sessions

import two1.lib.bitrequests
from two1.lib.bitrequests import BitTransferRequests
from two1.commands.config import Config
from two1.lib.wallet import Wallet

# Max price per request, hard-coded for now.
MAX_PRICE = 10000

wallet = Wallet()
username = Config().username
bt_requests = BitTransferRequests(wallet, username)


class BitTransferSession(requests.sessions.Session):
    """A requests Session with BitTransfer functionality.

    This substitutes for requests.sessions.Session in httpie.

    It makes use of BitTransferRequests.request, but only after monkey patching
    two1.lib.bitrequests.requests to refer to this session.

    Ideally BitRequests should subclass the requests.sessions.Session.
    """

    def request(self, **kwargs):
        """Wraps the superclass method."""
        # Force BitTransferRequests to use this Session.
        two1.lib.bitrequests.requests = self

        kwargs.update(max_price=MAX_PRICE)
        return bt_requests.request(**kwargs)
