#coding=utf8

import MySQLdb
from DBUtils.PooledDB import PooledDB
from conf import config
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')  

g_dbpool = PooledDB(creator=MySQLdb, mincached=2, maxcached=40, host=config.DBHOST, port=config.DBPORT,\
    user=config.DBUSER, passwd=config.DBPASSWORD, db=config.DBSCHEMA,charset="utf8")


def query(sql):
    conn = g_dbpool.connection()
    cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def execute(sql):
    conn = g_dbpool.connection()
    cur = conn.cursor()
    count = cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

    return count


if __name__ == '__main__':

    # sql = "SELECT i.profit_calc_date,i.refund_date from p2p_product_new.t_invest_record i where user_id ='e196ec2e-6d2a-4db0-bef1-63c44722f4ca'and fid = 'b9e7da50-407a-48d9-af87-6bd85c06cfed' ;"
    # profit_calc_date = str(query(sql)[0]['profit_calc_date'])
    # refund_date = str(query(sql)[0]['refund_date'])
    #
    # from common import timeutil
    # profit_start_time = timeutil.profit_start_time()
    # print profit_calc_date,profit_start_time
    # print profit_calc_date==profit_start_time

    #sql = "SELECT amount,status,redeem_type from p2p_product_new.t_current_redeem_request where user_id ='e196ec2e-6d2a-4db0-bef1-63c44722f4ca' ORDER BY request_time desc;"
    sql = "SELECT * FROM  payment.t_provider_payment where partner_trade_no ='20160006';"
    result = query(sql)
    print result



