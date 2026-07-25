import shutil, os, sys

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_pages', '主页照.jpg')
dst_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
dst = os.path.join(dst_dir, 'profile.jpg')

print(f'Source: {src}')
print(f'Source exists: {os.path.isfile(src)}')

if os.path.isfile(src):
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copy2(src, dst)
    print(f'Copied to: {dst}')
    print(f'Dest size: {os.path.getsize(dst)}')
else:
    sys.exit(1)
