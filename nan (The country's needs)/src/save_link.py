from bs4 import BeautifulSoup
links = []
data = open('/home/alireza/Desktop/alireza/web scraping/index.html','r')
soup = BeautifulSoup(data, 'html.parser')
for element in soup.find_all('a'):
    link = element.get('href')
    if isinstance(link, type(None)): 
        continue
    elif "/ViewNeed" in link:
        links.append(link)
links = list((set(links)))
print(f"total number of url {len(links)}")


file1 = open("/home/alireza/Desktop/alireza/web scraping/links.txt","w")
for link in links:
    file1.write(link)
    file1.write("\n")
file1.close()
