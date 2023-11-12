from flask import Flask, render_template, request
import json

import ml

app = Flask(__name__, static_folder="static", template_folder="template")

@app.route('/')
def hello_world():
   return render_template("index.html")


@app.route('/rank', methods=['POST'])
def rank_nursery_application():
   body = request.get_json()
   print("Request body:")
   print(body)

   rank = ml.rank_nursery_application(body)

   print(f"Rank: {rank}")

   return json.dumps({ 'rank': rank })

if __name__ == '__main__':
   app.run(debug=True)