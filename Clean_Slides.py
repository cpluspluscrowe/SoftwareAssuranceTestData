import re
reString = '''(style=".+?")'''
path = r"C:\Users\CCrowe\Documents\Software Assurance\Requirements for SSE.html"


with open(path,"r",encoding='utf-8', errors='ignore') as f:
	content = f.read()
	new_content = re.sub(reString,"",content,flags = re.M)

with open(path,"w",encoding='utf-8',errors='ignore') as f:
	f.write(new_content)
