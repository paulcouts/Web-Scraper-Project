import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Using ChatOpenAI for ChatGPT 4o
from browser_use import Agent

load_dotenv()

async def main():
    # Read resume text from resume.txt.
    with open("resume.txt", "r", encoding="utf-8") as f:
        resume_data = f.read()

    # Truncate and sanitize the resume to minimize any formatting issues.
    truncated_resume = resume_data[:500].replace("\n", " ").replace("\"", "'")
    
    
    task_instruction = (
        "Return only valid JSON with no extra text. "
        "The JSON must be a single object with a key 'steps' that is a list of step objects. "
        "Each step object must include an 'action' key, and optionally 'url', 'selector', or 'text'. "
        "Do not output any additional text. "
        "Finish with a step {\"action\":\"done\"}. "
        "Task: Navigate to https://app.parkerdewey.com, search for internships, and apply using the resume below. "
        "Resume: " + truncated_resume
    )
    

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=512,
        timeout=120,
        max_retries=3,
    )
    
    # IMPORTANT: In your Browser Use WebUI settings, ensure that "Use Vision" is disabled.
    agent = Agent(
        task=task_instruction,
        llm=llm,
    )
    
    result = await agent.run()
    print("Agent result:", result)

asyncio.run(main())
