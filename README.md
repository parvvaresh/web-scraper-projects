# web scraper and data analyze 


## web scraper
There is an Iani site called Nan, which contains all the needs of the country.

address this website: 

[![nan web site](https://nan.ac/Template/assets/images/nan-f-01.png)](https://nan.ac/)

First, scroll the page with the Selenium package until it reaches the end and download the HTML file (the size of the file is almost one gigabyte).

Then with the package *BeautifulSoup* extract all the links from the HTML file and save it in a text file named link.txt

Then we started extracting information from each link in the main.py file and after finishing, we saved it as a csv file

--------------------------------------------------------------------------------------------------------------------------------------
## data analyze 

Notebook is also availble on google colab. --> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DE_UIYWdnKAk56DPfZGd1AK7APCgrGsL?usp=sharing)


Now, using the Pandas package, diagrams about :
1. key words
2.  Application areas
3. city and province
4. Important application areas in each province
5. Super words (regarding the summary of requirements)
