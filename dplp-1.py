import requests

def get_dblp_results(author_name):
    base_url = "https://dblp.org/search/publ/api?h=1000000000"
    params = {
        "q": author_name,
        "format": "json",
        "h": 100000
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
def check_string_in_list_of_dicts(dict_list, string_to_check):
    for item in dict_list:
        if 'text' in item and item['text'] == string_to_check:
            return 1  # Return 1 if the string is found
    return 0  # Return 0 if the string is not found
def check_string_in_dict(dict_item, string_to_check):
    if 'text' in dict_item and dict_item['text'] == string_to_check:
        return 1  # Return 1 if the string is found
    return 0  # Return 0 if the string is not found

def correct_author(author_name:str,dblp_results: dict):
    correct_author_publication = {}
    overall_infos =dblp_results["result"]["hits"]["hit"]
    for i in range(len(overall_infos)):
            #print("------------------"+str(i)+"------------------")
            infos = overall_infos[i]["info"]
            author_arr = infos["authors"]["author"]
            if author_arr is not None:
                #print(author_arr)
                if isinstance(author_arr, dict):
                    check_result = check_string_in_dict(author_arr,author_name)
                    if check_result == 1:
                        correct_author_publication[i] = infos
                elif isinstance(author_arr, list):
                    check_result = check_string_in_list_of_dicts(author_arr,author_name)
                    if check_result == 1:
                        correct_author_publication[i] = infos
    return correct_author_publication
author_name = "Elena Ferrari"
dblp_results = get_dblp_results(author_name)
if dblp_results:
    correct_author_publication = correct_author(author_name,dblp_results)
    print(len(correct_author_publication))
    print(correct_author_publication)
else:
    print("No results found.")
