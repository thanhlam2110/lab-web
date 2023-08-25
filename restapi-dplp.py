from flask import Flask, request
from scholarly import scholarly
import json
import requests
#-----------------FUNTION-----------------
def get_dblp_results(author_name):
    base_url = "https://dblp.org/search/publ/api"
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

def correct_author(author_name:str):
    dblp_results = get_dblp_results(author_name)
    correct_author_publication = {}
    overall_infos =dblp_results["result"]["hits"]["hit"]
    index = 0
    for i in range(len(overall_infos)):
        #print("------------------"+str(i)+"------------------")
        infos = overall_infos[i]["info"]
        author_arr = infos["authors"]["author"]
        if author_arr is not None:
            #print(author_arr)
            if isinstance(author_arr, dict):
                check_result = check_string_in_dict(author_arr,author_name)
                if check_result == 1:
                    correct_author_publication[index] = infos
                    index += 1
            elif isinstance(author_arr, list):
                check_result = check_string_in_list_of_dicts(author_arr,author_name)
                if check_result == 1:
                    correct_author_publication[index] = infos
                    index += 1
    return correct_author_publication
def category_publication(author_name:str,category_name:str):
    correct_author_publication = correct_author(author_name)
    category_publication = {}
    #Books and Theses
    #Informal and Other Publications
    #Editorship
    #Journal Articles
    #Reference Works
    #Conference and Workshop Papers
    #Parts in Books or Collections
    for i in range(len(correct_author_publication)):
        types = correct_author_publication[i]["type"]
        if(types==category_name):
            category_publication[i] = correct_author_publication[i]
    return category_publication
def year_publication(author_name:str,year:str):
    correct_author_publication = correct_author(author_name)
    year_publication = {}
    for i in range(len(correct_author_publication)):
        yearInfo = correct_author_publication[i]["year"]
        if(yearInfo==year):
            year_publication[i] = correct_author_publication[i]
    return year_publication
def range_year_publication(author_name:str):
    correct_author_publication = correct_author(author_name)
    total_year_arr = []
    year_arr = []
    year_dict = {}
    for i in range(len(correct_author_publication)):
        total_year_arr.append(correct_author_publication[i]["year"])
    unique_values = set(total_year_arr)
    for value in unique_values:
        year_arr.append(value)
    year_arr = sorted(year_arr, reverse=True)
    year_dict["year"] = year_arr
    return year_dict
def list_type_publication(author_name:str):
    correct_author_publication = correct_author(author_name)
    total_type_publication = []
    type_publication = []
    type_publication_dict = {}
    for i in range(len(correct_author_publication)):
        total_type_publication.append(correct_author_publication[i]["type"])
    unique_values = set(total_type_publication)
    for value in unique_values:
        type_publication.append(value)
    type_publication_dict["type"] = type_publication
    return type_publication_dict
#---------------ROUTE--------------------
app = Flask(__name__)
@app.route('/')
def hello():
    return 'THIS IS RESTAPI FOR GETTING PUBLICATION FROM DBLP'
@app.route('/api/getAllPublication', methods=['GET'])
def getPublicationByName():
    author_name = request.args.get('author_name')
    allPulication = correct_author(author_name)
    return allPulication
@app.route('/api/getCategoryPublication', methods=['GET'])
def getCategoryPublication():
    author_name = request.args.get('author_name')
    categoryPublication = list_type_publication(author_name)
    return categoryPublication
@app.route('/api/getYearPublication', methods=['GET'])
def getYearPublication():
    author_name = request.args.get('author_name')
    yearPublication = range_year_publication(author_name)
    return yearPublication
@app.route('/api/getPublicationByCategory', methods=['GET'])
def getPublicationByCategory():
    author_name = request.args.get('author_name')
    category_name = request.args.get('category_name')
    categoryPublication= category_publication(author_name,category_name)
    return categoryPublication
@app.route('/api/getPublicationByYear', methods=['GET'])
def getPublicationByYear():
    author_name = request.args.get('author_name')
    year = str(request.args.get('year'))
    yearPublication= year_publication(author_name,year)
    return yearPublication
#---------------MAIN--------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0')