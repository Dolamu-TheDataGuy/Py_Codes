from bs4 import BeautifulSoup


with open("website.html", "r") as file:
    content = file.read()


soup = BeautifulSoup(content, "lxml")
# print(soup.name)
# print(soup.title.text)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

print(len(soup.find_all('a')))

all_anchor_tag = soup.find_all('a')

for tag in all_anchor_tag:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text)

company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(".heading")
print(headings)