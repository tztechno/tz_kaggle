
df["rectal_exam_feces"] = df["rectal_exam_feces"].replace('serosanguious', 'absent')
df["nasogastric_reflux"] = df["nasogastric_reflux"].replace('slight', 'none')
    
df["temp_of_extremities"] = df["temp_of_extremities"].fillna("normal").map({'cold': 0, 'cool': 1, 'normal': 2, 'warm': 3})
df["peripheral_pulse"] = df["peripheral_pulse"].fillna("normal").map({'absent': 0, 'reduced': 1, 'normal': 2, 'increased': 3})

train.drop('id',axis=1,inplace=True)
test.drop('id',axis=1,inplace=True)
   
