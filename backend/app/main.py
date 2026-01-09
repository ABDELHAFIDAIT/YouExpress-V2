from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Succès", "message": "Le Backend YouExpress V2 tourne bien ! 🐳"}