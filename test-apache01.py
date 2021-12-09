from bs4 import BeautifulSoup
import requests
import sys,json,csv

#--------------------------------------------------------------------------------------
def ipinfo(ip):
    if(ip=="127.0.0.1"):
        print("localhost 127.0.0.1")
        return 0

    ret_data = requests.get(f"http://ip-api.com/json/{ip}")
    result = ret_data.text
    data = json.loads(result)
    if(data["status"]=="fail"):
        print(data["message"])
        return 0
    
    ipstat = checkip(ip)
    if(ipstat!="error"):
        parseipjson(data)

    else:
        ipfile = open("ip.save","a")
        ipfile.write(f"{ip}>{data}\n")
        ipfile.close()
        

#--------------------------------------------------------------------------------------
       

def parseipjson(data):
    try:
        ip = data["query"];country = data["country"];countrycode = data["countryCode"]
        region = data["region"];regionname = data["regionName"];city = data["city"]
        zip = data["zip"];timezone = data["timezone"];isp = data["isp"]
        asn = data["as"];lat = data["lat"];lon = data["lon"]
        print(f"IP : {ip}\tISP : {isp}\tASN : {asn}\tLocation : {country}({countrycode})\nRegion : ({region})({regionname})({zip})({lat})({lon})")
    except:
        pass
        return 0

#--------------------------------------------------------------------------------------


def checkip(ip):
    savedline = "error"
    ipfile = open("ip.save","r")
    for line in ipfile:
        ipline = ipfile.readline()
        if(ip==ipline.split('>')[0]):
            ipfile.close()
            print(f"ip exists in file {ipline.split('>')[0]}")
            savedline = ipline
            print(f"printing {savedline}")
            return savedline
        else:

            ipfile.close()
            print(f" inside else - printing {savedline}")
            return savedline 
#--------------------------------------------------------------------------------------


host = input("Enter Site w/ cctld, w/o www : ")
url = f"http://www.{host}/server-status/"

filename = "ip.save"
file = open(filename,"a")
file.close()

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html,'html.parser') 

#title = str(soup.find_all('h1')[0]).replace('<h1>',"").replace('</h1>',"")
#file = open(filename,"a")
#file.write(f"{title}\n")
#file.close()

api_req_count = 0
count = 0
client_ip = "<><><>"
vhost = "<><><>"
request = "<><><>"


for i in range(8,(len(soup.find_all('tr')))-17):
    count = count + 1
    html1 = f"{soup.find_all('tr')[i]}"
    line = BeautifulSoup(html1,'html.parser')
    countxx = 0
    for j in range(0,len(line.find_all('td'))):
        countxx = countxx + 1
        if (countxx == 12):
            client_ip = str(line.find_all('td')[j]).replace('</td>',"").replace('<td>',"")
        if (countxx == 14):
            vhost = str(line.find_all('td')[j]).replace('<td nowrap=\"\">',"").replace('</td>',"")
        if (countxx == 15):
            request = str(line.find_all('td')[j]).replace('<td nowrap=\"\">',"").replace('</td>',"").replace('HEAD',"")
            rel_url = request.replace('GET',"").replace('HTTP/1.1',"").replace(' ',"").replace('POST',"")
            method = request[0:4].replace(' ',"")

    print(f"{count}) Client:{client_ip}\tVHost:{vhost}\tMethod:{method}\nRequested URL: http://www.{host}{rel_url}")
    
    ipstat = checkip(client_ip)
    if(ipstat=="error"):
        ipinfo(client_ip)

    else:
        savedjson = json.dumps(ipstat.split('>')[1])
        print("printing from saved file")
        parseipjson(savedjson)
        

