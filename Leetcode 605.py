def canPlaceFlowers(flowerbed, n):
    import math
    Max = math.ceil((len(flowerbed))/2)
    FreeSpots = Max - flowerbed.count(1)
    if FreeSpots>=n:
        print("True")
    else:
        print("False")

canPlaceFlowers([1,0,0,0,1],1)
