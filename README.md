Web Scraper Project
An AI-powered browser automation tool that leverages the browser-use library to navigate websites, extract data, and perform actions based on dynamic instructions. In this project, the agent reads your resume from a file and then automates the process of searching for internships and applying for them on ParkerDewey.

Overview
This project demonstrates how to integrate AI-driven instructions with browser automation. It uses:

Python 3.11+

browser-use for browser control and automation.

LangChain's ChatOpenAI to generate step-by-step JSON instructions.

dotenv to securely load API keys and configuration.

The core workflow includes:

Loading and Sanitizing Resume Data: Reads from a local resume.txt file.

Generating a Task Instruction: Constructs a detailed instruction for the AI agent to navigate to the job portal, search for internships, and apply using your resume.

Automated Browser Execution: Uses the Agent from browser-use to execute the generated steps.

Features
AI-Driven Instructions: Uses ChatOpenAI to convert a natural language task into a structured JSON command list.

Browser Automation: Automates navigation and interactions on websites.

Customizable Workflow: Easily modify the task prompt and target website to suit other applications.

Secure Configuration: Utilizes a .env file to manage API keys and sensitive data.

Installation
Prerequisites
Python 3.11 or higher

pip

Setup Steps
Clone the Repository:

bash
Copy
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

Install Playwright Browser Engine:

bash
Copy
playwright install chromium
Create a .env File:

Add your API keys and configuration:

bash
Copy
OPENAI_API_KEY=your_openai_api_key
# Add any additional keys if needed, for example:
# ANTHROPIC_API_KEY=
Prepare the Resume File:

Ensure a resume.txt file exists in the project root containing your resume details.

Usage
Run the Web Scraper:

Execute the main script:

bash
Copy
python main.py
The script will:

Load and truncate your resume.

Generate a JSON-formatted instruction set using ChatOpenAI.

Launch the browser automation agent to navigate to ParkerDewey, search for internships, and apply using your resume.

Review the Output:

The final output is printed to the terminal, showing the agent's JSON response and execution result.

Customization
Task Instructions:
You can modify the task_instruction string in main.py to change the target website or adjust the actions (e.g., apply to different job portals).

Output Handling:
Customize how and where the scraped or applied data is stored by editing the relevant sections in main.py.

Contributing
Contributions are welcome! If you’d like to add features, fix bugs, or improve documentation, please:

Fork the repository.

Create a feature branch.

Commit your changes and open a pull request.

Please follow the existing code style and include tests where applicable.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer
Use this tool responsibly. Ensure you comply with the terms of service for any website you interact with, and do not expose sensitive data in your commits. The project maintainers are not responsible for misuse or any issues arising from its use.

