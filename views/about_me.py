import streamlit as st
import requests
from forms.contact import contact_form

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")  # Two columns side by side

with col1:
    st.image("./assets/profile_image1.png", width=230)

with col2:
    st.title("Naveen Ashokkumar", anchor=False)
    st.write(
        "Automation Enthusiast | Software Engineering Analyst at Accenture | Full Stack Developer | Innovating Network Solutions & Operational Efficiency"
    )

    # Create another two columns within col2 to display buttons side by side
    button_col1, button_col2 = st.columns(2)  # Creates two columns in this specific section

    with button_col1:
        if st.button("✉️ Contact Me"):
            show_contact_form()

    with button_col2:
        # Add resume download button
        resume_url = "https://github.com/Nav0201/streamlit_multipage_app_demo/raw/main/views/nav_CV_2024.pdf"
        resume_file = requests.get(resume_url).content  # Fetch the file content
        
        st.download_button(
            label="My Resume 📥",
            data=resume_file,
            file_name="Naveen_CV_2024.pdf",
            mime="application/pdf"
        )




    
# --- ABOUT ME ---
st.write("\n")
st.subheader("About Me", anchor=False)
st.write(
    """
    I’m an ambitious engineer with strong product development and building expertise, coupled with analytical and interpersonal skills. Thriving to connect the gap between technical expertise and business outcomes, leveraging my skills to achieve impactful results.
    """
)

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
    - Bachelor's degree in Mechatronics Engineering from Hindustan Institute of Technology and Science (2018-2022)
    - Cumulative GPA: 7.90/10
    """
)

# # --- EDUCATION ---
# st.write("\n")
# st.subheader("Education", anchor=False)
# st.write(
#     """
    
#     """
# )

# --- AWARDS ---
st.write("\n")
st.subheader("Awards", anchor=False)
st.write(
    """
    - **2024**: Babel Fish Award, Best Associate at Accenture
    - **2022**: Best Innovation Project for UV Sterilization Box, Hindustan Institute
    - **2021**: Industry Innovation Grant, Robotic Manipulator for Skypoint Industries
    """
)

# --- PROJECTS ---
st.write("\n")
st.subheader("Projects & Research", anchor=False)
st.write(
    """
    - **Log Analysis Tool - LOGAN.V4 (2024)**: Built a Python and Django-based tool to automate log processing for network testers. Enabled efficient analysis, result visualization, and data downloads.
    - **Excel Automation Tools (2024)**: Created automation tools using PyQt and Tkinter, simplifying workflows for Excel data processing tasks.
    - **Bipolar Plates for Fuel Cells (2022)**: Designed and developed cost-effective bipolar plates for fuel cells in collaboration with Skypoint Industries.
    - **Robotic Manipulator (2021)**: Designed and developed a robotic manipulator for industrial applications.
    - **UV Sterilization Box (2020)**: Developed a UV Sterilization Box that eliminates bacteria from everyday objects.
    - **East West Combined Industries (Jan 2022 – May 2022)**: Researched and developed fuel cells and bipolar plates. 
      Collaborated with clients to understand requirements and delivered innovative, cost-effective solutions.
    - **Skypoint Industries (June 2021)**: Contributed to project planning and design for manufacturing centrifugal pumps, 
      ensuring efficient and high-quality production.
    - **CADD Center Training (Jan 2021 – Mar 2021)**: Achieved proficiency in CATIA, learning advanced skills such as part, 
      surface, and assembly design, kinematics, and rendering techniques.
    """
)

# # --- INTERNSHIPS ---
# st.write("\n")
# st.subheader("Internships", anchor=False)
# st.write(
#     """
    
#     """
# )

# --- SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - **Proficient**:
        - Python, Django, SQL, Java, HTML5, CSS3, Bootstrap 4/5
        - Tableau, Power BI, Alteryx, MySQL, PostgreSQL
        - Git, RESTful APIs, UI/UX (Wireframe & Prototyping)
    - **Experienced**:
        - Dassault Systèmes - CATIA, SolidWorks, Industrial IoT
        - Data Analysis, PyQt, Tkinter, MS Office Suite
        - Change Management Processes, Agile Development
    """
)

st.write("\n")
st.subheader("Project Management", anchor=False)
st.write(
    """
    - Business Requirement Analysis
    - Industry Analysis
    - Data Analytics Tools
    - Process Automation
    """
)

st.write("\n")
st.subheader("Certifications", anchor=False)
st.write(
    """
    - CATIA
    - Industrial IoT (L&T Edutech)
    - Marketing in the Digital World
    - Introduction to Psychology
    """
)



# # --- SOFT SKILLS ---
# st.write("\n")
# st.subheader("Soft Skills", anchor=False)
# st.write(
#     """
    
#     """
# )


