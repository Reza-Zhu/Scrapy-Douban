def get_cookie():
    cookies = 'll="118172"; bid=RL-Ud9-M8Is; __utmc=30149280; __utmc=223695111; __yadk_uid=1zmMhETBDMVis3yMbUOGhNAuDNXvCMfO; _vwo_uuid_v2=D028E2287D9969D2E76DEC3EB4593E4C6|6481f784be57b1e49c6e37458118f7ae; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18489; douban-profile-remind=1; dbcl2="184896369:3JzWAGgS7TY"; ck=76wX; __utmz=30149280.1555124605.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1555125272.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1555141460%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fcat%3D1002%26q%3D%25E9%259C%25B8%25E7%258E%258B%22%5D; _pk_id.100001.4cf6=48856d09d3a72324.1555117412.4.1555141460.1555138770.; __utma=30149280.1020408546.1555117224.1555138758.1555141460.5; __utma=223695111.690157687.1555117412.1555138758.1555141460.4'
    return stringToDict(cookies)





def stringToDict(cookies):
    '''
    将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
    :return:
    '''
    itemDict = {}
    items = cookies.split(';')
    for item in items:
        arr=item.split('=')
        key = arr[0].replace(' ', '')
        value = arr[1]
        itemDict[key] = value
    return itemDict


if __name__ == "__main__":
    print(get_cookie())