from flask import Flask, render_template, request
import joblib
app = Flask(__name__)


@app.route('/')
def base():
    return render_template('data.html')

@app.route('/predict', methods=['post'])
def predict():

    # load the model
    model = joblib.load('diabetic_81.pkl')

    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    print(preg, plas, pres, skin, test, mass, pedi, age)
    preg=int(preg)
    plas=int(plas)
    pres=int(pres)
    skin=int(skin)
    test=int(test)
    mass=int(mass)
    pedi=int(pedi)
    age=int(age)
    
    output = model.predict([[preg, plas, pres, skin,test,mass, pedi, age]])

    if output[0] == 0:
        data = 'person is not diabetic'
    else:
        data = 'person is diabetic'

    return render_template('predict.html', data = data)
if __name__ == "__main__":
    app.run(debug=True)
