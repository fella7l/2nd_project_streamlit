import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('medical_students_dataset.csv')

st.title('Data Analysis of Future Healthcare Professionals')

st.header('Students_informations')

B = df.dropna(subset=['Student ID','Blood Type','Gender', 'Diabetes'])

st.sidebar.subheader('Welcome to Medical Students Data Analysis!')
st.sidebar.write("""
This Streamlit app allows you to explore and analyze medical students' data.
Use the filters in the sidebar to customize your analysis.
""")

Gender_filter = st.sidebar.selectbox('Select Gender:', B['Gender'].unique())

# Filter data by genre
filtered_B= B[B['Gender'] == Gender_filter]

# Display the filtered dataframe
st.write(filtered_B)

B.loc[B['Smoking'].isna(), 'Smoking'] = 'No'



st.subheader('Mean Age')
mean_age_value = filtered_B['Age'].mean().round(2)
st.markdown(f'<div style="border:1px solid black; padding:10px">{mean_age_value}</div>', unsafe_allow_html=True)
 
st.subheader('Average Weight')           
average_weight = B['Weight'].mean().round(2)
st.markdown(f'<div style="border:1px solid black; padding:10px">{average_weight}</div>', unsafe_allow_html=True)


st.subheader('Medium Height')
medium_height_value = filtered_B['Height'].mean().round(2)
st.markdown(f'<div style="border:1px solid black; padding:10px">{medium_height_value}</div>', unsafe_allow_html=True)



float_column = B.select_dtypes(include=['float64', 'int64']).columns

B[float_column] = B[float_column].apply(lambda col: col.fillna(col.mean().round()))

st.header('Gender Distribution in Medical Students')

st.subheader('1_Number of Students per Gender')

Number_per_Gender = B['Gender'].value_counts()
Number_per_Gender


percentage_by_gender = Number_per_Gender / len(df['Gender']) * 100
percentage_by_gender = percentage_by_gender.round(2)

# Affichage Streamlit

st.subheader('2_Percentage of Students per Gender')

# Création du graphique en secteurs (pie chart) avec Matplotlib
fig, ax = plt.subplots(figsize=(6, 6))
fig, ax = plt.subplots(figsize=(6, 6))
colors = ['palevioletred', 'steelblue']
wedges, texts, autotexts = ax.pie(percentage_by_gender, labels=percentage_by_gender.index, autopct='%1.1f%%', startangle=180, colors=colors)
ax.set_title('Percentage of Gender')

# Ajout de la légende
ax.legend(wedges, percentage_by_gender.index, title="Gender", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize='small')

# Affichage du graphique avec Streamlit
st.pyplot(fig)



st.header( 'Diabetes Distribution Among Students')
st.subheader('Number of Students with Diabetes')
Having_diabetes = B.value_counts('Diabetes')
Having_diabetes


# Création du graphique en barres avec Matplotlib
plt.figure(figsize=(8, 6))
colors = ['slategray']
plt.bar(Having_diabetes.index, Having_diabetes.values, color=colors)
plt.title('Students Having Diabetes')

# Affichage du graphique avec Streamlit
st.pyplot(plt)
# Affichage du graphique avec Streamlit


Having_diabetes_and_Smoking = pd.crosstab(B['Gender'], B['Smoking'])
Having_diabetes_and_Smoking




st.header('Number of Smoking Students')
Smoking_students = B.value_counts('Smoking')
Smoking_students

plt.figure(figsize=(8, 6))
colors = 'navy'
z = B['Smoking'].value_counts().plot(kind='bar', color=colors)
z.set_title('Number of Smoking Students')
z.set_xlabel('Smoking Habits')
z.set_ylabel('Number of Students')

# Display the graph with Streamlit
st.pyplot(plt)
st.header('The Relationship Between Diabetes and Smoking')
l= pd.crosstab(B['Smoking'], B['Diabetes'])
l


st.header('BMI Groups Among Students')
intervalle_binsBMI = [0, 18.5, 24.9,30, float('inf')]

labels_BMI = ['Underweight','Healthy_Weight','Overweight','Obesity']

B['BMI_groupe'] = pd.cut(B['BMI'], bins=intervalle_binsBMI,labels= labels_BMI, right=False)

st.subheader('Number of Students in Each BMI Group')

o= pd.crosstab(B['BMI_groupe'], B['Gender'])
o
plt.figure(figsize=(8, 6))
colors = ('steelblue')
ax = B['BMI_groupe'].value_counts().sort_index().plot(kind='bar', color=colors)
ax.set_title('BMI Groups')
ax.set_xlabel('BMI Group')
ax.set_ylabel('Number of Students')

# Display the graph with Streamlit
st.pyplot(plt)


st.header('The Relationship Between BMI and Diabetes')
m= pd.crosstab( B['BMI_groupe'],B['Diabetes'])
m
colors = ['palevioletred', 'steelblue']
fig, ax = plt.subplots()
m.plot(kind='bar', stacked=True, color=colors, ax=ax)

# AjBMI_groupeouter des étiquettes et des titres
ax.set_xlabel('BMI_groupe')
ax.set_ylabel('Count')
ax.set_title('Relation Between Diabetes and BMI Groups')

# Afficher la légende
ax.legend(title='BMI groupe')

# Affichage du graphique avec Streamlit
st.pyplot(fig)


intervalle_bins = [70, 100, 140, float('inf')]

labels = ['low_pressure','Normal_pressure','high_pressure']


B['Groupe_blood-prs'] = pd.cut(B['Blood Pressure'], bins=intervalle_bins, labels=labels, right=False)

st.header(' Heart Rate Vs blood-prs')



intervalle_bins = [0, 60, 100, float('inf')]
labels = ['Bradycardia','Normal','Tachycardia']
B['Groupe_heart_rate'] = pd.cut(B['Heart Rate'], bins=intervalle_bins, labels=labels, right=False)
h= pd.crosstab(B['Groupe_blood-prs'], B['Groupe_heart_rate'])
h
