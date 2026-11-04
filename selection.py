# 15BODLOGO

# task1
toonuud=[5,2,8,1,4]
for i in range(len(toonuud)):
    baga=i
    for j in range(i+1,len(toonuud)):
        if toonuud[j]<toonuud[baga]:
            baga=j
    toonuud[i],toonuud[baga]=toonuud[baga],toonuud[i]
print(toonuud)