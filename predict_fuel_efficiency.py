import pandas as pd
import joblib

def input_data(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    input_data = [[x1, x2, x3, x4, x5, x6, x7, x8, x9]]
    new_data = pd.DataFrame(input_data, columns = ['var1', 'var2', 'var3', 'var4', 'var5', 'var6', 'var7', 'var8', 'var9'])
    return new_data

def prediction(model, data):
    result = model.predict(data)
    return result[0]

if __name__ == "__main__" :
    model = joblib.load("model/vehicle_fuel_efficiency_model.sav")
    print('\n----------------Predict Vehicle Fuel Efficiency----------------\n')
    print('Please input the features: ')
    var_1 = input('1. cylinders: ')
    var_2 = input('2. displacement: ')
    var_3 = input('3. horsepower: ')
    var_4 = input('4. weight: ')
    var_5 = input('5. acceleration: ')
    var_6 = input('6. model year: ')
    var_7 = 0
    var_8 = 0
    var_9 = 0
    
    country = input('7. Country(1 = USA, 2 = europe, 3=Japan): ')
    if country == 1:
        var_7 = 1
    elif country ==2:
        var_8 = 1
    else:
        var_9 = 1
    
    new_data = input_data(var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9)
    predict = prediction(model, new_data)
    print('\Vehicle Fuel Efficiency :', predict)