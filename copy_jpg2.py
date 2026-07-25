import shutil, os, sys

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_pages', '主页照.jpg')
dst_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
dst = os.path.join(dst_dir, 'profile.jpg')

log = f'__copy_log.txt'
with open(log, 'w') as f:
    f.write(f'CWD: {os.getcwd()}\n')
    f.write(f'Src: {src}\n')
    f.write(f'Src exists: {os.path.isfile(src)}\n')

    if os.path.isfile(src):
        f.write(f'Src size: {os.path.getsize(src)}\n')
        os.makedirs(dst_dir, exist_ok=True)
        shutil.copy2(src, dst)
        dst_exists = os.path.isfile(dst)
        f.write(f'Dst exists: {dst_exists}\n')
        if dst_exists:
            f.write(f'Dst size: {os.path.getsize(dst)}\n')
        f.write('SUCCESS\n')
    else:
        f.write('SOURCE NOT FOUND\n')
        sys.exit(1)
