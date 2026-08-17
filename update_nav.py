import os, glob, re

files = glob.glob('html/*.html')
files = [f for f in files if not f.endswith('index.html')]

nav_pattern = re.compile(r'<nav>[\s\S]*?</nav>')

back_link = '''<div style="text-align: center; margin-bottom: 20px;">
            <a href="index.html" style="display: inline-block; padding: 8px 20px; background-color: #8b2323; color: #fff; text-decoration: none; border-radius: 20px; font-weight: bold; transition: all 0.3s ease;">⮐ 返回首页</a>
        </div>'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<nav>' in content:
        new_content = nav_pattern.sub(back_link, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No <nav> found in {file}")

print("Replacement Complete")
