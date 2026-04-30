from fastapi import FastAPI
from contextlib import asynccontextmanager

from db.database import engine, Base
import db.models as models 

from agents.importance_agent.router import router as importance_router
from agents.evaluation_agent.router import router as evaluation_router
from agents.question_agent.router import router as question_router
from agents.retrieval_agent.router import router as retrieval_router
from api.workflow import router as workflow_router

# 서버가 켜질 때 자동으로 실행될 준비(시작) 작업을 정의
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Supabase DB 테이블 생성 완료!")
    
    yield 

# FastAPI 앱 객체를 생성하면서 lifespan을 연결
app = FastAPI(lifespan=lifespan)

# 서버가 잘 켜졌는지 확인하는 테스트용 API
@app.get("/")
def read_root():
    return {"message": "Highlite 멀티 에이전트 서버가 정상 작동 중입니다!"}

app.include_router(
    importance_router, 
    prefix="/importance",  
    tags=["중요도 분석 Agent"]
)

app.include_router(
    evaluation_router, 
    prefix="/evaluation",  
    tags=["평가+개인화 Agent"]
)

app.include_router(
    question_router, 
    prefix="/question",  
    tags=["문제 생성 Agent"]
)

app.include_router(
    retrieval_router, 
    prefix="/retrieval",  
    tags=["RAG Agent"]
)

app.include_router(
    workflow_router, 
    prefix="/api/v1", 
    tags=["Production"]
)