import re
with open("js/index.js", "r") as f:
    content = f.read()

content = content.replace("/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/", "/^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{8,}$/")

with open("js/index.js", "w") as f:
    f.write(content)
