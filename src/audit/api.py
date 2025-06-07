from fastapi import FastAPI
app = FastAPI()

@app.post("/audit/log")
def log_audit(entry: dict):
    # TODO: validate against schema, append to log
    return {"status":"ok"}
