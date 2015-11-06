from math import floor
from itertools import count
from decimal import *
from Tkinter import *

width = 106
height = 17

k_str = "960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719"
k = int(k_str)

getcontext().prec = len(k_str)


#
# DIY console graphics
#
buffer = [[None] * width for row in range(height)]

def draw(x, y, value):
    char = value and "##" or "  "
    buffer[y][width - x - 1] = char

def flush():
    print "\n".join(["".join(row) for row in buffer])

#
# Tkinter "real" graphics
#
# scale = 10

#tk = Tk()
#canvas = Canvas(tk, width=width * scale, height=height * scale)
#canvas.pack()

#def draw(x, y, value):
#    x1 = (width - x) * scale
#    y1 = y * scale
#    x2 = (width - (x + 1)) * scale
#    y2 = (y + 1) * scale
#   
#    fill = value and "black" or "white"
#    canvas.create_rectangle(x1, y1, x2, y2, width=0, fill=fill)

#def flush():
#    tk.mainloop()

two = Decimal(2)

def floor(n):
    return n.to_integral_exact(rounding=ROUND_FLOOR)

def tupper(x, y):
    yy = Decimal(y + k)
    return 0.5 < floor(yy / 17 * two ** (-17 * x - y) % 2)

for x in range(width):
    for y in range(height):
        value = tupper(x, y)
        draw(x, y, value)


flush()

