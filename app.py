import pickle
from flask import Flask,render_template,request


model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__) #create the flask object

@app.route('/')  #some open opens the sever
def htmlPage():
    return render_template('index.html')

@app.route('/predict',methods=['post'])
def predict():
    #collecting data from form
    Type=float(request.form['Type'])
    AT=float(request.form['AT'])
    PT=float(request.form['PT'])
    RPM=float(request.form['RPM'])
    Torque=float(request.form['Torque'])
    TW=float(request.form['TW'])
    result=model.predict([[Type,AT,PT,RPM,Torque,TW]])
    if result[0] == 0:
        return render_template('index.html',result="Working")
    else :
        return render_template('index.html',result1="Failure")
    
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)