from flask import Flask,request,jsonify

from flask_cors import CORS

from github_service import fetch_repo

from analysis import analyze_code

from score import calculate_score

app=Flask(__name__)

CORS(app)

@app.route('/analyze',methods=['POST'])

def analyze():

    data=request.get_json()

    repo=data["repo"]

    code=fetch_repo(repo)

    security,bugs,performance,summary=analyze_code(code)

    score=calculate_score(

    security,

    bugs,

    performance

    )

    return jsonify({

    "score":score,

    "security":security,

    "bugs":bugs,

    "performance":performance,

    "summary":summary

    })

if __name__=="__main__":

    app.run(debug=True)
