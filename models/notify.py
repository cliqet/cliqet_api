import httpx
import json
from cliqet_api.models.base import BaseModel

class Notify(BaseModel):
    def notify_mobile(self,
                      subscriber_id: str,
                      message: str,
                      webhook_name: str,
                      source_id: str) -> dict:
        """
            Sends a mobile notification to a subscriber.
            @param subscriber_id - The subscriber ID of the user
            @param message - The message to be sent to the subscriber
            @param webhook_name - The name of the webhook that will receive the results 
                of the api call
            @param source_id - The unique identifier for the specific api call
        """
        data = json.dumps({
            'service': 'notify-mobile',
            'payload': {
                'subscriber_id': subscriber_id,
                'message': message,
                'webhook_name': webhook_name,
                'source_id': source_id
            }
        })

        response = httpx.post(self.notify_url, headers=self.headers, data=data)
        return response.json()