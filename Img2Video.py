import cv2

fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
cap_fps = 48
size = (640, 480)
video = cv2.VideoWriter('video/result-500-10.avi', fourcc, cap_fps, size)

for i in range(200):
    img = cv2.imread("./picture/DataRe-500-10/pic-{0}.png".format(i))
    video.write(img)
video.release()
