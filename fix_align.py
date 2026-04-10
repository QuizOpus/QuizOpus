with open('saiten.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("const cx = L2 + 2.5 + col * 4.2;", "const cx = L2 + 1.5 + col * 4.2;")

with open('saiten.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed bubble alignment.")
