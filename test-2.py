from scholarly import scholarly

# Specify the author ID
author_id = "Yt6EcJYAAAAJ"  

search_query = scholarly.search_author("Elena Ferrari")
author = next(search_query)
scholarly.pprint(scholarly.fill(author, sections=['basics', 'indices', 'coauthors']))
