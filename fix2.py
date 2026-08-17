import glob
import re

files = glob.glob('html/*.html')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # .onclick = identifier; -> .click(identifier);
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.onclick\s*=\s*([a-zA-Z0-9_]+);",
        r"\1.click(\2);",
        content
    )

    # document.createElement('tr') -> $('<tr>')[0] or just $ ('<tr>')
    # Because there are likely native operations on it like td = document.createElement('td'); row.appendChild(td)
    # If we convert it completely to jQuery, it's better. But wait, `festival.html` uses document.createElement.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
print("Fixes applied.")