#!/usr/bin/python3
import yaml
import sys
import json

OUT=open('output.yaml','w')
IN=open(sys.argv[1], 'r')

JSON = json.load(IN)
IN.close()
yaml.dump(JSON, OUT)
OUT.close()

# toys = {1: {
#             "name": "boat",
#             "status": "broken",
#             "status_updated": 2018-3-19,
#             "games": [
#                 {
#                     "id": 1,
#                     "note": "need repair"
#                 },
#                 {
#                     "id": 14,
#                     "note": "boat is broken"
#                 }
#             ]
#     },
#         7: {
#             "name": "Teddy Bear",
#             "status": "ok",
#             "status_updated": 2018-3-30,
#             "games": [
#                 {
#                     "id": 5,
#                     "note": "baer feel well"
#                 }
#             ]
#     },
#         43: {
#             "name": "octopus",
#             "status": "ok",
#             "status_updated": 2018-3-19,
#             "games": [
#                 {
#                     "id": 5,
#                     "note": "felt rather good though had no water to swim"
#                 },
#                 {
#                     "id": 14,
#                     "note": "two tentacles are lost"
#                 },
#             ]
#     }
# }