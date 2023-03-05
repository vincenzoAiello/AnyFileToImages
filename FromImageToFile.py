from PIL import Image
from tqdm import tqdm


pathFile=input("Insert path to input image : ")
pathOutput=input("Insert path to output file : ")

#per eliminare limite di pillow sulla dimenione delle immagini lette
#delete the pillow dimension image limit
Image.MAX_IMAGE_PIXELS = None

##leggo l'immagine e converto i pixel neri in uno 0 e quelli bianchi in 1. I bytes che usciranno li scrivo nel file di output
#read the image and convert the black pixels to 0 and the white pixels to 1. Write bytes in the output file
saved_img= Image.open(pathFile)
pixelsList = list(saved_img.getdata())
currentByte=""
countBytes = 0
with open(pathOutput,"wb") as out :
    for pixel in tqdm(pixelsList):
        if(pixel==255):
            currentByte += "1"
            countBytes +=1 
        if(pixel==0):
            currentByte +="0"
            countBytes +=1
        if(countBytes == 8):
            ##leggo il byte corrente, ne ricavo il decimale e ottengo il carattere a cui corrisponde il byte
            binaryToDecimal = int(currentByte,2)
            out.write(binaryToDecimal.to_bytes(1,"big"))
            currentByte=""
            countBytes=0
    out.close()