from scholarly import scholarly
import json
author = scholarly.search_author_id('Yt6EcJYAAAAJ')
#scholarly.pprint(author)
json_payload = json.dumps(author)
print(json_payload)