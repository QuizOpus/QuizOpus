import re
with open("js/index.js", "r") as f:
    content = f.read()

# Add autoGenPwd
js_to_add = """
function generateStrongPassword() {
	const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	const lower = 'abcdefghijklmnopqrstuvwxyz';
	const num = '0123456789';
	const all = upper + lower + num + '!@#';
	let pwd = '';
	pwd += upper[Math.floor(Math.random() * upper.length)];
	pwd += lower[Math.floor(Math.random() * lower.length)];
	pwd += num[Math.floor(Math.random() * num.length)];
	for(let i = 3; i < 12; i++) {
		pwd += all[Math.floor(Math.random() * all.length)];
	}
	return pwd.split('').sort(() => 0.5 - Math.random()).join('');
}

function autoGenPwd(id) {
	document.getElementById(id).value = generateStrongPassword();
}

"""

if "function generateStrongPassword()" not in content:
    content = js_to_add + content

# Modify setTab to auto-generate if fields are empty
old_set_tab = """function setTab(tab) {
	currentTab = tab;
	document.getElementById('tab-join').className = tab === 'join' ? 'tab active' : 'tab';
	document.getElementById('tab-create').className = tab === 'create' ? 'tab active' : 'tab';
	document.getElementById('section-join').style.display = tab === 'join' ? 'block' : 'none';
	document.getElementById('section-create').style.display = tab === 'create' ? 'block' : 'none';
	document.getElementById('section-import').style.display = tab === 'import' ? 'block' : 'none';
}"""

new_set_tab = """function setTab(tab) {
	currentTab = tab;
	document.getElementById('tab-join').className = tab === 'join' ? 'tab active' : 'tab';
	document.getElementById('tab-create').className = tab === 'create' ? 'tab active' : 'tab';
	
	if (tab === 'create') {
		if (!document.getElementById('create-admin-password').value) autoGenPwd('create-admin-password');
		if (!document.getElementById('create-scorer-password').value) autoGenPwd('create-scorer-password');
	} else if (tab === 'import') {
		if (!document.getElementById('import-admin-password').value) autoGenPwd('import-admin-password');
		if (!document.getElementById('import-scorer-password').value) autoGenPwd('import-scorer-password');
	}

	document.getElementById('section-join').style.display = tab === 'join' ? 'block' : 'none';
	document.getElementById('section-create').style.display = tab === 'create' ? 'block' : 'none';
	document.getElementById('section-import').style.display = tab === 'import' ? 'block' : 'none';
}"""

content = content.replace(old_set_tab, new_set_tab)

with open("js/index.js", "w") as f:
    f.write(content)
