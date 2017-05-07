#coding:utf-8
import dbutil
from logutil import print_log,print_step

def payment(partner_trade_no):
    print_step('t_provider_payment表查询')
    sql = '''SELECT * FROM  payment.t_provider_payment where partner_trade_no ='%s';''' %(partner_trade_no)
    print_log(sql)
    result=dbutil.query(sql)
    if len(result)!= 0:
        provider_paymentstatus=result[0]["status"]
    else:
        print_log('查询不到数据')
        provider_paymentstatus=''
    print_step('t_payment表查询')
    sql2= '''SELECT * FROM  payment.t_payment where partner_trade_no ='%s';''' %(partner_trade_no)
    print_log(sql2)
    result2 = dbutil.query(sql2)
    if result2 !=():
        paymentstatus = result2[0]["payment_status"]
    else:
        print_log('查询不到数据')
        provider_paymentstatus=''
    print  provider_paymentstatus, paymentstatus
    return   provider_paymentstatus,paymentstatus


def settle(partner_trade_no):
    print_step('t_payment_settlement表查询')
    sql = '''SELECT * FROM  payment.t_payment_settlement where partner_trade_no ='%s';''' %(partner_trade_no)
    print_log(sql)
    result=dbutil.query(sql)
    if result!= ():
        settlementstatus=result[0]["settlement_status"]
    else:
        print_log('查询不到数据')
        settlementstatus=''
    print  settlementstatus
    return settlementstatus


if __name__=='__main__':
    payment('20160928233225')
    settle('2016000000307488')