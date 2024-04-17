from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(url="https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvote = [int(score.find(class_="score").get_text().split()[0]) for score in soup.find_all(class_="subline")]
largest_upvotes = article_upvote.index(max(article_upvote))
#
print(article_texts[largest_upvotes])
print(article_links[largest_upvotes])
print(article_upvote[largest_upvotes])
print(max(article_upvote))


# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText()) sam text
    # print(tag.get("href")) same linki


# heading = soup.find(name="h1", id="name")
# print(heading.getText())

# section_heading = soup.find_all("h3")
# print(section_heading)

# company_url = soup.select_one(selector="#name")
# print(company_url)

# headings = soup.select(".heading")
# print(headings)