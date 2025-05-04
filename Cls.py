import streamlit as st

st.set_page_config(page_title="CORE Loop Strategy Assistant", layout="centered") st.title("CORE Loop Strategy Assistant")

st.write("Answer the prompts below to define your problem and generate a structured action plan using the CORE methodology.")

Step 1: Context

context = st.text_area("1. CONTEXT - What environment/system are you working in?")

Step 2: Objective

objective = st.text_area("2. OBJECTIVE - What exactly do you want to achieve or solve?")

Step 3: Resources

resources_have = st.text_area("3. RESOURCES - What resources/tools do you currently have?") resources_need = st.text_area("What resources/tools are you missing or need to acquire?")

Step 4: Execution Plan

execution = st.text_area("4. EXECUTION - What are the first 2-3 small steps you can take to move forward?")

Step 5: Review Criteria

review = st.text_area("5. REVIEW - How will you know you're on the right track? What will you check?")

if st.button("Generate Action Plan"): st.subheader("CORE Loop Action Plan") st.markdown(f"Context: {context}") st.markdown(f"Objective: {objective}") st.markdown(f"Resources Available: {resources_have}") st.markdown(f"Resources Needed: {resources_need}") st.markdown(f"Initial Execution Steps: {execution}") st.markdown(f"Review Plan: {review}") st.success("Use this action plan as a loop—review and refine after every cycle.")

