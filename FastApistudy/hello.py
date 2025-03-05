from fastapi import FastAPI as FA
app = FA()

@app.get("/hi")
def greet():
    return "Hello World!"

if __name__ == "main":
    import uvicorn
    uvicorn.run("hello:app",reload=True)
#    uvicorn.run("hello:app",reload=True, host="127.0.0.1", port=4000)