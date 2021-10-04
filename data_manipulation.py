
import pandas as pd
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


