import urllib.request

# response = urllib.request.urlopen('https://www.zhihu.com/')
# html = response.read()
#
# with open('zhihu.html', 'wb') as f:
#     f.write(html)

req = urllib.request.Request('https://www.zhihu.com/')
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page)
with open('the_page', 'wb') as f:
    f.write(the_page)