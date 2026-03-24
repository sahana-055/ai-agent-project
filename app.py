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

from fastapi import FastAPI
import google.generativeai as genai
import requests   

@app.get("/wiki-summary")
def wiki_summary(topic: str):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
        
        res = requests.get(url)

        # Check status
        if res.status_code != 200:
            return {"error": "Wikipedia API failed"}

        data = res.json()

        text = data.get("extract", "")

        if not text:
            return {"error": "No summary found"}

        prompt = f"Summarize this:\n{text}"

        result = model.generate_content(prompt)

        if result and hasattr(result, "text"):
            return {"summary": result.text}
        else:
            return {"summary": text[:200]}  # fallback

    except Exception as e:
        return {"error": str(e)}