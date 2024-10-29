from flask import Flask, render_template
from app import create_app  # app 폴더의 __init__.py에서 create_app 함수를 import




app = Flask(__name__, template_folder='C:/Users/gmltn/Desktop/DongaUniversity/SW-ECO_WEB/ecoweb/app/templates')



@app.route('/')
def home():
    return render_template('에코웹5-올블랙.html')

if __name__ == '__main__':
    app.run(debug=True)