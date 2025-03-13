# Multi-Agent Prompt Refinement System

This project is a Streamlit-based application that leverages a multi-agent system powered by **CrewAI** and **Google's Gemini API** to refine and enhance user prompts. The system uses two specialized agents: a **Prompt Refinement Expert** and a **Prompt Quality Assurance Expert**, to ensure that user prompts are professional, clear, and actionable.

---

## Features

- **Gemini API Integration**: Securely configure and use the Gemini API for prompt refinement.
- **Multi-Agent System**: Utilizes two agents to refine and verify prompts for quality and clarity.
- **Streamlit Interface**: Provides an intuitive and user-friendly interface for inputting prompts and viewing refined outputs.
- **Modular Codebase**: Organized into multiple files and directories for better maintainability and scalability.

---

## Project Structure

```
multi_agent_prompt_refinement/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Main Streamlit application
│   ├── agents.py        # Agent definitions
│   ├── tasks.py         # Task definitions
│   └── utils.py         # Utility functions (e.g., Gemini API configuration)
│
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

---

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/IQLynxAI/LLM-Applications.git
   cd ai-agents/prompt optimizer/app
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8 or higher installed. Then, install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Gemini API Key**:
   - Obtain your Gemini API key from the [Google AI Studio](https://aistudio.google.com/).
   - Add the API key in the Streamlit sidebar when running the application.

4. **Run the Application**:
   Start the Streamlit app:
   ```bash
   streamlit run app/main.py
   ```

5. **Access the Application**:
   Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

---

## Usage

1. **Enter Your Gemini API Key**:
   - In the sidebar, input your Gemini API key and click "Submit API Key."

2. **Input Your Prompt**:
   - In the main area, type or paste your prompt into the text box.

3. **Refine Your Prompt**:
   - Click the "Refine Prompt" button to process your prompt using the multi-agent system.

4. **View the Refined Prompt**:
   - The final refined prompt will be displayed in the "Final Refined Prompt" section.

---

## How It Works

1. **Agents**:
   - **Prompt Refinement Expert**: Refines the user's input into a professional, detailed, and clear prompt.
   - **Prompt Quality Assurance Expert**: Verifies and adjusts the refined prompt to ensure it is clear, actionable, and professional.

2. **Tasks**:
   - **Refine Task**: Takes the user's prompt and refines it.
   - **Verify Task**: Ensures the refined prompt meets quality standards.

3. **CrewAI**:
   - Orchestrates the agents and tasks to produce the final refined prompt.

---

## Dependencies

- **Streamlit**: For building the web interface.
- **CrewAI**: For creating and managing agents and tasks.
- **Google Generative AI**: For leveraging the Gemini API for prompt refinement.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **CrewAI**: For providing the multi-agent framework.
- **Google Generative AI**: For the Gemini API.
- **Streamlit**: For the easy-to-use web application framework.
---