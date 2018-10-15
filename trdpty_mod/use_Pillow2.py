#生成字母验证码
#通过ImageDraw模块，可以进行绘图操作
#通过ImageFont模块，定义字体参数

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母:
def rndChar():
	return chr(random.randint(65, 90))

#随机旋转:
def rndRotate():
	return random.randint(-90, 90)

#随机颜色1
def rndColor():
	return (random.randint(64, 255),random.randint(64, 255), random.randint(64, 255))

#随机颜色2
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#生成字母
def rndCharImg():
	charimage = Image.new('RGB',(60, 60), (0,0,0))       # 创建新的图像
	drawChar =ImageDraw.Draw(charimage)                  # 创建可绘画对象
	font = ImageFont.truetype('arial.ttf', 36)           # 定义字体参数
	drawChar.text((10, 10), rndChar(), font = font, fill = rndColor2())  # 添加字母到图像中
	charimage = charimage.rotate(rndRotate())            # 旋转图像
	return charimage                                     # 返回生成的字母图像

#创建主图像
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))      # 创建主图像
draw = ImageDraw.Draw(image)                   # 创建可绘画对象
for x in range(width):                         # 填充每个像素
	for y in range(height):
		draw.point((x, y), fill = rndColor())

# 添加模糊效果
image = image.filter(ImageFilter.BLUR)

# 添加字母到主图像中
for t in range(4):
	img = rndCharImg()
	r, g, b= img.split()                       # 分离图层
	image.paste(img, (60 * t + 10, 10),r)      # 把字母图像粘贴到r图层中

# 保存图像
image.save('code.jpg', 'jpeg')


#相关函数：
#Image.new(mode, size, color = 0):可创建一个图像，参数依次是图像模式，大小，颜色
#ImageDraw.Draw():是指定图像变为可绘画对象
#ImageFont.truetype(font, size):定义字体，参数依次是字体，大小
#drawChar.text(position, text, font, fill):
#可以把文本添加到图像中，参数依次是文本左上角点位置，文本，字体，填充颜色
#.roate()可旋转对象
#r,g,b = img.split():分离图层
#.paste():把图像粘贴到指定的位置，参数依次是粘贴对象，位置，图层