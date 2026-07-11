def get_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:
        recommendations.append(f"Learn {skill}")
            
    return recommendations