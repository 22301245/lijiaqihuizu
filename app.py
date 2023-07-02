from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/wordcloud.html')
def wordcloud():  # put application's code here
    return render_template('wordcloud.html')

@app.route('/timeline.html')
def timeline():  # put application's code here
    return render_template('timeline.html')

@app.route('/topic.html')
def topic():  # put application's code here
    return render_template('topic.html')

@app.route('/contrast.html')
def contrast():  # put application's code here
    return render_template('contrast.html')

@app.route('/sentiment.html')
def sentiment():  # put application's code here
    return render_template('sentiment.html')



@app.route('/conclude.html')
def conclude():  # put application's code here
    return render_template('conclude.html')

if __name__ == '__main__':
    app.run()
