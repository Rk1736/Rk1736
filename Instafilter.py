from Instafilter import Instafilter

model = Instafilter("Lo-fi")
new_image = model("image.jpg")

#To save the image using cv2
import cv2
cv2.imwrite("modified_image.jpg", new_image)