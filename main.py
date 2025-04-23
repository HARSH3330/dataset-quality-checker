from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
import os
from io import BytesIO

app = FastAPI()

@app.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    # Accept only .csv and .xlsx
    if not (file.filename.endswith('.csv') or file.filename.endswith('.xlsx')):
        return JSONResponse(
            status_code=400,
            content={"status": "❌ Rejected", "message": "Only .csv and .xlsx files are allowed."}
        )
    
    contents = await file.read()
    buffer = BytesIO(contents)
    
    try:
        # Read file
        if file.filename.endswith('.csv'):
            df = pd.read_csv(buffer)
        else:
            df = pd.read_excel(buffer)
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"status": "❌ Rejected", "message": "Error reading the file. Please upload a valid dataset."}
        )

    issues = []

    # Rule 1: Check for headers
    if df.columns.str.contains('Unnamed').any():
        issues.append("Missing or incorrect header row.")

    # Rule 2: Missing data
    missing_ratio = df.isnull().mean()
    if (missing_ratio > 0.2).any():
        issues.append("Some columns have more than 20% missing values.")

    # Rule 3: Check for minimum rows
    if df.shape[0] < 50:
        issues.append("Dataset has less than 50 rows. Too small for analysis.")

    # Rule 4: Duplicate rows
    if df.duplicated().sum() > 0:
        issues.append("Dataset contains duplicate rows.")

    # Rule 5: Inconsistent data types
    inconsistent_types = df.apply(lambda col: col.map(type).nunique() > 1 if col.dtype == 'object' else False)
    if inconsistent_types.any():
        issues.append("Some columns have inconsistent data types.")

    # Final judgment
    if not issues:
        status = "✅ Green"
        message = "Your dataset looks great! No major issues found."
    elif len(issues) <= 2:
        status = "⚠️ Yellow"
        message = "Dataset is usable, but could be improved:\n- " + "\n- ".join(issues)
    else:
        status = "❌ Red"
        message = "Dataset has several issues:\n- " + "\n- ".join(issues)

    return {
        "status": status,
        "message": message
    }
