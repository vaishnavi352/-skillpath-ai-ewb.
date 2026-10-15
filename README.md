# SkillPath AI — EWB Courses Project

A beginner-friendly website that recommends a career/skill direction and four-week starter roadmap.

## Deploy from Android
1. Sign in to GitHub in your phone browser.
2. Create a repository named `skillpath-ai-ewb`.
3. Add `app.py` and `requirements.txt` from this folder to the repository using **Add file → Create new file** or upload the files if your browser supports it.
4. Open https://share.streamlit.io/ and sign in with GitHub.
5. Choose **Create app → Yup, I have an app**.
6. Select repository `skillpath-ai-ewb`, branch `main`, and main file path `app.py`.
7. Click **Deploy** and wait for the app to start.

## Run locally
`pip install -r requirements.txt`
`streamlit run app.py`

## Important
This version uses transparent rule-based matching, not a trained machine-learning model. Do not describe the match score as an employment probability. Test the app before submitting it.
