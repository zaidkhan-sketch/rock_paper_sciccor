ROCK PAPER SCISSORS - STREAMLIT GAME
=====================================

ABOUT
-----
A simple Rock Paper Scissors game built with Python and Streamlit.
Play against the computer, keep score, and review previous rounds.

FEATURES
--------
- Play Rock, Paper, or Scissors against the computer.
- Computer randomly selects its move.
- Automatically determines the winner.
- Tracks player wins, computer wins, and draws.
- Displays game history.
- Reset scores and history.

PROJECT FILES
-------------
app.py             Main Streamlit application
requirements.txt   Python dependencies
README.txt         Project instructions

RUN LOCALLY
-----------
1. Open a terminal in this project folder.
2. (Optional) Create and activate a virtual environment:

   Windows:
       python -m venv venv
       venv\Scripts\activate

   macOS/Linux:
       python3 -m venv venv
       source venv/bin/activate

3. Install dependencies:

       pip install -r requirements.txt

4. Run the application:

       streamlit run app.py

5. Open the local URL shown in the terminal, usually:
       http://localhost:8501

DEPLOY TO STREAMLIT COMMUNITY CLOUD
-----------------------------------
1. Create a GitHub account if you do not already have one.
2. Create a new GitHub repository.
3. Upload app.py, requirements.txt, and README.txt to the
   repository's root folder.
4. Visit https://share.streamlit.io/ and sign in with GitHub.
5. Choose "Create app" / "New app".
6. Select your repository and branch.
7. Set the main file path to:
       app.py
8. Click "Deploy".
9. After deployment, Streamlit will provide a public URL.

DEPLOYMENT TIPS
---------------
- Keep app.py and requirements.txt in the repository root,
  or specify the correct app.py path during deployment.
- Do not upload passwords, API keys, or private information.
- If deployment fails, check the app logs for the error.

HOW TO PLAY
-----------
1. Click Rock, Paper, or Scissors.
2. The computer randomly chooses its move.
3. The app displays both moves and the round result.
4. Check the scoreboard and play another round.
5. Click Reset Game to clear the scores and history.

GAME RULES
----------
- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- Matching choices result in a draw.

DEPENDENCIES
------------
Streamlit (listed in requirements.txt)
Python random module (built in)

LICENSE
-------
Free to use and modify for learning and personal projects.
