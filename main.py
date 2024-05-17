import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sqlite3
params={
        'q':'id:5478',
        'categories':111,
        'purity':111,
        'sorting':'date_added',#date_added,favorites
        'order':'desc',
        'ai_art_filter':0,
        'page':2
}
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    "Cookie":'_pk_id.1.01b8=49823d0507245383.1712473608.; cf_clearance=acYRLTmg0lnzn2iOxzCjMgXNfRrNdpQiXRI8XZo2YQ4-1715685069-1.0.1.1-5agiTnGUwNCGl.VscBD3TtBZoLm_xs1Rl_2nRpL4NLfSGcCvKYm9r_zi8X6sywzi0ndaQP9IJ4ExQt9f.QcA.A; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IllkWU9yazNqY25ydmh1cUVPTE9aQVE9PSIsInZhbHVlIjoiVHNpNHJ0ZjNoUGRrUUZ1TDRFaGc4XC8yMlRibHVKWE1iZ2xyaU43M1hkeCsrZzcxTitJUDlLYXlzUVNaMVdJT3hGRW9lMnp3VHJrOFV2bFE1eVJcL1ZBV1g2Vm1RUWZVTmw1eVV5UjU2MkFaWVBLQVd0eG02SlBsVytXM2lpK0J5dXdXYVZcL2lLRVpXeTNLUFJWZlhNN3kwanRFODdiNHYyZlBYSHo0S1M5d3piMHVDWlJqRFZXemZOTVk0Rk1BcmZvIiwibWFjIjoiMjhlZjdiMmE2OWJiY2FmYWIwNWM2M2U1MWVmODE2MGQxNjYyYTk5NDM0N2Y5NTJmMmQ0ZjhlNDc1NDIzZmRmMiJ9; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6Im1hUzdoTGk5U2JIZHBya2hpZE5JY0E9PSIsInZhbHVlIjoib3piVllFREppWUNuS0VGVThJZW9rZ3NhU3RBMENZRVgzUGJXVVFxV1VrYkN6TURyMVlKcFptMVJmbjdiVWFCeCIsIm1hYyI6ImJiZDEzOWEzMjRjNjc3YjcxNjM1NjI2NDc0Nzc0NWNkYzQ4YWVhOTE1ZmMwYjA1OGUwMWMwZjdhMjRhYmNhODAifQ%3D%3D; wallhaven_session=eyJpdiI6ImRLajFIaU9XQUpsOVBETUxuRlZLUVE9PSIsInZhbHVlIjoiVDY4ajFETmJEejBydmV5eWpVSnQxdjZzVXE5ZGduOUR4dFJjSzhTWklZU1Uxb0cxc3ZrQWoxZk5HMUt0MTZGRyIsIm1hYyI6ImQ2OTM4MjE5YTU0NTEzNmY0ZDU5ZDY4YzcwOGU0N2ZkYjdlMzg5YmFlNmY0YTIwNDdlOWJjM2I2MjY2NmM3ODAifQ%3D%3D'
}
a=0
response=requests.get('https://wallhaven.cc/search',headers=header,params=params)
file=open('wallhaven.html','w',encoding="utf-8")
file.write(response.text)
file.close()
soup = BeautifulSoup(open('wallhaven.html','r'),'html.parser')
data=soup.find_all(class_='lazyload')
con=sqlite3.connect("Img.db")
cur=con.cursor()
for i in data:
    img_url=i.get("data-src")
    img_pathinfo=urlparse(img_url)
    img_url=img_url.replace("small","full")
    img_name=img_pathinfo.path[-10:]
    if (cur.execute("SELECT * FROM Img WHERE name=?",(img_name,)).fetchone())!=None:
        a=1
    else:
        a=0
    f_img_name="wallhaven-"+img_name
    img_url=img_url.replace(img_name,f_img_name)
    img_url=img_url.replace("//th","//w")
    if a==0:
        cur.execute("INSERT INTO Img VALUES(?,?)",((cur.execute("select datetime('now')").fetchone())[0],img_name))
        con.commit()
        response_2=requests.get(url=img_url)
    else:
        print("picture "+img_name+" has been downloaded")
        continue
    if response_2.status_code==404:
        img_url=img_url.replace("jpg","png")
        response_2=requests.get(url=img_url)
        f_img_name=f_img_name.replace("jpg","png")
    l_img_name="./img/"+f_img_name
    img_file=open(l_img_name,'wb')
    img_file.write(response_2.content)
    img_file.close()
con.close()  
