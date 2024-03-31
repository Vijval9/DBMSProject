from time import sleep
import mysql.connector
import streamlit as st
#from streamlit.state.session_state import SessionState

db = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    password = "Duppu0903)()#",
    database = "mydb"
    
    
)

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    [data-testid="collapsedControl"] { display: none }
    </style>
""", unsafe_allow_html=True)




global cr
cr = db.cursor()
cr.execute("use mydb")

def buy(cr):
    
    cr.execute("select * from cartitem;")
    recs = cr.fetchall()
    #st.write(product_id)
    total = 0
    for r in recs:
    # Fetch product details based on product_id
        product_id = r[1]
        quantity = r[0]
        cr.execute(f"select Description, Cost from product where ProductID = '{product_id}';")
        product_data = cr.fetchone()
        total += product_data[1]*quantity
    
    st.write(f"Total Amount: {total}")
    #st.write(f"Shipping address: {}")
    a,b = st.columns(2)
    
    with a:
        if(st.button("BACK")):
            st.switch_page(r"pages\cart.py")
    with b:
        if(st.button("Confirm PAYment")):
            st.switch_page(r"pages\paymentdone.py")
        
        
buy(cr)   
    
    
    
