import streamlit as st

st.set_page_config(
    page_title="AI Automation Agent",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Automation Agent")
st.caption("AI/Robotics • STEM • Projects • Reports")

st.success("✅ App is running correctly!")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Agents", "6")

with col2:
    st.metric("Email", "Gmail")

with col3:
    st.metric("AI Model", "Gemini")

st.divider()

st.subheader("Available Agents")

agents = [
    "📰 Daily AI/Robotics News",
    "🏫 STEM Class Update",
    "💡 Daily STEM Tip",
    "🔧 Project Idea",
    "📊 Weekly Progress Report",
    "🏆 Competition Update",
]

for agent in agents:
    st.write(agent)
