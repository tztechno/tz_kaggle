#####################################################
------------------------------------------------
#####################################################
------------------------------------------------
#####################################################
------------------------------------------------
#####################################################
------------------------------------------------
# NEW FEATURE - COMBINATIONS OF CATS
PAIRS = []
for i,c1 in enumerate(CATS[:-1]):
    for j,c2 in enumerate(CATS[i+1:]):
        n = f"{c1}_{c2}"
        m1 = train[c1].max()+1
        m2 = train[c2].max()+1
        train[n] = ((train[c1]+1 + (train[c2]+1)/(m2+1))*(m2+1)).astype("int8")
        test[n] = ((test[c1]+1 + (test[c2]+1)/(m2+1))*(m2+1)).astype("int8")
        COMBO.append(n)
        PAIRS.append(n)
        
#####################################################
------------------------------------------------
# NEW FEATURE - COMBINATIONS OF DIGITS 
for i in range(4):
    for j in range(i+1,5):
        n = f"digit_{i+1}_{j+1}"
        train[n] = ((train[f'digit{i+1}']+1)*11 + train[f'digit{j+1}']+1).astype("int8")
        test[n] = ((test[f'digit{i+1}']+1)*11 + test[f'digit{j+1}']+1).astype("int8")
        COMBO.append(n)
#####################################################
------------------------------------------------
# NEW FEATURE - DIGIT EXTRACTION FROM WEIGHT CAPACITY
for k in range(1,10):
    train[f'digit{k}'] = ((train['Weight Capacity (kg)'] * 10**k) % 10).fillna(-1).astype("int8")
    test[f'digit{k}'] = ((test['Weight Capacity (kg)'] * 10**k) % 10).fillna(-1).astype("int8")
DIGITS = [f"digit{k}" for k in range(1,10)]
#####################################################
------------------------------------------------
# NEW FEATURE - BIN WEIGHT CAPACITY USING ROUNDING
for k in range(7,10):
    n = f"round{k}"
    train[n] = train["Weight Capacity (kg)"].round(k)
    test[n] = test["Weight Capacity (kg)"].round(k)
    COMBO.append(n)
#####################################################
------------------------------------------------
CATS=test.columns.tolist()
COMBO = ["NaNs"]
train["NaNs"] = np.float32(0)
test["NaNs"] = np.float32(0)

for i,c in enumerate(CATS):

    # NEW FEATURE - ENCODE ALL NAN AS ONE BASE-2 FEATURE
    train["NaNs"] += train[c].isna()*2**i
    test["NaNs"] += test[c].isna()*2**i

    # NEW FEATURE - COMBINE EACH COLUMN'S NAN WITH WEIGHT CAPACITY
    n = f"{c}_nan_wc"
    train[n] = train[c].isna()*100 + train["Weight Capacity (kg)"]
    test[n] = test[c].isna()*100 + test["Weight Capacity (kg)"]
    COMBO.append(n)
    
    combine = pd.concat([train[c],test[c]],axis=0)
    combine,_ = pd.factorize(combine)
    train[c] = combine[:len(train)].astype("float32")
    test[c] = combine[len(train):].astype("float32")
    n = f"{c}_wc"
    train[n] = train[c]*100 + train["Weight Capacity (kg)"]
    test[n] = test[c]*100 + test["Weight Capacity (kg)"]
    COMBO.append(n)
#####################################################
