import cv2
import argparse
import os

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-id','--id', help='Description for foo argument', required=True)
args = vars(parser.parse_args())

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
            cv2.imwrite(outputFile + str(c).zfill(5) + '.jpg', frame)
        c += 1
        cv2.waitKey(1)
    vc.release()

if __name__ == '__main__':
    print(f'=========== Processing Video of Subject ID: [' + args['id'] + '] ===========')
    # videoFile = 'D:/SmartRehab/Video Data/Pilot/Pilot_Iphone12.MOV'
    videoFile = 'D:/SmartRehab/Data_Video/' + args['id'] + '/Iphone12_RGB.MOV'
    # outputFile = 'D:/SmartRehab/Video Data/Pilot/IphoneVideo2Img/'
    outputFile = 'D:/SmartRehab/Data_Image/' + args['id'] + '/'

    if not os.path.exists(outputFile):
        os.makedirs(outputFile)

    vc = cv2.VideoCapture(videoFile)
    processing(vc, outputFile)