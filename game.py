import random
import streamlit as st

st.title("Let's Play Stone Paper Scissors")

player = st.selectbox("Choose :",['stone','paper','scissors'])

if st.button('Play'):
        
        st.write("You :",player)
        
        computer = random.choice(['stone','paper','scissors'])

        st.write("Computer :",computer)
        
        if player == computer:
            st.success('Draw')
        elif (player == 'stone' and computer == 'paper') or (player == 'paper' and computer == 'scissors') or (player == 'scissors' and computer == 'stone'):
            st.error('computer wins :(')
        else : 
            st.success('You win!!!')