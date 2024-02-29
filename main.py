import mysql.connector
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Libraray Management System",page_icon="https://tse2.mm.bing.net/th?id=OIP.bBuO6fprF8op2JIpFaVz5QHaHa&pid=Api&P=0&h=220")
st.title("LIBRARY MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("Main Menu",("HOME","STUDENT","ADMIN","REGISTRATION"))
st.sidebar.image("https://www.paatham.in/assets/images/img/lib.png")

if(choice=="HOME"):
    st.image("https://tse4.mm.bing.net/th?id=OIP.AJUqxQYtkkD_wK_PQHDK0gHaEQ&pid=Api&P=0&h=220")
    st.write("This is an library management system made by Mansi")
elif(choice=="STUDENT"):
    if "islogin" not in st.session_state:
        st.session_state['islogin']=False
    sid=st.text_input("Enter student ID")
    pwd=st.text_input("Enter student password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
        c=mydb.cursor()
        c.execute("select * from student")
        data=c.fetchall()
        for k in data:
            if (k[0]==sid and k[1]==pwd):
                st.session_state['islogin']=True
                break
        if not st.session_state['islogin']:
            st.subheader("Incorrect ID or Passwowrd")
            
    if st.session_state['islogin']:
         st.subheader("Login Successfull")
         choice2=st.selectbox("Features",("None","View All Books","Issue Books","Delete Book"))
         if(choice2=="View All Books"):
              mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
              c=mydb.cursor()
              c.execute("select * from books")
              mydata=c.fetchall()
              mycolumns=c.column_names
              df=pd.DataFrame(data=mydata,columns=mycolumns)
              st.dataframe(df)
         elif(choice2=="Issue Books"):
              bid=st.text_input("Enter Book ID")
              stid = st.text_input("Enter student ID", key="student_id_input")
              btn2=st.button("Issue Book")
              if btn2:
                  iid=str(datetime.datetime.now())
                  mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
                  c=mydb.cursor()
                  c.execute("insert into issues values(%s,%s,%s)",(iid,bid,stid))
                  mydb.commit()
                  st.subheader("Book Issued Successfully")
elif(choice=="ADMIN"):
    if "islogin2" not in st.session_state:
        st.session_state['islogin2']=False
    sid=st.text_input("Enter Librarian ID")
    pwd=st.text_input("Enter your librarian password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
        c=mydb.cursor()
        c.execute("select * from admin")
        data=c.fetchall()
        for k in data:
            if (k[0]==sid and k[1]==pwd):
                st.session_state['islogin2']=True
                break
        if not st.session_state['islogin2']:
            st.subheader("Incorrect ID or Passwowrd")
            
    if st.session_state['islogin2']:
         st.subheader("Login Successfull")
         choice2=st.selectbox("Features",("None","View Issued Books","Add Books","Delete Book"))
         if(choice2=="View Issued Books"):
              mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
              c=mydb.cursor()
              c.execute("select * from issues")
              mydata=c.fetchall()
              mycolumns=c.column_names
              df=pd.DataFrame(data=mydata,columns=mycolumns)
              st.dataframe(df)
         elif(choice2=="Add Books"):
              bid=st.text_input("Enter Book ID")
              bname = st.text_input("Enter Book Name")
              aname= st.text_input("Enter Author Name")
              btn2=st.button("Add Book")
              if btn2:
                  mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
                  c=mydb.cursor()
                  c.execute("insert into books values(%s,%s,%s)",(bid,bname,aname))
                  mydb.commit()
                  st.subheader("Book Added Successfully")
         elif(choice2=="Delete Book"):
              mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
              c=mydb.cursor()
              c.execute("select * from books")
              mydata=c.fetchall()
              mycolumns=c.column_names
              df=pd.DataFrame(data=mydata,columns=mycolumns)
              bid=st.selectbox("Choose Book ID to delete",df['book_id'])
              btn2=st.button("Delete Book")
              if btn2:
                  mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
                  c=mydb.cursor()
                  c.execute("delete from books where book_id=%s",(bid,))
                  mydb.commit()
                  st.subheader("Book Deleted Successfully")
elif(choice=="REGISTRATION"):
      sid=st.text_input("Enter Student ID")
      pwd = st.text_input("Choose a Password")
      btn2=st.button("Register")
      if btn2:
          mydb=mysql.connector.connect(host="localhost",user="root",password="mansi@1234",database="lms")
          c=mydb.cursor()
          c.execute("insert into student values(%s,%s)",(sid,pwd))
          mydb.commit()
          st.subheader("Registration Successfull")
    

              
             
