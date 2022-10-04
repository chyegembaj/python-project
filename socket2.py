from bs4 import BeautifulSoup
import urllib.request

#Get count of numbers in the span tag, and find the sum of the numbers.
html = urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_1659403.html").read()

soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    print(tag.contents[0])
    sum += int(tag.contents[0])
    count += 1
print('Count',count)
print('Sum',sum)
