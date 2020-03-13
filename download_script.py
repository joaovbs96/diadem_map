from urllib.request import urlopen, Request, urlretrieve
import json
from io import BytesIO
from PIL import Image

item_ids = [29896, 29909, 29919, 29929, 29939, 29944, 29895,
            29907, 29916, 29926, 29936, 29899, 29906, 29915,
            29925, 29935, 29947]

keys = ['Icon', 'Name_de', 'Name_en', 'Name_fr', 'Name_ja']

for i in item_ids:
    request = Request(url=("http://xivapi.com/Item/" + str(i)))
    request.add_header('User-Agent', '&lt;User-Agent&gt;')
    data = json.loads(urlopen(request).read())

    # only save the data we need
    new_data = {}
    for k in keys:
        new_data[k] = data[k]

    final_dict = {}
    final_dict["id"] = i
    final_dict["data"] = new_data

    # save dictionary to json
    with open('data/' + str(i) + '.json', 'w', encoding='utf-8') as f:
        json.dump(final_dict, f, ensure_ascii=False, indent=4)

    """# download icons
    request = Request(url=("http://xivapi.com" + data['Icon']))
    request.add_header('User-Agent', '&lt;User-Agent&gt;')
    icon = Image.open(BytesIO(urlopen(request).read()))
    icon.save('icons/' + str(i) + '.png')"""
