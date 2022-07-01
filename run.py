import os
import cv2
from PIL import ImageFont, Image, ImageDraw
import numpy as np

list_of_names = []


def clear_folder():
   for i in os.listdir("generated-certificates/"):
      os.remove("generated-certificates/{}".format(i))


def clean_data():
   with open('names.txt') as f:
      for line in f:
          list_of_names.append(line.strip())


def generate_certificates():

   for index, name in enumerate(list_of_names):


      image = cv2.imread("Certificate.png")
      cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
   
      pil_im = Image.fromarray(cv2_im_rgb)  
         
      draw = ImageDraw.Draw(pil_im)

      font = ImageFont.truetype("berkshire-swash.regular.ttf", 72)

      name = str(name).strip()

      w, h = draw.textsize(name, font=font)
      W, H = (2000, 1414)
      text_start = 620

      draw.text(((W-w)/2,text_start),str(name), font=font, fill="#000000")

      
      cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  

      f_name = name.replace(':', " ")

      cv2.imwrite("generated-certificates/{}.png".format(f_name), cv2_im_processed)
      print("Processing {} / {}".format(index + 1,len(list_of_names)))
      
def main():
   clear_folder()
   clean_data()
   generate_certificates()


if __name__ == '__main__':
   main()

