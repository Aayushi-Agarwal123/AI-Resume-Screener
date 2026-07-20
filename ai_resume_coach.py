def generate_ai_feedback(score, matched_skills, missing_skills, matched_qualification):

    # Remove duplicate skills
    matched_skills = sorted(set(matched_skills))
    missing_skills = sorted(set(missing_skills))

    feedback = []

    # ================= Overall Assessment =================

    feedback.append("🤖 AI Resume Coach\n")

    if score >= 90:
        feedback.append(
            "🟢 Excellent! Your resume is highly aligned with the job description and demonstrates a very strong profile."
        )

    elif score >= 80:
        feedback.append(
            "🟢 Good Match! Your resume satisfies most of the job requirements with only a few improvements needed."
        )

    elif score >= 70:
        feedback.append(
            "🟡 Moderate Match! Your profile has good potential, but adding a few missing skills would significantly improve your ATS score."
        )

    else:
        feedback.append(
            "🔴 Your resume currently has limited alignment with the job description. Improving your skills and resume content is recommended."
        )

    # ================= Strengths =================

    feedback.append("\n💪 Strengths")

    if matched_qualification:
        feedback.append("✔ Qualification matches the job requirements.")

    if matched_skills:
        feedback.append(
            f"✔ Matched Technical Skills: {', '.join(matched_skills[:6])}"
        )

    if score >= 80:
        feedback.append("✔ Strong ATS compatibility.")

    # ================= Areas to Improve =================

    feedback.append("\n⚠ Areas to Improve")

    if missing_skills:
        feedback.append(
            "Consider learning these skills to improve your profile:"
        )

        feedback.append(
            ", ".join(missing_skills[:6])
        )

    else:
        feedback.append(
            "No major missing skills were identified."
        )

    if score < 70:
        feedback.append(
            "• Add more real-world projects."
        )

        feedback.append(
            "• Quantify achievements in your resume."
        )

        feedback.append(
            "• Include certifications and deployment links."
        )

    # ================= Interview Probability =================

    feedback.append("\n🎯 Interview Probability")

    if score >= 90:
        probability = 95

    elif score >= 80:
        probability = 85

    elif score >= 70:
        probability = 70

    else:
        probability = 40

    feedback.append(f"{probability}% Chance of Selection")

    # ================= Recruiter Decision =================

    feedback.append("\n👨‍💼 Recruiter Decision")

    if score >= 85 and matched_qualification:

        feedback.append(
            "✅ Highly Recommended for Interview"
        )

    elif score >= 70:

        feedback.append(
            "🟡 Recommended after improving the missing skills."
        )

    else:

        feedback.append(
            "❌ Not Recommended at the current stage."
        )

    # ================= Final Suggestion =================

    feedback.append("\n🚀 Final Suggestion")

    if score >= 85:

        feedback.append(
            "Your resume is already competitive. Focus on interview preparation and continue enhancing your technical portfolio."
        )

    elif score >= 70:

        feedback.append(
            "Adding the recommended skills and improving project descriptions can noticeably increase your ATS score."
        )

    else:

        feedback.append(
            "Improve your technical skills, add quality projects, certifications, and measurable achievements before applying."
        )

    return "\n".join(feedback)