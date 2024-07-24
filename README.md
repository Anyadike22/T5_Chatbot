# T5_Chatbot

# T5 Data Analytics Chatbot

## Description
The T5 Data Analytics Chatbot is an interactive Streamlit application that allows users to analyze various datasets related to African infrastructure development. Powered by a large language model, this chatbot can answer questions about the data, providing insights and generating visualizations on demand.

## Features
- Interactive data selection from multiple datasets
- AI-powered question answering about the selected data
- Dynamic data visualization
- Question history tracking

## Datasets
The application includes the following datasets:
- Africa Infrastructure Development Index (AIDI)
- Water and Sanitation Service (WSS) Composite Index
- Electricity Composite Index
- ICT Composite Index
- Transport Composite Index
- Fused Dataset (combined metrics)

## Requirements
- Python 3.7+
- Streamlit
- Pandas
- PandasAI
- LangChain
- Groq API access

## Installation
1. Clone this repository:
   git clone https://github.com/yourusername/t5-data-analytics-chatbot.git
cd t5-data-analytics-chatbot

2. Install the required packages: pip install -r requirements.txt

3. 3. Set up your Groq API key in Streamlit secrets or as an environment variable.

## Usage
1. Run the Streamlit app: streamlit run streamlit_app.py

2. 2. Select a dataset from the sidebar.
3. Enter your question about the data in the text input field.
4. Click "Get Answer" to receive AI-generated insights.
5. View any generated charts and your question history.

## Configuration
- The `datasets` dictionary in the script can be modified to include additional datasets.
- The AI model can be adjusted by changing the `model_name` in the `ChatGroq` initialization.

## Contributing
Contributions to improve the T5 Data Analytics Chatbot are welcome. Please feel free to submit pull requests or open issues to discuss proposed changes.

## License
[Include your chosen license here]

## Acknowledgements
- This project uses the Groq API for natural language processing.
- Data sources: [List your data sources/providers here]
