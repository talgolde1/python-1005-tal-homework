
from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open("Scores.txt", "r") as file:
            score = file.read()
            html = f'''
                <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{score}</div></h1>
                </body>
                </html>
            '''
            return html
    except IOError as e:
        error = str(e)
        html = f'''
            <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{error}</div></h1>
            </body>
            </html>
        '''
        return html


if __name__ == '__main__':
    app.run()
