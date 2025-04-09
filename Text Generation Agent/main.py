from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_KEY")

# Set up the Gemini model using LangChain - Will use better model. Gemini used as placeholder as it's free
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5,
    api_key=GOOGLE_API_KEY,
)

# Define function to generate campaign description - User_promt and system_prompt will be changed 
def generate_campaign_description(campaign_info):
    system_prompt = "You are a professional copywriter specialized in fundraising campaigns. Do not use markdown or special formatting symbols."
    user_prompt = f"""
    Write a compelling fundraising campaign description (250–500 words) clearly conveying urgency, emotional appeal, and impact. Include a strong call-to-action. Avoid using markdown or formatting symbols.

    Campaign Info:
    {campaign_info}

    Tone: {campaign_info['tone']}
    Audience: {campaign_info['audience']}
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]

    response = llm.invoke(messages)
    return response.content

# Example campaign information - Will be changed to connect with Google Form
campaign_info = {
    "name": "Clean Water for All",
    "cause": "Environmental Protection",
    "urgency": "Immediate",
    "background": "Millions lack access to clean drinking water, affecting health and survival.",
    "goal": "Raise $50,000 to build 50 water wells in rural communities.",
    "impact": "Every $1000 builds one well, supplying clean water to approximately 200 people.",
    "tone": "Emotionally compelling, persuasive, hopeful",
    "audience": "General public, potential donors"
}

# Generate campaign description
campaign_description = generate_campaign_description(campaign_info)

# Output to a text file
with open("campaign_description.txt", "w", encoding="utf-8") as file:
    file.write(campaign_description)

print("Campaign description generated and saved to 'campaign_description.txt'")