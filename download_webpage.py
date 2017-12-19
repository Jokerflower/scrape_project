from urllib.request import urlopen

url = "https://www.goodreads.com/author/list/7509399.Lu_Xun"

def get_webpage(url):

    print("Getting Request Object")
    request = urlopen(url)
    print("Reading Request Object")
    data = request.read()
    text = data.decode("utf-8")

    print("Web Page Downloaded, Hooray")
    return text

text = get_webpage(url)



with open('html_text.txt', 'w') as f:
    f.write(text)