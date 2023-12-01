import requests
import json
import settings

def SendNormalMessage(webhook_url, content, user):
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "embeds": [{
            "author": {
            "name": f"{user}",
            },
            "description": content,
            "color": 333333,
            "footer": {
                "text": settings.GetFullTime()
            },
        }]
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 204:
        #print("Message sent successfully.")
        pass
    else:
        #print(f"Failed to send message. Status code: {response.status_code}")
        pass
