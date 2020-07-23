class electronic_device():
    fm_radio=2

class electronic_gadget (electronic_device):
    pingpong=3
    mp3=4

class phone (electronic_gadget, electronic_device):
    callfeature=4
    healthapp=7
    msgs=3

dad= electronic_device ()
son=electronic_gadget ()
grandson=phone()

print (phone.mp3)
print (son.pingpong, son.fm_radio)