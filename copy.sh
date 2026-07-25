#!/bin/sh
python -c "
import shutil, os
src = '/d/Homepage/juntaoyou.github.io/_pages/主页照.jpg'
dst_dir = '/d/Homepage/juntaoyou.github.io/images/'
dst = dst_dir + 'profile.jpg'
os.makedirs(dst_dir, exist_ok=True)
shutil.copy2(src, dst)
print('COPY SUCCESSFUL')
"