from flask import Flask, request, render_template
from myHTMLedit import bad_html, god_html
from DctToTxt import dct_r_txt
from myHTMLedit import ranktable
from rank import top3rank

app = Flask(__name__)


@app.route('/ScoreFlask', methods=['GET', 'POST', 'DELETE'])
def ScoreFlask():
    if request.method == 'GET':
        #     f = open("scores.txt", 'r')
        #    score = f.read()
        #   f.close()
        #  html = god_html(score)
        dct = dct_r_txt()
        if dct == False:
            html = bad_html()
            return html
        rankList = top3rank(dct)
        html = ranktable(rankList)

    return html

app.run(host="0.0.0.0", port=8777, debug=True, use_reloader=False)


