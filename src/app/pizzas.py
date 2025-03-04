import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df_pizzas = pd.read_csv('../data/pizzas.csv')

model = LinearRegression()
x= df_pizzas[['diametro']].values
y = df_pizzas[['preco']].values

model.fit(x, y)

st.title('Pizza Value Prediction')

diameter = st.number_input('Insert pizza diameter:')

result = model.predict([[float(diameter)]])[0][0]
st.text(f'The prize payd will be {result:.2f}.')