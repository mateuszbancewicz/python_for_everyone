class Tv:
    def __init__(self, channel=1, volume=10):
        print('Yay, you have new TV')
        print('You have 20 channels')
        self._channel = channel
        self.__volume = volume

    def _set_channel(self, new_channel):
        if 1 <= new_channel <= 21:
            self._channel = new_channel
        print(f'You are watching now channel {self._channel}')

    def next_channel(self):
        self._set_channel(new_channel=self._channel + 1)

    def prev_channel(self):
        self._set_channel(new_channel=self._channel - 1)

    def _volume_up(self):
        amount = int(input('How much? '))
        self.__volume += amount
        self.__volume = min(self.__volume, 100)
        self.show_volume()

    def _volume_down(self):
        amount = int(input('How much? '))
        self.__volume -= amount
        self.__volume = max(self.__volume, 0)
        self.show_volume()

    def show_volume(self):
        print(f'Volume is now on {self.__volume}')

    def menu(self):
        print(f'''
                    TV MENU:
                1. Set channel (1-20)
                2. Next channel
                3. Previous Channel
                4. Volume up
                5. Volume down
                0. EXIT
            
        CHANNEL: {self._channel}    VOLUME: {self.__volume}''')

    def remote(self):
        choice = ''
        while choice != 0:
            self.menu()
            choice = int(input('\nChoose: '))
            if choice == 1:
                channel = int(input('Set channel: '))
                self._set_channel(new_channel=channel)
            elif choice == 2:
                self.next_channel()
            elif choice == 3:
                self.prev_channel()
            elif choice == 4:
                self._volume_up()
            elif choice == 5:
                self._volume_down()
            elif choice == 0:
                print('Enjoy watching :)')
                break
            else:
                print("Wrong choice")


if __name__ == '__main__':
    tv = Tv()
    tv.remote()
