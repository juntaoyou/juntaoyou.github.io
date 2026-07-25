import os, shutil

base_dir = r'd:\Homepage\juntaoyou.github.io'

# 1. Create images directory if it doesn't exist
images_dir = os.path.join(base_dir, 'images')
os.makedirs(images_dir, exist_ok=True)
print('Step 1: images/ directory ensured.')

# 2. Copy source to destination
src = os.path.join(base_dir, '_pages', '主页照.jpg')
dst = os.path.join(base_dir, 'images', 'profile.jpg')

if not os.path.exists(src):
    print(f'ERROR: Source file {src} does not exist!')
    # Try to find the file
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if '主页' in f or 'profile' in f or f.endswith('.jpg'):
                print(f'  Found: {os.path.join(root, f)}')
else:
    shutil.copy2(src, dst)
    print(f'Step 2: Copied {src} -> {dst}')

# 3. Verify
if os.path.exists(dst):
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    print(f'Step 3: Verification PASSED. File exists at {dst}')
    print(f'  Source size: {src_size} bytes')
    print(f'  Dest size:   {dst_size} bytes')
    print(f'  Sizes match: {src_size == dst_size}')
else:
    print(f'ERROR: Destination file {dst} does not exist after copy!')
