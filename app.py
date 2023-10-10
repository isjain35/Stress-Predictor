from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('mymodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction=model.predict(features)
    
    output = round(prediction[0])
    
    msg=''

    if output == 1:
        msg = '-> Low'
    elif output == 2:
        msg = '-> Medium'
    else:
        msg = '-> High'

    return render_template('index.html', predictionText = 'Stress level: {}'.format(output)+' '+msg)

if __name__== "__main__":
    app.run()