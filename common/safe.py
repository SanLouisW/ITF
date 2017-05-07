#coding=utf-8
import hashlib
import json

def md5(str):
  m=hashlib.md5()
  m.update(str)
  psw=m.hexdigest()
  print psw
  return psw

def use_sign(data,k):
  data=json.loads(data)
  if data.has_key('data'):
      data=data['data'][0]
  data.pop('sign')
  new_list=sorted(data.iteritems(),key=lambda d:d[0],reverse=False)
  #print"new_list: ",new_list
  new_data = ''
  for i in new_list:
     temp = i[0]+'='+str(i[1])+'&'
     new_data+= temp
  new_data = new_data.strip('&')
  #new_data=url_encode(new_dict)
  #print'new_data:',new_data
  post_data=new_data+k
  print"post_data: ",post_data
  sign=md5(post_data)
  return sign

if __name__=='__main__':
    pass