import hashlib
import hmac
import base64
from cliqet_api.models.locate import Locate
from cliqet_api.models.notify import Notify
from cliqet_api.models.identify import Identify


class CliqetApi:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.identify = Identify(api_key)
        self.notify = Notify(api_key)
        self.locate = Locate(api_key)

    def verify_signature(self,
                         request_body: str, 
                         hmac_header: str) -> bool:
        """
            Verify payload from webhook received for Cliqet api calls
            @param request_body - The raw request body received from webhook
            @param hmac_header - The signature received from webhook under the header 
                cliqet-signature
        """
        data_bytes = request_body.encode('utf-8')
        digest = hmac.new(self.api_key.encode('utf-8'), data_bytes, digestmod=hashlib.sha256).digest()
        computed_hmac = base64.b64encode(digest).decode('utf-8')
        return hmac.compare_digest(computed_hmac.encode('utf-8'), hmac_header.encode('utf-8'))
        