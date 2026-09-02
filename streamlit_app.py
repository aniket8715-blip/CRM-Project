import os
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ICICI Bank — AI Credit Card Cross-Sell Platform",
    page_icon="🏦",
    layout="wide",
)

# --- Make sure Python can find crew.py sitting next to this file ---
THIS_DIR = Path(__file__).parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

# --- Load the Gemini API key from Streamlit secrets before crewai is imported ---
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

from crew import AirtelNexusAiCustomerGrowthPlatformCrew

MAX_RUNS_PER_SESSION = 5  # simple cost guardrail for a public demo link
DATA_PATH = THIS_DIR / "icici_customer_360.csv"


@st.cache_data
def load_customer_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


st.title("🏦 ICICI Bank — AI Credit Card Cross-Sell Platform")
st.caption(
    "A multi-agent CrewAI demo: 7 AI agents analyze real ICICI Bank Customer 360 "
    "data to score credit card cross-sell propensity and generate a next-best-action "
    "growth plan — no synthetic data, every customer is real."
)

if "run_count" not in st.session_state:
    st.session_state.run_count = 0

df = load_customer_data()

with st.form("crew_form"):
    col1, col2 = st.columns(2)
    with col1:
        num_customers = st.number_input(
            "Number of real customers to analyze",
            min_value=1,
            max_value=15,
            value=5,
            help="Sampled from the real 300-customer ICICI Customer 360 dataset. Keep small — more customers means a longer, more expensive run.",
        )
        segment_filter = st.selectbox(
            "Filter by customer segment (optional)",
            options=["All segments"] + sorted(df["Customer_Segment"].dropna().unique().tolist()),
        )
    with col2:
        business_objective = st.text_input(
            "Business objective",
            value="Increase credit card cross-sell activation and reduce Approved-Dormant card rates",
        )
    submitted = st.form_submit_button("Run Crew 🚀")

if submitted:
    if not os.environ.get("GEMINI_API_KEY"):
        st.error(
            "No Gemini API key configured. Add GEMINI_API_KEY under this app's "
            "Settings → Secrets in Streamlit Community Cloud."
        )
    elif st.session_state.run_count >= MAX_RUNS_PER_SESSION:
        st.warning(
            f"This demo session has reached its limit of {MAX_RUNS_PER_SESSION} runs. "
            "Please refresh the page later to try again."
        )
    else:
        pool = df if segment_filter == "All segments" else df[df["Customer_Segment"] == segment_filter]
        if len(pool) == 0:
            st.error("No customers match that segment filter.")
        else:
            sample = pool.sample(n=min(int(num_customers), len(pool)), random_state=None).reset_index(drop=True)

            PROMPT_COLUMNS = [
                "Customer_ID", "Full_Name", "City", "Customer_Segment",
                "CIBIL_Score", "Has_Vehicle_Loan", "Has_Home_Loan",
                "Credit_Card_Status", "Credit_Card_Variant",
                "Total_Relationship_Value_INR", "Cross_Sell_Propensity_Score",
                "Product_Engagement_Tier", "Digital_Segment", "Preferred_Channel",
                "Total_CrossSell_Revenue_Potential_INR",
            ]
            customer_data_md = sample[PROMPT_COLUMNS].to_markdown(index=False)

            with st.spinner(
                "Running 7 AI agents sequentially on real ICICI customer data — this usually takes 1-3 minutes..."
            ):
                try:
                    inputs = {
                        "num_customers": str(len(sample)),
                        "business_objective": business_objective,
                        "customer_data": customer_data_md,
                    }
                    crew_instance = AirtelNexusAiCustomerGrowthPlatformCrew().crew()
                    result = crew_instance.kickoff(inputs=inputs)
                    st.session_state.run_count += 1

                    with st.expander("📄 Real customer sample fed into the pipeline", expanded=False):
                        st.dataframe(sample)

                    st.success("Done! Here's what each agent produced:")

                    for i, task in enumerate(crew_instance.tasks, start=1):
                        agent_role = getattr(task.agent, "role", f"Agent {i}")
                        with st.expander(f"Step {i}: {agent_role}", expanded=False):
                            if task.output is not None:
                                st.markdown(str(task.output.raw))
                            else:
                                st.caption("No output captured for this step.")

                    st.divider()
                    st.subheader("📋 Final Executive Brief")
                    st.markdown(str(result))
                except Exception as e:
                    st.error(f"Something went wrong while running the crew: {e}")

st.divider()
st.caption(
    "Built with CrewAI · Customer data is real (ICICI Bank MBA case-study dataset, "
    "all names/account numbers synthetic) · Portfolio-scale projections are illustrative assumptions, clearly labeled in the output."
)
