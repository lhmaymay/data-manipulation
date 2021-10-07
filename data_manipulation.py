
import pandas as pd
df = pd.read_csv(‘file.csv’, header=0, index_col=0, quotechar=’”’,sep=’:’, na_values = [‘na’, ‘-‘, ‘.’, ‘’])

# Reading the password from a text file
with open('credentials.txt','r') as f:
    password = f.read().strip()

# Establishing a connection to mysql database 
conn = mysql.connector.connect(host='127.0.0.1',port=3306, username='root',password=password,auth_plugin='mysql_native_password',
                               database='mydb')
# Reading the data 
people = pd.read_sql('SELECT * FROM people',conn)
preferences = pd.read_sql('SELECT * FROM preferences',conn)
job = pd.read_sql('SELECT * FROM job',conn)

# Closing the connection 
conn.close()
    
churn = pd.read_csv("/content/churn.csv")

# compare to sql
# DESC CHURN;
churn.dtypes
# SELECT * FROM CHURN LIMIT 5;
churn.head(5)
# SELECT CustomerId, Geography FROM CHURN;
churn[['CustomerId', 'Geography']]
churn[churn.Geography == 'France'][['CustomerId','Geography']][:5]

churn.Geography.unique()
# array(['France', 'Spain', 'Germany'], dtype=object)
churn.Geography.nunique()

churn.Geography.value_counts()
churn[['Geography','Age']].groupby('Geography').mean().sort_values(by='Age', ascending=False)

combined = pd.concat([people,preferences,job],axis=1) # using concat function because we have more than 2 dataframes
combined.drop('id',axis=1,inplace=True) # dropping the id column as it is not significant in analysis and it is repeated

bins = [0,20,60,100] # create bins for age group
labels = ['Young','Working','Senior Citizen'] #create labels for age groups 
combined['AGE GROUP'] = pd.cut(combined['AGE'],bins=bins, labels=labels) # create a new column for age groups


age_grp_gender = pd.DataFrame(combined.groupby(by=['GENDER','AGE GROUP'])['AGE GROUP'].count())
age_grp_men = age_grp_gender.xs('M').rename(columns={'AGE GROUP':'NUM_MEN'})
age_grp_women = age_grp_gender.xs('F').rename(columns={'AGE GROUP':'NUM_WOMEN'})

tips.assign(tip_rate=tips["tip"] / tips["total_bill"])
