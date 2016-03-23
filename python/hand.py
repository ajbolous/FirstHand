from serial_connection import SerialConnection

class Hand(object):
    def __init__(self):
        self._axis = []
        self._serial = SerialConnection()

    def moveAxis(self, axis_id, angle):
        self._axis[axis_id].angle = angle
        self._serial.send(self._axis)