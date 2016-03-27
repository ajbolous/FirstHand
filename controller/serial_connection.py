import serial
import thread
import time

class SerialConnection(object):
    def __init__(self):
        self._serial=None

    def connect(self, port, baud):
        self._serial=serial.Serial(port,baud)
        time.sleep(1)
        thread.start_new_thread(self.read,())
        return self._serial.isOpen()

    def disconnect(self):
        self._serial.close()

    def read(self):
        while(True):
            data = self._serial.readline()
            print(data)

    def write(self, data):
        for d in data:
            self._serial.write(chr(d))

    def create_packet(self,angles):
        data = [200, 200, angles[0], angles[1], angles[2], angles[3],200,200]
        return data
