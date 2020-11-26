import requests
import yaml

BASE = "http://127.0.0.1:5000/"

toys = [{
            "name": "boat",
            "status": "broken",
            "status_updated": 2018-3-19,
            "games": "dadawd"
    },
        {
            "name": "Teddy Bear",
            "status": "ok",
            "status_updated": 2018-3-30,
            "games": "dadadadaw"
    },
        {
            "name": "octopus",
            "status": "ok",
            "status_updated": 2018-3-19,
            "games": "dawdadawdawd"
        }
]


for i in range(len(toys)):
    response = requests.put(BASE + "toys/" + str(i), toys[i])
    print(response.json())


input()
response = requests.get(BASE + "toys/2")
print(response.json())
