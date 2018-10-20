class RemoteTemp:
    def __init__(self):
        self.tempAC = 25

    def set_temp(self, temp):
        self.tempAC = self.tempAC + temp


if __name__ == '__main__':
    objWhiteRemote = RemoteTemp()
    objWhiteRemote.set_temp(2)

    objBlackRemote = RemoteTemp()
    objBlackRemote.set_temp(-2)


