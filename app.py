import streamlit as st

st.title("Birthday quiz with Hints")

# Questions, answers, and hints
quiz = [
    {"question": "Get one of our favorite snack!", "answer": "unigiri", "hint": "sushi?"},
    {"question": "Go to a spot which can bring you to another place whats it called?", "answer": "mtr", "hint": "middle"},
    {"question": "Great Job, now go to Hysan Place, where is it?", "answer": "cwb", "hint": "middle"},
    {"question": "Correct! Now go to exit D2 and go to the seven eleven we normally go to and buy a drink for yourself I pay. When done say ok", "answer": "ok", "hint": "middle"},
    {"question": "Greatttt, refreshing drink huh? go to the apple store!!! When done say yes", "answer": "yes", "hint": "middle"},
    {"question": "Are you happy??? Then go to the D2 exit again, its time to leave. When arrive at the mtr say ok", "answer": "ok", "hint": "middle"},
    {"question": "Time to make some steps, we are not leaving CWB, Where do you need to go to? Guess and if you don't know say idk", "answer": "idk", "hint": "Hong Kong in Hong Kong?"},
    {"question": "time to have some other food!! There are some great spots here sooo lets gooo. Answer ok and see where you need to go!.", "answer": "ok", "hint": "place"},
    {"question": "Great job! Time to have ramen!! The restaurant is called ramenya shima. When done with food say ok", "answer": "ok", "hint": "green and brown!"},
    {"question": "Time to leave? Choose yes or no", "answer": "yes", "hint": "choose what you want"},
    {"question": "Eventhough it is your birthday you can't decide!!, what would you say in this case? hint: poop", "answer": "shit", "hint": "poop"},
    {"question": "Hehehehe joke!!! Go to the apple store, you need to return your gift is that ok for you? say no or yes?", "answer": "yes", "hint": "you better say yes"},
    {"question": "you said yes because otherwise you can not see this. But instead, it is time to go back home! hope you had a great tourrrr and workout hihihi. happy bday <3 and hope you enjoyed it hihihi. say ok", "answer": "ok", "hint": "read carefully"},
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
