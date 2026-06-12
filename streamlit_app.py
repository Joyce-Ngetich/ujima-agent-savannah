
import streamlit as st
from crewai import Agent, Task, Crew, Process

# ----------------------------------------------------
# UJIMA AGENT SAVANNAH PROTOTYPE
# Assignment Demonstration Version
# ----------------------------------------------------

st.set_page_config(
    page_title="Ujima Agent Savannah",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------
# AGENTS
# -------------------------------

scout_agent = Agent(
    role="Ujima Financial Literacy Coach & Field Scout",
    goal="Deliver agricultural liquidity education based on harvest cycles.",
    backstory=(
        "You are a community-focused advisor grounded in local market realities. "
        "You provide educational guidance while respecting operational limits."
    ),
    verbose=True,
    allow_delegation=False
)

guardian_agent = Agent(
    role="Ujima Loan Underwriting Triage Guardian",
    goal="Assess application profiles against transaction history and crop calendars.",
    backstory=(
        "You evaluate risk indicators and prepare escalation packets when necessary."
    ),
    verbose=True,
    allow_delegation=False
)

hunter_agent = Agent(
    role="Ujima Human-in-the-Loop Integration Liaison",
    goal="Generate clear operational briefings for human decision-makers.",
    backstory=(
        "You summarize findings in plain language for regional credit officers."
    ),
    verbose=True,
    allow_delegation=False
)

# -------------------------------
# STREAMLIT INTERFACE
# -------------------------------

st.title("🌾 Ujima Agent Savannah")
st.subheader("Multi-Agent Agricultural Credit Assessment Prototype")

user_case = st.text_area(
    "Enter Applicant Scenario",
    value="No money for school fees, next matooke harvest not until October."
)

if st.button("Run Assessment"):

    scout_literacy_task = Task(
        description=f"""
        Analyze the following applicant message:

        '{user_case}'

        Extract key metrics and produce a structured household profile.
        """,
        expected_output="Structured household profile.",
        agent=scout_agent
    )

    guardian_triage_task = Task(
        description="""
        Analyze the Scout profile.
        Evaluate repayment capacity, income variance and seasonal risks.
        Produce an underwriting assessment packet.
        """,
        expected_output="Risk and compliance assessment.",
        agent=guardian_agent
    )

    hunter_briefing_task = Task(
        description="""
        Convert the underwriting packet into a concise briefing suitable
        for a regional credit officer.
        """,
        expected_output="Plain-language credit officer briefing.",
        agent=hunter_agent
    )

    crew = Crew(
        agents=[
            scout_agent,
            guardian_agent,
            hunter_agent
        ],
        tasks=[
            scout_literacy_task,
            guardian_triage_task,
            hunter_briefing_task
        ],
        process=Process.sequential
    )

    with st.spinner("Running multi-agent analysis..."):
        result = crew.kickoff()

    st.success("Assessment Complete")

    st.markdown("### Assessment Output")
    st.write(result)

st.markdown("---")
st.caption(
    "Academic Prototype: Demonstrates multi-agent orchestration using CrewAI."
)