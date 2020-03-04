
def get_brand(some_list):
    list_brand = []
    for x in some_list:
        splitter = x[0].split()
        brand = splitter[0]
        list_brand.append(brand)
    return list_brand


def get_model(some_list):
    list_model = []
    for x in some_list:
        splitter = x[0].split()
        model = splitter[1]
        list_model.append(model)
    return list_model


def get_price(some_list):
    list_price = list()
    for i in some_list:
        list_price.append(i[1])
    return list_price


def get_screen(some_list):
    list_screen = []
    for x in some_list:
        splitter = x[2].split()
        screen = splitter[1]
        for i in screen:
            if i.isdigit():
                list_screen.append(i)
    return list_screen


def get_ram(some_list):
    list_ram = []
    for x in some_list:
        splitter = x[3].split()
        ram = splitter[1]
        list_ram.append(ram)
    return list_ram


def get_rom(some_list):
    list_rom = []
    for x in some_list:
        splitter = x[4].split(':')
        rom = splitter[1]
        list_rom.append(rom.strip())
    return list_rom


def get_qnty(some_list):
    list_qnty = []
    for x in some_list:
        splitter = x[5].split(':')
        qnty = splitter[1]
        list_qnty.append(qnty.strip())
    return list_qnty


def get_cam(some_list):
    list_cam = []
    for x in some_list:
        if len(x) > 6:
            splitter = x[6].split()
            cam = splitter[1]
            list_cam.append(cam.strip())
        if len(x) < 7:
            list_cam.append('without of camera')
    return list_cam


def new_list(some_list):
    for i in list_item:
        x = i.split(';')
        list_items.append(x)
    return list_items


def make_new_list():
    for i in range(0, len(brand)):
        info = dict()
        info['brand'] = brand[i]
        info['model'] = model[i]
        info['price'] = price[i]
        info['screen'] = screen[i]
        info['ram'] = ram[i]
        info['rom'] = rom[i]
        info['qnty'] = qnty[i]
        info['camera'] = camera[i]
        list_dict.append(info)


open_file = open('test.txt', 'r')
in_file = open_file.read()

list_item = in_file.split('\n')
list_items = []
list_dict = []
info = {}

new_list(list_item)
brand = get_brand(list_items)
model = get_model(list_items)
price = get_price(list_items)
screen = get_screen(list_items)
ram = get_ram(list_items)
rom = get_rom(list_items)
qnty = get_qnty(list_items)
camera = get_cam(list_items)
make_new_list()
print(list_dict)



