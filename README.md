# AI Assistant within 1 hour

This repository contains templates for a simple AI assistant built using the OpenAI API. You can choose to run it as a Command Line Interface (CLI) or as a Web Application using Streamlit.

## Prerequisites

1.  **Python 3.8+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2.  **OpenAI API Key**: You need an API key from OpenAI.
    *   Go to [https://platform.openai.com/](https://platform.openai.com/) and sign up or log in.
    *   Navigate to the API keys page and create a new secret key.

## Installation

1.  Clone this repository or download the files.
2.  Open your terminal or command prompt and navigate to the folder containing the files.
3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Setting up your API Key

You should set your OpenAI API key as an environment variable.

*   **Linux/macOS:**
    ```bash
    export OPENAI_API_KEY="your_api_key_here"
    ```
*   **Windows (Command Prompt):**
    ```cmd
    set OPENAI_API_KEY="your_api_key_here"
    ```
*   **Windows (PowerShell):**
    ```powershell
    $env:OPENAI_API_KEY="your_api_key_here"
    ```

## Running the Assistant

### Option 1: Command Line Interface (CLI)

Run the simple Python script to chat in your terminal:

```bash
python assistant.py
```

### Option 2: Web Interface (Streamlit)

Run the Streamlit application for a nice graphical chat interface:

```bash
streamlit run app.py
```

This will open a new tab in your web browser where you can interact with the assistant.
