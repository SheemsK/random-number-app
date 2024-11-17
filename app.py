import streamlit as st
import random

# Set the title of the app
st.title("Random Number Generator") 

# Add a button to generate a random number
if st.button("Generate Random Number"): 
	# Generate a random number between 1 and 10 
	random_number = random.randint(1, 10)
	# Display the random number 
	st.success(f"The random number is: {random_number}")