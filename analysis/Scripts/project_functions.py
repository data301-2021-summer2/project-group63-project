def load_process(path):
    # First load data and remove unnecessary columns and NaN
    df = pd.read_csv(path)
    df1 = (
        pd.DataFrame(df.drop(columns=(column_names))
            .dropna(axis=0))
                    )
    # add column for Temperature Class
    for i in df1['Temperature']:
        if i in range(0,9):
            df1['Temp_Class'] = 1
        elif i in range(9,17):
            df1['Temp_Class'] = 2
        elif i in range(18,25):
             df1['Temp_Class'] = 3
        elif i in range(25,33):
            df1['Temp_Class'] = 4
        elif i in range (33,41):
            df1['Temp_Class'] = 5
    return df1