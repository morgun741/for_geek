import time
class TrafficLight:
    def __init__(self, colour):
        self.__colour = colour
    def running(self):
        for i in self.__colour.items():
            print(i[0])
            time.sleep(i[1])
t = TrafficLight({"red": 7, "ellow": 2, "green": 1})
print(t.running())

