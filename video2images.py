import os

import cv2 as cv

# 读取视频地址
VIDEO_FILE = "./source_video/source.mkv"
# 存放图片目录
IMAGE_DIR = "./source_images"
# RATIO 代表多少秒截一帧
RATIO = 8;

def store_image(filename, content):
    with open(filename, "wb") as fd:
        fd.write(content)

cap = cv.VideoCapture(VIDEO_FILE)

index = 0
while True:
    # 设定当前视频流读取位置
    cap.set(cv.CAP_PROP_POS_MSEC, index * RATIO * 1000)                      
    success, image = cap.read()
    # 视频流已经读完了
    if not success:
        break
    
    # 将图片转为 jpg，并进行一定压缩
    success, image = cv.imencode(".jpg", image, [cv.IMWRITE_JPEG_QUALITY, 80])

    # 持久化，index 作为图片标题和时间戳
    store_image(os.path.join(IMAGE_DIR, "{0}.jpg".format(index)), image)

    index += 1


cap.release()
