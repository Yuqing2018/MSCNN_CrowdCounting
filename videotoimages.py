# -*- coding: utf-8 -*-
"""videoToImages.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yMXcyDRyafyu9eZWKRfkr0nxvxmDNji0
"""

# coding=utf-8

import os
import cv2 
from tensorflow.python.platform import gfile

video_src_path= 'Data_original/Data_videos/'

video_formats = [".mp4", ".MOV"]

frame_save_path = 'Data_original/Data_im/subway_test_im/'

time_interval = 20
 

def video2frame(video_src_path, formats, frame_save_path, interval):

    """

    将视频按固定间隔读取写入图片

    :param video_src_path: 视频存放路径

    :param formats:　包含的所有视频格式

    :param frame_save_path:　保存路径

    :param frame_width:　保存帧宽

    :param frame_height:　保存帧高

    :param interval:　保存帧间隔

    :return:　帧图片

    """
    if not gfile.Exists(video_src_path):

        gfile.MakeDirs(video_src_path)
        
    if not gfile.Exists(frame_save_path):

        gfile.MakeDirs(frame_save_path)
       
        
    videos = os.listdir(video_src_path) 

    def filter_format(x, all_formats):

        if x[-4:] in all_formats:

            return True
        else:
            return False
          
    videos = filter(lambda x: filter_format(x, formats), videos) 
    
    for each_video in videos:

        print("正在读取视频：", each_video) 

        each_video_name = each_video[:-4]

        os.makedirs(frame_save_path, exist_ok=True)

        each_video_full_path = os.path.join(video_src_path, each_video) 

        cap = cv2.VideoCapture(each_video_full_path)

        frame_index = 0

        frame_count = 0

        if cap.isOpened():

            success = True

        else:

            success = False

            print("读取失败!") 

        while(success):

            success, frame = cap.read()

            print ("---> 正在读取第%d帧:" % frame_index, success)
 

            if frame_index % interval == 0:

#                 resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)

                # cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_index, resize_frame)

                cv2.imwrite(frame_save_path + "IMG_%s_%d.jpg" % (each_video_name, frame_count), frame)
#                 cv2.imread(each_video_save_full_path + "%d.jpg" % frame_count, 0)

                frame_count += 1 

            frame_index += 1 

    cap.release()
 

if __name__ == '__main__':

  video2frame(video_src_path, video_formats, frame_save_path, time_interval)
