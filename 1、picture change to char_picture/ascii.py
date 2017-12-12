#-*-coding:utf-8-*-#
from PIL import Image
import argparse


#命令行输入参数处理

parse =argparse.ArgumentParser()
parse.add_argument('file')
parse.add_argument('-o','--output')
parse.add_argument('--width',type= int ,default = 80)
parse.add_argument('--height',type= int , default = 80)

args = parse.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


#可以随意的字符list尽量不重复
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

def get_char(r, g, b, alpha = 256):
    if alpha == 0:#当透明度是0的时候输出空格
        return ' '
    length = len(ascii_char)
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    unit = (256.0 +1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = ""

    for x in range(WIDTH):
        for y in range(HEIGHT):
            txt +=get_char(*im.getpixel((y,x)))
        txt +='\n'

    print txt

    #将字符串画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)



