#Katy Madier | kmadier
#SI507 Waiver Part 3

# these should be the only imports you need
import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

home_data = requests.get("http://michigandaily.com")
home_content = home_data.text
home_soup = BeautifulSoup(home_content, "html.parser")

print("Michigan Daily -- MOST READ\n")

#most read articles
mostRead=home_soup.find_all("div",class_="view-most-read")
for section in mostRead:
    for a in section.find_all('a', href=True):
        title = a.text
        link = a['href']
        #get author
        article_data = requests.get("http://michigandaily.com" + link)
        article_content = article_data.text
        article_soup = BeautifulSoup(article_content, "html.parser")
        if article_soup.find_all("div",class_="byline"):
            author_section=article_soup.find_all("div",class_="byline")
            for section in author_section:
                for a in section.find_all('a', href=True):
                    author = a.text
        else:
            author = "Daily Staff Writer"
        print("{}\n" "  by " "{}\n".format(title,author))
