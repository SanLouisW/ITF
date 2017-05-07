#coding=utf-8


import random
import string
from Crypto.Cipher import AES
import base64
from conf import config


#生成手机号码
def mobile():
    char_list1 = ["1","2","3","4","5","6","7","8","9","0"]
    #char_list2 = ["2","4","6","1","9"]
    char_list2 = ["3","5","8"]
    str1 = string.join(random.sample(char_list2, 1)).replace(' ','')
    str2 = string.join(random.sample(char_list1, 9)).replace(' ','')
    return "1" + str1 +str2

#生成微信UnionId
def gen_peopleUnionId():
    char_list1 = ["1","2","3","4","5","6","7","8","9","0",'a','b','c','d','e','f','g','h','i','j'
                  'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
                  'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
                  'Y','Z','_'
                  ]

    str1 = string.join(random.sample(char_list1, 16)).replace(' ','')

    return str1



#aes加密算法
def aes_encrypt(key,text):
    obj = AES.new(key, AES.MODE_ECB)

    length = 16
    count = len(text)
    add = length - (count % length)
    text = (text + ('' * add)).encode('utf-8')
    msg = obj.encrypt(text)
    msg = base64.b64encode(msg)
    return msg

#aes解密算法
def aes_decrypt(key,text):
    obj = AES.new(key, AES.MODE_ECB)
    text = base64.b64decode(text)
    msg = obj.decrypt(text)
    return msg



def X_Form_Id(t, mobile):
    text = '''{"mobile":"%s","t":"%s"}'''%(str(mobile), (t))
    msg = aes_encrypt(config.key, text)
    return msg



if __name__=='__main__':
    #print mobile()


    key  = "U6!LZyPfl0#uF4z1"
    text = 'uw5W1k7GZYE/k6z2Jp/cwMkDBQqn8wbz9mygUd68jetdMXvDnlwxa66C31M5tCqn'
    # X_Form_Id = '''{"mobile":"15112517947","t":"1458900232459"}'''
    # print len(X_Form_Id)
    #
    # print aes_encrypt(key, X_Form_Id)
    print aes_decrypt(key, text)
    # print gen_peopleUnionId()