
import pandas as pd
# Reading the password from a text file
with open('credentials.txt','r') as f:
    password = f.read().strip()
    
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


