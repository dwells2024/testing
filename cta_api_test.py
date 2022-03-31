import requests
from xml.etree import ElementTree

my_key = "18ed136cc1a548b28def38fbae4cd0e6"

lines = ["red", "blue", "brn", "g", "org", "p", "pink", "y"]

route = 3
id = 0
dest = 2
stop = 6

for line in lines:
    url = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key=" + my_key + "&rt=" + line
    response = requests.get(url)

    tree = ElementTree.fromstring(response.content)

    print(tree[route].attrib)

    for train in tree[route]:
        print(train[id].text, "to", train[dest].text + "- Next Stop: " + train[stop].text)

