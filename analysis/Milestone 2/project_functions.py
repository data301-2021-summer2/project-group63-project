def clean_and_process(path):
    
    import numpy as np 
    import pandas as pd 
    
    df = (pd.read_csv(path))
    
    bins = [0, 10, 20, 30, 40, np.inf]
    names = ['<10', '10-20', '20-30', '30-40', '40+']
    lbls = ['Admin_Unit_Code', 'Sub_Unit_Code', 'Plot_Name', 'Location_Type', 'Date', 'Start_Time', 'End_Time', 'Observer', "Visit", 'NPSTaxonCode', "AOU_Code", 'PIF_Watchlist_Status', 'Regional_Stewardship_Status', 'Humidity', 'Sky', 'Wind', 'Initial_Three_Min_Cnt','Interval_Length','ID_Method','Distance','Flyover_Observed', 'Sex', 'Scientific_Name', 'AcceptedTSN','Disturbance']
    
    df_clean = (
        df.drop(labels = lbls,axis=1)
        .rename(columns={'Site_Name':'Site','Common_Name':'Species'})
        .assign(Temp_Range=pd.cut(df['Temperature'], bins, labels=names))
    )
    
    return df_clean