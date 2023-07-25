
import holidays
from datetime import datetime, timedelta
from holidays import CountryHoliday

def GetHolidays(df):
    
    # Analyzing country specific holidays:-
    Holidays = pd.DataFrame(columns = ['date', 'holiday_name', 'country'])
    country_list = df.country.unique()
    min_year = df.year.min()
    max_year = df.year.max()
    number_of_days = (df['date'].max() - df['date'].min()).days + 1
    date_list = [df['date'].min() + timedelta(days=day) for day in range(number_of_days)]
    
    if min_year == max_year:
        years = [min_year]
    else:
        years = np.arange(min_year, max_year, 1)
        
    for country in tqdm(country_list):
        for h in CountryHoliday(country, years = years).items():   
            i=len(Holidays)
            Holidays.loc[i,'date']=h[0]
            Holidays.loc[i,'holiday_name']=h[1]
            Holidays.loc[i,'country']=country
    #print(Holidays)
    Holidays['isHoliday'] = 1

    # Merge on unique combinations of date and country
    date_country = df[['date', 'country']].drop_duplicates().reset_index(drop=True)
    date_country['date_str'] = date_country['date'].astype(str)
    Holidays['date_str'] = Holidays['date'].astype(str)
    date_country_holidays = pd.merge(date_country, Holidays[['date_str', 'country', 'isHoliday','holiday_name']], how='left', on=['date_str', 'country'])

    # Merge back to the original DataFrame
    df = pd.merge(df, date_country_holidays[['date', 'country', 'isHoliday','holiday_name']], how='left', on=['date', 'country'])
    df['isHoliday'] = df['isHoliday'].fillna(0).astype(int)
    df['holiday_name'] = df['holiday_name'].fillna('Not Holiday')
    
    #Add Weekend
    #df['Friday']=(df['dayname']=='Friday').astype(int) 
    #df['Saturday']=(df['dayname']=='Saturday').astype(int) 
    #df['Sunday']=(df['dayname']=='Sunday').astype(int)  
    return df,Holidays

df, Holidays = GetHolidays(df)
print(Holidays)
