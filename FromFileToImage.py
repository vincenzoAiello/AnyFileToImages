from PIL import Image
import os
import math
from tqdm import tqdm


pathFile=input("Insert path to input file : ")
pathOutput=input("Insert path to output image : ") 


##leggo quanti bytes è il file 
##get the file size
totBytesFile= os.stat(pathFile).st_size

##preparo l'immagine con larghezza e lunghezza pari alla radice quarata della dimensione del file + 1
# prepare the image with width and length equal to the fourth root of the file size + 1
width=round(math.sqrt(totBytesFile * 8)) +1
height=round(math.sqrt(totBytesFile * 8)) +1
img  = Image.new( mode = "L", size = (width, height), color=170)

##leggo i bytes del file e imposto i pixel dell'immagine a bianco per i bit a 1 e a nero per i bit a 0
#read the bytes of the file and set the pixels to white  for the bits at 1 and black for the bits at 0
countI=0
countJ=0
with open(pathFile, "rb") as f:
    bytes_read = f.read()
    #con tqdm creo una progress bar
    #create a progress bar with tqdm
    for b in tqdm(bytes_read):
        bits = format(b,'08b')
        for bit in bits:
            if(bit=="0"):
                img.putpixel((countI,countJ),0)
            else:
                img.putpixel((countI,countJ),255)
            if(countI<width-1):
                countI +=1
            else:
                countI =0
                countJ +=1
    f.close()


##salvo l'immagine
#save the image
img.save(pathOutput)





