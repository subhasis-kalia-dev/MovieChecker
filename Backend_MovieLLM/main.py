from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

#uv run fastapi dev main.py
# Load environment variables FIRST
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# ✅ Verify load (optional)
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("❌ OPENAI_API_KEY not found. Check your .env file.")


# Initialize FastAPI app
app = FastAPI()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins temporarily
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Input model
class UserInput(BaseModel):
    name: str


# Prompts
SYSTEM_PROMPT = """
You are a highly accurate movie and TV series information assistant.

Your task is to take the name of a movie or series and generate a structured, factually correct summary containing key details.

Guidelines:
- Use a clear and professional tone.
- Present the response in a clean, structured format (not as a paragraph).
- Include the following fields if available:
    • Title  
    • Release Date  
    • Runtime  
    • Genre  
    • Director  
    • Main Cast (up to 5 key actors)  
    • Production Company / Studio  
    • IMDb Rating  
    • Rotten Tomatoes Rating  
    • Plot Summary (2–4 concise sentences)  
    • Two Similar Movies or Series (with short reason for similarity)
- If any data is not available, omit that field.
- Ensure factual accuracy — no invented information.
- Avoid opinions, filler words, or irrelevant details.
- Focus only on movie/series-specific information.

Output Format Example:

Title: <Movie Name>  
Release Date: <Date>  
Runtime: <Time>  
Genre: <Genre>  
Director: <Director Name>  
Main Cast: <Actor 1>, <Actor 2>, ...  
Production Company: <Company Name>  
IMDb Rating: <Rating>/10  
Rotten Tomatoes Rating: <Rating>%  
Plot Summary: <Brief overview of the storyline.>  
Similar Titles:  
1. <Similar Movie 1> — <Reason why it's similar>  
2. <Similar Movie 2> — <Reason why it's similar>
"""

USER_PROMPT_PREFIX = """
You will be given the name of a movie or TV series.
Retrieve or infer factual information about it and present the details according to the format specified above.

Movie/Series name:
"""

def get_messages(movie_tv_name: str):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT_PREFIX + movie_tv_name},
    ]

# Endpoint
@app.post("/info")
def information(request: UserInput):
    movie_tv_name = request.name

    # Call OpenAI model
    llm_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=get_messages(movie_tv_name),
        temperature=0.2,
    )

    summary_text = llm_response.choices[0].message.content

    return {"summary": summary_text}
