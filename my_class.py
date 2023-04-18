############################################

class HeartDataSet:

    def __init__(self, data):        
        dataY=data['target']
        dataX=data.drop(['target'],axis=1)
        dataX=normalize_df(dataX)#normalize
        dataY=pd.get_dummies(dataY, columns=['target'])#one hot encoding
        self.data = data
        self.dataX = dataX
        self.dataY = dataY
        #display(self.data)

    def __len__(self):              
        return len(self.data)

    def __getitem__(self, index):    
        return self.dataX[index], self.dataY[index]   
      
############################################
