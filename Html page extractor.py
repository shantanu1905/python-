import requests
from bs4 import BeautifulSoup

url=input("Enter website link you want to copy HTML source code :")
#step 1 : get html
r = requests.get(url)
htmlcontent=r.content
#print(htmlcontent)

#step 2 : parse the html
soup=BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify)

#Shantanu Nimkar
#from this program you can extract html source code ,
#you can copy html code from output screen ,
#save it as text.html file
#Note that only html code get extracted 

