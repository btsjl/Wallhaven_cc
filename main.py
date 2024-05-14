import requests
from bs4 import BeautifulSoup
import os
params={
        'q':'id:5478',
        'categories':111,
        'purity':111,
        'sorting':'date_added',
        'order':'desc',
        'ai_art_filter':0,
        'page':2
}
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    "Cookie":'_pk_id.1.01b8=49823d0507245383.1712473608.; cf_clearance=acYRLTmg0lnzn2iOxzCjMgXNfRrNdpQiXRI8XZo2YQ4-1715685069-1.0.1.1-5agiTnGUwNCGl.VscBD3TtBZoLm_xs1Rl_2nRpL4NLfSGcCvKYm9r_zi8X6sywzi0ndaQP9IJ4ExQt9f.QcA.A; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IllkWU9yazNqY25ydmh1cUVPTE9aQVE9PSIsInZhbHVlIjoiVHNpNHJ0ZjNoUGRrUUZ1TDRFaGc4XC8yMlRibHVKWE1iZ2xyaU43M1hkeCsrZzcxTitJUDlLYXlzUVNaMVdJT3hGRW9lMnp3VHJrOFV2bFE1eVJcL1ZBV1g2Vm1RUWZVTmw1eVV5UjU2MkFaWVBLQVd0eG02SlBsVytXM2lpK0J5dXdXYVZcL2lLRVpXeTNLUFJWZlhNN3kwanRFODdiNHYyZlBYSHo0S1M5d3piMHVDWlJqRFZXemZOTVk0Rk1BcmZvIiwibWFjIjoiMjhlZjdiMmE2OWJiY2FmYWIwNWM2M2U1MWVmODE2MGQxNjYyYTk5NDM0N2Y5NTJmMmQ0ZjhlNDc1NDIzZmRmMiJ9; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6Im1hUzdoTGk5U2JIZHBya2hpZE5JY0E9PSIsInZhbHVlIjoib3piVllFREppWUNuS0VGVThJZW9rZ3NhU3RBMENZRVgzUGJXVVFxV1VrYkN6TURyMVlKcFptMVJmbjdiVWFCeCIsIm1hYyI6ImJiZDEzOWEzMjRjNjc3YjcxNjM1NjI2NDc0Nzc0NWNkYzQ4YWVhOTE1ZmMwYjA1OGUwMWMwZjdhMjRhYmNhODAifQ%3D%3D; wallhaven_session=eyJpdiI6ImRLajFIaU9XQUpsOVBETUxuRlZLUVE9PSIsInZhbHVlIjoiVDY4ajFETmJEejBydmV5eWpVSnQxdjZzVXE5ZGduOUR4dFJjSzhTWklZU1Uxb0cxc3ZrQWoxZk5HMUt0MTZGRyIsIm1hYyI6ImQ2OTM4MjE5YTU0NTEzNmY0ZDU5ZDY4YzcwOGU0N2ZkYjdlMzg5YmFlNmY0YTIwNDdlOWJjM2I2MjY2NmM3ODAifQ%3D%3D'
}
response=requests.get('https://wallhaven.cc/search',headers=header,params=params)
file=open('wallhaven.html','w',encoding="utf-8")
file.write(response.text)
file.close()
soup = BeautifulSoup(open('wallhaven.html','r'),'html.parser')
data=soup.find_all(class_='lazyload')
for i in data:
    soup2 = BeautifulSoup(str(i),'html.parser')
    img=soup2.img['src']
    print(img)