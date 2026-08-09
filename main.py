from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from io import BytesIO
import traceback

from parser.pdf_parser import extract_text
from preprocessing.text_cleaner import clean_text
from extractor.skills import extract_skills
from similarity.score import calculate_score
from recommadation.recommadate import get_recommendations


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="AI Resume Screener API",
    version="1.0"
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():
    return {
        "message": "AI Resume Screener Backend Running 🚀"
    }


# =========================================================
# ANALYZE RESUMES
# =========================================================

@app.post("/analyze")
async def analyze_resume(
    resumes: List[UploadFile] = File(...),
    job_description: str = Form(...)
):

    print("\n==============================================")
    print("🔥 ANALYZE ENDPOINT HIT")
    print("==============================================")

    print("JD received:", bool(job_description))
    print("Resume count:", len(resumes) if resumes else 0)


    # =====================================================
    # VALIDATE RESUMES
    # =====================================================

    if not resumes:
        raise HTTPException(
            status_code=400,
            detail="No resumes uploaded."
        )


    # =====================================================
    # VALIDATE JOB DESCRIPTION
    # =====================================================

    if not job_description or not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description is empty."
        )


    # =====================================================
    # PROCESS JOB DESCRIPTION
    # =====================================================

    print("\n==============================================")
    print("📌 PROCESSING JOB DESCRIPTION")
    print("==============================================")


    try:

        cleaned_jd = clean_text(
            job_description
        )

        print(
            "JD cleaned length:",
            len(cleaned_jd)
        )


        jd_skills = extract_skills(
            cleaned_jd
        )

        print(
            "🎯 JD Skills:",
            jd_skills
        )


    except Exception as error:

        print("\n❌ JD PROCESSING FAILED")

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"Job description processing failed: {str(error)}"
        )


    # =====================================================
    # RESULTS
    # =====================================================

    results = []


    # =====================================================
    # PROCESS EACH RESUME
    # =====================================================

    for resume_file in resumes:

        print("\n==============================================")
        print(
            "📄 PROCESSING RESUME:",
            resume_file.filename
        )
        print("==============================================")


        try:

            # -------------------------------------------------
            # FILE TYPE
            # -------------------------------------------------

            filename = (
                resume_file.filename or ""
            ).lower()


            if not filename.endswith(".pdf"):

                raise ValueError(
                    "Only PDF resumes are supported."
                )


            # -------------------------------------------------
            # READ PDF
            # -------------------------------------------------

            pdf_bytes = await resume_file.read()


            print(
                "PDF size:",
                len(pdf_bytes),
                "bytes"
            )


            if not pdf_bytes:

                raise ValueError(
                    "Uploaded PDF is empty."
                )


            # -------------------------------------------------
            # CREATE PDF STREAM
            # -------------------------------------------------

            pdf_stream = BytesIO(
                pdf_bytes
            )


            # -------------------------------------------------
            # EXTRACT TEXT
            # -------------------------------------------------

            resume_text = extract_text(
                pdf_stream
            )


            print(
                "Resume text length:",
                len(resume_text)
            )


            if not resume_text:

                raise ValueError(
                    "No text extracted from PDF."
                )


            if not resume_text.strip():

                raise ValueError(
                    "PDF contains no readable text."
                )


            # -------------------------------------------------
            # CLEAN RESUME
            # -------------------------------------------------

            cleaned_resume = clean_text(
                resume_text
            )


            print(
                "Cleaned resume length:",
                len(cleaned_resume)
            )


            if not cleaned_resume.strip():

                raise ValueError(
                    "Resume became empty after cleaning."
                )


            # -------------------------------------------------
            # EXTRACT RESUME SKILLS
            # -------------------------------------------------

            resume_skills = extract_skills(
                cleaned_resume
            )


            print(
                "🎯 Resume Skills:",
                resume_skills
            )


            # -------------------------------------------------
            # CALCULATE ATS SCORE
            # -------------------------------------------------

            (
                matched_skills,
                missing_skills,
                ats_score
            ) = calculate_score(
                resume_skills,
                jd_skills
            )


            print(
                "✅ Matched:",
                matched_skills
            )


            print(
                "⚠️ Missing:",
                missing_skills
            )


            print(
                "📊 ATS Score:",
                ats_score
            )


            # -------------------------------------------------
            # RECOMMENDATIONS
            # -------------------------------------------------

            recommendations = get_recommendations(
                missing_skills
            )


            # -------------------------------------------------
            # CANDIDATE RESULT
            # -------------------------------------------------

            candidate_result = {

                "candidate":
                    resume_file.filename,

                "ats_score":
                    float(ats_score or 0),

                "matched_skills":
                    list(matched_skills or []),

                "missing_skills":
                    list(missing_skills or []),

                "recommendations":
                    list(recommendations or []),

                "education":
                    "B.Tech CSE",

                "experience":
                    "Fresher"
            }


            # -------------------------------------------------
            # ADD RESULT
            # -------------------------------------------------

            results.append(
                candidate_result
            )


            print(
                "✅ CANDIDATE SUCCESSFULLY ANALYZED"
            )


            print(
                candidate_result
            )


        except Exception as error:

            print("\n==============================================")
            print("❌ RESUME PROCESSING FAILED")
            print("==============================================")


            print(
                "File:",
                resume_file.filename
            )


            print(
                "Error type:",
                type(error).__name__
            )


            print(
                "Error:",
                str(error)
            )


            print("\nFULL TRACEBACK:")

            traceback.print_exc()


            raise HTTPException(

                status_code=422,

                detail={

                    "candidate":
                        resume_file.filename,

                    "error":
                        str(error)
                }
            )


    # =====================================================
    # CHECK RESULTS
    # =====================================================

    if not results:

        raise HTTPException(
            status_code=422,
            detail="No resumes could be analyzed."
        )


    # =====================================================
    # SORT RESULTS
    # =====================================================

    results.sort(

        key=lambda candidate:
            float(
                candidate["ats_score"]
            ),

        reverse=True
    )


    # =====================================================
    # TOTAL CANDIDATES
    # =====================================================

    total_candidates = len(
        results
    )


    # =====================================================
    # AVERAGE ATS
    # =====================================================

    average_ats_score = round(

        sum(
            float(
                candidate["ats_score"]
            )

            for candidate in results
        )

        / total_candidates,

        2
    )


    # =====================================================
    # QUALIFIED CANDIDATES
    # =====================================================

    qualified = sum(

        1

        for candidate in results

        if float(
            candidate["ats_score"]
        ) >= 70
    )


    # =====================================================
    # FINAL RESPONSE
    # =====================================================

    response = {

        "total_candidates":
            total_candidates,

        "average_ats_score":
            average_ats_score,

        "top_candidate":
            results[0],

        "highest":
            results[0],

        "lowest":
            results[-1],

        "qualified":
            qualified,

        "ranking":
            results
    }


    # =====================================================
    # DEBUG
    # =====================================================

    print("\n==============================================")
    print("🎯 FINAL BACKEND RESPONSE")
    print("==============================================")


    print(
        "Total Candidates:",
        total_candidates
    )


    print(
        "Average ATS:",
        average_ats_score
    )


    print(
        "Qualified:",
        qualified
    )


    print(
        "Ranking:",
        results
    )


    print("\n==============================================")
    print("✅ ANALYSIS COMPLETED")
    print("==============================================\n")


    return response