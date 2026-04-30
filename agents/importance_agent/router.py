from fastapi import APIRouter

router = APIRouter()

# 통신이 잘 되는지 확인하기 위한 임시 테스트 API
@router.post("/test-analyze")
async def test_importance():
    return {"message": "중요도 분석 라우터 정상 작동 중!"}