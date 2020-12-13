import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout


def My_NN_train(X_train,y_train):

	regressor = Sequential()
	regressor.add(LSTM(units = 60, activation = 'relu', return_sequences = True, input_shape = (X_train.shape[1], 10)))
	regressor.add(Dropout(0.2))
	regressor.add(LSTM(units = 60, activation = 'relu', return_sequences = True))
	regressor.add(Dropout(0.2))
	regressor.add(LSTM(units = 80, activation = 'relu', return_sequences = True))
	regressor.add(Dropout(0.2))
	regressor.add(LSTM(units = 120, activation = 'relu'))
	regressor.add(Dropout(0.2))
	regressor.add(Dense(units = 3))
	regressor.summary()

	regressor.compile(optimizer='adam', loss = 'mean_squared_error', metrics = ['accuracy']) #find a different loss function for classification
	history = regressor.fit(X_train, y_train, epochs=100, batch_size=320)

	return (regressor,history)

def My_NN_predict(data_pred, regressor):
	y_pred = regressor.predict(X_test) #predicted values for bhs
	scaler.scale_ #generated coefficient for scaling our data back to initial
	for i in range(y_pred.shape[0]):
	    #print(i,y_pred[i])
	    k = (np.argmax(y_pred[i]))
	    y_pred[i] = [0,0,0]
	    y_pred[i][k] = 1
	    #for dealing with the negative and non-format abiding output predictions

	return y_pred

def Test_NN(y_pred,y_test,history):
	count = 0
	for i in range(y_pred.shape[0]):
	    if np.array_equal(y_pred[i],y_test[i]):
	        pass
	    else:
	        count+=1
	print("No of Times where our model predicted wrong output",count)
	# print(i,y_pred[i],y_test[i])
	plt.plot(history.history['loss'])
	history.history['loss']

def get_training_data(data):
	data_training = data[:].copy()
	
	scaler = MinMaxScaler() #read on this from the sklearn - Rich to Rich
	data_training = scaler.fit_transform(data_training) #scales data to reduce error

	X_train = []
	y_train = []
	for i in range(60, data_training.shape[0]):
	    X_train.append(data_training[i-60:i]) #sliding window of data to help predict next day
	    y_train.append(data_training[i,[7,8,9]]) #60 chosen arbitrarily
	X_train, y_train = np.array(X_train), np.array(y_train) #converted to np array

	return (X_train, y_train)

def get_testing_data(data):
	data_testing = data[8000:].copy()

	data_train = data[:8000].copy()
	past_60_days = data_train.tail(60)

	df = past_60_days.append(data_testing, ignore_index = True) #for the fist 60 values of pridict data set

	inputs = scaler.transform(df) #scaling data
	# inputs
	#inputs = df.copy()
	X_test = []
	y_test = []
	x_pred = []
	#reformatting and now feeding data into the model for prediction
	for i in range(60, inputs.shape[0]):
	    X_test.append(inputs[i-60:i])
	    y_test.append(inputs[i, [7,8,9]])
	    x_pred.append(inputs[i, [:7]])

	X_test, y_test = np.array(X_test), np.array(y_test)

	return (X_test, y_test, x_pred)


def My_NN():
	data = pd.read_csv('train2.csv', date_parser = True)
	data = data.dropna()
	data = data.reset_index(drop=True)

	X_train, y_train = get_training_data(data)
	X_test, y_test, x_pred = get_testing_data(data)

	Pred_NN, Pred_history = My_NN_train(X_train, y_train)
	# Train the NN
	y_pred = My_NN_predict(X_test,Pred_NN)
	# Predict the testing data
	Test_NN(y_pred,y_test,Pred_history)
	# Test the performance of NN on testing data

	data_pred = []
	y_pred = list(y_pred)
	for i in range(X_test.shape[0]):
		data_pred.append(x_pred[i]+y_pred[i])
	with open("train3.csv","w") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["Open","High","Low	Close","Volume","20_day","50_day","b","h","s"])
		writer.writerow(data_pred)
	# write the predicted one hot vector (["b","h","s"]) with the information of everyday's stock price in the new csv file

My_NN()




