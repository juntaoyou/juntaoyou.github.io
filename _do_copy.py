import os, shutil

src = r'd:\Homepage\juntaoyou.github.io\_pages\主页照.jpg'
dst_dir = r'd:\Homepage\juntaoyou.github.io\images'
dst = os.path.join(dst_dir, 'profile.jpg')

# Check source exists
src_exists = os.path.isfile(src)
print(f'Source file exists: {src_exists}')
if not src_exists:
    print(f'ERROR: Source file not found: {src}')
else:
    src_size = os.path.getsize(src)
    print(f'Source file size: {src_size} bytes')

# Create destination directory if needed
if not os.path.isdir(dst_dir):
    os.makedirs(dst_dir)
    print(f'Created directory: {dst_dir}')

# Check if destination already exists
dst_exists = os.path.isfile(dst)
print(f'Destination file already exists: {dst_exists}')

# Copy the file
if src_exists:
    shutil.copy2(src, dst)
    print(f'Copied: {src} -> {dst}')
    print(f'Destination file size: {os.path.getsize(dst)} bytes')
