from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
model = pickle.load(open('model1.pkl', 'rb'))


@app.route('/page')
def main():
    return render_template('text.html')


@app.route('/prediction', methods=['POST'])
def predict():

        int_features = [float(x) for x in request.form.values()]
        features = [np.array(int_features)]
        prediction = model.predict(features)
        output = prediction[0]

        # Check if the output is a string
        if isinstance(output, str):
            prediction_text = f'The prediction is {output}'
        else:
            output = float(output)
            output = round(output, 2)
            prediction_text = f'The above payment is {output}'

        return render_template('text.html', prediction_text='The above payment is {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
