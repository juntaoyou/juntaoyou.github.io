import shutil, os
src = r'd:\Homepage\juntaoyou.github.io\_pages\主页照.jpg'
dst_dir = r'd:\Homepage\juntaoyou.github.io\images'
dst = os.path.join(dst_dir, 'profile.jpg')
os.makedirs(dst_dir, exist_ok=True)
shutil.copy2(src, dst)
