import serial
import thread

class SerialConnection(object):
    def __init__(self):
        self._serial=None

    def connect(self, port, baud):
        self._serial=serial.Serial(port,baud)
        return self._serial.isOpen()

    def disconnect(self):
        self._serial.close()

    def _start_reading(self):
        thread.start_new_thread(self._read,())

    def _read(self):
        while(True):
            data = self._serial.readline()
            print(data)

    def write(self, data):
        for d in data:
            self._serial.write(chr(d))

    def create_packet(self,axis):
        data = [200,
                axis[0].angle,
                axis[1].angle,
                axis[2].angle,
                axis[3].angle,
                200]
        return data
