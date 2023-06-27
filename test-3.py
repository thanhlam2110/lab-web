from scholarly import scholarly
import json
def write_json(path: str,json_str: str):
    with open(path, "w") as outfile:
            outfile.write(json_str)
# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
author_name = "Lam Tran Thanh Nguyen"
search_query = scholarly.search_author(author_name)
# Retrieve the first result from the iterator
first_author_result = next(search_query)
#scholarly.pprint(first_author_result)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result )
#scholarly.pprint(author)

publications = author['publications']
publications_dict = {}
for i in range(len(publications)):
    print("--------------------------Loop i ="+str(i)+"--------------------------")
    print(publications[i])
    publications_dict[i]=publications[i]
filename = author_name.replace(" ", "-")
write_json("publication-"+filename+".json",json.dumps(publications_dict))
