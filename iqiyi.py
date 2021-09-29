import requests

# server酱开关，填0不开启(默认)，填1只开启cookie失效通知，填2同时开启cookie失效通知和签到成功通知
server = ''
# 填写酷Q sckey,不开启酷Q则不用填
sckey = ''
# 抓包  psp_cki 替换到下面三个链接即可
# 填入爱奇艺签到页面url
#url = 'https://tc.vip.iqiyi.com/taskCenter/task/queryUserTask?deviceId=8C3790737125815A460F947EB9EC2839&appname=memberTask&messageId=memberTask_kIcToWFjPeDqlUwSrH6evGcycL8bDClB&version=2.0&invokeType=outer_http&lang=zh_cn&P00001=替换到这里&belong=GOLD_TASK&autoSign=yes&platform=bb136ff4276771f3&fv=8810d5688ee1a7a6&appVersion=11.6.5'
# 填入爱奇艺摇一摇次数查询url
#url1 = 'https://iface2.iqiyi.com/aggregate/3.0/lottery_activity?&lottery_chance=1&app_k=456ddd1ff52a6089c7e3f806d609520d&app_v=11.6.5&app_gv=&app_t=0&platform_id=10&dev_os=10&dev_ua=Redmi+K20+Pro&net_sts=1&qyid=dfc51460c2551c7df8702b70324828b11104&psp_uid=000000&&psp_cki=替换到这里&psp_status=1&secure_v=1&secure_p=GPhone&cupid_v=3.47.008&core=1&req_sn=1595627019676'
# 填入爱奇艺摇一摇页面url
#url2 = 'https://iface2.iqiyi.com/aggregate/3.0/lottery_activity?&lottery_num=1&&app_k=456ddd1ff52a6089c7e3f806d609520d&app_v=11.6.5&app_gv=&app_t=0&platform_id=10&dev_os=10&dev_ua=Redmi+K20+Pro&net_sts=1&qyid=dfc51460c2551c7df8702b70324828b11104&psp_uid=000000&&psp_cki=替换到这里&psp_status=1&secure_v=1&secure_p=GPhone&cupid_v=3.47.008&core=1&req_sn=1595627019676'
def start():
    try:
        res = requests.get(url).json()['data']['signInfo']
        a=res['msg']+',获得成长值:'+str(res['data']['todayGrowth'])
        print(a)
        re = requests.get(url1)
        b=re.json()['daysurpluschance']
        print('剩余抽奖次数:',b)
        d = '  \n'
        if b != '0':
            for _ in range(int(b)):
                r = requests.get(url2).json()
                c=r['title']+','+r['awardName']
                d=d+c+'  \n'
                print(c)
        if server == '2':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + a +'剩余抽奖次数'+ b + d)
    except:
        print('error')
        if server != '0':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text=爱奇艺签到/抽奖url失效请更新')

def main_handler(event, context):
    return start()

if __name__ == '__main__':
    start()
