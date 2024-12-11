import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
# project_1_page = st.Page(
#     page="views/sales_dashboard.py",
#     title="Sales Dashboard",
#     icon=":material/bar_chart:",
# )
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_3_page = st.page(
    page="views/Web_Automation.py",
    title="Web Automation",
    icon=":tools:",  # Or choose any other service-related icon
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [ project_2_page],
        # "Projects": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/IMG_20211202_121623.jpg")
st.sidebar.markdown("Made with ❤️ by [Naveen](https://www.linkedin.com/in/naveen-a-9101001b6/)")


# --- RUN NAVIGATION ---
pg.run()
