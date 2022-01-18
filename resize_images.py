import cv2
import glob
images=glob.glob("D:\Python\supermarkets\sample_images\*.jpg")
for image in images:
    img=cv2.imread(image,1)
    re=cv2.resize(img,(100,100))
    cv2.imwrite("D:\Python\supermarkets\sample_images\resized_"+image,re)
    cv2.imshow("hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    