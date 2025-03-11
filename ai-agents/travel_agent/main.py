import streamlit as st
from services.researcher_service import create_researcher_agent
from services.planner_service import create_planner_agent
from utils.text_utils import dedent

# Set up the Streamlit app
st.title("AI Travel Planner ✈️")
st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary using Gemini AI")

# Get Gemini API key from user
gemini_api_key = st.text_input("Enter Gemini API Key", type="password")

# Get SerpAPI key from the user
serp_api_key = st.text_input("Enter Serp API Key for Search functionality", type="password")

if gemini_api_key and serp_api_key:
    # Initialize the Researcher and Planner agents
    researcher = create_researcher_agent(gemini_api_key, serp_api_key)
    planner = create_planner_agent(gemini_api_key)

    # Input fields for the user's destination and the number of days they want to travel for
    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    if st.button("Generate Itinerary"):
        with st.spinner("Processing..."):
            # Get the response from the assistant
            response = planner.run(f"{destination} for {num_days} days", stream=False)
            st.write(response.content)