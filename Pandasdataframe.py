import pandas as pd

#Bob = {"Animals:" : ["Lion" ,"Tiger", "Giraffe", "Kangaroo", "Polar Bear"] , "Birds:" : ["Eagle" , "Crow", "Pigeon", "Peacock", "Dove"]}
#Bobby = pd.DataFrame(Bob)
#print(Bobby)

#Reading data from CSV
titanic = pd.read_csv("C:\\Users\\Biju\\Desktop\\Jetlearn\\Data Science\\Resources\\titanic.csv")
print(titanic)

#Displaying the first few rows
print(titanic.head())

#Displaying the last few rows
print(titanic.tail())

#Finding the number of rows and columns
print(titanic.shape)

#Extracting values of one column
fare = titanic["Fare"]

#Mean Fare:
print(fare.mean())

#What are the different passenger classes:
pclass = titanic["Pclass"]
print(pclass.value_counts())

#Summary of the data:
print(titanic.info())

#Statistical summary of data set
print(titanic.describe())

#Extracting values of multiple columns:
print(titanic[["Fare", "Name", "Age"]])

#Filtering Rows:
John = titanic[titanic["Age"]>35]
print(John)
print(John["Fare"].mean())

Rebecca = titanic[titanic["Age"]<=35]
print(Rebecca["Fare"].mean())

#Multiple functions (use or with | and and with &)
Denise = titanic[(titanic["Age"]>=18)&(titanic["Pclass"]==1)]
Robert = titanic[(titanic["Age"]>=18)&(titanic["Pclass"]==2)]
Thomas = titanic[(titanic["Age"]>=18)&(titanic["Pclass"]==3)]

print(Denise["Fare"].mean())
print(Robert["Fare"].mean())
print(Thomas["Fare"].mean())

#Index based slicing:
print(titanic.iloc[0:30:2 , 0:7:2 ]) #[Start row: End row: Step , Start column: End column: Step]

#Conditional Slicing:
print(titanic.loc[titanic["Age"]>=35 , ["Name","Sex"]])

#Changing values for a dataframe:
titanic.iloc[0:2 , 2:3] = ["Mr. Bob Marley" , "Mrs. Bobby Whinehouse Jr."]
print(titanic.head())

#Saving CSV:

titanic.to_csv("ronaldojr.csv")