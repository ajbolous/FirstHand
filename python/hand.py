from serial_connection import SerialConnection

class Hand(object):
    def __init__(self):
        self._axis = []
        self._serial = SerialConnection()
        self._serial.connect('com1', 9600)

    def move(self, angles):
        for axis,angle in self._axis,angles:
            if angle<1:
                axis =1
            axis.angle = angle
        packet = self._serial.create_packet(angles)
        self._serial.send(packet)