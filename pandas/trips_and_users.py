import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    banned_users=users[users['banned']=='Yes']['users_id'].values
    trips['request_at']=pd.to_datetime(trips['request_at'])
    trips=trips[trips['request_at'].between('2013-10-01','2013-10-03')]

    df_temp=trips[~(trips['client_id'].isin(banned_users)) & ~(trips['driver_id'].isin(banned_users))]
    
    condition=df_temp['status'].str.contains('cancel')
    df_temp.loc[:,'cancel_status']=np.where(condition,1,0)

    return df_temp.groupby('request_at')['cancel_status'].apply(lambda x:np.round(x.sum()/x.count(),2))\
.reset_index().rename(columns={'request_at':'Day','cancel_status':'Cancellation Rate'})
