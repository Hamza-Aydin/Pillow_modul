from PIL import Image,ImageFilter

foto=Image.open("kuş.jpg")

#foto.show() fotoğrafı görmemizi sağlar.

#foto.save("kuş2.jpg") fotoğrafı farklı isimle kopyalamamızı sağlar.

#foto.rotate(180).save("kuş3.jpg") fotoğrafları istediğimiz derecede döndürebilmemizi sağlar.
#foto.rotate(90).save("kuş4.jpg")

#foto.convert(mode="L").save("kuş5.jpg") fotoğrafı siyah-beyaz haline getirdik.

#degisim=(120,130)
#foto.thumbnail(degisim)   (fotoğrafı istediğimiz boyutlarda küçültmemizi sağlar.)
#foto.save("kuş6.jpg")

#foto.filter(ImageFilter.GaussianBlur(5)).save("kuş7.jpg")  (fotoğrafları blurlamamızı sağlıyor)


#kırpılacak_alan=(218,0,385,310)
#foto2=Image.open("atatürk.jpg")                    =fotoğrafları kırmak isteidiğmizde kordinat buluruz ve böyle yaparız.
#foto2.crop(kırpılacak_alan).save("atatürk2.jpg")








