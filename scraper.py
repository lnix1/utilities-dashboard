#--------------------------------------------------------------------#
# Trying a headleass browser approach instead. For linux, this 
# required downloading chromium and placing the the chrome driver
# in /usr/bin
# Basically follow the 'For Linux' comment here:
# https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome
#
# Selenium documentation could also be useful:
# https://selenium-python.readthedocs.io/locating-elements.html
#--------------------------------------------------------------------#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd
from bs4 import BeautifulSoup
import re

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# Open the pop-out window and prompt user to login and navigate to the correct order page
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://primenow.amazon.com/home")

# Extract the entire html for the page (ideally, this would be initiated by the user when they have 
# arrived at the correct order page)
order_page_html = driver.page_source

# Finish the browsing session
driver.quit()

# Create the function for extracthing the order table from a given order page selected by the user
def OrderTableExtractor(html_source):
   order_soup = BeautifulSoup(order_page_html)
   # Grab the table on the right of the page with the items ordered
   order_container = order_soup.find('div', class_ = 'a-column a-span5 a-span-last')
   # Break the order table out by the individual items, placing the the html for each as an item in a list
   order_containers = order_container.find_all('div', class_ = 'a-box-inner')
   # Initialize a table to fill with the order information
   order_data_columns = ['item_name', 'qty/wgt', 'by_unit_wgt', 'unit_price', 'item_url']
   order_data_frame = pd.DataFrame(columns=order_data_columns)
   # Iterate over the order items and extract the desired information, placing it into a table
   for o in order_containers[1:len(order_containers)]:
      # Grab and format the order url 
      item_url_end = o.find('a').get('href')
      amazon_url_base = 'https://www.amazon.com'
      item_url = amazon_url_base + item_url_end
      # Grab the item name and reformat
      item_name = o.find('span').text.strip('\n').strip()
      # Extract all of the text from the grocery item cell
      e = o.find_all('span')
      # We can use the contents of the second <span> container to determine whether we are dealing with 'by unit' or 'by weight' items
      # 'by unit' items will contain 'Qty' while 'by weight' items will contain 'per pound'
      # The first two possible cases (for items priced by count w/ or w/o replacement) are treated the same
      if 'Qty' in e[1].text:
         # Extract the quantity and unit price
         qnty_wgt_unit_price = e[1].text.split()
         # Append both of the features to the relevant vectors
         qty_wgt = qnty_wgt_unit_price[1]
         unit_price = qnty_wgt_unit_price[2]
         # Append a label specifying that this item was priced by unit
         by_unit_wgt = 'by unit'
      # The second two possible cases (for items bought by weight w/ or w/o replacement) are treated the same
      else:
         # Extract and append per_unit price
         unit_price = re.sub('[a-z]', '', e[1].text.strip('\n').strip()).strip()
         # Extract and append weight
         qty_wgt = re.sub('[a-z]', '', e[6].text.strip('\n').strip()).strip()
         # Append a label specifying that this item was priced by weight
         by_unit_wgt = 'by weight' + ' (' + re.sub(r'\d+', '', e[1].text.strip('\n').strip()).strip('$').strip('.').strip() + ')'
      new_order_row = pd.DataFrame({'item_name':[item_name], 'qty/wgt': [qty_wgt], 'by_unit_wgt': [by_unit_wgt], 'unit_price': [unit_price], 'item_url': [item_url]})
      order_data_frame = order_data_frame.append(new_order_row, ignore_index=True)
   return order_data_frame;

# Call the function to test and extract a table for the Mar. 5th grocery order
order_data_frame2 = OrderTableExtractor(order_page_html)

# Write out the table into a csv. I initially tested this for March 5th grocery order
order_data_frame2.to_csv(r'groceries_mar_5_2020.csv', index = False, header=True)
#--------------------------------------------------------------------#