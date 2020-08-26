import os
from vid2vid_lib.scripts.download_gdrive import *

file_id = '1E8re-b6csNuo-abg1vJKCDjCzlIam50F'
chpt_path = 'datasets/models/'
destination = os.path.join(chpt_path, 'FlowNet2_checkpoint.pth.tar')
download_file_from_google_drive(file_id, destination) 