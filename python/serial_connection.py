import serial

class SerialConnection(object):
    def __init__(self):
        self._serial=None

    def connect(self, port, baud):
        self._serial=serial.Serial(port,baud)
        return self._serial.isOpen()

    def disconnect(self):
        self._serial.close()

    def send(self, data):
        pass
