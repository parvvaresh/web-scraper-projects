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

Notebook is also availble on google colab. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DE_UIYWdnKAk56DPfZGd1AK7APCgrGsL?usp=sharing)


Now, using the Pandas package, diagrams about :
1. key words
2.  Application areas
3. city and province
4. Important application areas in each province
5. Super words (regarding the summary of requirements)

[![pandas](https://camo.githubusercontent.com/a0395c46031320934c51cdbf5b65fedfcaa0d6a3c91d354ff608bb0f3863d3a7/68747470733a2f2f73746167696e672e61636164656d792e6e756d666f6375732e6f72672f77702d636f6e74656e742f75706c6f6164732f323031362f30372f70616e6461732d6c6f676f2d3330302e706e67)]()
