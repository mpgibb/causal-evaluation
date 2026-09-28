"""Local API scaffold. No production deployment is claimed."""
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,ConfigDict
app=FastAPI(title='Measuring an intervention’s effect',version="0.1.0",description="Research baseline; see README for assumptions and incomplete work.")
@app.get("/health")
def health():return {"status":"ok","implementation":"research_baseline","version":"0.1.0"}
class Request(BaseModel):
 model_config=ConfigDict(extra="forbid",allow_inf_nan=False)
 treated_before:float
 treated_after:float
 control_before:float
 control_after:float
@app.post("/v1/baseline")
def baseline(request:Request):
 from .core import difference_in_differences
 return {"version":"0.1.0","status":"research_baseline","contrast":difference_in_differences(**request.model_dump()),"causal_interpretation":"Requires stated identification assumptions; no uncertainty estimate supplied."}
