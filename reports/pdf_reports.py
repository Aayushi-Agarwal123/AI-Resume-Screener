from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    results,
    best_candidate,
    total_candidates,
    highest_score,
    average_score,
    qualified_candidates
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate("Hiring_Report.pdf")

    elements = []

    elements.append(
        Paragraph("<b>Dashboard Overview</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(
            f"""
            Total Candidates : {total_candidates}<br/>
            Highest ATS Score : {highest_score:.2f}%<br/>
            Average ATS Score : {average_score:.2f}%<br/>
            Qualified Candidates : {qualified_candidates}
            """,
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph("<b>Best Candidate</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(
            f"""
            Candidate : {best_candidate['Candidate']}<br/>
            ATS Score : {best_candidate['Score']:.2f}%<br/>
            Qualification : {best_candidate['Qualification']}
            """,
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph("<b>Candidate Ranking</b>", styles["Heading2"])
    )

    for candidate in results:

        elements.append(
            Paragraph(
                f"""
                {candidate['Rank']}. {candidate['Candidate']}<br/>
                ATS Score : {candidate['Score']:.2f}%<br/>
                Qualification : {candidate['Qualification']}<br/><br/>
                """,
                styles["BodyText"]
            )
        )

    doc.build(elements)

    return "Hiring_Report.pdf"