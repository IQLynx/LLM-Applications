## 🛫 AI Travel Planner

This Streamlit app is an AI-powered travel planner that generates personalized travel itineraries using **Gemini AI**. It automates the process of researching, planning, and organizing your dream vacation, allowing you to explore exciting destinations with ease.

---

## Features

### **Research and Discovery**
- Discover exciting travel destinations, activities, and accommodations.
- Automatically generate search terms based on your destination and travel duration.

### **Personalized Itineraries**
- Customize your itinerary based on the number of days you want to travel.
- Get a well-structured, informative, and engaging travel plan.

### **Powered by Gemini AI**
- Utilize the power of **Gemini AI** to generate intelligent and personalized travel plans.
- Combine AI insights with real-time web search results for accurate and up-to-date recommendations.

---

## File Structure

The project is organized into the following directories and files:

```
ai_travel_planner/
├── main.py
├── requirements.txt
├── README.md
├── config/
│   └── config.py
├── services/
│   ├── researcher_service.py
│   ├── planner_service.py
│   └── serpapi_service.py
└── utils/
    └── text_utils.py
```

### **Key Files**
- **`main.py`**: The entry point of the application. Initializes the Streamlit app and ties everything together.
- **`config/config.py`**: Contains configuration settings like API keys and constants.
- **`services/researcher_service.py`**: Handles the **Researcher** agent, which searches for travel activities and accommodations.
- **`services/planner_service.py`**: Handles the **Planner** agent, which generates personalized itineraries.
- **`services/serpapi_service.py`**: Manages the SerpAPI tool for web searches.
- **`utils/text_utils.py`**: Contains utility functions for text formatting.

---

## How to Get Started

### **1. Clone the Repository**
```bash
git clone https://github.com/IQLynx/LLM-Applications.git
cd LLM-Appications/ai-agents/travel_agent
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Get API Keys**
- **Gemini API Key**: Sign up for a [Gemini API key](https://ai.google.dev/).
- **SerpAPI Key**: Sign up for a [SerpAPI account](https://serpapi.com/) and obtain your API key.

### **4. Run the Streamlit App**
```bash
streamlit run main.py
```

---

## How It Works

The **AI Travel Planner** has two main components:

### **1. Researcher**
- Generates search terms based on your destination and travel duration.
- Uses **SerpAPI** to search the web for relevant activities and accommodations.
- Returns the top 10 most relevant results.

### **2. Planner**
- Takes the research results and generates a personalized draft itinerary.
- Ensures the itinerary is well-structured, informative, and engaging.
- Provides a balanced and nuanced travel plan, quoting facts where possible.

---

## Usage

1. **Enter API Keys**:
   - Provide your **Gemini API key** and **SerpAPI key** in the sidebar.
2. **Input Travel Details**:
   - Enter your **destination** and the **number of days** you want to travel.
3. **Generate Itinerary**:
   - Click the **Generate Itinerary** button to create your personalized travel plan.
4. **View Results**:
   - The generated itinerary will be displayed, including suggested activities and accommodations.

---

## Example Query

**Input**:  
- Destination: "Paris"
- Number of Days: 7

**Output**:  
- A detailed 7-day itinerary for Paris, including:
  - Day-by-day activities (e.g., Eiffel Tower visit, Louvre Museum tour).
  - Recommended accommodations (e.g., hotels, Airbnb).
  - Travel tips and insights.

---

## Dependencies

- **Streamlit**: For the web interface.
- **Gemini AI**: For generating travel plans.
- **SerpAPI**: For web searches.
- **Agno**: For agent and tool management.

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

- **Gemini AI**: For providing the AI capabilities.
- **SerpAPI**: For enabling web searches.
- **Streamlit**: For the web framework.