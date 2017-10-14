#-*- coding:utf-8 -*-
#字符画：将图片中的像素用字符代替

'''
RGB色彩模式是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色。
通常情况下，RGB各有256级亮度，用数字表示为从0、1、2...直到255。注意虽然数字最高是255，但0也是数值之一，因此共256级。
'''

from PIL import Image
import argparse

'''
import argparse                        # 首先导入该模块
parser = argparse.ArgumentParser()     # 然后创建一个解析对象
parser.add_argument()                  # 向该对象中添加需要的命令行参数和选项，每一个add_argument方法对应一个你要关注的参数或选项
parser.parse_args()                    # 最后调用parse_args()方法进行解析；解析成功之后即可使用
'''
#命令行输入参数处理
parser = argparse.ArgumentParser()                        # 创建一个对象parser

parser.add_argument('file')                               # 输入文件
parser.add_argument('-o', '--output')                     # 输出文件
parser.add_argument('--width', type = int, default = 80)  # 输出字符画宽
parser.add_argument('--height', type = int, default = 80) # 输出字符画高

#获取参数
args = parser.parse_args()            # 解析成功后为 args

IMG = args.file                      
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 定义一个ascii的列表，其实就是让图片上的灰度与字符对应
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):  #这个调用跟im.getpixel函数有关，这个函数是根据图片的横纵坐标，把图片解析成r,g,b,alpha(灰度） 有关的四个参数，所以这里输入参数是四个
                                 
    if alpha == 0:                #如果灰度是0，说明这里没有图片
        return ' '
    length = len(ascii_char)      #字符集长度
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)       #把彩色图片的RGB值转换成灰度值

    unit = (256.0 + 1)/length                              #没个字符对应的gray值，也就是区间宽度
    return ascii_char[int(gray/unit)]                      #gray值对应到ascii_char中的位置（索引值）

if __name__ == '__main__':                                 #如果是本程序调用，则执行以下程序

    im = Image.open(IMG)                                   #打开图片
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)          #更改图片的显示比例

    txt = ""                                               # txt初始值为空

    for i in range(HEIGHT):                                # i代表纵坐标
        for j in range(WIDTH):                             # j代表纵坐标
            txt += get_char(*im.getpixel((j,i)))           #把图片按照横纵坐标解析成r,g,b以及alpha这几个参数，然后调用get_char函数，把对应的图片转换成灰度值，把对应值的字符存入txt中
        txt += '\n'

    print txt                                              #每行的结尾处，自动换行
    
    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
