import streamlit as st

st.set_page_config(page_title="SkillPath AI", page_icon="🎓", layout="centered")

CAREERS = {
    "AI / Machine Learning": {
        "interests": {"AI", "Python", "Mathematics", "Data"},
        "skills": ["Python basics", "NumPy and pandas", "Data visualization", "Machine learning basics", "A small prediction project"],
        "roadmap": ["Week 1: Revise Python variables, conditions, loops, and functions.",
                    "Week 2: Learn pandas and basic data cleaning.",
                    "Week 3: Learn charts and introductory ML concepts.",
                    "Week 4: Build a small project and document the results."],
        "resources": ["Python: https://docs.python.org/3/tutorial/",
                      "scikit-learn: https://scikit-learn.org/stable/getting_started.html"]
    },
    "Web Development": {
        "interests": {"Websites", "Design", "JavaScript", "Building apps"},
        "skills": ["HTML", "CSS", "JavaScript", "Responsive design", "Backend basics", "Database basics"],
        "roadmap": ["Week 1: Create pages with HTML and CSS.",
                    "Week 2: Add JavaScript interactions.",
                    "Week 3: Learn backend and database basics.",
                    "Week 4: Build a small portfolio website."],
        "resources": ["MDN Web Docs: https://developer.mozilla.org/",
                      "Flask: https://flask.palletsprojects.com/"]
    },
    "Data Analyst": {
        "interests": {"Data", "Mathematics", "Business", "Charts"},
        "skills": ["Spreadsheets", "SQL", "Python pandas", "Data visualization", "Dashboard storytelling"],
        "roadmap": ["Week 1: Practice spreadsheet formulas.",
                    "Week 2: Learn SQL SELECT, WHERE, GROUP BY, and JOIN.",
                    "Week 3: Analyze a dataset with pandas and charts.",
                    "Week 4: Create a dashboard and write three insights."],
        "resources": ["SQLBolt: https://sqlbolt.com/",
                      "pandas: https://pandas.pydata.org/docs/getting_started/"]
    },
    "Cybersecurity": {
        "interests": {"Security", "Networks", "Problem solving", "Linux"},
        "skills": ["Networking basics", "Linux commands", "Web security fundamentals", "Threat awareness", "Ethical lab practice"],
        "roadmap": ["Week 1: Learn IP addresses, DNS, HTTP, and ports.",
                    "Week 2: Practice basic Linux commands.",
                    "Week 3: Study authentication and defensive security.",
                    "Week 4: Complete beginner labs in authorized training environments."],
        "resources": ["Cisco Skills for All: https://skillsforall.com/",
                      "OWASP Top 10: https://owasp.org/www-project-top-ten/"]
    },
    "Cloud Computing": {
        "interests": {"Cloud", "Networks", "Building apps", "Infrastructure"},
        "skills": ["Cloud concepts", "Linux basics", "Networking", "Git and GitHub", "Deploy a small application"],
        "roadmap": ["Week 1: Learn cloud service models.",
                    "Week 2: Practice Linux and networking.",
                    "Week 3: Learn Git and version control.",
                    "Week 4: Deploy a small demo application."],
        "resources": ["AWS Training: https://aws.amazon.com/training/",
                      "Git documentation: https://git-scm.com/doc"]
    }
}

st.title("🎓 SkillPath AI")
st.subheader("Skill and career recommendations for students")
st.write("Enter your preferences to receive a suggested starting path and a four-week learning roadmap.")

with st.form("profile"):
    name = st.text_input("Name (optional)")
    level = st.selectbox("Current coding level", ["No coding experience", "Basic Python", "Intermediate"])
    goal = st.selectbox("Main goal", ["Get an internship", "Prepare for a job", "Build projects", "Explore careers"])
    weekly_time = st.selectbox("Time available each week", ["1–3 hours", "4–6 hours", "7–10 hours", "10+ hours"])
    interests = st.multiselect("Choose your interests",
        ["AI", "Python", "Mathematics", "Data", "Websites", "Design", "JavaScript",
         "Building apps", "Business", "Charts", "Security", "Networks",
         "Problem solving", "Linux", "Cloud", "Infrastructure"],
        default=["AI", "Python"])
    learning_style = st.selectbox("Preferred learning style", ["Videos", "Reading", "Hands-on projects", "A mix of all"])
    submitted = st.form_submit_button("Recommend my path")

def get_recommendations(selected, level, goal):
    scored = []
    for career, details in CAREERS.items():
        overlap = len(set(selected) & details["interests"])
        score = round(100 * overlap / max(1, len(details["interests"])))
        if career == "AI / Machine Learning" and level == "Basic Python":
            score += 10
        if career == "Web Development" and goal == "Build projects":
            score += 10
        scored.append((career, min(score, 100), details))
    return sorted(scored, key=lambda item: item[1], reverse=True)

if submitted:
    if not interests:
        st.warning("Please select at least one interest.")
    else:
        results = get_recommendations(interests, level, goal)
        career, score, details = results[0]
        st.success(f"{name.strip() or 'Student'}, your suggested starting path is: {career}")
        st.metric("Interest-match score", f"{score}/100")
        st.caption("This is a simple rule-based match score, not a probability of employment or a validated career assessment.")

        st.header("Skills to learn")
        for skill in details["skills"]:
            st.write(f"• {skill}")

        st.header("Your four-week roadmap")
        for step in details["roadmap"]:
            st.write(f"• {step}")

        st.header("Learning resources")
        for resource in details["resources"]:
            st.markdown(f"- {resource}")

        st.header("Other paths to explore")
        for other_career, other_score, _ in results[1:3]:
            st.write(f"{other_career}: {other_score}/100 match score")

        st.info(f"Goal: {goal} | Weekly time: {weekly_time} | Learning style: {learning_style}")
        roadmap_text = f"SkillPath AI Roadmap\nSuggested path: {career}\nGoal: {goal}\nWeekly time: {weekly_time}\n\nSkills:\n"
        roadmap_text += "\n".join("- " + s for s in details["skills"])
        roadmap_text += "\n\nFour-week roadmap:\n" + "\n".join(details["roadmap"])
        roadmap_text += "\n\nResources:\n" + "\n".join(details["resources"])
        st.download_button("Download my roadmap", roadmap_text, file_name="my_skill_roadmap.txt")

with st.expander("How does this recommendation work?"):
    st.write("The app compares selected interests with predefined career profiles, calculates a transparent rule-based score, and ranks the profiles. It is an educational prototype, not a trained machine-learning model.")
