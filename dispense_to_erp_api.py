import requests
import json

url = "http://waterstarters.test.com:8000/api/method/waterstarters.susteq_data.receive_water_dispense_data"

data = [
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220523",
        "liters dispensed": "1149.7",
        "dispense count": "71",
        "sum paid": "6.79"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220524",
        "liters dispensed": "908.4",
        "dispense count": "60",
        "sum paid": "5.36"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220525",
        "liters dispensed": "1472.1",
        "dispense count": "99",
        "sum paid": "8.69"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220526",
        "liters dispensed": "1272.8",
        "dispense count": "78",
        "sum paid": "7.52"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220527",
        "liters dispensed": "1884.2",
        "dispense count": "111",
        "sum paid": "11.12"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220528",
        "liters dispensed": "1863.7",
        "dispense count": "122",
        "sum paid": "11"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220529",
        "liters dispensed": "2107.1",
        "dispense count": "126",
        "sum paid": "12.43"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220530",
        "liters dispensed": "2127.5",
        "dispense count": "127",
        "sum paid": "12.56"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220531",
        "liters dispensed": "2402.8",
        "dispense count": "146",
        "sum paid": "14.18"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220601",
        "liters dispensed": "2072.9",
        "dispense count": "132",
        "sum paid": "12.23"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220602",
        "liters dispensed": "2289",
        "dispense count": "149",
        "sum paid": "13.51"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220603",
        "liters dispensed": "1731.8",
        "dispense count": "107",
        "sum paid": "10.22"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220604",
        "liters dispensed": "1889.9",
        "dispense count": "120",
        "sum paid": "11.15"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220605",
        "liters dispensed": "2257.2",
        "dispense count": "151",
        "sum paid": "13.33"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220606",
        "liters dispensed": "2008.8",
        "dispense count": "121",
        "sum paid": "11.85"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220607",
        "liters dispensed": "1614.4",
        "dispense count": "97",
        "sum paid": "9.54"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220608",
        "liters dispensed": "2018.8",
        "dispense count": "123",
        "sum paid": "11.92"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220609",
        "liters dispensed": "2655.9",
        "dispense count": "157",
        "sum paid": "15.68"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220610",
        "liters dispensed": "1418.7",
        "dispense count": "88",
        "sum paid": "8.39"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220611",
        "liters dispensed": "507.9",
        "dispense count": "35",
        "sum paid": "3"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220612",
        "liters dispensed": "1288.9",
        "dispense count": "83",
        "sum paid": "7.61"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220613",
        "liters dispensed": "1438.5",
        "dispense count": "91",
        "sum paid": "8.49"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 1",
        "hub ID": "99001",
        "hub name": "Waterkiosk 1 (99001)",
        "day": "20220614",
        "liters dispensed": "654.7",
        "dispense count": "42",
        "sum paid": "3.87"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220523",
        "liters dispensed": "175.1",
        "dispense count": "24",
        "sum paid": "0.88"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220524",
        "liters dispensed": "149.1",
        "dispense count": "9",
        "sum paid": "0.75"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220525",
        "liters dispensed": "132.6",
        "dispense count": "9",
        "sum paid": "0.66"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220526",
        "liters dispensed": "606.4",
        "dispense count": "56",
        "sum paid": "3.03"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220527",
        "liters dispensed": "26.1",
        "dispense count": "5",
        "sum paid": "0.13"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220528",
        "liters dispensed": "451.5",
        "dispense count": "31",
        "sum paid": "2.27"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220529",
        "liters dispensed": "166.6",
        "dispense count": "14",
        "sum paid": "0.83"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220530",
        "liters dispensed": "340.1",
        "dispense count": "23",
        "sum paid": "1.7"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220531",
        "liters dispensed": "195.9",
        "dispense count": "26",
        "sum paid": "0.98"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220601",
        "liters dispensed": "251.3",
        "dispense count": "15",
        "sum paid": "1.26"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220602",
        "liters dispensed": "216",
        "dispense count": "20",
        "sum paid": "1.08"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220603",
        "liters dispensed": "226.2",
        "dispense count": "14",
        "sum paid": "1.13"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220604",
        "liters dispensed": "767.2",
        "dispense count": "44",
        "sum paid": "3.83"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220605",
        "liters dispensed": "192.9",
        "dispense count": "39",
        "sum paid": "0.97"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220606",
        "liters dispensed": "0",
        "dispense count": "3",
        "sum paid": "0"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220608",
        "liters dispensed": "0",
        "dispense count": "3",
        "sum paid": "0"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220610",
        "liters dispensed": "0",
        "dispense count": "5",
        "sum paid": "0"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220612",
        "liters dispensed": "0",
        "dispense count": "2",
        "sum paid": "0"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220613",
        "liters dispensed": "0",
        "dispense count": "3",
        "sum paid": "0"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220614",
        "liters dispensed": "0",
        "dispense count": "1",
        "sum paid": "0"
    },
    {
        "service provider": "Water provider",
        "project": "Water provider",
        "community": "village community 2",
        "hub ID": "99002",
        "hub name": "Waterkiosk 2 (99002)",
        "day": "20220616",
        "liters dispensed": "0",
        "dispense count": "1",
        "sum paid": "0"
    }
]

request = requests.post(url, data=json.dumps(data), headers={
                        "Authorization": "Token 7c573638c75b0fc:b3a0fb9d6c26484"})
