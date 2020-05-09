import requests

#登录微博
log_url = "https://passport.weibo.cn/sso/login"

log_headers = {
"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36",
"Referer":"https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F"
}


form_data = {
"username":"13913043550",
"password":"092483",
"savestate":"1",
"r":"https://m.weibo.cn/",
"ec":"0",
"pagerefer":"https://m.weibo.cn/login?backURL=https%253A%252F%252Fm.weibo.cn%252F",
"entry":"mweibo",
"wentry":"",
"loginfrom":"",
"client_id":"",
"code":"",
"qq":"",
"mainpageflag":"1",
"hff":"",
"hfp":"",
}
res = requests.post(log_url,data = form_data,headers = log_headers)


#保存登录
requestsession = requests.Session()
requestsession.headers.update(log_headers)
Res = requestsession.post(log_url,data = form_data)

if Res.status_code == 200:
    print("登入成功")
else:
    print("登入失败")
    
#发微博

sent_url = "https://m.weibo.cn/api/statuses/update"

sent_headers = {
"mweibo-pwa":"1",
"origin":"https://m.weibo.cn",
"referer":"https://m.weibo.cn/compose/",
"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36"   
}

#获取st
st_url = "https://m.weibo.cn/api/config"
st_headers = {
"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36"
}
st_res = requestsession.get(st_url,headers = st_headers)
st1 = st_res.json()
st = st1["data"]["st"]

sent_data = {
"content":"第二天测试",
"st":st
}

sentcompose = requestsession.post(sent_url,data = sent_data)
print(sentcompose)
# if sentcompose == 200:
#     print("发表成功")
# else:
#     print("发表失败")