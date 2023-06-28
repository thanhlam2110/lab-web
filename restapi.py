from flask import Flask, request
from scholarly import scholarly
import json
app = Flask(__name__)
@app.route('/')
def hello():
    return 'THIS IS RESTAPI FOR GOOGLE SCHOLAR PUBLICATION'

@app.route('/api/author', methods=['GET'])
def getAuthorInformation():
        id = request.args.get('id')
        author_info = scholarly.search_author_id(id)
        return author_info
@app.route('/api/publication', methods=['GET'])
def getPublication():
    author_name = request.args.get('name')
    search_query = scholarly.search_author(author_name)
    first_author_result = next(search_query)
    author = scholarly.fill(first_author_result )
    publications = author['publications']
    publications_dict = {}
    for i in range(len(publications)):
        publications_dict[i]=publications[i]
    return publications_dict
if __name__ == '__main__':
    app.run(host='0.0.0.0')
