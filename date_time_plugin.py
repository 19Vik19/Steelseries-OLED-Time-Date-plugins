from time import sleep
import requests
import time
import json

class DateTimePlugin():
    corePropsPath = "c:/ProgramData/SteelSeries/SteelSeries Engine 3/coreProps.json"
    server_ip = 'http://'+json.load(open(corePropsPath))["address"]

    global stop 

    def bind_game_event():
        game_event = {
            "game": "DATEANDTIME",
            "event": "TIME",
            "data": {
                "value": 1
            },
            "handlers": [{
                "device-type": "screened",
                "mode": "screen",
                "zone": "one",
                "datas": [{
                    "lines": [{
                        "has-text": True,
                        "wrap": 1
                    },{
                        "has-text": True
                    }]
                }]
            }]
        }
        post_response = requests.post(DateTimePlugin.server_ip+"/bind_game_event", json=game_event)
        print(post_response.status_code)
        print(post_response.text)
        print(post_response.json)

    def send_heartbeat():
        heartbeat = {
            "game": "DATEANDTIME"
        }
        post_response = requests.post(DateTimePlugin.server_ip+"/game_heartbeat", json=heartbeat)
        print(post_response.status_code)
        print(post_response.text)
        print(post_response.json)

    def send_event(data):
        event = {
            "game": "DATEANDTIME",
            "event": "TIME",
            "data": {
                    "has-text": True,
                    "value": data
            }
        }
        post_response = requests.post(DateTimePlugin.server_ip+"/game_event", json=event)
        print(post_response.status_code)
        print(post_response.text)
        print(post_response.json)

    def stop_OLED_overwriting():
        global stop
        stop = True

    def start_OLED_overwriting():
        global stop 
        stop = False
        DateTimePlugin.bind_game_event()
        while True:
            dt = time.strftime("%d.%m.%Y     %A %H:%M", time.localtime())
            DateTimePlugin.send_event(dt+"_")
            DateTimePlugin.send_heartbeat()
            sleep(14)
            if (stop):
                break
