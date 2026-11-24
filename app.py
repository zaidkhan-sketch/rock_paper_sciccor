import random
import streamlit as st

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊", layout="centered")
st.title("✊ Rock Paper Scissors ✋")
st.write("Play against the computer. Choose your move!")

CHOICES = ["Rock", "Paper", "Scissors"]
EMOJIS = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}

def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    if ((user == "Rock" and computer == "Scissors")
        or (user == "Paper" and computer == "Rock")
        or (user == "Scissors" and computer == "Paper")):
        return "You win!"
    return "Computer wins!"

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.draws = 0
    st.session_state.rounds = 0
    st.session_state.history = []

def play(user_choice):
    computer_choice = random.choice(CHOICES)
    result = decide_winner(user_choice, computer_choice)
    st.session_state.rounds += 1
    if result == "You win!":
        st.session_state.user_score += 1
    elif result == "Computer wins!":
        st.session_state.computer_score += 1
    else:
        st.session_state.draws += 1
    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice
    st.session_state.result = result
    st.session_state.history.insert(0, {
        "Round": st.session_state.rounds,
        "You": user_choice,
        "Computer": computer_choice,
        "Result": result
    })

st.subheader("Choose your move")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✊ Rock", use_container_width=True):
        play("Rock")
with col2:
    if st.button("✋ Paper", use_container_width=True):
        play("Paper")
with col3:
    if st.button("✌️ Scissors", use_container_width=True):
        play("Scissors")

if "result" in st.session_state:
    st.divider()
    st.subheader("Round result")
    left, right = st.columns(2)
    with left:
        st.write("**Your move**")
        st.title(EMOJIS[st.session_state.user_choice])
        st.write(st.session_state.user_choice)
    with right:
        st.write("**Computer's move**")
        st.title(EMOJIS[st.session_state.computer_choice])
        st.write(st.session_state.computer_choice)

    if st.session_state.result == "You win!":
        st.success("🎉 You win this round!")
    elif st.session_state.result == "Computer wins!":
        st.error("🤖 Computer wins this round!")
    else:
        st.info("🤝 It's a draw!")

st.divider()
st.subheader("Scoreboard")
a, b, c = st.columns(3)
a.metric("Your wins", st.session_state.user_score)
b.metric("Computer wins", st.session_state.computer_score)
c.metric("Draws", st.session_state.draws)
st.caption(f"Rounds played: {st.session_state.rounds}")

if st.session_state.history:
    with st.expander("View game history"):
        st.dataframe(st.session_state.history, use_container_width=True, hide_index=True)

if st.button("🔄 Reset Game", use_container_width=True):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

st.caption("Rock beats Scissors. Scissors beats Paper. Paper beats Rock.")
