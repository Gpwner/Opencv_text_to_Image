import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont


def text_to_Image(text, image, position, font_size, font_color):
    img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype('fonts/simsun.ttc', font_size)
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, text, font=font, fill=font_color)
    image = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    return image


if __name__ == '__main__':
    image = cv2.imread('images/white.png')
    text = '作者：Gpwner\n\n' \
           '个人博客:https://blog.csdn.net/gpwner\n\n' \
           '个人Github :https://github.com/Gpwner'

    image = text_to_Image(text, image, (70, 50), 30, (0, 0, 0))
    cv2.imshow('使用Opencv在图片中写文字', image)
    # cv2.imwrite('result.png',image)
    cv2.waitKey(0)
