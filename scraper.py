#---------------------------------------------------------------------#
# Old code I no longer need that could be useful in pulling down
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

html = response.read()

# From here, I need to pull the captcha image from html, and them submit a 'get' request to '/errors/validateCaptcha'

# This doesn't quite do the job on getting the hidden values. the value for amzn-r is wrong.
# the last one appended called 'field-keywords' should be the captcha entry form to enter letters pulled from image
import lxml.html
def form_parsing(html):
   tree = lxml.html.fromstring(html)
   data = {}
   for e in tree.cssselect('form input'):
      if e.get('name'):
         data[e.get('name')] = e.get('value')
   return data

# Pull the input forms (though again, the second value for 'amzn-r' in the dict is wrong)
captcha_input_data = form_parsing(html)

# initialize new set of login data
login_data_captcha = {'action': 'sign-in',
                      'email': amazon_username,
                      'password': amazon_password,
                        }

# Update new dictionary with captcha input values
login_data_captcha.update(captcha_input_data)

# Pull image link from 'html' object to view. (if this function works properly, it should be probably be integrated in form_parsing to improve process efficiency)
def image_retrieval(html):
   tree = lxml.html.fromstring(html)
   for e in tree.cssselect('form img'):
      if e.get('src'):
         img = e.get('src')
   return img

captcha_image = image_retrieval(html)

# Update captcha login dict with a user input from viewing the captcha image and encode for use in the opener
captcha__user_input = input()
login_data_captcha.update({'field-keywords': captcha__user_input})

# I quite literally copy and pasted this value out of the html form since it wasn't scraped properly before
login_data_captcha.update({'amzn-r': '&#047;'})


login_captcha_encoded = urllib.parse.urlencode(login_data_captcha).encode('utf-8')

# Submit (i believe a 'get') request to amazon with new captcha login dict. Needs to go to the url: https://www.amazon.com//errors/validateCaptcha
# At present, this section did not return the intended response. Still stuck at captcha
response_captcha = opener.open('https://www.amazon.com//errors/validateCaptcha', login_captcha_encoded)
response_captcha_html = response_captcha.read()











#--------------------------------------------------------------------#
