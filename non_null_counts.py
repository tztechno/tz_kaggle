non_null_counts = data0.count()
columns_of_small_nulls = non_null_counts[non_null_counts >= 1200].index
data1 = data0[columns_of_small_nulls]
display(data1.info())
