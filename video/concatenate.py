# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-03-05 
"""
# import imageio
# import ssl
#
# # 下面这一句不是必须的, 但是某些情况下访问 https 会报SSL证书不受信任, 加上这一句可以允许通过
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # 下载 ffmpeg 组件
# imageio.plugins.ffmpeg.download()

# 主要是需要moviepy这个库
from moviepy.editor import *
import os
from natsort import natsorted
import gc
# 定义一个数组
L = []

# 访问 video 文件夹 (假设视频都放在这里面)
for root, dirs, files in os.walk("D:\\CodeWorkspace\\videos"):
    # 按文件名排序
    # files.sort()
    files = natsorted(files)
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            print(filePath)
            # 载入视频
            video = VideoFileClip(filePath)
            # 添加到数组
            L.append(video)

            del video.reader
            del video
        gc.collect()

# 拼接视频
final_clip = concatenate_videoclips(L)

# 生成目标视频文件
final_clip.to_videofile("./机器之血.mp4", fps=24, remove_temp=False)
