#coding=utf-8
'''
Created on 2015年3月23日

@author: houcp
'''
import random

#测试环境：test   预发布环境：pre
env = 'test'

'''
测试环境
'''
if env == 'test':
    #测试数据库配置
    DBHOST = "10.17.2.114"
    DBPORT = 3306
    DBUSER = "root"
    DBPASSWORD = "Root@123"
    DBSCHEMA = "test"
    #请求服务器地址
    host = '10.17.2.125:8098'


'''
预发布环境
'''
if env == 'pre':
    #预发布数据库配置
    DBHOST = "120.25.251.26"
    DBPORT = 3306
    DBUSER = "root"
    DBPASSWORD = "prexn2015"
    DBSCHEMA = "test"

    host = 'mappx.xiaoniuapp.com'
    #host = '120.25.157.47:8081'


http_addr = 'http://'+host


data_file_path = "E:\\workspace\\ITF\\data\\api_test_demo.xls"
#data_file_path = "E:\\workspace\\ITF\\data\\api_test_demo.xls"

key_10005='&key=niuDaiTest'


#aes加密key
key="U6!LZyPfl0#uF4z1"



#邮件信息设置

# authInfo = {'server':'smtp.163.com',
#             'user':'hcpyou@163.com',
#             'password':'zxmhcp163',
#             }
# #发件人
# fromAdd = 'hcpyou@163.com'
# #收件人,多个人之间用逗号（,）隔开
# toAdd = "houchunpeng@xiaoniu66.com"
# #抄送人,多个人之间用逗号（,）隔开
# ccAdd = "hcpyou@163.com"
# #邮件主题
# subject = u'Ams测试报告'
# ##邮件内容
# plainText = '这里是普通文本\n'
# #邮件内容为html格式
# htmlText = '<B>HTML文本</B>'


authInfo = {'server':'smtp.xiaoniu66.com',
            'user':'houchunpeng@xiaoniu66.com',
            'password':'zxmhcp163',
            }
#发件人
fromAdd = 'houchunpeng@xiaoniu66.com'
#收件人,多个人之间用逗号（,）隔开
#toAdd = "houchunpeng@xiaoniu66.com,oumingzhu@xiaoniu66.com"
toAdd = "houchunpeng@xiaoniu66.com"
#抄送人,多个人之间用逗号（,）隔开
ccAdd = "hcpyou@163.com"
#邮件主题
subject = u'Ams测试报告'
##邮件内容
plainText = '这里是普通文本\n'
#邮件内容为html格式
htmlText = '<B>HTML文本</B>'



'''
报告内容
'''
if env == 'pre':
    test_environment='120.25.157.47(预发布环境)'
if env == 'test':
    test_environment='10.10.16.151(测试环境)'

test_range='''
1)注册
2)登录
3)获取是否提醒状态
4)红包&体验金&好友发钱标识
5)查询用户信息
6)查询用户等级信息
7)登出
8)产品详情查询
9)产品购买流程
10)首页产品列表
11)用户投资记录查询
12)产品购买记录
13)活期宝收益统计
14)产品列表查询
15)我的账户
16)总资产信息
17)投资累计收益列表
18)今日预期收益列表
19)定期投资收益（总计待回款金额，累计收益|投资本金）
20)总资产明细
21)活期宝按照金额赎回
22)活期宝可赎回余额查询
23)活期宝按金额赎回对应资金情况
24)活期宝赎回记录查询
25)活期宝按笔赎回
26)活期宝可赎回投资记录列表接口
27)计算用户单笔投资金额可分享红包数
28)微信好友访问分享红包页面时分配红包
29)领取红包
30)好友分享红包领取记录
31)修改领取分享红包微信好友关联手机号
32)获取微信用户领取好友分享红包最新手机号
33)理财师等级信息查询
34)好友投资好友推荐佣金统计
35)获取本日_本月_累计佣金
36)获取客户明细--->head部分
37)统计好友注册，绑卡，投资数
38)统计pro版累计赏金客户投资信息
39)客户列表查询(low,pro)
40)查询客户投资明细(pro)
41)佣金明细->累计赏金页面(low,pro)
42)朋友接口
43)获取理财师业务员信息
44)获取理财师佣金等级信息
45)佣金明细查询(low,pro)-->我的佣金页
46)查看通讯录好友列表
47)获取产品购买记录Top3
48)往期募集中产品列表查询
'''
# test_range='''
# 活期宝产品购买
# '''












if __name__ == "__main__":
    pass
