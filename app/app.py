import os
from flask import Flask, render_template

app = Flask(__name__)


app = Flask(__name__)

@app.route('/')
def hello():
    host_name=os.environ.get('HOSTNAME')
    return render_template('index.html', host_name=host_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
