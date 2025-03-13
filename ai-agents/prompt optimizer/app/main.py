import streamlit as st
from crewai import Crew, LLM
from agents import create_prompt_refiner, create_prompt_verifier
from tasks import create_refine_task, create_verify_task
from utils import configure_gemini_api

# Streamlit App Title
st.title("Multi-Agent Prompt Refinement System")

# Sidebar for Gemini API Key
with st.sidebar:
    st.header("Gemini API Key")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    if st.button("Submit API Key"):
        if api_key:
            if configure_gemini_api(api_key):
                st.success("API Key submitted successfully!")
            else:
                st.error("Failed to configure Gemini API.")
        else:
            st.error("Please enter a valid API Key.")

# Main Area for User Prompt
st.header("Enter Your Prompt")
user_prompt = st.text_area("Type your prompt here:", height=150)

if st.button("Refine Prompt"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not user_prompt:
        st.error("Please enter a prompt.")
    else:
        my_llm = LLM(
            model='gemini/gemini-1.5-flash',
            api_key=api_key
        )

        # Define Agents
        prompt_refiner = create_prompt_refiner(my_llm)
        prompt_verifier = create_prompt_verifier(my_llm)

        # Define Tasks
        refine_task = create_refine_task(user_prompt, prompt_refiner)
        verify_task = create_verify_task(prompt_verifier)

        # Create Crew and Execute Tasks
        crew = Crew(
            agents=[prompt_refiner, prompt_verifier],
            tasks=[refine_task, verify_task]
        )

        # Run the Crew
        refined_prompt = crew.kickoff()

        # Display Final Refined Prompt
        st.header("Final Refined Prompt")
        st.write(refined_prompt.raw)