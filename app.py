import streamlit as st

st.title("Birthday quiz with Hints")

# Questions, answers, and hints
quiz = [
    {"question": "Get one of our favorite snack!", "answer": "unigiri", "hint": "sushi?"},
    {"question": "Go to a spot which can bring you to another place whats it called?", "answer": "MTR", "hint": "middle"},
    {"question": "Great Job, now go to Hysan Place, where is it?", "answer": "CausewayBay", "hint": "middle"},
    {"question": "Correct! Now go to exit D2 and go to the seven eleven we normally go to and buy a drink for yourself I pay. When done say say", "answer": "ok", "hint": "middle"},
    {"question": "Greatttt, refreshing drink huh? go to the apple store!!! When done say yes", "answer": "yes", "hint": "middle"},
    {"question": "Are you happy??? Then go to the D2 exit again, its time to leave. When done say ok", "answer": "ok", "hint": "middle"},
    {"question": "Go to the place, which is in the middle?", "answer": "central", "hint": "middle"},
    {"question": "Time to make some steps, Where do you need to go to? Say idk when you arrive at the mtr station central", "answer": "idk", "hint": "Hong Kong in Hong Kong?"},
    {"question": "Where can you go shopping, at the.....", "answer": "mall", "hint": "place"},
    {"question": "Great job! Then walk into the mall. Where do we normally buy coffee?", "answer": "starbucks", "hint": "green and brown!"},
    {"question": "Time to leave? Choose yes or no", "answer": "no", "hint": "choose what you want"},
    {"question": "Eventhough it is your birthday you can't decide!!, what would you say in this case? hint: poop", "answer": "shit", "hint": "poop"},
    {"question": "Well in this case, take a coffee break. You deserve it! Go to starbucks and buy your favorite drink, I pay! Say yes when you are DONE with drinking coffee", "answer": "yes", "hint": "Time to walk"},
    {"question": "Time to go up where I normally go to the toilet. Remember? Choose yes or no when you are NEAR the toilet when done say yes!", "answer": "yes", "hint": "Time to walk"},
    {"question": "Hehehehe joke!!! Go to the apple store, you need to return your gift is that ok for you? say no or yes?", "answer": "yes", "hint": "you better say yes"},
    {"question": "you said yes because otherwise you can not see this. Then it is time to go back to apple and I will give you further signals say yeah when you are DONE", "answer": "yeah", "hint": "read carefully"},
    {"question": "It is time to go back home! hope you had a great tourrrr and workout hihihi. happy bday <3 and hope you enjoyed it hihihi. say ok", "answer": "ok", "hint": "read carefully"},
]

# Track current step
if "step" not in st.session_state:
    st.session_state.step = 0

if st.session_state.step < len(quiz):
    q = quiz[st.session_state.step]

    st.subheader(f"Question {st.session_state.step + 1}")
    answer = st.text_input(q["question"])

    if st.button("Check"):
        if answer.lower().strip() == q["answer"]:
            st.success(q["hint"])
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("Not correct, try again. Read carefully please.")

else:
    st.balloons()
    st.success("You did itttt, eventhough I can not be in HK hope you still enjoyed it hihi. You finished the great hk tour on a sunday!! sorry hihi")
