#---------------------------------------------------------------------#
# Old code I no longer need that could be usefule in pulling down
# and scrapping the page I need.
#---------------------------------------------------------------------#
from bs4 import BeautifulSoup

# get login page
resp = session.get(site)
html = resp.text

# get BeautifulSoup object of the html of the login page
soup = BeautifulSoup(html , 'lxml')

# submit post request with username / password and other needed info
post_resp = session.post(site, data = data)

post_soup = BeautifulSoup(post_resp.content , 'lxml')
#---------------------------------------------------------------------#



#---------------------------------------------------------------------#
# New code that works in logging into the site
# look at the documentation for urllib.requests moving foward, particularly the .open method attached to build_opener
#---------------------------------------------------------------------#
import http.cookiejar
import urllib
import urllib2

amazon_username = 'louis.nix2@gmail.com'
amazon_password = 'Hutchinson3!'

login_data = urllib.parse.urlencode({'action': 'sign-in',
                               'email': amazon_username,
                               'password': amazon_password,
                               }).encode('utf-8')

cookie = http.cookiejar.CookieJar()    
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36')]

response = opener.open('https://www.amazon.com/gp/sign-in.html')
print(response.getcode())

response = opener.open('https://www.amazon.com/gp/flex/sign-in/select.html', login_data)
print(response.getcode())

response = opener.open("https://www.amazon.com/") # it should show that you are logged in
print(response.getcode())
#--------------------------------------------------------------------#
