import streamlit as st
from config.config import Config
from services.agent_service import create_prompt_transformation_agent
from services.firecrawl_service import search_for_urls, extract_user_info_from_urls
from utils.data_formatter import format_user_info_to_flattened_json
from services.google_sheets_service import write_google_sheets


def main():
    st.title("🎯 AI Lead Generation Agent")
    st.info(
        "This firecrawl powered agent helps you generate leads from Quora by searching for relevant posts and extracting user information.")

    with st.sidebar:
        st.header("API Keys")
        firecrawl_api_key = st.text_input("Firecrawl API Key", type="password")
        st.caption(" Get your Firecrawl API key from [Firecrawl's website](https://www.firecrawl.dev/app/api-keys)")
        gemini_api_key = st.text_input("Gemini API Key", type="password")
        st.caption(" Get your Gemini API key from [Gemini's website](https://ai.google.dev/)")
        composio_api_key = st.text_input("Composio API Key", type="password")
        st.caption(" Get your Composio API key from [Composio's website](https://composio.ai)")

        num_links = st.number_input("Number of links to search", min_value=1, max_value=10, value=3)

        if st.button("Reset"):
            st.session_state.clear()
            st.rerun()

    user_query = st.text_area(
        "Describe what kind of leads you're looking for:",
        placeholder="e.g., Looking for users who need automated video editing software with AI capabilities",
        help="Be specific about the product/service and target audience. The AI will convert this into a focused search query."
    )

    if st.button("Generate Leads"):
        if not all([firecrawl_api_key, gemini_api_key, composio_api_key, user_query]):
            st.error("Please fill in all the API keys and describe what leads you're looking for.")
        else:
            with st.spinner("Processing your query..."):
                transform_agent = create_prompt_transformation_agent(gemini_api_key)
                company_description = transform_agent.run(
                    f"Transform this query into a concise 3-4 word company description: {user_query}")
                st.write("🎯 Searching for:", company_description.content)

            with st.spinner("Searching for relevant URLs..."):
                urls = search_for_urls(company_description.content, firecrawl_api_key, num_links)

            if urls:
                st.subheader("Quora Links Used:")
                for url in urls:
                    st.write(url)

                with st.spinner("Extracting user info from URLs..."):
                    user_info_list = extract_user_info_from_urls(urls, firecrawl_api_key)

                with st.spinner("Formatting user info..."):
                    flattened_data = format_user_info_to_flattened_json(user_info_list)

                with st.spinner("Writing to Google Sheets..."):

                    google_sheets_link = write_google_sheets(flattened_data, st)

                if google_sheets_link:
                    st.success("Lead generation and data writing to Google Sheets completed successfully!")
                    st.subheader("Google Sheets Link:")
                    st.markdown(f"[View Google Sheet]({google_sheets_link})")
                else:
                    st.error("Failed to retrieve the Google Sheets link.")
            else:
                st.warning("No relevant URLs found.")


if __name__ == "__main__":
    main()