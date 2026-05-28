from fastapi import APIRouter

router = APIRouter(prefix="/research", tags=["Research Portal"])

@router.post("/proposals", summary="Proposal Submission")
def proposal_submission():
    return {"module": "Research Portal", "action": "proposal_submission"}

@router.get("/ethics-review", summary="Ethics Review")
def ethics_review():
    return {"module": "Research Portal", "page": "Ethics Review"}

@router.get("/study-tracking", summary="Study Tracking")
def study_tracking():
    return {"module": "Research Portal", "page": "Study Tracking"}

@router.get("/publications", summary="Publications")
def publications():
    return {"module": "Research Portal", "page": "Publications"}

@router.get("/data-repository", summary="Data Repository")
def data_repository():
    return {"module": "Research Portal", "page": "Data Repository"}

@router.get("/analytics", summary="Research Analytics")
def research_analytics():
    return {"module": "Research Portal", "page": "Research Analytics"}

