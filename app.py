import numpy as np
import pickle

from flask import Flask, redirect, url_for,jsonify, request,render_template
app = Flask(__name__)
model = pickle.load(open('model/model1.pkl', 'rb'))

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/ff',methods = ['POST', 'GET'])
def ff():
   return render_template("predict.html")

@app.route('/predict',methods = ['POST'])
def predict():
   values=[]
   form_value = dict()
   
   name=request.form['name']
   form_value['name']=name
   
   sex=request.form['sex']
   values.append(sex)
   if(sex=="0"):
      form_value['sex'] = "Male"
   else:
      form_value['sex'] = "Female"
   
   Married=request.form['Married']
   values.append(Married)
   if(Married=="0"):
      form_value['Married'] = "Married"
   else:
      form_value['Married'] = "Unmarried"

   Dependency=request.form['Dependency']
   values.append(Dependency)
   if(Dependency=="1"):
      form_value['Dependency'] = "Dependency with 1"
   elif(Dependency=="2"):
      form_value['Dependency'] = "Dependency with 2"
   else:
      form_value['Dependency'] = "Dependency with 3+"
   

   Graduation=request.form['Graduate']
   values.append(Graduation)
   if(Graduation=="0"):
      form_value['Graduation'] = "Graduate"
   else:
      form_value['Graduation'] = "Not Graduate"

   Self_Employed=request.form['Self_Employed']
   values.append(Self_Employed)
   if(Self_Employed=="0"):
      form_value['Self Employed'] = "Yes"
   else:
      form_value['Self Employed'] = "No"

   AppliLoanStatusntIncome=request.form['ApplicantIncome']
   values.append(AppliLoanStatusntIncome)
   form_value['AppliLoanStatusntIncome'] = AppliLoanStatusntIncome

   CoappliLoanStatusntIncome=request.form['CoapplicantIncome']
   values.append(CoappliLoanStatusntIncome)
   form_value['CoappliLoanStatusntIncome'] = CoappliLoanStatusntIncome
   

   LoanAmount=request.form['LoanAmount']
   values.append(LoanAmount)
   form_value['LoanAmount'] = LoanAmount

   Loan_Amount_Term=request.form['Loan_Amount_Term']
   values.append(Loan_Amount_Term)
   form_value['Loan_Amount_Term'] = Loan_Amount_Term

   Credits=request.form['Credits']
   values.append(Credits)
   form_value['Credits'] = Credits

   Property=request.form['Property']
   values.append(Property)
   if(Property=="0"):
      form_value['Property'] = "Urban"
   elif(Property=="1"):
      form_value['Property'] = "Rural"
   else:
      form_value['Property'] = "Semi Urban";

   
   final_values=[np.array(values)]
   print(final_values)
   
   prediction=model.predict(final_values)
   print(prediction)
   
   result=prediction
   form_value['result']=result
   print(result)
   
   if result==0:
      return render_template("result.html",result= form_value)
   else:
      return render_template("result.html",result= form_value)     


if __name__ == '__main__':
   app.run(debug=True,use_reloader=False)
