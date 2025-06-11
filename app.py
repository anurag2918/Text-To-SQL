from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    full_prompt = f"{prompt}\n\n{question}"
    response = model.generate_content(full_prompt)
    return response.text.strip()

def read_dql_query(sql, db):
    conn = sqlite3.connect(db)
    curr = conn.cursor()
    curr.execute(sql)
    rows = curr.fetchall()
    conn.close()
    return rows

prompt = """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.

For example,
Example 1 - How many entries of records are present?
→ SELECT COUNT(*) FROM STUDENT;

Example 2 - Tell me all the students studying in Data Science class?
→ SELECT * FROM STUDENT WHERE CLASS="Data Science";

Also, the SQL code should not have ``` in beginning or end and sql word in output.
"""


st.set_page_config(page_title="SQL Query Generator", page_icon=":guardsman:", layout="wide")
st.header("SQL Query Generator")

question = st.text_input("Input your question:", key="input")
submit = st.button("Ask the question")

if submit and question:
    try:
        response = get_gemini_response(question, prompt)
        st.subheader("Generated SQL Query:")
        st.code(response, language="sql")

        data = read_dql_query(response, "student.db")
        st.subheader("Query Results:")
        for row in data:
            st.write(row)
    except Exception as e:
        st.error(f"Error: {e}")
