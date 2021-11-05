# -*- coding: utf-8 -*-
# @Time : 2021/11/5 15:28
# @Author : Limusen
# @File : demo_path


import os
import time
from Common.config_utils import local_config


cur_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# file_path = os.path.join(current_path, local_config.get_screen_shot_path)
file_name = os.path.join(current_path, local_config.get_screen_shot_path, "{}_{}.png".format("page_action", cur_time))

print(file_name)
