from flask import Flask, request
import pickle

app = Flask(__name__)

def predictions(f1,f2,f3,f4):
    pred = [[f1,f2,f3,f4]]
    with open('iris.pkl', 'rb') as model:
        main_model = pickle.load(model)

    prediction = main_model.predict(pred)

    return prediction

@app.route('/prediction', methods = ['POST'])
def iris():
    sl = float(request.form['sl'])
    sw = float(request.form['sw'])
    pl = float(request.form['pl'])
    pw = float(request.form['pw'])

    a = predictions(sl,sw,pl,pw)

    return f'Predicted result is {a}'

app.run()


    

    