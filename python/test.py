from hand import Hand

h = Hand()
h.move([134,123,34,34])
for i in range (0,4):
    line = h._serial._serial.readline()
    print(line)