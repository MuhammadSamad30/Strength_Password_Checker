import streamlit as st
import re
import random
import string

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("""
## 🚀 Welcome to the Password Strength Checker!
This tool will help you determine the **strength** of your **password**. Simply type in your password and hit the button below to check its strength! 💪
""")


def generate_strong_pass(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%&*?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password = st.text_input("🔒 Enter your password:", type='password')
checkbtn = st.button("✅ Check Password")
generatebtn = st.button("✨ Generate Strong Password")

if generatebtn:
    strong_password = generate_strong_pass()
    st.text_input("🛡️ Your Strong Password:",
                  value=strong_password, type='default')
    st.success("New Password was Generated Successfully! 🎉")

if checkbtn:
    feedback = []
    score = 0

    if len(password) < 8:
        st.error("❌ Password must be at least 8 characters long.")
    else:
        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            score += 1
        else:
            feedback.append(
                "🔠 Add both **uppercase** and **lowercase** letters to strengthen your password.")

        if re.search("[0-9]", password):
            score += 1
        else:
            feedback.append(
                "🔢 Include at least one **number** (0-9) in your password.")

        if re.search("[!@#$%^&*?]", password):
            score += 1
        else:
            feedback.append(
                "✨ Use a **special character** like !@#$%^&* to make your password more secure.")

        if score == 3:
            st.success("🎉 Your password is **strong**! Great job! 🔥")
        elif score == 2:
            st.warning(
                "⚠️ Your password is **moderate**. Consider adding more variety to make it stronger.")
        else:
            st.error("❌ Your password is **weak**. Follow the suggestions below! 🚨")

        if feedback:
            st.markdown("## 🛠️ Suggestions:")
            for tip in feedback:
                st.markdown(f"- {tip}")

st.markdown("---")
st.markdown("**👨‍💻 Created by: Muhammad Samad**")
