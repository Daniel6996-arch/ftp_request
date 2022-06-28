import requests
import json

url = "http://waterstarters.test.com:8000/api/method/waterstarters.susteq_data.receive_token_credits_data"

data = [
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220523",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220525",
        "credits sold": "5",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220526",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220527",
        "credits sold": "15",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220528",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220529",
        "credits sold": "10",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220530",
        "credits sold": "15",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220531",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220601",
        "credits sold": "15",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220602",
        "credits sold": "20",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220603",
        "credits sold": "5",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220604",
        "credits sold": "10",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220605",
        "credits sold": "15",
        "transactions count": "3"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220606",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220607",
        "credits sold": "10",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220608",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220609",
        "credits sold": "20",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220610",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220612",
        "credits sold": "5",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220613",
        "credits sold": "10",
        "transactions count": "1"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220614",
        "credits sold": "6",
        "transactions count": "2"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220530",
        "credits sold": "85",
        "transactions count": "13"
    }
]

request = requests.post(url, data=json.dumps(data), headers={
                        "Authorization": "Token 7c573638c75b0fc:b3a0fb9d6c26484"})
