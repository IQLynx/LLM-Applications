## 🎯 AI Lead Generation Agent - Powered by Firecrawl's Extract Endpoint

The **AI Lead Generation Agent** automates the process of finding and qualifying potential leads from Quora. It uses Firecrawl's search and the new Extract endpoint to identify relevant user profiles, extract valuable information, and organize it into a structured format in Google Sheets. This agent helps sales and marketing teams efficiently build targeted lead lists while saving hours of manual research.

---

## Features
- **Targeted Search**: Uses Firecrawl's search endpoint to find relevant Quora URLs based on your search criteria.
- **Intelligent Extraction**: Leverages Firecrawl's new Extract endpoint to pull user information from Quora profiles.
- **Automated Processing**: Formats extracted user information into a clean, structured format.
- **Google Sheets Integration**: Automatically creates and populates Google Sheets with lead information.
- **Customizable Criteria**: Allows you to define specific search parameters to find your ideal leads for your niche.

---

## File Structure
The project is organized into the following directories and files:

```
ai_lead_generation/
├── main.py
├── requirements.txt
├── README.md
├── config/
│   └── config.py
├── models/
│   └── schemas.py
├── services/
│   ├── firecrawl_service.py
│   ├── google_sheets_service.py
│   └── agent_service.py
└── utils/
    └── data_formatter.py
```

### Key Files
- **`main.py`**: The entry point of the application. Initializes the Streamlit app and ties everything together.
- **`config/config.py`**: Contains configuration settings like API keys and constants.
- **`models/schemas.py`**: Defines Pydantic models for data validation.
- **`services/firecrawl_service.py`**: Handles Firecrawl-related functionality (e.g., searching for URLs and extracting user info).
- **`services/google_sheets_service.py`**: Manages Google Sheets operations (e.g., writing data to sheets).
- **`services/agent_service.py`**: Creates and manages agents (e.g., Google Sheets agent, prompt transformation agent).
- **`utils/data_formatter.py`**: Contains utility functions for formatting data (e.g., flattening JSON).

---

## How to Get Started

### 1. Clone the Repository
```bash
git clone https://github.com/IQLynx/LLM-Applications.git
cd LLM-Appications/ai-agents/lead_generation
```

### 2. Install the Required Packages
```bash
pip install -r requirements.txt
```

### 3. Set Up Composio Integration
- In the terminal, run the following command:
  ```bash
  composio add googlesheets
  ```
- In your Composio dashboard, create a new Google Sheets integration and ensure it is active in the **Active Integrations/Connections** tab.

### 4. Set Up Your API Keys
- **Firecrawl API Key**: Get your API key from [Firecrawl's website](https://www.firecrawl.dev/app/api-keys).
- **Gemini API Key**: Get your API key from [Gemini's website](https://ai.google.dev/).
- **Composio API Key**: Get your API key from [Composio's website](https://composio.ai).

### 5. Run the Application
```bash
streamlit run main.py
```

---

## Usage
1. **Enter API Keys**: Provide your Firecrawl, Gemini, and Composio API keys in the sidebar.
2. **Describe Your Query**: Enter a description of the leads you're looking for (e.g., "Looking for users who need automated video editing software with AI capabilities").
3. **Generate Leads**: Click the **Generate Leads** button to start the process.
4. **View Results**: The extracted lead information will be written to a Google Sheet, and a link to the sheet will be provided.

---

## Example Query
**Input**:  
"Generate leads looking for AI-powered customer support chatbots for e-commerce stores."

**Output**:  
- A Google Sheet containing user information (username, bio, post type, timestamp, upvotes, and links) from relevant Quora posts.
- A link to the Google Sheet for easy access.

---

## Dependencies
- **Streamlit**: For the web interface.
- **Firecrawl**: For searching and extracting data from Quora.
- **Gemini**: For transforming user queries into concise descriptions.
- **Google Sheets API**: For writing data to Google Sheets.
- **Pydantic**: For data validation and schema definitions.

---

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **Firecrawl**: For providing the search and extract endpoints.
- **Gemini**: For powering the AI transformations.
- **Composio**: For simplifying Google Sheets integration.