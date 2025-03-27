<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./static/browser-use-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="./static/browser-use.png">
  <img alt="Browser-use Logo" src="./static/browser-use.png" style="width:100%;">
</picture>

# Web Scraper Project

An AI-powered browser automation tool that leverages the [browser-use](https://docs.browser-use.com) library to navigate websites, extract data, and perform defined actions based on detailed instructions. This project demonstrates how to use structured commands to automate web interactions—using your resume data as an example input—to search for relevant opportunities on platforms like [ParkerDewey](https://app.parkerdewey.com).

---

## Overview

This project showcases how to integrate AI-driven instruction generation with browser automation. It uses:

- **Python 3.11+**
- **[browser-use](https://docs.browser-use.com)** for browser control and automation.
- **LangChain's ChatOpenAI** to convert natural language tasks into a structured JSON command list.
- **dotenv** to securely load API keys and configuration settings.

The core workflow includes:
1. **Loading and Sanitizing Resume Data:** Reads from a local `resume.txt` file.
2. **Generating a Task Instruction:** Constructs a detailed instruction that directs the automation agent to navigate to a job portal, search for opportunities, and interact with the site using your resume as reference.
3. **Automated Browser Execution:** Uses the `Agent` from browser-use to execute the generated steps.

---

## Features

- **AI-Driven Instruction Generation:** Converts a natural language task into a structured JSON command list.
- **Browser Automation:** Simulates user interactions to navigate and extract information from websites.
- **Customizable Workflow:** Easily adapt the task prompt to target other websites or tailor interactions for different use cases.
- **Secure Configuration:** Uses a `.env` file to manage API keys and sensitive data.

---

## Installation

### Prerequisites

- **Python 3.11 or higher**
- **pip**

### Setup Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Web-Scraper-Project.git
   cd Web-Scraper-Project
Install Python Dependencies:

bash
Copy
pip install -r requirements.txt
Ensure that your requirements.txt includes:

browser-use

langchain_openai

python-dotenv

Install the Playwright Browser Engine:

bash
Copy
playwright install chromium
Create a .env File:

Add your API keys and configuration:

bash
Copy
OPENAI_API_KEY=your_openai_api_key
# Add any additional keys if needed
Prepare the Resume File:

Ensure a resume.txt file exists in the project root containing your resume or other data you wish to use.

Usage
Run the Web Scraper:

Execute the main script:

bash
Copy
python main.py
The script will:

Load and process your resume data.

Generate a JSON-formatted instruction set using ChatOpenAI.

Launch the browser automation agent to navigate to ParkerDewey, search for opportunities, and interact with the site based on the provided input.

Review the Output:

The final output is printed to the terminal, showing the agent's JSON response and the execution result.

Customization
Task Instructions:
Modify the task_instruction string in main.py to change the target website or adjust the specific interactions (for example, focusing on data extraction or different site interactions).

Output Handling:
Customize how and where the data is stored or processed by editing the relevant sections in main.py.
