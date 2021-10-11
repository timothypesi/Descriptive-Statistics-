
#Function to remove outliers using z-score
def remove_outliers(data, col):
    col_upper = data[col].mean() + 3*data[col].std()
    col_lower = data[col].mean() - 3*data[col].std()
    df = data[(data[col]< col_upper) & (data[col]> col_lower)]
    #return df 


#Function to remove outliers using percentile 

def percentile_based_outlier(data, col):
    upper_limit = data[col].quantile(0.975)
    lower_limit = data[col].quantile(0.025)
    df_percentile = data[(data[col]< upper_limit) & (data[col]> lower_limit)]
    return df_percentile 
 #drop all nas in a dataset   
def drop_all_na(data):
    df = data.dropna(inplace=True)
    return df
#Drop all na rows on specific columns 
def drop_nans(data, cols):
    df = data.dropna(subset=cols, inplace=True)
    return df

#Convert categoriacl columns to integer
def convert_categorical_cols(data,col):
    colum_values = list(data[col].unique())
    dicts = {}
    values = range(len(colum_values))
    for i in range(len(colum_values)):
        dicts[colum_values[i]] = values[i]
        values = range(len(colum_values))
    print(dicts)
    data[col]=data[col].map(dicts)