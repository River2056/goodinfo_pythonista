class Menus():
    def __init__(self, *args):
        self.menus = args

    def print_msg_to_console(self):
        for menu in self.menus:
            print(f'{menu.id_no}: {menu.msg}.')
