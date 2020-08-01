import requests
import html5lib
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

file = '/Users/jeeva/Desktop/ebay/Ebay.csv'      #location and name of ur input file
ebaylist= pd.read_csv(file)

import pandas as pd
df = pd.DataFrame({'price':[],                                          # price of the product
                   'rating':[],                                         # Ratings of the product
                   'unit_price':[],                                     # Unit Price of the product
                   'status':[],                                         # Status New/refurbished? etc
                   'title':[],                                          # Title of the product
                   'object_loc':[],                                     # Object Location
                   'ship_loc':[]})                                      # Shipping Location

# put the number in range based on the number of Ebay urls 
for x in tqdm(range(50)):
   url = ebaylist.iat[x,0]
   r = requests.get(url) 
   
   soup = BeautifulSoup(r.content, 'lxml') 
   

   price = soup.find(id="prcIsum")
   rating = soup.find(id='si-fb')
   unit_price = soup.find(id='itmUnitPrice')
   status = soup.find(id='vi-itm-cond')
   title = soup.find(id='itemTitle')

   object_loc = soup.find(itemprop = 'availableAtOrFrom')

   if object_loc is not None:
      object_text = object_loc.get_text()
   else:
      object_text = ''
   ship_loc = soup.find(id='vi-acc-shpsToLbl-cnt')

   if price is not None:
      price1 = price.get_text()
   else:
      price1 = ''
   
   if rating is not None:
      rating1 = rating.get_text()
   else:
      rating1 = ''

   if status is not None:
      status1 = status.get_text()
   else:
      status1 = ''

   if title is not None:
      title1 = title.get_text()
   else:
      title1 = ''

   if ship_loc is not None:
      ship_loc1 = ship_loc.text.strip()
   else:
      ship_loc1 = ''
      
   data = [{'price':price1,'rating':rating1,'unit_price': unit_price,'status':status1,'title': title1,'object_loc': object_text,'ship_loc': ship_loc1}]
   df=df.append(data ,ignore_index=False,sort=False)

   '''
   print(price.text.strip())
   print(rating.text.strip())
   print(unit_price)
   print(status.text.strip())
   print(title.text.strip())
   print(object_loc)
   print(ship_loc.text.strip()) 
   '''


#print(df)     
# use the above to check ur output in terminal
save_path = "ebay_df.csv"     # the location and name of ur output file
df.to_csv (save_path, index = False, header=True)
