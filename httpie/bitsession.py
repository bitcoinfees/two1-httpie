"""The 21 BC functionality."""
import requests.sessions

from two1.lib.bitrequests import BitTransferRequests
from two1.commands.config import Config
from two1.lib.wallet import Wallet

wallet = Wallet()
username = Config().username
bt_requests = BitTransferRequests(wallet, username)


class BitTransferSession(requests.sessions.Session):
    """A requests Session with BitTransfer functionality.

    This substitutes for requests.sessions.Session in httpie.

    We want to use BitTransferRequests.request, but that in turn uses
    requests.request, which uses the default Session, with no way to specify
    a custom one.

    The solution for now is to monkey patch requests.request to
    this Session's bound request function.

    Ideally, BitRequests should subclass requests.sessions.Session.
    """

    def __init__(self):
        # See httpie.cli for the default value.
        # This variable is set in httpie.client.get_response.
        self.max_price = None
        super(BitTransferSession, self).__init__()

    def request(self, method, url, **kwargs):
        """Wraps the superclass method."""
        # Force BitTransferRequests to use this Session.
        requests.request = super(BitTransferSession, self).request

        return bt_requests.request(method, url, max_price=self.max_price,
                                   **kwargs)
