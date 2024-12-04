import streamlit as st

from forms.contact import contact_form



if st.button("Contact Me"):
def show_contact_form():
    # st.text_input("first name")
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image1.png", width=230)

with col2:
    st.title("Naveen Ashokkumar", anchor=False)
    st.write(
        "Automation Enthusiast | Software Engineering Analyst at Accenture | Full Stack Developer | Innovating Network Solutions & Operational Efficiency"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Analyst at Accenture with expertise in building web tools, automation, and services
    - Skilled in full-stack development, data visualization, and data analysis
    - Proficient in Python, Java, Business Requirement Analysis, Django
    - Extensive experience in data visualization using Tableau, Power BI, and MS Excel
    - Creative designer experienced in product, house, interior, and fashion design 
    - Strong interest in business, aiming to pursue an MBA to enhance knowledge and grow as a business analyst
    - Excellent under pressure, with strong task management and team collaboration skills
    """
)


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Django, Tkinter,, streamlit, Pandas), JavaScript, HTML, CSS, SQL
    - Data Visualization: PowerBi, Tableau, MS Excel, Matplotlib
    - Modeling: Data analysis, forecasting, and optimization
    - Tools: CATIA, SolidWorks, Power BI
    - Databases: PostgreSQL, MySQL
    """
)
