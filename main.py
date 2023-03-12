import cv2
img=cv2.imread("solarsystem.jpg")
print(img,len(img))

cv2.putText(img,
            "Mercury",
            (120,245),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.putText(img,
            "Venus",
            (195,255),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.putText(img,
            "Earth",
            (290,262),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.putText(img,
            "Mars",
            (385,250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.putText(img,
            "Jupiter",
            (560,370),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.putText(img,
            "Saturn",
            (780,295),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.putText(img,
            "Uranus",
            (975,285),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.putText(img,
            "Neptune",
            (1120,280),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255))

cv2.imshow("solarsystem",img)
cv2.waitKey(0)

