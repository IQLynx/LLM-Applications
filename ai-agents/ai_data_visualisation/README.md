# 📊 AI Data Visualization Agent

A Streamlit application that acts as your personal data visualization expert, powered by LLMs. Simply upload your dataset and ask questions in natural language—the AI agent will analyze your data, generate appropriate visualizations, and provide insights through a combination of charts, statistics, and explanations.

---

## Features

### **Natural Language Data Analysis**
- Ask questions about your data in plain English.
- Get instant visualizations and statistical analysis.
- Receive explanations of findings and insights.
- Interactive follow-up questioning.

### **Intelligent Visualization Selection**
- Automatic choice of appropriate chart types.
- Dynamic visualization generation.
- Statistical visualization support.
- Custom plot formatting and styling.

### **Multi-Model AI Support**
- **Meta-Llama 3.1 405B**: For complex analysis.
- **DeepSeek V3**: For detailed insights.
- **Qwen 2.5 7B**: For quick analysis.
- **Meta-Llama 3.3 70B**: For advanced queries.

---

## File Structure

The project is organized into the following directories and files:

```
ai_data_visualization/
├── main.py
├── requirements.txt
├── README.md
├── config/
│   └── config.py
├── services/
│   ├── llm_service.py
│   ├── code_interpreter_service.py
│   └── file_upload_service.py
├── utils/
│   └── code_utils.py
```

### **Key Files**
- **`main.py`**: The entry point of the application. Initializes the Streamlit app and ties everything together.
- **`config/config.py`**: Contains configuration settings like API keys and constants.
- **`services/llm_service.py`**: Handles interactions with the Together AI LLM.
- **`services/code_interpreter_service.py`**: Manages code execution in the E2B sandbox.
- **`services/file_upload_service.py`**: Handles file uploads and dataset management.
- **`utils/code_utils.py`**: Contains utility functions for code parsing and execution.

---

## How to Run

Follow the steps below to set up and run the application:

### **1. Get API Keys**
- **Together AI API Key**: Get your free API key from [Together AI](https://api.together.ai/signin).
- **E2B API Key**: Get your free API key from [E2B](https://e2b.dev/docs/legacy/getting-started/api-key).

### **2. Clone the Repository**
```bash
git clone https://github.com/IQLynx/LLM-Applications.git
cd ai_agent_tutorials/ai_data_visualisation
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Streamlit App**
```bash
streamlit run main.py
```

---

## Usage

1. **Enter API Keys**:
   - Provide your Together AI and E2B API keys in the sidebar.
2. **Upload Dataset**:
   - Upload a CSV file containing your dataset.
3. **Ask Questions**:
   - Enter your query in natural language (e.g., "Can you compare the average cost for two people between different categories?").
4. **Analyze**:
   - Click the **Analyze** button to generate visualizations and insights.

---

## Example Query

**Input**:  
"Can you compare the average cost for two people between different categories?"

**Output**:  
- A bar chart comparing the average cost across categories.
- Statistical insights and explanations.
- A table summarizing the results.

---

## Dependencies

- **Streamlit**: For the web interface.
- **Together AI**: For interacting with the LLM.
- **E2B Code Interpreter**: For executing Python code in a sandbox.
- **Pandas**: For data manipulation.
- **Pillow**: For image processing.

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

- **Together AI**: For providing the LLM API.
- **E2B**: For the code interpreter sandbox.
- **Streamlit**: For the web framework.