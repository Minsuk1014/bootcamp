#RESTful API
"""
보통 모델을 서빙할 때, 백엔드에게 넘겨주기 위해서 사용
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/encore/")
def myfunc():
    return {"massage" : "ㅋㅋㅋㅋ"}
