# -*- coding: utf-8 -*-
"""Coding Big Data Finale.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K8MoVwy46lHajb4D65FXCykVVIFECsrr
"""

#Group 3:
#Ervino Alifio Ramadhan – 001202000133
#Markus Raja Sinabutar – 001202000038
#Mulya Fajar Ningsih Alwi – 001202000101
#Rafli Ersandy – 001202000111
#Samuel Pandohan Terampil Gultom – 001202000095

#Importing Dataset
import numpy as np 
import pandas as pd

#Setting Dataset to Variable
df=pd.read_csv('travel insurance.csv')

#Previewing Datasets
df

#Previewing NaN Values
df.isnull().sum().any

#Deleting NaN Values
df = df.dropna()

#Previewing Datasets after Deleting NaN Values
df

#Creating New Variable with a dropped Columns
inputs = df.drop("Claim", axis = "columns")
target1 = df.drop("Agency", axis = "columns")

from sklearn.preprocessing import LabelEncoder
le_agency = LabelEncoder()
le_agencytype = LabelEncoder()
le_distchan	 = LabelEncoder()
le_destination = LabelEncoder()
le_gender	 = LabelEncoder()
le_claim	 = LabelEncoder()

#Transforming String Values to Integers Value
inputs["agency_n"] = le_agency.fit_transform(inputs["Agency"])
inputs["agencytype_n"] = le_agencytype.fit_transform(inputs["Agency Type"])
inputs["distchan_n"] = le_distchan.fit_transform(inputs["Distribution Channel"])
inputs["destination_n"] = le_destination.fit_transform(inputs["Destination"])
inputs["gender_n"] = le_gender.fit_transform(inputs["Gender"])
target1["claim_n"] = le_claim.fit_transform(target1["Claim"])

#Previewing the 'inputs' Variable
inputs

#Previewing the 'target1' variable
target1

#Making New Variable with the Transformed Values
inputs_n = inputs.drop(["Agency", "Agency Type", "Distribution Channel", "Destination",	"Gender", "Product Name", "Commision (in value)"], axis="columns")
target_n = target1["claim_n"]

inputs_n

target_n

from sklearn import tree
clf = tree.DecisionTreeClassifier()

clf.fit(inputs_n, target_n)

clf.score(inputs_n, target_n)

#12 = duration real, 30 = net sales real, 35 = age real, 8 = agency_n (JZI), 
#0 = agencytype_n (Airlines), 1 = distchan_n (online), 81 = destination_n (vietnam), 1 = gender_n (male)
clf.predict([[12,30,35,8,0,1,81,1]])

#186 = duration real, -29.0 = net sales real, 81 = age real, 3 = agency_n (CBH), 
#1 = agencytype_n (Travel Agency), 0 = distchan_n (offline), 43 = destination_n (MALAYSIA), 0 = gender_n (female)
clf.predict([[186,-29.0,81,3,1,0,43,0]])