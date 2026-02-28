import streamlit as st

# Page Configuration
st.set_page_config(page_title="Helalur Rahman Swapon - Portfolio", page_icon="📍", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stHeader {
        color: #2e4053;
    }
    </style>
    """, unsafe_allow_stdio=True)

# Header Section
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Helalur Rahman Swapon")
    st.subheader("Urban and Regional Planner | GIS & Data Analyst")
    st.write("📍 Kuabashi, Kuabashi-6610, Foiljana, Chatmohor, Pabna, Bangladesh")
    st.write("📅 Date of Birth: 29 August 2002")

with col2:
    st.write(f"📞 **Phone:** +8801785242400")
    st.write(f"📧 **Email:** hrswapon00@gmail.com")
    st.write(f"🌐 [Portfolio](https://hrswapon.github.io/helalur-rahman-swapon/)")
    st.write(f"🔗 [LinkedIn](https://www.linkedin.com/in/helalur-rahman-swapon)")

st.divider()

# Career Objective
st.header("🎯 Career Objective")
st.write("""
A passionate and dedicated Urban and Regional Planning undergraduate with strong interests in GIS, remote sensing, and spatial data analysis. Proficient in Python programming, ArcGIS, and statistical tools, with hands-on experience in urban research, field surveys, and GIS-based mapping. Aspires to build a career as a GIS Spatial Analyst, applying data-driven approaches to solve real-world urban and environmental challenges.
""")

# Academic Credential
st.header("🎓 Academic Credential")
st.markdown("""
- **Rajshahi University of Engineering & Technology (RUET)** [March 2022 – July 2026]
    - Bachelor of Urban and Regional Planning (BURP), **CGPA: 3.40 / 4.00**
- **Rajuk Uttara Model College (RUMC)**
    - Higher Secondary Certificate (HSC) – Science | Passing Year: 2020, **GPA: 5.00 / 5.00**
- **Foiljana High School (FHS)**
    - Secondary School Certificate (SSC) – Science | Passing Year: 2018, **GPA: 5.00 / 5.00**
""")

# Work Experience
st.header("💼 Work Experience")

st.subheader("Internship – Sheltech Consultants (Pvt.) Ltd. Dhaka, Bangladesh")
st.caption("Feb 28, 2025 – Mar 25, 2025")
st.write("""
- Assisted in urban and infrastructure planning projects through research and GIS-based analysis
- Prepared technical reports and supported consultants in field surveys
- Gained practical exposure to master planning, consultancy workflows, and spatial data handling
- **Tools:** ArcGIS, KoboToolbox, MS Office, GIS Mapping
""")

st.subheader("Research Assistant (RA), Dhaka North City Corporation (DNCC)")
st.caption("Jun 2, 2024 – Sep 30, 2024")
st.write("""
- Designed and conducted surveys and questionnaires
- Collected, processed, and analyzed large-scale urban data
- Produced GIS maps and analytical outputs for research purposes
- **Tools:** ArcGIS, Excel, Stata
""")

st.subheader("Programme Management, “Planning Carnival 2022” – URP, RUET")
st.caption("Nov 20, 2022 – Nov 25, 2022")
st.write("- Assisted in organizing academic and technical events related to planning and GIS")

# Skills Summary
st.header("🛠 Skills Summary")
skills_data = {
    "Category": ["GIS & Remote Sensing", "Programming", "Data & Statistics", "Survey Tools", "Documentation", "Soft Skills"],
    "Skills": [
        "ArcGIS Desktop/Pro, QGIS, Google Earth Pro, ERDAS, ENVI, DroneDeploy, Pix4D",
        "Python, C, HTML",
        "Excel, SPSS, Stata, MySQL, MS SQL, PowerBI",
        "KoboToolbox, ArcMap, FieldSurvey",
        "MS Office, Google Suites, Canva, Mendeley, Jupyter Notebook",
        "Leadership, Adaptability, Time Management, Problem Solving"
    ]
}
st.table(skills_data)

# Certifications
st.header("📜 Certifications")
st.markdown("""
- **Drone-Based Geospatial Data Collection and Processing** (URP, RUET | GIS Club & Tiller)
- **Basic Programming with Python** (EDGE-RUET IICT)
- [Python Basics – University of Michigan](https://www.coursera.org/account/accomplishments/records/0VWQ421QIYW6)
- [Machine Learning with Python – IBM](https://www.coursera.org/account/accomplishments/verify/YPMEIAG9BZRK)
- [Data Analysis with Python – IBM](https://www.coursera.org/account/accomplishments/verify/LW2YEVVVDJYJ)
- [Deep Learning with Keras & TensorFlow – IBM](https://www.coursera.org/account/accomplishments/verify/6LHLVF2Q2A4W)
- [Introduction to Neural Networks & PyTorch – IBM](https://www.coursera.org/account/accomplishments/verify/WJHAM8Z04CUI)
- [Six Sigma and the Organization (Advanced) – Kennesaw State University](https://coursera.org/verify/I17HCWKL0H4N)
""")

# References
st.header("👥 References")
ref1, ref2 = st.columns(2)
with ref1:
    st.bold("Dr. MST Ilme Faridatul")
    st.write("Professor & Head, Dept of URP, RUET")
    st.write("📧 mifaridatul@urp.ruet.ac.bd")

with ref2:
    st.bold("Dr. Md. Abdul Wakil")
    st.write("Professor, Dept of URP, RUET")
    st.write("📧 mawakil@urp.ruet.ac.bd")