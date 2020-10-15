import requests
import random
url = "https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=21581199&t=1521463484600&starttime=2018%2F3%2F19%2020%3A44%3A30&rn=990598061.78751211" #问卷地址
data = {
 "submitdata" : "1$%s}2$%s}3$%s}4$%s}5$%s}6$%s}7$%s}8$%s}9$%s}10$%s"
}
header = {
 "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
 "Cookie": ".ASPXANONYMOUS=iBuvxgz20wEkAAAAZGY4MDE1MjctNWU4Ni00MDUwLTgwYjQtMjFhMmZhMDE2MTA3h_bb3gNw4XRPsyh-qPh4XW1mfJ41; spiderregkey=baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a71; UM_distinctid=1623e28d4df22d-08d0140291e4d5-102c1709-100200-1623e28d4e1141; _umdata=535523100CBE37C329C8A3EEEEE289B573446F594297CC3BB3C355F09187F5ADCC492EBB07A9CC65CD43AD3E795C914CD57017EE3799E92F0E2762C963EF0912; WjxUser=UserName=17750277425&Type=1; LastCheckUpdateDate=1; LastCheckDesign=1; DeleteQCookie=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1521461468568; jac21581199=78751211; CNZZDATA4478442=cnzz_eid%3D878068609-1521456533-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1521461319; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1521461287,1521463471; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1521463471",
 "X-Forwarded-For" : "%s"
}
for i in range(0,500):
 choice = (
 random.randint(1, 2),
 random.randint(1, 4),
 random.randint(1, 3),
 random.randint(1, 4),
 random.randint(1, 3),
 random.randint(1, 3),
 random.randint(1, 3),
 random.randint(1, 3),
 random.randint(1, 3),
 random.randint(1, 3),
 )
 data["submitdata"] = data["submitdata"] % choice
 header["X-Forwarded-For"] = (str(random.randint(1,255))+".")+(str(random.randint(1,255))+".")+(str(random.randint(1,255))+".")+str(random.randint(1,255))
 r = requests.post(url = url,headers=header,data=data)
 print(header["X-Forwarded-For"],r.text)
 data["submitdata"] = "1$%s}2$%s}3$%s}4$%s}5$%s}6$%s}7$%s}8$%s}9$%s}10$%s"
 header["X-Forwarded-For"] = "%s"