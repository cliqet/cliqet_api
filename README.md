# Cliqet API Python Module

This python module can be used to interact with Cliqet API services which can be found here.

```bash
https://app.cliqet.com/
```

### Dependencies
- httpx

### About Cliqet API Services

Cliqet offers a wide range of APIs that cater to the specific needs of startups, empowering them to leverage advanced functionalities without the burden of high upfront costs.

### Services include:
- Identify Services - Allows you to automate your process of verifying your users.
```bash
https://app.cliqet.com/docs/identify/overview
```
-- Face Compare - The API service for comparing an image in an ID to a selfie image offers a secure and convenient solution for identity verification.
-- OCR Extract with Name Comparison - The text extraction service from an ID, combined with optional name comparison, simplifies the onboarding process by automatically capturing personal details from the ID document.
-- Anti-Spoof - The liveness detection service for selfie images provides a robust solution for verifying the authenticity and liveliness of a user's identity.

- Notify Services - Allows you to send notifications to your users.
```bash
https://app.cliqet.com/docs/notify/overview
```
-- Notify Mobile - The API service provides a seamless solution to send mobile notifications to your customers. 

- Locate Services - Allow you to get location data, geocode and suggest places based on search.
```bash
https://app.cliqet.com/docs/locate/overview
```
-- Locate Device - The API service is a powerful and reliable service that offers precise location data.
-- Locate Suggestions - The API service is a powerful tool that provides users with intelligent place recommendations based on their search queries.
-- Locate Geocode - The API service is a versatile service that enables users to convert addresses or place names into geographic coordinates.
-- Locate Calculate Routes - The API service is a robust solution that enables calculation of optimal routes based on distance and time metrics.

### Sample Usage
```python
from cliqet_api.models.api import CliqetApi

# Instantiate a CliqetApi instance
cliqet_api = CliqetApi('<YOUR API KEY>')

# Get text location of a device
device_location = cliqet_api.locate.locate_device(106.72691, 10.7211255)

# Verify webhook from Cliqet
is_valid = cliqet_api.verify_signature(raw_request_body, cliqet_signature_header)
```