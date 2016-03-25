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
        self._serial.write(data)

    def create_packet(self,angles):
        data = [angles[0],angles[1],angles[2],angles[3],0,0]
        data=bytearray(data)
        return str(data)

    def create_send_package(self,angles):
        packet=self.create_packet(angles)
        self.send(packet)
