from PIL import Image # 
img=Image.open("photosecrete.png")
L,H=img.size
img2 = Image.new("RGB",(L,H))
for x in range(0,L) :
    for y in range(0,H) :
        a=img.getpixel((x,y))
        b=(a[0],a[1],a[2])
        img2.putpixel((x,y),b)
img2.save("photo_copie.png")
def decoupeNombre(nombre):
    return [nombre//100,(nombre%100)//10,nombre%10]
def codeUnPixel(pixel,caractere):
    # recupération du nombre correspondant au caractère avec la table ASCII
    decimale=ord(caractere)
    # récupérer dans la variable decimale la liste contenant les valeurs du pixel
    decimale=decoupeNombre(decimale)
    # créer le nouveau pixel (liste)
    new_pixel=((pixel[0]//10)*10+decimale[0])
    return new_pixel
codeUnPixel((254, 56, 100),"Du passé faisons table en marbre")
decoupeNombre(97)
# Du passé faisons table en marbre