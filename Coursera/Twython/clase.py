
from twython import TwythonStreamer

C_Key = "DE4vyuzfT6vDM0rt5QgIshvyN"
C_Secret = "Y7d4XySIEDxUzdro1uzCnJSgUOSqgfErZzpbYkgyU7QfDQfeHv"
A_Token = "110487247-vUIcCw1Cbip3MWfuSv9nUrqs8l4Q4jdsO5Ma0v5E"
A_Secret = "vmlo8PrPortZT9bzmLvi3FiTYq0Irqvgt36bFKbSg4mx1"

class MyStreamer (TwythonStreamer):
        def on_success (self, data):
                if 'text' in data:
                        print ("found it")

stream= MyStreamer (C_Key, C_Secret, A_Token, A_Secret)

stream.statuses.filter(track = "hola_adb")
        

