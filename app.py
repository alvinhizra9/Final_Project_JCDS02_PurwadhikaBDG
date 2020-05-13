from flask import Flask,render_template,request,send_from_directory
from data import contract_type,province,group,history_type,data_clean
from plot import barplot,heatmap,distplot1,distplot2
from prediction import prediction
import pandas as pd


## translate Flask to python object
app = Flask(__name__,static_url_path='', 
            static_folder='web/static')

@app.route("/", methods=['GET','POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        data['family_size'] = int(data['family_size'])
        data['age'] = int(data['age'])
        data['monthly_expense'] = int(data['monthly_expense'])
        data['loan_amount'] = int(data['loan_amount'])
        hasil = prediction(data)
        return render_template('prediction.html', hasil_prediction=hasil[0],hasil_msg=hasil[1],
        hasil_risk=hasil[2])
    return render_template('home.html',data_contract_type=sorted(contract_type),
    data_province=sorted(province),data_group=sorted(group),data_history_type=sorted(history_type))

@app.route('/data')
def data():
    data = data_clean()
    return render_template('data.html', data=data.sample(n=500,random_state=101))

@app.route('/plot')
def plot():
    return render_template('plot.html', data=barplot(),data2=heatmap(),data3=distplot1(),data4=distplot2())

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=1111)