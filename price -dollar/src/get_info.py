import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import warnings
import re
from persiantools.jdatetime import JalaliDate
import datetime


class Get_info():
	def __init__(self, url = "https://www.tgju.org/"):
		self.url = url
		self.df = pd.DataFrame({
			"بورس" : None,
			"انس طلا" : None,
			"مثقال طلا" : None,
			"طلا ۱۸" : None,
			"سکه" : None,
			"دلار" : None,
			"نفت برنت" : None,
			"تتر" : None,
			"بیت کوین" : None
			}, index=[0])

	def _update_time(self):
		self.hours = time.strftime("%H,%M,%S").replace(",", ":")
		self.date = str(JalaliDate.today())


	def _clean_text(self, temp_string):
		temp_string =  temp_string.lstrip()
		temp_string =  temp_string.rstrip()
		return temp_string

	def get_price(self):
		self._update_time()
		print(f"---- and we are get informations this time : {self.date} --- {self.hours}")
		print("-" * 30)

		reqs = requests.get(self.url)
		soup = BeautifulSoup(reqs.content, 'html.parser')  

		price_list = soup.find('ul', class_='info-bar mobile-hide')
		price_list = price_list.text
		price_list = price_list.split("\n")
		price_list = list(map(self._clean_text, price_list))
		price_list = [element for element in price_list if not (element == "" or  element == ")" or "%" in element)]

		temp = pd.DataFrame({
					"بورس" : price_list[price_list.index("بورس") + 1],
					"انس طلا" : price_list[price_list.index("انس طلا") + 1],
					"مثقال طلا" : price_list[price_list.index("مثقال طلا") + 1],
					"طلا ۱۸" : price_list[price_list.index("طلا ۱۸") + 1],
					"سکه" : price_list[price_list.index("سکه") + 1],
					"دلار" : price_list[price_list.index("دلار") + 1],
					"نفت برنت" : price_list[price_list.index("نفت برنت") + 1],
					"تتر" : price_list[price_list.index("تتر") + 1],
					"بیت کوین" : price_list[price_list.index("بیت کوین") + 1],
					"تاریخ" : self.date,
					"ساعت - دقیقه - ثانیه" : self.hours
					},index=[0])
		self.df = self.df._append(temp, ignore_index = True)
		self.df = self.df.dropna()
		self.df.to_csv("price.csv")

		print("FINISHED get informations")
		print("-" * 30)

      	

		

