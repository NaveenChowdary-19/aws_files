import requests
#r=requests.get("https://xkcd.com/353/")
#r=requests.get("https://imgs.xkcd.com/comics/python.png")
#print(dir(requests))
'''with open('comics.png','wb') as f:
    f.write(r.content)
    
print(r.headers)'''
'''
r=requests.get("https://httpbin.org/get?page=2&count=25")
print(r.text)
'''
'''
payload={"page":2,"count":25}
r=requests.get("https://httpbin.org/get",params=payload)
#print(r.text)
print(r.url)
'''

'''payload={'username':'Naaveen','Pswd':'Nav19'}
r=requests.post("https://httpbin.org/post",data=payload)
print(r.text)
'''

'''payload={'username':'Naaveen','Pswd':'Nav19'}
r=requests.post("https://httpbin.org/post",data=payload)
print(r.json())
'''



payload={'username':'Naaveen','Pswd':'Nav19'}
r=requests.post("https://httpbin.org/post",data=payload)
r_dict=r.json()
print(r_dict['form'])




            
