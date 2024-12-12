from flask import Flask, request
import pickle

app = Flask(__name__)

with open("C:/Users/ayushi.barsaiya/Desktop/projects/flask/mlops_env/classifier.pkl", "rb") as modelFile:

    model = pickle.load(modelFile)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Loan Approval Application</h1>"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # use model and predict
        
        loan_req = request.get_json()
        
        if loan_req['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1

        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History= loan_req['Credit_History']

        # Pre-processing will happen here.

        result = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return  {"loan_approval_status":pred}
    else:
        return "I will make the predictions"