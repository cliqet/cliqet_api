class BaseModel:
    def __init__(self, api_key: str):
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': api_key
        }
        self.locate_url = 'https://api.cliqet.com/locate'
        self.notify_url = 'https://api.cliqet.com/notify'
        self.identify_url = 'https://api.cliqet.com/identify'