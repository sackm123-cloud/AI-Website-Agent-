import streamlit as st

st.set_page_config(
    page_title="AI Automation Agent",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------

st.title("🤖 AI Automation Agent")
st.write("Your personal AI-powered automation dashboard")

st.divider()

# -----------------------------
# STATUS
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("AI Agents", "6")

with col2:
    st.metric("AI Model", "Gemini")

with col3:
    st.metric("Email", "Gmail")

with col4:
    st.metric("Status", "Online")

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("⚙️ Control Panel")

page = st.sidebar.radio(
    "Select Agent",
    [
        "Dashboard",
        "AI/Robotics News",
        "STEM Class Update",
        "Daily STEM Tip",
        "Project Idea",
        "Weekly Report",
        "Competition Update",
        "Settings"
    ]
)

# -----------------------------
# DASHBOARD
# -----------------------------

if page == "Dashboard":

    st.header("📊 Dashboard")

    st.success("AI Automation Agent is running.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🤖 Available Agents")

        st.write("📰 Daily AI/Robotics News")
        st.write("🏫 STEM Class Update")
        st.write("💡 Daily STEM Tip")

    with col2:
        st.subheader("🚀 Automation")

        st.write("🔧 Project Idea Agent")
        st.write("📊 Weekly Progress Report")
        st.write("🏆 Competition Update")

    st.divider()

    st.subheader("📧 Email")

    if st.button("📨 Test Gmail"):
        st.success("Gmail test button working.")

# -----------------------------
# NEWS
# -----------------------------

elif page == "AI/Robotics News":

    st.header("📰 Daily AI/Robotics News")

    st.write("Generate the latest AI and robotics news summary.")

    if st.button("🔎 Generate News"):

        with st.spinner("Generating news..."):
            st.success("News agent started.")

        st.text_area(
            "Generated News",
            value="Your AI/Robotics news will appear here.",
            height=250
        )

    if st.button("📧 Send News by Gmail"):
        st.success("Gmail sending function will be connected here.")

# -----------------------------
# STEM CLASS
# -----------------------------

elif page == "STEM Class Update":

    st.header("🏫 STEM Class Update")

    grade = st.selectbox(
        "Select Grade",
        ["Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"]
    )

    topic = st.text_input(
        "Session Topic",
        placeholder="Example: Transistor as a switch"
    )

    activities = st.text_area(
        "Activities",
        placeholder="Describe today's class activities..."
    )

    if st.button("🤖 Generate Class Report"):

        if not topic:
            st.warning("Please enter the session topic.")
        else:
            st.success("Class report generated.")

            st.write(
                f"""
                **{grade}**

                **Topic:** {topic}

                **Activities:** {activities}

                Students participated in a practical STEM session
                and explored the concepts through hands-on activities.
                """
            )

# -----------------------------
# STEM TIP
# -----------------------------

elif page == "Daily STEM Tip":

    st.header("💡 Daily STEM Tip")

    if st.button("✨ Generate STEM Tip"):

        st.info(
            """
            **Today's STEM Tip**

            Build an LED brightness controller using a potentiometer
            and Arduino.

            Components:
            - Arduino Uno
            - LED
            - 220Ω resistor
            - Potentiometer
            - Jumper wires

            Concept:
            Analog input → PWM output
            """
        )

# -----------------------------
# PROJECT IDEA
# -----------------------------

elif page == "Project Idea":

    st.header("🔧 Project Idea Agent")

    category = st.selectbox(
        "Project Category",
        [
            "Arduino",
            "ESP8266",
            "ESP32",
            "Robotics",
            "IoT",
            "AI/ML"
        ]
    )

    level = st.selectbox(
        "Difficulty",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("🚀 Generate Project"):

        st.success("Project generated.")

        st.subheader("🤖 Smart Obstacle Avoiding Robot")

        st.write(f"**Platform:** {category}")
        st.write(f"**Level:** {level}")

        st.write(
            """
            **Components**

            • ESP32  
            • Ultrasonic sensor  
            • Motor driver  
            • DC motors  
            • Robot chassis  
            • Battery

            **Circuit Concept**

            Ultrasonic sensor → ESP32 → Motor Driver → Motors

            **Software**

            Read distance → detect obstacle → change direction.
            """
        )

# -----------------------------
# WEEKLY REPORT
# -----------------------------

elif page == "Weekly Report":

    st.header("📊 Weekly Progress Report")

    activities = st.text_area(
        "Enter weekly activities",
        placeholder="Enter classes, projects, robotics activities..."
    )

    if st.button("📄 Generate Weekly Report"):

        st.success("Weekly report generated.")

        st.write(
            """
            ## Weekly STEM Progress Report

            The week focused on practical STEM learning,
            electronics, robotics and programming activities.

            Students participated in hands-on experiments
            and developed practical problem-solving skills.
            """
        )

# -----------------------------
# COMPETITION
# -----------------------------

elif page == "Competition Update":

    st.header("🏆 Competition Update")

    repository = st.text_input(
        "GitHub Repository",
        value="sackm123-cloud/Kaggriculture-competition"
    )

    if st.button("🔍 Check Competition"):

        st.info(f"Checking: {repository}")

        st.write(
            """
            Competition monitoring will check:

            • GitHub commits
            • Agent versions
            • Submission status
            • Score changes
            • Recent improvements
            """
        )

# -----------------------------
# SETTINGS
# -----------------------------

elif page == "Settings":

    st.header("⚙️ Settings")

    st.subheader("Gemini")

    gemini_key = st.text_input(
        "Gemini API Key",
        type="password"
    )

    st.subheader("Gmail")

    gmail_user = st.text_input("Gmail Address")

    gmail_password = st.text_input(
        "Gmail App Password",
        type="password"
    )

    if st.button("💾 Save Settings"):

        st.success("Settings received.")

st.divider()

st.caption("AI Automation Agent • Streamlit • Gemini • Gmail")
