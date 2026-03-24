from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()

# Add your Gemini API key
genai.configure(api_key="AIzaSyC3LmBXbsX9J1AO9XJjBl3CzSYte-mSnXg")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.get("/")
def home():
    return {"message": "AI Agent is running!"}

@app.get("/summarize")
def summarize(text: str):
    prompt = f"Summarize this text in simple words:\n{text}"
    
    response = model.generate_content(prompt)
    
    return {"summary": response.text}
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    import requests

@app.get("/wiki-summary")
def wiki_summary(topic: str):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    
    response = requests.get(url).json()
    
    text = response.get("extract", "")
    
    prompt = f"Summarize this:\n{text}"
    
    result = model.generate_content(prompt)
    
    return {"summary": result.text}

