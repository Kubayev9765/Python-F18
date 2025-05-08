import pandas as pd
from datetime import datetime
df = pd.read_csv('stackoverflow_qa.csv')

1
con1=df['creationdate']<'2014-01-01 00:00:00'
con2=df['score']>50
con3=(df['score']>50 ) & (df['score']<100)
con4=df['quest_name']=='Scott Boston'
con5=df['answercount']>5
con6=(df['creationdate'] > '2014-03-01 00:00:00') & (df['creationdate']<'2014-10-01 00:00:00')
con7=((df['score']>5) & (df['score']<10)) ^ (df['viewcount']>10000)
con8=df['quest_name'] !='Scott Boston'
print(con)

1.1.
final_con=con1
colum=['creationdate']
new_df=df[final_con]
new_df.loc[final_con,colum]
print(new_df)

1.2.
final=con2
col=['score']
new=df[final]
new.loc[final,col]
print(new)

1.3.
final=con3
col=['score']
new=df[final]
new.loc[final,col]
print(new)


1.4.
final=con4
col=['quest_name']
col
final
new_r=df[final]
new_r.loc[con4,col]
print(new_r)


1.5.
final=con5
col=['answercount']
new_ans_count=df[final]
new_ans_count.loc[con5,col].head()
print(new_ans_count)

1.6.
final=con6
col=['creationdate']
new_cr_da=df[final]
new_cr_da.loc[con6, col]
print(new_cr-da)

1.7
final=con7
new_con7=df[final]
col=['score','viewcount']
new_con7.loc[con7, col]
print(new_con7)

1.8.
final=con8
new_qu=df[final]
col=['quest_name']
new_qu.loc[con8,col]
print(new_qu)

2.
import pandas as pd
from datetime import datetime
df_2=pd.read_csv('titanic.csv')
df_2.head()

2.1.
con1=df_2['Age']>=20
con2=df_2['Age']<=30
con3=df_2['Sex']=='female'
con4=df_2['Pclass']==1
finall=con1 & con2 & con3 & con4
column= ['Age','Sex','Pclass']
new_rus=df_2.loc[finall, column]
new_rus
print(new_rus)

2.2.
con1=df_2['Fare']>100
finall=con1
col=['Fare']
new_df=df_2.loc[finall,col]
new_df
print(new_df)

2.3.
con1= df_2['Survived'] == 1
con2=df_2['SibSp'] == 0
con3=df_2['Parch'] == 0
col=['Survived', 'SibSp', 'Parch']
finall=con1&con2&con3
new_df=df_2.loc[finall,col]
new_df
print(new_df)

2.4.
con1= df_2['Embarked']=='C'
con2= df_2['Fare']>=50
final= con1 & con2
col=['Embarked','Fare']
new_df=df_2[final]
new_df[col]
print(new_df)

2.5.
con1=df_2['SibSp'] > 0
con2= df_2['Parch'] > 0
final= con1 & con2
colum=['SibSp', 'Parch']
new_df=df_2[final]
new_df[colum]

2.6.
con1=df_2['Age']<=15
con2=df_2['Survived']==0
col=['Age', 'Survived']
final=con1& con2
new_df=df_2.loc[final, col]
new_df
print(new_df)

2.7.
con1=df_2['Cabin'].notna()
con2=df_2['Fare']>200
final=con1 & con2
col=['Cabin', 'Fare']
new_df=df_2.loc[final, col]
new_df
print(new_df)

2.8.
odd_passenger_ids = df_2[df_2['PassengerId'] % 2 == 1]
con=df_2['PassengerId']% 2==1
col=['PassengerId']
new_df=df_2.loc[con, col]
new_df
print(new_df)

2.9.
con=df_2[~df_2['Ticket'].duplicated(keep=False)]
col=['Ticket']
new_df=df_2.loc[con,col]
new_df
print(new_df)

2.10
con1=df_2['Name'].str.contains('Miss')
con2=df_2['Pclass'] == 1
col=['Name', 'Pclass']
final= con1 & con2
new_df=df_2.loc[final, col]
new_df
print(new_df)

