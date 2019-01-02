# geopy模块是通过抽象出一系列不同的地理编码服务的API来工作，它可以让你获得
# 某一地点的完整街道地址、维度、精度甚至海拔高度

from geopy import GoogleV3

place = "221b Baker Street, London"
location = GoogleV3().geocode(place)

print(location.address)
print(location.location)
