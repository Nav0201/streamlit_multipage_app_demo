import streamlit as st
from forms.contact import contact_form

# --- CACHE RESUME FILE ---
@st.cache_data
def load_resume():
    try:
        with open("views/Naveen_Ashokkumar_CV_26_TS.pdf", "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None


# --- CONTACT FORM DIALOG ---
@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile_image1.png", width=230)

with col2:
    st.title("Naveen Ashokkumar", anchor=False)
    st.write("📧 naveensiva383@gmail.com")
    st.write("📞 +91-6379272850")

    st.write(
        """
        **Data & Analytics Engineer | Automation & Operations Lead | 
        Python • SQL • Power BI • Data Workflows • Analytics Platforms**
        """
    )

    button_col1, button_col2 = st.columns(2)

    # --- CONTACT BUTTON ---
    with button_col1:
        if st.button("✉️ Contact Me"):
            show_contact_form()

    # --- RESUME DOWNLOAD (FIXED) ---
    with button_col2:
        resume_file = load_resume()

        if resume_file:
            st.download_button(
                label="My Resume 📥",
                data=resume_file,
                file_name="Naveen_Ashokkumar_CV.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Resume file not found. Please check 'views/' folder.")


# --- CAREER SUMMARY ---
st.write("\n")
st.subheader("Career Summary", anchor=False)
st.write(
"""
Results-driven **Data & Analytics Engineer with 3 years of experience** designing and optimizing
production-grade **data workflows, ETL pipelines, and analytics platforms**.

Adept at leveraging **Python, SQL, Power BI, and automation frameworks** to enable
data-driven decision making and operational intelligence.

Passionate about **workflow automation, scalable data solutions, and data quality governance**, with
proven experience translating complex operational challenges into **high-impact analytics
and automation systems.**
"""
)


# --- WORK EXPERIENCE ---
st.write("\n")
st.subheader("Work Experience", anchor=False)

st.markdown("""
### **Data Analyst / Automation & Operations Lead — Accenture**
**Nov 2022 – Present**
""")

st.markdown("""
#### LOGAN – Network Log Analysis & Automation Platform
- Designed and built **LOGAN**, a Python & Django-based web application to automate network log analysis.
- Automated ingestion, parsing, and analysis of logs for OTT, HTTP, YouTube, Voice, and M2M services.
- Implemented success/failure detection logic with remediation insights.
- Enabled visualization, downloads, and structured troubleshooting workflows.
- Improved engineer productivity and troubleshooting accuracy.
""")

st.markdown("""
#### Automation & Analytics Enablement Program
- Built end-to-end automation accelerators across operations.
- Developed Python + Excel automation tools using PyQt and Tkinter.
- Designed QoS J+5 Automation & KPI Advancement Framework.
- Automated QoS decision workflows.
- Mentored team members on automation and analytics design.
""")

st.markdown("""
#### Bytel – Data Workflow & Power BI Platform
- Built automated pipelines from email ingestion to Python transformations.
- Created centralized trackers with deduplication and delivery logic.
- Integrated multiple data sources into scalable analytical models.
- Developed Power BI dashboards for KPI tracking and insights.
""")

st.markdown("""
#### Bytel – 5G Operations Analytics & Leadership
- Led analytics for large-scale 5G operations.
- Designed KPI frameworks for productivity and SLA tracking.
- Acted as SPOC between teams and leadership.
- Implemented reporting and governance dashboards.
""")

st.markdown("""
#### AI / Copilot Analytics Assistants
- Built rule-driven assistants for troubleshooting guidance.
- Embedded analytics into workflows.
- Enabled self-service analytics and faster onboarding.
""")


# --- TECHNICAL SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)

st.markdown("""
**Data & Programming**
- Python, SQL
- Excel & Google Sheets (Automation, Power Query)

**Analytics & BI**
- Power BI (DAX, Data Modeling, Dashboards)
- KPI Reporting, Trend Analysis

**Data Engineering & Automation**
- ETL Pipelines
- Data Consolidation
- API Integrations
- Log Analytics

**Tools & Platforms**
- Django, PyQt, Tkinter
- SharePoint
- Power BI Workspaces
""")


# --- EDUCATION ---
st.write("\n")
st.subheader("Education", anchor=False)

st.markdown("""
**B.Tech – Mechatronics Engineering**  
Hindustan Institute of Technology and Science, Chennai  
**2022 | CGPA: 7.9**

**Class XII**  
Chennai, Tamil Nadu  
**2018 | 82%**
""")


# --- AWARDS ---
st.write("\n")
st.subheader("Awards & Recognition", anchor=False)

st.markdown("""
**Accenture – Best Associate Award**  
Recognized for strong ownership and high performance.

**Accenture – Innovation Igniter Award**  
Recognized for driving impactful ideas and process improvements.
""")
