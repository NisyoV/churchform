import streamlit as st
import pandas as pd
import numpy as np
import time

import random

Key_length = 12

characters = "abcdefghijklmnopqrstuvwxyz12345678910"

keys = ""   

for index in range(Key_length):
    keys = keys + random.choice(characters)
#if "load_state" not in st.session_state: #To save the load state 
#		st.session_state.load_state = False

#def callback():
	
#		st.session_state["songs"] =  0
		
if "count" not in st.session_state: #to save the count
	st.session_state.count = 0 

st.title("Formulario de alabanzas")
Nombre, cancion1 = st.columns([1, 2])
Nombre.selectbox("Nombre", ["Yonis Alvarez", "Marisol Lopez Martinez", "Alexander ",  "Jonathan M"])



Cancion,Tono = st.columns([0.80,1 ])
Cancion.selectbox("Selecciona tu cancion", ["Increible", "Casa de Dios", "te doy gloria",  "Alabare"], )
Tono.selectbox("Tonalidad", ["C","D","E","F","G","A","B"])

button_clicked = st.button("Agregar alabanza", key = "boton")






if button_clicked :
#or st.session_state.load_state: 
	
	st.session_state.count +=1 
	counting =   st.session_state.count 

	

	New = Cancion.selectbox("Cancion" + str(counting), ["Increible", "Casa de Dios", "te doy gloria",  "Alabare"], key = "song" + keys)
	New2  = Tono.selectbox("Tonalidad de la cancion" + str(counting) , ["C","D","E","F","G","A","B"])
	counting +=1
	st.write(st.session_state)
	
	#st.session_state.load_state = True
			


#last.text_input("Primer Apellido")
email,mobile = st.columns([3,1])
email.text_input("Correo")
mobile.text_input("Telefono")

user,pw,pw2 = st.columns(3)
user.text_input("Username")
pw.text_input("Password", type = "password")
pw2.text_input("Retype Password", type = "password")
ch, bl,sub = st.columns(3)
ch.checkbox("Listo")
sub.button("Enviar")
