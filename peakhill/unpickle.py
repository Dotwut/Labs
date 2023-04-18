import pickle

output = pickle.load(open('/home/jason/TryHackMe/peakhill/download.dat', 'rb'))

pass_str = ''
user_str = ''
password_list = []
username_list = []

for i,x in output:
	if 'ssh_pass' in i:
		i = int(i[8::])
		password_list.append((i,x))

	else:
		i = int(i[8::])
		username_list.append((i,x))

password_list.sort()
for i, x in password_list:
	pass_str += x

username_list.sort()
for i, x in username_list:
	user_str += x

print('Username: ' + user_str)
print('Password: ' + pass_str)