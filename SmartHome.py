from abc import ABC , abstractmethod
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class LightBulb(Switchable):
    def turn_on(self):
        return f"Light is Bright"
    def turn_off(self):
        return f"Light is Turning Off"
class Fan(Switchable):
    def turn_on(self):
        return f" Fan is Spinning"
    def turn_off(self):
        return f" Fan is Turning Off"
class SmartHub:
    def __init__(self,device):
        self._device = device
    def run_timer(self,duration):
        print(f"[Hub] Timer started for {duration} seconds.")
        print(f"1. {self._device.turn_on()}")
        print(f"...(waiting {duration}s) ...")
        print(f"2. {self._device.turn_off()}")
        

Bulb = LightBulb()
fan = Fan()

living_room = SmartHub(Bulb)
living_room.run_timer(2)
bedroom = SmartHub(fan)
bedroom.run_timer(2)

