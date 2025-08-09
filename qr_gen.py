import qrcode
import sys


def generate(data, name, color, back, size):
    qr = qrcode.QRCode(version = 1, box_size = size, border = 5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color = color, back_color = back)
    img = qrcode.make(data)
    img.save(name + '.png')


info = sys.argv[1]



if info == "help":
    print("Requires five arguments: data, name of file, color, background, & size of the code")
    print("Example: python3 qr_gen.py Hi! qrFile1 red 10")
    print("Help: Displays this image and exits the program")
    print("Example: python3 qr_gen.py help")

else:
    fileName = sys.argv[2]
    foreColor = sys.argv[3]
    backColor = sys.argv[4]
    codeSize = int(sys.argv[5])
    generate(info, fileName, foreColor, backColor, codeSize)