import requests
from bs4 import BeautifulSoup

def parser(url, class_, third):
    # url = 'https://www.fourseasons.com/ru/moscow/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    link = soup.find(class_, {'class': third})
    x = open('new.txt', 'a')
    x.write(link.text)
    x.close()
    return (link.text)
parser('https://www.fourseasons.com/ru/moscow/','p','normal Introduction-text ty-b2')


def parser_2(url, class_):
    # url = 'https://www.fourseasons.com/ru/moscow/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    link = soup.find(class_)
    x = open('new2.txt', 'a')
    x.write(link.text)
    x.close()
    return (link.text)
parser_2('https://kg.akipress.org/news:1693908/?from=portal&place=nowread&b=1', 'h1')



def parser_3(url, class_, third):
    # url = 'https://www.fourseasons.com/ru/moscow/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    link = soup.find(class_, {"class":third})
    x = open('new3.txt', 'a')
    x.write(link.text)
    x.close()
    return (link.text)
parser_3('https://akipress.org/','a','newslink')

# x = open("new_parser.text", "a")
# x.write(link.text))
# x.close()
