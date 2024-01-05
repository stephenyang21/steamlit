import streamlit as st
from Attack import Attack


st.title("Wallet Attack")

walletAddress = st.text_input("Insert your wallet address:")
numberOfCharacter = st.number_input("Number of Character", 0, 10)
OkButtom = st.button("Ok")

if OkButtom:

    maliciousAddress = None

    attack = Attack()
    maliciousAddress = attack.generate_malicious_wallet(walletAddress, numberOfCharacter)
    st.write("Your malicious address is: ", maliciousAddress)