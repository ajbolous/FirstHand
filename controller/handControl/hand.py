from handControl.axis import Axis
from handControl.communication.serial_connection import SerialConnection
import time


class Hand(object):
    def __init__(self, port):
        self._axis = []
        for i in range(0, 4):
            self._axis.append(Axis())
            self._axis[i].set_angle(90)

        self._serial = SerialConnection()
        self._serial.connect(port, 9600)

        time.sleep(1)
        self._serial._start_reading()

    def _move(self):
        packet = self._serial.create_packet(self._axis)
        self._serial.write(packet)

    def move(self, angles):
        for i in range(0, 4):
            self._axis[i].set_angle(angles[i])
        self._move()

    def move_axis(self, axis, angle):
        self._axis[axis].set_angle(angle)
        self.move([axis._angle for axis in self._axis])

hand = Hand('/dev/ttyACM0')