from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pyflowchart import Flowchart
import ast

app = FastAPI()

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.post("/generate-flowchart/")
async def generate_flowchart(data: CodeInput):
    try:
        code_ast = ast.parse(data.code)
        flowchart = Flowchart.from_code(data.code)
        return {"flowchart": flowchart.flowchart()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/upload/")
async def upload_python_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".py"):
        raise HTTPException(status_code=400, detail="Please upload a .py file.")

    content = await file.read()
    try:
        code = content.decode("utf-8")
        flowchart = Flowchart.from_code(code)
        return {"flowchart": flowchart.flowchart()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Python to Flowchart API is running"}
