import re
def test():

    reg = re.compile("(https?://)?www\.[a-z.-]+\.(de|com)([a-z/]*)")

    m = reg.match("www.google.com")
    print(m)

    m = reg.match("https://www.youtube.com")
    print(m)

    m = reg.match("http://www.uni-wuerzburg.de")
    print(m)

    m = reg.match("www.wiwi.uni-wuerzburg.de/wiba/startseite/")
    print(m)
form = re.compile("(123)")
match = form.findall("123123")
print(match)


