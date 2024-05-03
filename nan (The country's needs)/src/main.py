import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import warnings
import re

warnings.simplefilter("ignore")

 
class get_website:
   def __init__(self):
      
      self.reqs = None
      self.soup = None
      self.data = None
   


   def get_all_url(self):
    links = []
    data = open('/home/alireza/Desktop/index.html','r')
    soup = BeautifulSoup(data, 'html.parser')
    for element in soup.find_all('a'):
        link = element.get('href')
        if isinstance(link, type(None)): 
            continue
        elif "/ViewNeed" in link:
            links.append(link)
    links = (set(links))
    print(f"total number of url {len(links)}")
    return set(links)

   def set_url(self, url):
      self.reqs = requests.get(url)
      self.soup = BeautifulSoup(self.reqs.content, 'html.parser')     
          
   def get_title(self):
      

      title = self.soup.find('p', class_='mb-1')
      title = (title.text)
      title = title.split("\n")
      title = ["".join(element.rstrip()) for element in title]
      title = ["".join(element.lstrip()) for element in title]
      for element in title:
         if (element) == '' or (element) == '\r':
            title.remove(element)
         
      return title[0]

   def get_abstract(self):


      abstract = self.soup.find('p', class_='fs-7 text-secondary text-justify')
      abstract = (abstract.text)
      abstract = abstract.split("\n")
      abstract = ["".join(element.rstrip()) for element in abstract]
      abstract = ["".join(element.lstrip()) for element in abstract]
      for element in abstract:
         if (element) == '' or (element) == '\r':
            abstract.remove(element)
      return abstract[0]

   def clean(self, data):
      for element in data:
         if (element) == '' or (element) == '\r' or (element) == '\n':
            data.remove(element)
      return data

   def set_data(self):     

      self.data = self.soup.find('div', class_= "col-md-3 col-sm-12")
      if isinstance(self.data, type(None)): 
         return False
      else :
         self.data = self.data.text
      self.data = self.data.split("\n")
      self.data = ["".join(element.rstrip()) for element in self.data]
      self.data = ["".join(element.lstrip()) for element in self.data]
      self.data = self.clean(self.data)
      while ("" in self.data):
         self.data = self.clean(self.data) 

   def get_owner(self):
      index_owner = -1
      result = None

      for index in range(0, len(self.data)):
        if "مالک :" in self.data[index]:
            index_owner = index
            break
      if index_owner != -1:
          result = self.data[index_owner].split(" : ")[1]
          result = "".join(result.rstrip()) 
          result = "".join(result.lstrip())
      return result
   
   def get_field(self):
      index_field = -1
      result = None

      for index in range(0, len(self.data)):
        if "حوزه موضوعی :" in self.data[index]:
            index_field = index
            break
      
      if index_field != -1:
          result = self.data[index_field].split(" : ")[1]
          result = "".join(result.rstrip()) 
          result = "".join(result.lstrip())
      return result


   def get_keyword(self):
      index_keyword = -1
      result = None

      for index in range(0, len(self.data)):
        if "کلمات کلیدی : " in self.data[index]:
            index_keyword = index
            break
      if index_keyword != -1:
          result = self.data[index_keyword].split(" : ")[1]
          result = result.split(",")
          result = ["".join(element.rstrip()) for element in result]
          result = ["".join(element.lstrip()) for element in result]

      return result
   def get_country(self):
      index_country = -1
      result = None

      for index in range(0, len(self.data)):
        if "کشور:" in self.data[index]:
            index_country = index
            break
      
      if index_country != -1:
          result = self.data[index_country + 1]
          result = "".join(result.rstrip()) 
          result = "".join(result.lstrip())
      return result

   def get_state(self):
      index_state = -1
      result = None

      for index in range(0, len(self.data)):
        if "استان:" in self.data[index]:
            index_state = index
            break
      
      if index_state != -1:
          result = self.data[index_state + 1]
          result = "".join(result.rstrip()) 
          result = "".join(result.lstrip())
      return result
   
   def get_city(self):
      index_city = -1
      result = None
      for index in range(0, len(self.data)):
        if "شهر:" in self.data[index]:
            index_city = index
            break
      
      if index_city != -1:
          result = self.data[index_city + 1]
          result = "".join(result.rstrip()) 
          result = "".join(result.lstrip())
      return result

   
   def get_target_group(self):
      index_target_group = -1
      result = None
      for index in range(0, len(self.data)):
        if "گروه/های هدف:" in self.data[index]:
            index_target_group = index
            break
      
      if index_target_group != -1:
          result = self.data[index_target_group]
          result = "".join(result.rstrip()) 
          result = "".join(result.lstrip())
      return result

model = get_website()

df = pd.DataFrame({
   "Title" : "",
   "Abstract" : "",
   "Owner" : "",
   "field" : "",
   "Key word" : "",
   "country" : "",
   "State" : "",
   "City" : "",
   "Target group" : "",
   "link of page" : ""
}, index=[0])




file1 = open("/home/alireza/Desktop/alireza/web scraping/links.txt","r")
temp = file1.readlines()
urls = []
temp = list(temp)
for element in temp:
    if "\n" in element:
        urls.append(element[: -1])
     


print(f"all url receved !----------------{len(urls)}")


urls_no_sign = []
urls_copy = urls.copy()
index = 0
counter = 1
for url in urls:

 
   
   try:
      model.set_url(url)
      print(f"{counter} --- {model.get_title()}")
      if(model.set_data() == False):
         print(f"{counter} -----> no have data")
         counter +=1 
         continue
      else:
         temp =  {
               "Title" : model.get_title(),
               "Abstract" : model.get_abstract(),
               "Owner" : model.get_owner(),
               "field" : model.get_field(),
               "Key word" : model.get_keyword(),
               "country" : model.get_country(),
               "State" : model.get_state(),
               "City" : model.get_city(),
               "Target group" : model.get_target_group(),
               "link of page" : url
         }
         df = df.append(temp, ignore_index = True)
         print(f"{counter} -----> success")
         counter += 1
      urls_copy.remove(url)
         

        
   except:
      urls_no_sign.append(url)
      print ("No Connectio")   


print(f"Links that have not been taken {len(urls_copy)}")
df.drop(0 ,axis=0,inplace=True)
df.to_csv("/home/alireza/Desktop/alireza/web scraping/Data_nan.csv") 

