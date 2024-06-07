#Import required Image library
from PIL import Image, ImageFilter

#Open existing image
OriImage = Image.open("Autoclicker/img/bg.png")
OriImage.show()

#Applying GaussianBlur filter
gaussImage = OriImage.filter(ImageFilter.GaussianBlur(3))
gaussImage.show()

#Save Gaussian Blur Image
gaussImage.save("Autoclicker/img/bg_blur.png")