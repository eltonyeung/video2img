import cv2

def processing(vc,outputFile):
    c = 0
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        print('openerror!')
        rval = False

    timeF = 1  #视频帧计数间隔次数
    while rval:
        rval, frame = vc.read()
        if c % timeF == 0:
            print('Frame: ',c)
            # frame = np.rot90(frame, -1)
            cv2.imwrite(outputFile + str(c) + '.jpg', frame)
        c += 1
        cv2.waitKey(1)
    vc.release()
if __name__ == '__main__':
    videoFile = 'Demo.MP4'
    outputFile = 'Trial12/'
    vc = cv2.VideoCapture(videoFile)
    processing(vc, outputFile)