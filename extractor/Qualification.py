def extract_qualification(text):

    text = text.lower()

    qualifications = {
        "Bachelor of Technology (B.Tech)": [
            "b.tech", "btech", "bachelor of technology"
        ],

        "Bachelor of Engineering (B.E.)": [
            "b.e", "be", "bachelor of engineering"
        ],

        "Bachelor of Computer Applications (BCA)": [
            "bca", "bachelor of computer applications"
        ],

        "Master of Computer Applications (MCA)": [
            "mca", "master of computer applications"
        ],

        "Bachelor of Science (B.Sc)": [
            "b.sc", "bsc", "bachelor of science"
        ],

        "Master of Technology (M.Tech)": [
            "m.tech", "mtech", "master of technology"
        ]
    }

    found = []

    for degree, keywords in qualifications.items():
        for keyword in keywords:
            if keyword in text:
                found.append(degree)
                break

    return found