import cv2
from argparse import ArgumentParser as args 

def cartoonize(img_path):
   num_down = 2
   num_bilateral = 7 

   img=cv2.imread(img_path)
   img_copy = img

   try:
      for _ in range(num_down):
         img_copy = cv2.pyrDown(img_copy)
   except:
      print("No such image found. Please check file path.")
      return 

   for _ in range(num_bilateral):
        img_copy = cv2.bilateralFilter(img_copy, d=9, sigmaColor=9, sigmaSpace=7)

   for _ in range(num_down):
      img_copy = cv2.pyrUp(img_copy)


   img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
   img_blur = cv2.medianBlur(img_gray, 7)


   img_edge = cv2.adaptiveThreshold(img_blur, 255,
      cv2.ADAPTIVE_THRESH_MEAN_C,
      cv2.THRESH_BINARY,
      blockSize=9,
      C=2)

   #Converting to RGB from GrayScale
   img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

   try:
      img_cartoon = cv2.bitwise_and(img_copy, img_edge)
   except:
      print("Image could not be cartoonized due to inconsistency in channels")
      return

   cv2.imshow("cartooned image", img_cartoon)
   cv2.waitKey(0)

parser=args()
parser.add_argument('-i','--image',default='def.jpg',type=str,help='Path to image file')
argument=parser.parse_args()
img_path=argument.image 

cartoonize(img_path)