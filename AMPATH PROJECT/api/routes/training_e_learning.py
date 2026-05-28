from fastapi import APIRouter

router = APIRouter(prefix="/training", tags=["Training & E-Learning"])

@router.get("/courses", summary="Courses")
def courses():
    return {"module": "Training & E-Learning", "page": "Courses"}

@router.get("/exams", summary="Exams")
def exams():
    return {"module": "Training & E-Learning", "page": "Exams"}

@router.get("/certifications", summary="Certifications")
def certifications():
    return {"module": "Training & E-Learning", "page": "Certifications"}

@router.get("/learning-materials", summary="Learning Materials")
def learning_materials():
    return {"module": "Training & E-Learning", "page": "Learning Materials"}

@router.get("/attendance", summary="Attendance")
def attendance():
    return {"module": "Training & E-Learning", "page": "Attendance"}

