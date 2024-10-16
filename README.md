# Chatbot using OpenAI API and Streamlit

## Overview

This project is a simple interactive chatbot built using the OpenAI API and Streamlit. The chatbot utilizes the GPT-3.5-turbo model to provide conversational responses based on user input. It manages conversation history to create a seamless chat experience.

## Features

- Interactive chat interface
- Maintains conversation history
- Handles errors gracefully
- Utilizes OpenAI's GPT-3.5-turbo model for generating responses

## Getting Started

### Prerequisites

To run this project, you'll need:

1. **Python 3.7 or higher**: Ensure you have Python installed on your machine.
2. **OpenAI API Key**: You must have a valid OpenAI API key with sufficient quota. You can sign up at [OpenAI's website](https://platform.openai.com/signup).

### Installation

Install the required packages:

```
pip install streamlit openai
```

- (Optional) Set up your OpenAI API key:

Create a file named .streamlit/secrets.toml in your project directory.
Add your OpenAI API key to this file: (secrets.toml)
api-key = "your_openai_api_key_here"

### Running the Application
Run the Streamlit application with the following command:

```
streamlit run main.py
```
Your browser will open the chatbot interface, where you can start chatting.

### Troubleshooting OpenAI Version Issues
If you encounter issues related to the OpenAI version (e.g., "You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0"), follow these steps:
Upgrade the OpenAI library:

```
pip install --upgrade openai
```
Then update your code to align with the new OpenAI API structure. For detailed guidance, [grit](https://docs.grit.io/patterns/library/openai#change-openai-import-to-sync).This provides information on how to modify your code to ensure compatibility with the latest version.

### Important Note
Ensure you have a valid OpenAI API key with sufficient quota; otherwise, the application will not function properly. You can check your quota and manage your billing details on the OpenAI dashboard.

### Code Explanation
The code is structured to handle user input, generate responses from the OpenAI API, and maintain conversation history. It employs error handling to ensure a smooth user experience.
### Acknowledgments
- [OpenAI](https://openai.com)
- [Streamlit](https://streamlit.io)
