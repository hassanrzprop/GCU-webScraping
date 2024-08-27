from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Example: Extracting headlines
    headlines = soup.find_all("h2")
    data = [headline.get_text() for headline in headlines]
    
    return jsonify({"headlines": data}) #return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
