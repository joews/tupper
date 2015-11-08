import math
from decimal import *
from Tkinter import *

width = 106
height = 17

k_str = "960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719"

k_str = "4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300"

k = int(k_str)

getcontext().prec = len(k_str)


#
# DIY console graphics
#
buffer = [[None] * width for row in range(height)]

def draw(x, y, value):
    char = value and "##" or "  "
    buffer[y][x] = char

def flush():
    print "\n".join(["".join(row) for row in buffer])

#
# Tkinter "real" graphics
#
scale = 10

tk = Tk()
canvas = Canvas(tk, width=width * scale, height=height * scale)
canvas.pack()

#def draw(x, y, value):
#    x1 = x * scale
#    y1 = y * scale
#    x2 = (x + 1) * scale
#    y2 = (y + 1) * scale
   
#    fill = value and "black" or "white"
#    canvas.create_rectangle(x1, y1, x2, y2, width=0, fill=fill)

#def flush():
#   tk.mainloop()


#
# Approach 1
# Iteratively apply Tupper's formula to each (x, y) coordinate
# Slow!
#

two = Decimal(2)

def floor(n):
    return n.to_integral_exact(rounding=ROUND_FLOOR)

def tupper(x, y):
    return 0.5 < floor((y + k) / 17 * two ** (-17 * x - y) % 2)

def tupper_formula():
    for x in range(width):
        for y in range(height):
            # invert the x axis
            x_out = width - x - 1
            draw(x, y, tupper(x, y))

#
# Approach 2
# Decode the bitmap directly
# Fast! and, in Python, doesn't need special Large Number handling
#
def tupper_decode():
    # binary representation of k / 17
    # strip the "0b" prefix and zero-pad to the required length
    binary_str = bin(k / 17 )
    bits = binary_str[2::].zfill(width * height)

    for x in range(width):
        col_offset = (x * height)

        for y in range(height):
            # natural index: inverted y axis
            # index = (x * height + y)

            # invert y
            # surely better to decode naturally and use different k!
            row_offset = (height - y - 1)
            index = col_offset + row_offset
            draw(x, y, int(bits[index]))

tupper_decode()
flush()

tupper_formula()
flush()
