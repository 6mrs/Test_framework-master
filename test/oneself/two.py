# -*- coding=utf-8 -*-

from PIL import Image

IMG = 'docs/img/ic.jpg'  # 设置图片文件
WIDTH = 150  # 设置字符画的宽
HEIGHT = 80  # 设置字符画的高
OUTPUT = 'output5.txt'  # 设置存放字符画的文本文件
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")  # 设置显示的字符集


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    # alpha为透明度
    # 判断 alpha 值，为0表示全透明
    if alpha == 0:
        return ' '

    # 获取字符集的长度，这里为 70
    length = len(ascii_char)
    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    # 防止当灰度值为255时，输出的第70个字符超出列表索引，所以需要将(255+1)
    unit = (255.0 + 1) / length

    # 返回灰度值对应的字符
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':

    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = "111"

    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j, i)))
        # 遍历完一行后需要增加换行符
        txt += '\n'
    # 输出到屏幕
    print(txt)
    with open(OUTPUT, 'w') as f:
        f.write(txt)
