# use emoji

from emoji import emojize

print(emojize(":thumbs_up:"))

for i in range(0x1f600,0x1f650):
    print(chr(i),end=" ")
    if i%16==15:
        print()
