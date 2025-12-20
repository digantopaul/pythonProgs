import urllib.request


link="https://tools.gss.akamai.com/monitor/certs/history/allcerts.csv"

f = urllib.request.urlopen(link)

myfile = f.read()
print(myfile)