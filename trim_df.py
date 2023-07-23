def trim(df, max_samples, min_samples, column):
    # column specifies which column of the dataframe to use, typically this is the labels column
    # df is typically train_df
    df=df.copy()
    classes=df[column].unique() # get the classes in df
    class_count=len(classes)
    length=len(df)
    print ('dataframe initially is of length ',length, ' with ', class_count, ' classes')
    groups=df.groupby(column)   # creates a set of  dataframes that only contains rows that have the class label  
    trimmed_df = pd.DataFrame(columns = df.columns) # create an empty dataframe with columns filepaths, labels    
    for label in df[column].unique(): # iterate through each class label
        group=groups.get_group(label) # get the dataframe associate with the label
        count=len(group) # determine how many files are in the dataframe   
        if count > max_samples: # if there more files in the dataframe sample it so the sampled files has only n rows
            sampled_group=group.sample(n=max_samples, random_state=123,axis=0)
            trimmed_df=pd.concat([trimmed_df, sampled_group], axis=0) # add the sampled files to the trimmed_df dataframe
        else:
            if count>=min_samples: # if the dataframe has more than the minimum number of files include it in the dataset
                sampled_group=group        
                trimmed_df=pd.concat([trimmed_df, sampled_group], axis=0)
    print('after trimming, the maximum samples in any class is now ',max_samples, ' and the minimum samples in any class is ', min_samples)
    classes=trimmed_df[column].unique()# return this in case some classes have less than min_samples
    class_count=len(classes) # return this in case some classes have less than min_samples and so will have less classes in it
    length=len(trimmed_df)
    print ('the trimmed dataframe now is of length ',length, ' with ', class_count, ' classes')
    return trimmed_df, classes, class_count
