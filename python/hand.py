from serial_connection import SerialConnection
from axis import Axis

class Hand(object):
    def __init__(self):
        self._axis = []
        self._serial = SerialConnection()
        self._serial.connect('com4', 9600)
        for i in range(0,4):
            self._axis.append(Axis())
            print("adde axis")

    def move(self, angles):
        print(self._axis)
        print(angles)
        for i in range(0,4):
            self._axis[i].set_angle(angles[i])
        packet = self._serial.create_packet(angles)
        self._serial.send(packet)