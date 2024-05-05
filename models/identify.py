import httpx
import json
from cliqet_api.models.base import BaseModel

class Identify(BaseModel):
    def ocr_extract(self,
                    image_link: str,
                    webhook_name: str,
                    source_id: str,
                    name_compare_data: dict | None = None):
        """
            Extracts information from an ID card. See well-supported ID types at 
            https://app.cliqet.com/docs/identify/supported-ids.
            @param image_link - The link to download the image of the ID
            @param webhook_name - The name of the webhook that will receive the results 
                of the api call
            @param source_id - The unique identifier for the specific api call
            @param name_compare_data - An optional dictionary to use if you want 
                name comparison. Please refer to https://app.cliqet.com/docs/identify/api-ocr-extract 
                for format.
        """
        data = json.dumps({
            'service': 'identify-ocr-extract',
            'payload': {
                'image_link': image_link,
                'webhook_name': webhook_name,
                'source_id': source_id,
                'name_compare_data': name_compare_data
            }
        })

        response = httpx.post(self.identify_url, headers=self.headers, data=data)
        return response.json()

    def face_compare(self,
                     image_source_link: str,
                     image_target_link: str,
                     webhook_name: str,
                     source_id: str):
        """
            Compare face from ID image to a selfie image.
            @param image_source_link - The link to download the image as point of comparison
            @param image_target_link - The link to download the image to compare with image_source_link
            @param webhook_name - The name of the webhook that will receive the results 
                of the api call
            @param source_id - The unique identifier for the specific api call
        """
        data = json.dumps({
            'service': 'identify-face-compare',
            'payload': {
                'image_source_link': image_source_link,
                'image_target_link': image_target_link,
                'webhook_name': webhook_name,
                'source_id': source_id
            }
        })

        response = httpx.post(self.identify_url, headers=self.headers, data=data)
        return response.json()

    def anti_spoof(self,
                   image_link: str,
                   webhook_name: str,
                   source_id: str):
        """
            Checks whether a selfie image has been spoofed or taken live.
            @param image_source_link - The link to download the image
            @param webhook_name - The name of the webhook that will receive the results 
                of the api call
            @param source_id - The unique identifier for the specific api call
        """
        data = json.dumps({
            'service': 'identify-anti-spoof',
            'payload': {
                'image_link': image_link,
                'webhook_name': webhook_name,
                'source_id': source_id
            }
        })

        response = httpx.post(self.identify_url, headers=self.headers, data=data)
        return response.json()