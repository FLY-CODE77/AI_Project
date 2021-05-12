# module load
import pandas as pd
from module.norm import normalization
from module.model import mlplinear
from module import visual

# data load
dataset = pd.read_csv("dataset2.csv") 

# Split data 8:2
train_data = dataset.sample(frac=0.8, random_state=0)
test_data = dataset.drop(train_data.index)

# normalization data for MLP layers
norm_train = normalization(train_data)
norm_test = normalization(test_data)

normed_train_data = norm_train.forward()
normed_test_data = norm_test.forward()

# pop y data
y_train_data = normed_train_data.pop("avgPrice")
y_test_data = normed_test_data.pop("avgPrice")

# build mlp model
dim = len(normed_train_data.columns) 
mlplinear = mlplinear(dim=dim, learning_rate=0.000005, epochs=10000, x_data=normed_train_data, y_data=y_train_data, batch_size=16)
'''
mlplinear package need 
x dimention , learning rate, epochs, x_data, y_data, batch_size, validation split rate
'''

model = mlplinear.build()        #.build() build MLP linear layers
history = mlplinear.prediction(model)          # predition need layers data

# evaluate 
loss, mae, mse = history.model.evaluate(normed_test_data, y_test_data, verbose=2)
mae = norm_test.y_backward(mae)
print("테스트 세트의 평균 절대 오차: {:5.2f} Price".format(mse))

# log data save .csv format
hist = pd.DataFrame(history.history) 
hist['epoch'] = history.epoch
hist.to_csv("log_data.csv",index=False)

# log data visualization
log_data = pd.read_csv("log_data.csv") 
visual.plot_history(log_data)         # plot_history need only log dataframe, MAE, MSE plot

# test prediction visualization
test_predictions = model.predict(normed_test_data).flatten()
visual.plot_error(test_predictions, y_test_data)       # plot_error(predict y, real y) plot True vs Predictions, prediction - real data