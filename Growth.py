#streamlit
import streamlit as st

st.set_page_config(page_title=" 🌱 Growth Mindset Challenge")
st.title(" 🌱Growth Mindset Challenge  🌟 ")

st.header("🚀 Welcome To your Growth Journey!")
st.write("Enclose challenges, learn from mistakes, and unlock your full thought. This AI powered app helps you build a GROWTH MINDSET with impression, challanges and achievements! ⭐")

#quote 
st.header("💡 Today's Growth Mindset Quote")
st.write(" The growth mindset is always there to help you see that it does not matter what stage you are in your life you can always learn more and be the best at anything if you apply yourself 100%!- CAROL DWECK")

st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.sucess(f" you're facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header(" 🧠 Reflect On Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f" ⭐ Great Insight! Your Reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties")
    
#achivement
st.header("🏆 Celebrates Your Wins!")
achievement = st.text_input("Share you've recently achievement:")

if achievement:
    st.success(f"🎉 Amazing You Achieved: You achieved: {achievement}")
else:
    st.info("Big or small , every achievementcounts! Share one now 😍")

#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")