import urllib
import urllib.request
import http.cookiejar
import string
import re

hosturl = 'https://os.ncuos.com/api/user/token'
posturl = 'https://os.ncuos.com/api/user/token'

cj = http.cookieljar.CookieJar()
cookie_support = urllib.HTTPCookieProcessor(cj)

opener = urllib.build_opener(cookie_support,urllib.HTTPHandler)
urllib.install_opener(opener)

h = urllib.urlopen(hosturl)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
           'Referer':'https://os.ncuos.com/api/user/token'}

postData = {'op' : 'dmlogin',
            'f' : 'st',
            'user' : '8002118162',
            'pass' : '200617',
            'rmbr' : 'ture',
            'tmp' : '0.0008502006530761719s'
            }

postData = urllib.urllib.urlencode(postData)

request = urllib.Request(posturl,postData,headers)
print(request)
response = urllib.urlopen(request)
text = response.read()
print(text)
