import glob
import re

files = glob.glob('html/*.html')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Echarts init requires native element, so handle this first
    # echarts.init(document.getElementById('...')) -> echarts.init($('#...')[0])
    content = re.sub(
        r"echarts\.init\(\s*document\.getElementById\((['\"])(.*?)\1\)\s*\)",
        r"echarts.init($('#\2')[0])",
        content
    )

    # Step 2: generic document.getElementById('id') -> $('#id')
    # Use a generic approach for all remaining, but wait it replaces the expression, 
    # we need to be careful with method calls like `.innerText`.
    # Let's replace document.getElementById('id') with $('#id')
    content = re.sub(
        r"document\.getElementById\((['\"])(.*?)\1\)",
        r"$('#\2')",
        content
    )
    
    # querySelector
    content = re.sub(
        r"document\.querySelector\((['\"])(.*?)\1\)",
        r"$('\2')",
        content
    )
    
    # querySelectorAll
    content = re.sub(
        r"document\.querySelectorAll\((['\"])(.*?)\1\)",
        r"$('\2')",
        content
    )

    # getElementsByTagName('tbody')[0] -> find('tbody').eq(0) maybe, or just .find('tbody') 
    content = re.sub(
        r"\.getElementsByTagName\((['\"])(.*?)\1\)\[0\]",
        r".find('\2').eq(0)",
        content
    )

    # Step 3: Now we have cases like $('#id').innerText = ...
    # That is invalid in jQuery. We need $('#id').text(...)
    # Let's do this via regex: \$\('.*?'\)\.innerText\s*=\s*(.+?);
    # Actually, the variable might be stored: var a = $('#id'); a.innerText = ...
    # We should search for \.innerText\s*=\s*([^;]+) and replace it with .text(\1)
    # Be careful not to replace it inside quotes.
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.innerText\s*=\s*([^;]+)",
        r"\1.text(\2)",
        content
    )

    # .innerHTML = 
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.innerHTML\s*=\s*([^;]+)",
        r"\1.html(\2)",
        content
    )

    # .value =
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.value\s*=\s*([^;]+)",
        r"\1.val(\2)",
        content
    )

    # reading .value directly, like .value.trim() -> .val().trim()
    # or .value -> .val()
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.value(?![\w\(])",
        r"\1.val()",
        content
    )
    
    # .src = ...
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.src\s*=\s*([^;]+)",
        r"\1.attr('src', \2)",
        content
    )

    # .style.display = "flex" or 'flex'
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.style\.display\s*=\s*([\"']flex[\"'])",
        r"\1.css('display', \2)",
        content
    )
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.style\.display\s*=\s*([\"']none[\"'])",
        r"\1.css('display', \2)",
        content
    )
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.style\.block\s*=\s*([\"']block[\"'])",
        r"\1.css('display', \2)",
        content
    )

    # .onclick = function() -> .click(function()
    content = re.sub(
        r"([a-zA-Z0-9_\$\(\)\'\".\[\]]+)\.onclick\s*=\s*function\s*\(\)",
        r"\1.click(function()",
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
print("Basic regex conversions done.")