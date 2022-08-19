import cv2 
print("package imported")

img = cv2.imread("photos/wallpapers/static wallpapers/zoro.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)