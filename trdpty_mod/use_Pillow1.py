#通过Pillow提供的模块，可以对图像进行一系列的操作,如缩放、旋转、切片、添加滤镜、输出文字等等

#图像缩放

from PIL import Image                     #引入Image模块

im = Image.open('test.jpg')               #打开一个jpg图像文件，注意是当前路径
w,h = im.size                             #获得图像尺寸
print('Original image size: %s x %s'%(w,h))
im.thumbnail((w * 0.5,h * 0.5))           #缩放到50%
print('Resize image to: %sx%s' % (w*0.5, h*0.5))
im.save('chunjiao.jpg','jpeg')            #把缩放后的图像用jpeg格式保存

from PIL import ImageFilter               #额外添加ImageFilter模块

im1 = Image.open('test.jpg')              #打开原始图
im2 = im1.filter(ImageFilter.BLUR)        #添加模糊效果
im2.save('blur.jpg','jpeg')               #保存新图像