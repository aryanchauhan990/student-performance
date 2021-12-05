import pickle
from flask import Flask , url_for , request , jsonify , render_template
import numpy as np

app = Flask(__name__)
filename = "studentperformance.sav"
model = pickle.load(open(filename,'rb'))

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict",methods=['GET','POST'])
def predict():
    features = [float(x) for x in request.form.values()]

    lis_race=[]
    lis_parent=[]
    if(features[-2]==0):
        lis_race=[1,0,0,0,0]
    elif(features[-2]==1):
        lis_race=[0,1,0,0,0]
    elif(features[-2]==2):
        lis_race=[0,0,1,0,0]
    elif(features[-2]==3):
        lis_race=[0,0,0,1,0]
    elif(features[-2]==4):
        lis_race=[0,0,0,0,1]



    if(features[-1]==0):
        lis_parent=[1,0,0,0,0,0]
    elif(features[-2]==1):
        lis_parent=[0,1,0,0,0,0]
    elif(features[-2]==2):
        lis_parent=[0,0,1,0,0,0]
    elif(features[-2]==3):
        lis_parent=[0,0,0,1,0,0]
    elif(features[-2]==4):
        lis_parent=[0,0,0,0,1,0]
    elif(features[-2]==5):
        lis_parent=[0,0,0,0,0,1]


    features=features[:3]+lis_race+lis_parent

    f_features = [np.array(features)]

    prediction = model.predict(f_features)
    print(prediction)
    
    return render_template('index.html', prediction_text="Student's overall score out of 300 will be :" + str(round(prediction[0],2)))



if __name__ == "__main__":
    app.run(debug=True)



