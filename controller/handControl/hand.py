from handControl.axis import Axis
from handControl.serial_connection import SerialConnection


class Hand(object):
    def __init__(self, port):
        self._axis = []
        self._serial = SerialConnection()
        self._serial.connect(port, 9600)
        for i in range(0, 4):
            self._axis.append(Axis())
            self._axis[i].set_angle(90)

    def move(self, angles):
        for i in range(0, 4):
            self._axis[i].set_angle(angles[i])
        packet = self._serial.create_packet(angles)
        self._serial.write(packet)

    def move_axis(self, axis, angle):
        self._axis[axis].set_angle(angle)
        self.move([axis._angle for axis in self._axis])

hand = Hand('/dev/ttyACM1')