import pickle
from pandas import DataFrame,get_dummies

model = pickle.load(open('finalized_model.sav','rb'))
real_columns = pickle.load(open('real_column.sav','rb'))
one_hot_columns = pickle.load(open('dummies_column.sav','rb'))

def prediction(data):
    result = []
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil = model.predict(df)
    if hasil[0] == 0:
        res = 'Not Default'
        msg = 'Congratulations, your loan is Approved!'
    else:
        res = 'Default'
        msg = 'Sorry, your loan is Not Approved!'
    result.append(res)
    result.append(msg)
    hasil_proba = model.predict_proba(df)
    result.append(str(round(hasil_proba[:,1][0]*100))+'%')
    return result