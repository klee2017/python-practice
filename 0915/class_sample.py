class Shop(object):

    def __init__(self, name, shop_type, address):
        self.name = name
        self._shop_type = shop_type
        self.address = address

    def show_info(self):
        print(f'상점 ({self.name})')
        print(f'    유형: {self._shop_type}')
        print(f'    주소: {self.address}')


    @static method
    def make_dummy_shop():
        return Shop('untitled', 'undefined', 'unknown')
