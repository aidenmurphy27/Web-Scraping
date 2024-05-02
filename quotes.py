from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.express as px
from plotly.graph_objs import bar
from plotly import offline

count_dict = {}
page_counter = 1
quote_dict = {}
quote_lengths = {}
tags_list = []

counter = 0

for _ in range(10):
    url = 'http://quotes.toscrape.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    quote = soup.findAll("span", attrs={"class": "text"})
    find_author = soup.findAll("small", attrs={"class": "author"})
    tag = soup.findAll("div", attrs={"class": "tags"})

    for counter in range(min(len(quote), len(find_author), len(tag))):
        quote_text = quote[counter].text
        new_quote = quote[counter].text.replace('.', '').replace(u"\u201C", "").replace(u"\u201D", "")
        author = find_author[counter].text
        new_tag = tag[counter].text.replace("Tags:", "")
        tags_list.extend(new_tag.split())

        quote_lengths[quote_text] = len(quote_text)

        if author in quote_dict:
            quote_dict[author].append(new_quote)
        else:
            quote_dict[author] = [new_quote]

    for item in tags_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1


total_length = sum(quote_length for quote_length in quote_lengths.values())
count_quotes = len(quote_lengths)
avg_length = round((total_length / count_quotes), 4)
longest_quote = max(quote_lengths, key=lambda quote: quote_lengths[quote])
shortest_quote = min(quote_lengths, key=lambda quote: quote_lengths[quote])

max_count = max(count_dict.values())
top_tags = [word for word, count in count_dict.items() if count == max_count]

quote_count = {author: len(quotes) for author, quotes in quote_dict.items()}
most_quotes = max(quote_count.values())
least_quotes = min(quote_count.values())

most_author = [author for author, count in quote_count.items() if count == most_quotes]
least_author = [author for author, count in quote_count.items() if count == least_quotes]

print()

print('----Author Statistics----')
print(f"Quotes by Author: {quote_count}\n")
print(f"Author with most quotes: {most_author}\n")
print(f"Author with least quotes: {least_author}\n")

print('----Quote Statistics----')
print(f'Average Length of Quote: {avg_length}\n')
print(f'Longest Quote: {longest_quote}\n')
print(f'Shortest Quote: {shortest_quote}\n')

print('----Tag Statistics----')
print(f'Most Popular Tag: {top_tags}\n')
print(f'Number of Tags: {len(tags_list)}')

print()

sorted_list_authors = []
sorted_num_authors = []

total_list_authors = sorted(quote_count.items(), key=lambda x: x[1], reverse=True)

for author in total_list_authors:
    sorted_list_authors.append(author[0])
    sorted_num_authors.append(author[1])

top_ten_authors = sorted_list_authors[:10]
top_ten_num_authors = sorted_num_authors[:10]

sorted_list_tags = []
sorted_num_tags = []

total_list_tags = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

for tag in total_list_tags:
    sorted_list_tags.append(tag[0])
    sorted_num_tags.append(tag[1])

top_ten_tags = sorted_list_tags[:10]
top_ten_num_tags = sorted_num_tags[:10]

author_graph = [{"type": "bar","x": top_ten_authors,"y": top_ten_num_authors,"marker": {"color": "rgb(60,120,180)", "line": {"width": 2, "color": "rgb(25,50,75)"}},"opacity": 0.8}]
author_layout = {"title": "Top Ten Authors that have the most quotes", "xaxis": {"title": "Authors"},"yaxis": {"title": "Number of Quotes"}}
fig = {"data": author_graph, "layout": author_layout} 
offline.plot(fig, filename="author_graph.html")

sorted_list_tags = []
sorted_num_tags = []

total_list_tags = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

for tag in total_list_tags:
    sorted_list_tags.append(tag[0])
    sorted_num_tags.append(tag[1])

top_10_tags = sorted_list_tags[:10]
top_10_num_tags = sorted_num_tags[:10]

tag_graph = [{"type": "bar","x": top_10_tags,"y": top_10_num_tags,"marker": {"color": "rgb(60,120,180)", "line": {"width": 2, "color": "rgb(25,50,75)"}},"opacity": 0.8}]
tag_layout = {"title": "Top Ten Tags with the most occurrences", "xaxis": {"title": "Tags"},"yaxis": {"title": "Number of Occurrences"}}
tag_fig = {"data": tag_graph, "layout": tag_layout}
offline.plot(tag_fig, filename="tag_graph.html")
