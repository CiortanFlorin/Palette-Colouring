from tkinter.filedialog import askopenfilename
from PIL import Image

dictionary={}
present_values=[]
def get_image():
    i=1
    #Open the image
    image = Image.open(askopenfilename())
    #Get values for each pixel in the image
    pixel_values = list(image.getdata())
    #Count how many time a pixel appears in the image
    for n in pixel_values:
        if n in present_values:
            dictionary[n]+=1
        else:
            dictionary[n]=1
            present_values.append(n)
    #Order the pixels by qunatity
    ordered_colors=sorted(dictionary.items(),key=lambda x: x[1], reverse=True)
    #Turn RGB values to hexa and return the percent of each color in image
    for n in ordered_colors[0:10]:
        print(f"{i}.{'#%02x%02x%02x' % n[0][:3]} with {round((n[1]/(len(pixel_values)))*100, 2)}% of the image")
        i+=1

get_image()

