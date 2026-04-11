import re
with open("index.html", "r") as f:
    content = f.read()

# Add a tiny button style
style_to_add = """
    .btn-micro {
      background: transparent;
      border: 1px solid rgba(255,255,255,0.2);
      color: #94a3b8;
      border-radius: 6px;
      padding: 4px 8px;
      font-size: 11px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s;
    }
    .btn-micro:hover {
      background: rgba(255,255,255,0.1);
      color: white;
    }
    .label-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .label-row label {
      margin-bottom: 0;
    }
"""

if ".btn-micro" not in content:
    content = content.replace("</style>", style_to_add + "</style>")

# Replace the labels for create-admin
old_label1 = '<label><i class="fa-solid fa-crown" style="color: #fbbf24;"></i> 管理者用 マスターパスワード（8文字以上）</label>'
new_label1 = '''<div class="label-row">
        <label><i class="fa-solid fa-crown" style="color: #fbbf24;"></i> 管理者用 マスターパスワード</label>
        <button class="btn-micro" onclick="autoGenPwd('create-admin-password')"><i class="fa-solid fa-rotate-right"></i> 再生成</button>
      </div>'''
content = content.replace(old_label1, new_label1)

# Replace the labels for create-scorer
old_label2 = '<label><i class="fa-solid fa-users" style="color: #60a5fa;"></i> 採点者共有用 アクセスコード</label>'
new_label2 = '''<div class="label-row">
        <label><i class="fa-solid fa-users" style="color: #60a5fa;"></i> 採点者用 アクセスコード</label>
        <button class="btn-micro" onclick="autoGenPwd('create-scorer-password')"><i class="fa-solid fa-rotate-right"></i> 再生成</button>
      </div>'''
content = content.replace(old_label2, new_label2)

# Replace the labels for import-admin
old_label3 = '<label><i class="fa-solid fa-crown" style="color: #fbbf24;"></i> 新管理者 パスワード</label>'
new_label3 = '''<div class="label-row">
        <label><i class="fa-solid fa-crown" style="color: #fbbf24;"></i> 新管理者 パスワード</label>
        <button class="btn-micro" onclick="autoGenPwd('import-admin-password')"><i class="fa-solid fa-rotate-right"></i> 再生成</button>
      </div>'''
content = content.replace(old_label3, new_label3)

# Replace the labels for import-scorer
old_label4 = '<label><i class="fa-solid fa-users" style="color: #60a5fa;"></i> 新採点者 アクセスコード</label>'
new_label4 = '''<div class="label-row">
        <label><i class="fa-solid fa-users" style="color: #60a5fa;"></i> 新採点者 アクセスコード</label>
        <button class="btn-micro" onclick="autoGenPwd('import-scorer-password')"><i class="fa-solid fa-rotate-right"></i> 再生成</button>
      </div>'''
content = content.replace(old_label4, new_label4)

# Change the input types from "password" to "text" initially so users can see the generated passwords, but keep them editable.
# Wait, let's keep them as password but users can click the eye icon. Or just make them type="text" by default for creation.
# Makes sense to have them be type="text" by default since they are randomly generated.
content = content.replace('<input type="password" id="create-admin-password"', '<input type="text" id="create-admin-password"')
# And toggle the FontAwesome icon to eye-slash since we start as text
content = content.replace('onclick="togglePassword(\'create-admin-password\', \'toggle-icon-create1\')"><i class="fas fa-eye"', 'onclick="togglePassword(\'create-admin-password\', \'toggle-icon-create1\')"><i class="fas fa-eye-slash"')

content = content.replace('<input type="password" id="create-scorer-password"', '<input type="text" id="create-scorer-password"')
content = content.replace('onclick="togglePassword(\'create-scorer-password\', \'toggle-icon-create2\')"><i class="fas fa-eye"', 'onclick="togglePassword(\'create-scorer-password\', \'toggle-icon-create2\')"><i class="fas fa-eye-slash"')

content = content.replace('<input type="password" id="import-admin-password"', '<input type="text" id="import-admin-password"')
content = content.replace('onclick="togglePassword(\'import-admin-password\', \'toggle-icon-import1\')"><i class="fas fa-eye"', 'onclick="togglePassword(\'import-admin-password\', \'toggle-icon-import1\')"><i class="fas fa-eye-slash"')

content = content.replace('<input type="password" id="import-scorer-password"', '<input type="text" id="import-scorer-password"')
content = content.replace('onclick="togglePassword(\'import-scorer-password\', \'toggle-icon-import2\')"><i class="fas fa-eye"', 'onclick="togglePassword(\'import-scorer-password\', \'toggle-icon-import2\')"><i class="fas fa-eye-slash"')


with open("index.html", "w") as f:
    f.write(content)
