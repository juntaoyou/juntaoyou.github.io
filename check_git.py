import subprocess, os

os.chdir(r'd:\Homepage\juntaoyou.github.io')

# Step 1: git status before
print("=== BEFORE ===")
r = subprocess.run(['git', 'status'], capture_output=True, text=True)
print(r.stdout)
if r.stderr: print("STDERR:", r.stderr)

# Step 2: git add
print("=== GIT ADD ===")
r = subprocess.run(['git', 'add', '_pages/about.md', '_pages/cv.md'], capture_output=True, text=True)
print("add stdout:", repr(r.stdout))
print("add stderr:", repr(r.stderr))
print("add returncode:", r.returncode)

# Step 3: git commit
print("=== GIT COMMIT ===")
r = subprocess.run(['git', 'commit', '-m', 'Remove GPA and coursework info'], capture_output=True, text=True)
print("commit stdout:", repr(r.stdout))
print("commit stderr:", repr(r.stderr))
print("commit returncode:", r.returncode)

# Step 4: git push
print("=== GIT PUSH ===")
r = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print("push stdout:", repr(r.stdout))
print("push stderr:", repr(r.stderr))
print("push returncode:", r.returncode)

# Step 5: log after
print("=== LOG AFTER ===")
r = subprocess.run(['git', 'log', '--oneline', '-3'], capture_output=True, text=True)
print(r.stdout)

print("=== DONE ===")
