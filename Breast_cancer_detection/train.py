#importing libraries and reading data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
# import seaborn as sns
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import f1_score
# from sklearn.metrics import accuracy_score
# %matplotlib inline
df=pd.read_csv('data_1.csv')

#shows column name that contains zero values
columns=[]
for col in df.columns: 
   columns.append(col) 
a=[]
f = (df != 0).all(axis=0)
for i in range(len(f)):
    if f[i]==False:
     a.append(i) 


#for i in range(len(a)):
#     print(columns[a[i]])

for i in range(len(a)):
    df.loc[df[columns[a[i]]] == 0,columns[a[i]]] = np.NaN
    df[columns[a[i]]].fillna((df[columns[a[i]]].mean()),inplace=True)
    df_2 = df.copy()    

#for column radius_mean
#outliers check
data=df['radius_mean']
# sns.boxplot(data)
#checking skewness of radius_mean
# df['radius_mean'].skew()

# sns.distplot(df['radius_mean'])
#removing skewness
df['radius_mean_log']=np.sqrt(df['radius_mean'])
# sns.distplot(df['radius_mean_log'])
# df['radius_mean_log'].skew()

#calculating outliers
#for outliers for fractal_dimension_se
q1, q3= np.percentile(df['radius_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['radius_mean_log'])
count=0
for i in range (len(df['radius_mean_log'])):
    if (df.iloc[i]['radius_mean_log']>upper_bound) or (df.iloc[i]['radius_mean_log']<lower_bound):
        count=count+1

# print((count/len(df['radius_mean_log']))*100)
#for column concavity_se
#outliers check
data=df['concavity_se']
# sns.boxplot(data)
#checking skewness of radius_mean
# df['concavity_se'].skew()

# sns.distplot(df['concavity_se'])
#removing skewness
df['concavity_se_log']=np.cbrt(df['concavity_se'])
# sns.distplot(df['concavity_se_log'])
# df['concavity_se_log'].skew()

#calculating outliers
#for outliers for fractal_dimension_se
q1, q3= np.percentile(df['concavity_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['concavity_se_log'])
count=0
for i in range (len(df['concavity_se_log'])):
    if (df.iloc[i]['concavity_se_log']>upper_bound) or (df.iloc[i]['concavity_se_log']<lower_bound):
        count=count+1
# print((count/len(df['concavity_se_log']))*100)

#for column concave points_se
#outliers check
data=df['concave points_se']
# sns.boxplot(data)
#checking skewness of radius_mean
# df['concave points_se'].skew()
df['concave_points_se_log']=np.sqrt(df['concave points_se'])

q1, q3= np.percentile(df['concave_points_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['concave_points_se_log'])
count=0
for i in range (len(df['concave_points_se_log'])):
    if (df.iloc[i]['concave_points_se_log']>upper_bound) or (df.iloc[i]['concave_points_se_log']<lower_bound):
        count=count+1
#for column symmetry_se
#outliers check
data=df['symmetry_se']
# sns.boxplot(data)
#checking skewness of radius_mean
# df['symmetry_se'].skew()

# sns.distplot(df['symmetry_se'])
#removing skewness
df['symmetry_se_log']=np.log(df['symmetry_se'])
# sns.distplot(df['symmetry_se_log'])
# df['symmetry_se_log'].skew()

q1, q3= np.percentile(df['symmetry_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['symmetry_se_log'])
count=0
for i in range (len(df['symmetry_se_log'])):
    if (df.iloc[i]['symmetry_se_log']>upper_bound) or (df.iloc[i]['symmetry_se_log']<lower_bound):
        count=count+1
# print((count/len(df['symmetry_se_log']))*100)

data=df['fractal_dimension_se']
df['fractal_dimension_se_log']=np.log(df['fractal_dimension_se'])

#calculating outliers
#for outliers for fractal_dimension_se
q1, q3= np.percentile(df['fractal_dimension_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['fractal_dimension_se_log'])
count=0
for i in range (len(df['fractal_dimension_se_log'])):
    if (df.iloc[i]['fractal_dimension_se_log']>upper_bound) or (df.iloc[i]['fractal_dimension_se_log']<lower_bound):
        count=count+1
# print((count/len(df['fractal_dimension_se_log']))*100)

data=df['radius_worst']
df['radius_worst_log']=np.log(df['radius_worst'])

#calculating outliers
#for outliers for radius_worst_log
q1, q3= np.percentile(df['radius_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['radius_worst_log'])
count=0
for i in range (len(df['radius_worst_log'])):
    if (df.iloc[i]['radius_worst_log']>upper_bound) or (df.iloc[i]['radius_worst_log']<lower_bound):
        count=count+1



        
# sns.distplot(df['texture_worst'])
#removing skewness
df['texture_worst_log']=np.cbrt(df['texture_worst'])
# sns.distplot(df['texture_worst_log'])
# df['texture_worst_log'].skew()

#calculating outliers
#for outliers for texture_worst_log
q1, q3= np.percentile(df['texture_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['texture_worst_log'])
count=0
for i in range (len(df['texture_worst_log'])):
    if (df.iloc[i]['texture_worst_log']>upper_bound) or (df.iloc[i]['texture_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['texture_worst_log']))*100)

#for column perimeter_worst        
#outliers check
data=df['perimeter_worst']
# sns.boxplot(data)
#checking skewness of radius_mean
# df['perimeter_worst'].skew()

# sns.distplot(df['perimeter_worst'])
#removing skewness
df['perimeter_worst_log']=np.cbrt(df['perimeter_worst'])
# sns.distplot(df['perimeter_worst_log'])
# df['perimeter_worst_log'].skew()

#calculating outliers
#for outliers for perimeter_worst_log
q1, q3= np.percentile(df['perimeter_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['perimeter_worst_log'])
count=0
for i in range (len(df['perimeter_worst_log'])):
    if (df.iloc[i]['perimeter_worst_log']>upper_bound) or (df.iloc[i]['perimeter_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['perimeter_worst_log']))*100)

#for column area_worst        
#outliers check
data=df['area_worst']
# sns.boxplot(data)
#checking skewness of radius_mean
# df['area_worst'].skew()

# sns.distplot(df['area_worst'])
#removing skewness
df['area_worst_log']=np.cbrt(df['area_worst'])
# sns.distplot(df['area_worst_log'])
# df['area_worst_log'].skew()

#calculating outliers
#for outliers for area_worst_log
q1, q3= np.percentile(df['area_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['area_worst_log'])
count=0
for i in range (len(df['area_worst_log'])):
    if (df.iloc[i]['area_worst_log']>upper_bound) or (df.iloc[i]['area_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['area_worst_log']))*100)

#for column radius_mean
#outliers check
data=df['radius_mean']
# sns.boxplot(data)
# check Sqewness
# df['radius_mean'].skew()

#  Outliers And Sqewness of radius_mean
# sns.distplot(df['radius_mean'])
# Removing the skewness by Cbrt method
df['radius_mean_log']=np.cbrt(df['radius_mean'])
# sns.distplot(df['radius_mean_log'])
# df['radius_mean_log'].skew()

q1, q3= np.percentile(df['radius_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['radius_mean_log'])
count=0
for i in range (len(df['radius_mean_log'])):
    if (df.iloc[i]['radius_mean_log']>upper_bound) or (df.iloc[i]['radius_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['radius_mean_log']))*100)

#  Outliers And Sqewness of texture_mean
# sns.distplot(df['texture_mean'])
# Removing the skewness by Cbrt method
df['texture_mean_log']=np.cbrt(df['texture_mean'])
# sns.distplot(df['texture_mean_log'])
# df['texture_mean_log'].skew()

q1, q3= np.percentile(df['texture_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['texture_mean_log'])
count=0
for i in range (len(df['texture_mean_log'])):
    if(df.iloc[i]['texture_mean_log']>upper_bound) or (df.iloc[i]['texture_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['texture_mean_log']))*100)

#for column perimeter_mean
#outliers check
data=df['perimeter_mean']
# sns.boxplot(data)
# check Sqewness
# df['perimeter_mean'].skew()

#  Outliers And Sqewness of perimeter_mean
# sns.distplot(df['perimeter_mean'])
# Removing the skewness by Cbrt method
df['perimeter_mean_log']=np.cbrt(df['perimeter_mean'])
# sns.distplot(df['perimeter_mean_log'])
# df['perimeter_mean_log'].skew()

q1, q3= np.percentile(df['perimeter_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['perimeter_mean_log'])
count=0
for i in range (len(df['perimeter_mean_log'])):
    if (df.iloc[i]['perimeter_mean_log']>upper_bound) or (df.iloc[i]['perimeter_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['perimeter_mean_log']))*100)

#for column area_mean
#outliers check
data=df['area_mean']
# sns.boxplot(data)
# check Sqewness
# df['area_mean'].skew()

#  Outliers And Sqewness of area_mean
# sns.distplot(df['area_mean'])
# Removing the skewness by Cbrt method
df['area_mean_log']=np.cbrt(df['area_mean'])
# sns.distplot(df['area_mean_log'])
# df['area_mean_log'].skew()

q1, q3= np.percentile(df['area_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['area_mean_log'])
count=0
for i in range (len(df['area_mean_log'])):
    if (df.iloc[i]['area_mean_log']>upper_bound) or (df.iloc[i]['area_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['area_mean_log']))*100)

#for column smoothness_mean
#outliers check
data=df['smoothness_mean']
# sns.boxplot(data)
# check Sqewness
# df['smoothness_mean'].skew()

#  Outliers And Sqewness of smoothness_mean
# sns.distplot(df['smoothness_mean'])
# Removing the skewness by Cbrt method
df['smoothness_mean_log']=np.cbrt(df['smoothness_mean'])
# sns.distplot(df['smoothness_mean_log'])
# df['smoothness_mean_log'].skew()

q1, q3= np.percentile(df['smoothness_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1-(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['smoothness_mean_log'])
count=0
for i in range (len(df['smoothness_mean_log'])):
    if (df.iloc[i]['smoothness_mean_log']>upper_bound) or (df.iloc[i]['smoothness_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['smoothness_mean_log']))*100)

#for column compactness_mean
#outliers check
data=df['compactness_mean']
# sns.boxplot(data)
# check Sqewness
# df['compactness_mean'].skew()

#  Outliers And Sqewness of compactness_mean
# sns.distplot(df['compactness_mean'])
# Removing the skewness by Cbrt method
df['compactness_mean_log']=np.cbrt(df['compactness_mean'])
# sns.distplot(df['compactness_mean_log'])
# df['compactness_mean_log'].skew()

#calculating the outliers
q1, q3= np.percentile(df['compactness_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['compactness_mean_log'])
count=0
for i in range (len(df['compactness_mean_log'])):
    if (df.iloc[i]['compactness_mean_log']>upper_bound) or (df.iloc[i]['compactness_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['compactness_mean_log']))*100)

#for column concavity_mean
#outliers check
data=df['concavity_mean']
# sns.boxplot(data)
# check Sqewness
# df['concavity_mean'].skew()

#  Outliers And Sqewness of concavity_mean
# sns.distplot(df['concavity_mean'])
# Removing the skewness by Cbrt method
df['concavity_mean_log']=np.cbrt(df['concavity_mean'])
# sns.distplot(df['concavity_mean_log'])
# df['concavity_mean_log'].skew()

#calculating the outliers
q1, q3= np.percentile(df['concavity_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['concavity_mean_log'])
count=0
for i in range (len(df['concavity_mean_log'])):
    if (df.iloc[i]['concavity_mean_log']>upper_bound) or (df.iloc[i]['concavity_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['concavity_mean_log']))*100)
#for column concave points_mean
#outliers check
data=df['concave points_mean']
# sns.boxplot(data)
# check Sqewness
# df['concave points_mean'].skew()

#  Outliers And Sqewness of concave points_mean
# sns.distplot(df['concave points_mean'])
# Removing the skewness by Cbrt method
df['concave_points_mean_log']=np.cbrt(df['concave points_mean'])
# sns.distplot(df['concave_points_mean_log'])
# df['concave_points_mean_log'].skew()

#calculating the outliers
q1, q3= np.percentile(df['concave_points_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['concave_points_mean_log'])
count=0
for i in range (len(df['concave_points_mean_log'])):
    if (df.iloc[i]['concave_points_mean_log']>upper_bound) or (df.iloc[i]['concave_points_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['concave_points_mean_log']))*100)

#for column symmetry_mean
#outliers check
data=df['symmetry_mean']
# sns.boxplot(data)
# check Sqewness
# df['symmetry_mean'].skew()

#  Outliers And Sqewness of symmetry_mean
# sns.distplot(df['symmetry_mean'])
# Removing the skewness by Cbrt method
df['symmetry_mean_log']=np.cbrt(df['symmetry_mean'])
# sns.distplot(df['symmetry_mean_log'])
# df['symmetry_mean_log'].skew()

#calculating the outliers
q1, q3= np.percentile(df['symmetry_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['symmetry_mean_log'])
count=0
for i in range (len(df['symmetry_mean_log'])):
    if (df.iloc[i]['symmetry_mean_log']>upper_bound) or (df.iloc[i]['symmetry_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['symmetry_mean_log']))*100)

# for column fractal_dimension_mean
#outliers check
data=df['fractal_dimension_mean']
# sns.boxplot(data)
# check Sqewness
# df['fractal_dimension_mean'].skew()

#  Outliers And Sqewness of fractal_dimension_mean
# sns.distplot(df['fractal_dimension_mean'])
# Removing the skewness by Cbrt method
df['fractal_dimension_mean_log']=np.cbrt(df['fractal_dimension_mean'])
# sns.distplot(df['fractal_dimension_mean_log'])
# df['fractal_dimension_mean_log'].skew()

#ating the outliers
q1, q3= np.percentile(df['fractal_dimension_mean_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['fractal_dimension_mean_log'])
count=0
for i in range (len(df['fractal_dimension_mean_log'])):
    if (df.iloc[i]['fractal_dimension_mean_log']>upper_bound) or (df.iloc[i]['fractal_dimension_mean_log']<lower_bound):
        count=count+1
# print((count/len(df['fractal_dimension_mean_log']))*100)

# for column radius_se
#outliers check
data=df['radius_se']
# sns.boxplot(data)
# check Sqewness
# df['radius_se'].skew()

#  Outliers And Sqewness of radius_se
# sns.distplot(df['radius_se'])
# Removing the skewness by Cbrt method
df['radius_se_log']=np.log(df['radius_se'])
# sns.distplot(df['radius_se_log'])
# df['radius_se_log'].skew()

#ating the outliers
q1, q3= np.percentile(df['radius_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['radius_se_log'])
count=0
for i in range (len(df['radius_se_log'])):
    if (df.iloc[i]['radius_se_log']>upper_bound) or (df.iloc[i]['radius_se_log']<lower_bound):
        count=count+1
# print((count/len(df['radius_se_log']))*100)

# for column texture_se
#outliers check
data=df['texture_se']
# sns.boxplot(data)
# check Sqewness
# df['texture_se'].skew()
#  Outliers And Sqewness of radius_se
# sns.distplot(df['texture_se'])
# Removing the skewness by Cbrt method
df['texture_se_log']=np.cbrt(df['texture_se'])
# sns.distplot(df['texture_se_log'])
# df['texture_se_log'].skew()

#ating the outliers
q1, q3= np.percentile(df['texture_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['texture_se_log'])
count=0
for i in range (len(df['texture_se_log'])):
    if (df.iloc[i]['texture_se_log']>upper_bound) or (df.iloc[i]['texture_se_log']<lower_bound):
        count=count+1
# print((count/len(df['texture_se_log']))*100)

# for column perimeter_se
#outliers check
data=df['perimeter_se']
# sns.boxplot(data)
# check Sqewness
# df['perimeter_se'].skew()

#  Outliers And Sqewness of radius_se
# sns.distplot(df['perimeter_se'])
# Removing the skewness by Cbrt method
df['perimeter_se_log']=np.log(df['perimeter_se'])
# sns.distplot(df['perimeter_se_log'])
# df['perimeter_se_log'].skew()

#ating the outliers
q1, q3= np.percentile(df['perimeter_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['perimeter_se_log'])
count=0
for i in range (len(df['perimeter_se_log'])):
    if (df.iloc[i]['perimeter_se_log']>upper_bound) or (df.iloc[i]['perimeter_se_log']<lower_bound):
        count=count+1
# print((count/len(df['perimeter_se_log']))*100)

# for column area_se
#outliers check
data=df['area_se']
# sns.boxplot(data)
# check Sqewness
# df['area_se'].skew()

#  Outliers And Sqewness of area_se
# sns.distplot(df['area_se'])
# Removing the skewness by Cbrt method
df['area_se_log']=np.log(df['area_se'])
# sns.distplot(df['area_se_log'])
# df['area_se_log'].skew()

#calculating the outliers
q1, q3= np.percentile(df['area_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['area_se_log'])
count=0
for i in range (len(df['area_se_log'])):
    if (df.iloc[i]['area_se_log']>upper_bound) or (df.iloc[i]['area_se_log']<lower_bound):
        count=count+1
# print((count/len(df['area_se_log']))*100)

# for column smoothness_se
#outliers check
data=df['smoothness_se']
# sns.boxplot(data)
# check Sqewness
# df['smoothness_se'].skew()

#  Outliers And Sqewness of smoothness_se
# sns.distplot(df['smoothness_se'])
# Removing the skewness by Cbrt method
df['smoothness_se_log']=np.cbrt(df['smoothness_se'])
# sns.distplot(df['smoothness_se_log'])
# df['smoothness_se_log'].skew()

#calculating the outliers
q1, q3= np.percentile(df['smoothness_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['smoothness_se_log'])
count=0
for i in range (len(df['smoothness_se_log'])):
    if (df.iloc[i]['smoothness_se_log']>upper_bound) or (df.iloc[i]['smoothness_se_log']<lower_bound):
        count=count+1
# print((count/len(df['smoothness_se_log']))*100)

# for column compactness_se
#outliers check
data=df['compactness_se']
# sns.boxplot(data)
# check Sqewness
# df['compactness_se'].skew()

#  Outliers And Sqewness of compactness_se
# sns.distplot(df['compactness_se'])
# Removing the skewness by Cbrt method
df['compactness_se_log']=np.cbrt(df['compactness_se'])
# sns.distplot(df['compactness_se_log'])
# df['compactness_se_log'].skew()

#calculating the outliers
q1, q3= np.percentile(df['compactness_se_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['compactness_se_log'])
count=0
for i in range (len(df['compactness_se_log'])):
    if (df.iloc[i]['compactness_se_log']>upper_bound) or (df.iloc[i]['compactness_se_log']<lower_bound):
        count=count+1
# print((count/len(df['compactness_se_log']))*100)

# for column smoothness_worst
#outliers check
data=df['smoothness_worst']
# sns.boxplot(data)
# check Sqewness
# df['smoothness_worst'].skew()

#  Outliers And Sqewness of smoothness_worst
# sns.distplot(df['smoothness_worst'])
# Removing the skewness by Cbrt method
df['smoothness_worst_log']=np.cbrt(df['smoothness_worst'])
# sns.distplot(df['smoothness_worst_log'])
# df['smoothness_worst_log'].skew()

# Calculating the outliers for smoothness_worst

q1, q3= np.percentile(df['smoothness_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['smoothness_worst_log'])
count=0
for i in range (len(df['smoothness_worst_log'])):
    if (df.iloc[i]['smoothness_worst_log']>upper_bound) or (df.iloc[i]['smoothness_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['smoothness_worst_log']))*100)

#  Outliers And Sqewness of compactness_worst
# sns.distplot(df['compactness_worst'])
# Removing the skewness by Cbrt method
df['compactness_worst_log']=np.cbrt(df['compactness_worst'])
# sns.distplot(df['compactness_worst_log'])
# df['compactness_worst_log'].skew()

# Calculating the outliers for compactness_worst

q1, q3= np.percentile(df['compactness_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['compactness_worst_log'])
count=0
for i in range (len(df['compactness_worst_log'])):
    if (df.iloc[i]['compactness_worst_log']>upper_bound) or (df.iloc[i]['compactness_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['compactness_worst_log']))*100)

# for column concavity_worst
#outliers check
data=df['concavity_worst']
# sns.boxplot(data)
# check Sqewness
# df['concavity_worst'].skew()
#  Outliers And Sqewness of concavity_worst
# sns.distplot(df['concavity_worst'])
# Removing the skewness by Cbrt method
df['concavity_worst_log']=np.sqrt(df['concavity_worst'])
# sns.distplot(df['concavity_worst_log'])
# df['concavity_worst_log'].skew()

q1, q3= np.percentile(df['concavity_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['concavity_worst_log'])
count=0
for i in range (len(df['concavity_worst_log'])):
    if (df.iloc[i]['concavity_worst_log']>upper_bound) or (df.iloc[i]['concavity_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['concavity_worst_log']))*100)

# for column concave points_worst
#outliers check
data=df['concave points_worst']
# sns.boxplot(data)
# check Sqewness
# df['concave points_worst'].skew()
#  Outliers And Sqewness of concave points_worst
# sns.distplot(df['concave points_worst'])
# Removing the skewness by sqrt method
df['concave_points_worst_log']=np.sqrt(df['concave points_worst'])
# sns.distplot(df['concave_oints_worst_log'])
# df['concave_points_worst_log'].skew()

# Calculating the outliers for concave points_worst 


q1, q3= np.percentile(df['concave_points_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['concave_points_worst_log'])
count=0
for i in range (len(df['concave_points_worst_log'])):
    if (df.iloc[i]['concave_points_worst_log']>upper_bound) or (df.iloc[i]['concave_points_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['concave_points_worst_log']))*100)

# for column symmetry_worst
#outliers check
data=df['symmetry_worst']
# sns.boxplot(data)
# check Sqewness
# df['symmetry_worst'].skew()

#  Outliers And Sqewness of symmetry_worst
# sns.distplot(df['symmetry_worst'])
# Removing the skewness by Cbrt method
df['symmetry_worst_log']=np.cbrt(df['symmetry_worst'])
# sns.distplot(df['symmetry_worst_log'])
# df['symmetry_worst_log'].skew()

# Calculating the outliers for symmetry_worst


q1, q3= np.percentile(df['symmetry_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['symmetry_worst_log'])
count=0
for i in range (len(df['symmetry_worst_log'])):
    if (df.iloc[i]['symmetry_worst_log']>upper_bound) or (df.iloc[i]['symmetry_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['symmetry_worst_log']))*100)


# for column fractal_dimension_worst
#outliers check
data=df['fractal_dimension_worst']
# sns.boxplot(data)
# check Sqewness
# df['fractal_dimension_worst'].skew()

#  Outliers And Sqewness of fractal_dimension_worst
# sns.distplot(df['fractal_dimension_worst'])
# Removing the skewness by Cbrt method
df['fractal_dimension_worst_log']=np.log(df['fractal_dimension_worst'])
# sns.distplot(df['fractal_dimension_worst_log'])
df['fractal_dimension_worst_log'].skew()

# Calculating the outliers for fractal_dimension_worst


q1, q3= np.percentile(df['fractal_dimension_worst_log'],[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
median=np.median(df['fractal_dimension_worst_log'])
count=0
for i in range (len(df['fractal_dimension_worst_log'])):
    if (df.iloc[i]['fractal_dimension_worst_log']>upper_bound) or (df.iloc[i]['fractal_dimension_worst_log']<lower_bound):
        count=count+1
# print((count/len(df['fractal_dimension_worst_log']))*100)

# sns.countplot(x='diagnosis',data=df)

from sklearn.preprocessing import LabelEncoder as LE
df['diagnosis_1']=LE().fit_transform(df['diagnosis'])
# print ("\n\n", df.head(15))

df.drop(['radius_mean','Unnamed: 32','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean','concave points_mean','texture_worst','perimeter_worst','area_worst','smoothness_worst','fractal_dimension_mean','radius_se','texture_se','perimeter_se','area_se','smoothness_se','compactness_se','concavity_se','concave points_se','symmetry_se','fractal_dimension_se','radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst','concave points_worst','symmetry_worst','fractal_dimension_worst'],axis=1,inplace=True)
df.drop(['symmetry_mean','diagnosis'],axis=1,inplace=True)
# df.head(5)
# heatmap
# plt.figure(figsize=(25,15))
# sns.heatmap(df.corr(),annot=True)
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
x = df.iloc[:,0:32]  
y = df.iloc[:,-1] 

bestfeatures=SelectKBest(score_func=f_classif,k=3)
fit=bestfeatures.fit(x,y)

dfscores=pd.DataFrame(fit.scores_)#creating a df containing the scores of the column
dfcolumns=pd.DataFrame(x.columns)
#create a dataframe with the columns and their scores
featurescores=pd.concat([dfcolumns,dfscores],axis=1)
featurescores.columns=['Features','Scores']
# print(featurescores)

#separate majority and minority class
from sklearn.utils import resample
df_majority=df[df.diagnosis_1==1]
df_minority=df[df.diagnosis_1==0]
#upsampling of minority class

df_minority_upsampled=resample(df_minority,replace=True,n_samples=1200,random_state=123)
  #n-sample->to match majority class,random_state->reproductible results,
 #replace->sample with replacements
#display new class
#combine majority class with upsampled minority class
df_upsampled=pd.concat([df_majority,df_minority_upsampled])
df_upsampled.diagnosis_1.value_counts()

df.drop(['fractal_dimension_se_log','symmetry_se_log','fractal_dimension_mean_log','texture_se_log','smoothness_se_log','symmetry_mean_log','id','fractal_dimension_worst_log'],axis=1,inplace=True)

# 'fractal_dimension_se_log','symmetry_se_log',
#Train data

from sklearn.model_selection import train_test_split
X=df.drop('diagnosis_1',axis=1)
Y=df['diagnosis_1']

# X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=5)

#decision tree



#splitting into train and test
# from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=5)


#performing training using entropy
from sklearn.tree import DecisionTreeClassifier
classifier_entropy=DecisionTreeClassifier(criterion='entropy',random_state=42,max_depth=3)
#creating model
classifier_entropy.fit(X_train,Y_train)

#make predictions
# y_pred=classifier_entropy.predict(X_test)



#k nearest neighbour
# from sklearn.neighbors import NearestNeighbors
# classifier=KNeighborsClassifier(n_neighbors=11,p=2,metric='euclidean')
# classifier.fit(X_train,Y_train)
#
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=10)
rf.fit(X_train,Y_train)
# d=pd.DataFrame(dict(radius_mean_log=[],concavity_se_log=[],concave_points_se_log=[],radius_worst_log=[],texture_worst_log=[],perimeter_worst_log=[],area_worst_log=[],texture_mean_log=[],perimeter_mean_log=[],area_mean_log=[],smoothness_mean_log=[],compactness_mean_log=[],concavity_mean_log=[],concave_points_mean_log=[],radius_se_log=[],perimeter_se_log=[],area_se_log=[],compactness_se_log=[],smoothness_worst_log=[],compactness_worst_log=[],concavity_worst_log=[],concave_points_worst_log=[],symmetry_worst_log=[]))


# new={'radius_mean_log':2.482545,'concavity_se_log':0.329457,'concave_points_se_log':0.104067,'radius_worst_log':3.009142,'texture_worst_log':3.323493,'perimeter_worst_log':5.305015,'area_worst_log':10.826478,'texture_mean_log':2.934507,'perimeter_mean_log':4.678428,'area_mean_log':9.01397,'smoothness_mean_log':0.476514,'compactness_mean_log':0.55364,'concavity_mean_log':0.552113,'concave_points_mean_log':0.443969,'radius_se_log':-0.823256,'perimeter_se_log':1.252191,'area_se_log':3.772761,'compactness_se_log':0.312679,'smoothness_worst_log':0.547482,'compactness_worst_log':0.848556,'concavity_worst_log':0.795927,'concave_points_worst_log':0.449889,'symmetry_worst_log':0.73846}

# d=d.append(new,ignore_index=True)
# rf.predict_proba(d)
# z=x_test.head(3)
# rf.predict_proba(z)
#k nearest neighbour
# classifier_entropy.predict_proba(z)

import pickle
filename='a.sav'
pickle.dump(rf,open(filename,'wb'))