import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


random_chapter = random.randrange(1,22)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter +'.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

# Find all verse elements with class 'p'
page_verses = soup.find_all('div', class_='p')

myverses = []

for section_verses in page_verses:
    verse_list = section_verses.text.split('.')

    for v in verse_list:
        myverses.append(v)

mychoice = random.choice(myverses)

print(f"Chapter: {random_chapter} Verse: {mychoice}")



# # Select a random verse from the list
# random_verse = random.choice(page_verses)

# # Extract and print the text of the selected verse
# verse_text = random_verse.get_text(strip=True)  # Get the text of the verse
# print(verse_text)

        

