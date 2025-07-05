import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access the API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")

def main():
    st.set_page_config(page_title="SQL QueryPilot", page_icon="🔮", layout="wide")

    # CSS styling
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/Bhanudahiyaa/SQL-QueryPilot/main/artistic-blurry-colorful-wallpaper-background.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    .main-container {
        max-width: 700px;
        margin: 0.2rem auto 1rem auto;
        padding: 0.5rem 2rem;
        border-radius: 20px;v
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.4rem;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 20px #667eea; }
        to { text-shadow: 0 0 30px #764ba2, 0 0 40px #764ba2; }
    }
    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
    }
    .custom-textarea textarea {
        background-color: #1e1e2f;
        color: #ffffff;
        border: 2px solid #667eea;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .custom-textarea textarea::placeholder {
        color: #a0aec0;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: left;
        color: #ffffff;
        backdrop-filter: blur(6px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem;
    }
    .feature-icon {
        font-size: 28px;
        margin-bottom: 0.8rem;
        display: block;
    }
    .feature-title {
        font-weight: 600;
        font-size: 1.2rem;
        margin-bottom: 0.4rem;
    }
    .feature-desc {
        font-size: 0.95rem;
        color: #c0c0c0;
    }
    .testimonial-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.2rem;
        color: #ffffff;
        backdrop-filter: blur(6px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .testimonial-quote {
        font-size: 1rem;
        font-style: italic;
        color: #c0c0c0;
        margin-bottom: 0.8rem;
    }
    .testimonial-name {
        font-weight: bold;
        color: #ffffff;
        font-size: 1.05rem;
    }
    .testimonial-title {
        font-size: 0.9rem;
        color: #a0aec0;
    }
    .github-btn {
        background: linear-gradient(to right, #000000, #434343, #764ba2);
        border: none;
        padding: 0.7rem 1.5rem;
        font-size: 16px;
        color: white;
        border-radius: 10px;
        margin-top: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .github-btn:hover {
        opacity: 0.85;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.markdown('<h1 class="main-title">🔮 SQL Whisperer</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Transform natural language into powerful SQL queries with AI magic</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    prompt = st.text_area("🔍 Enter your SQL-related question:")

    if "generate_clicked" not in st.session_state:
        st.session_state.generate_clicked = False

    if st.button("Generate SQL Query"):
        st.session_state.generate_clicked = True
         # Generate SQL
    if st.session_state.get("generate_clicked") and prompt.strip():
        with st.spinner("Generating query..."):
            try:
                template = f"""Create a SQL query snippet using the below text:\n'''\n{prompt}\n'''\nI just want a SQL Query."""
                response = model.generate_content(template)
                sql_query = response.text.strip().replace("```sql", "").replace("```", "").strip()

                expected_output = model.generate_content(
                    f"What would be the expected response of this SQL query snippet:\n{sql_query}\nProvide sample tabular response with no explanation:"
                ).text.strip()

                explanation = model.generate_content(
                    f"Explain the SQL query snippet:\n{sql_query}\nProvide a detailed explanation of the query."
                ).text.strip()

                st.markdown("---")
                st.success("✅ SQL Query generated successfully!")
                st.code(sql_query, language="sql")
                st.success("✅ Expected Output of this SQL Query:")
                st.markdown(expected_output)
                st.success("✅ Explanation of the SQL Query:")
                st.markdown(explanation)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    # Database logos
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Supports all SQL Databases</h2>", unsafe_allow_html=True)
    db_logos = [
        ("MySQL", "https://img.icons8.com/color/48/mysql-logo.png"),
        ("PostgreSQL", "https://img.icons8.com/color/48/postgreesql.png"),
        ("Microsoft SQL Server", "https://img.icons8.com/color/48/microsoft-sql-server.png"),
        ("Oracle", "https://img.icons8.com/color/48/oracle-logo.png"),
        ("SQLite", "https://img.icons8.com/ios-filled/50/000000/sql.png"),
        ("MariaDB", "https://img.icons8.com/color/48/mariadb.png"),
        ("IBM DB2", "https://img.icons8.com/color/48/ibm.png"),
        ("SAP HANA", "https://img.icons8.com/color/48/sap.png"),
        ("Redis", "https://img.icons8.com/color/48/redis.png"),
        ("Amazon RDS", "https://img.icons8.com/color/48/amazon-web-services.png"),
    ]
    cols = st.columns(5)
    for index, (name, url) in enumerate(db_logos):
        with cols[index % 5]:
            st.image(url, width=40)
            st.markdown(f"<p style='text-align: center; color: white;'>{name}</p>", unsafe_allow_html=True)
                # How It Works section (without Step 1)
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: white;'>📘 How It Works</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0aec0;'>Easy Steps to start SQL Query Generation with AI</p>", unsafe_allow_html=True)

    how_it_works = [
        ("Step 1 - Add Database Context", 
         "Although adding your database schema as context is optional, it enables AI to fine tune queries to your database's constraints and indexes."),
        ("Step 2 - Use AI assistance for Queries", 
         "AI assists with your requirements, whether generating new queries, explaining, or refactoring existing ones."),
        ("Step 3 - Collaborate and Automate", 
         "Utilize collaborative workspaces to efficiently share, review, and refine SQL queries. Set up custom AI-powered pipelines for your workflow.")
    ]

    for title, desc in how_it_works:
        st.markdown(f"""
        <div style='
            background-color: rgba(255,255,255,0.05); 
            padding: 1rem 1.5rem; 
            margin: 1rem auto; 
            border-radius: 10px; 
            color: white;
            max-width: 900px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.25);'>
            <h4 style='margin-bottom: 0.3rem;'>{title}</h4>
            <p style='color: #a0aec0; margin: 0;'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    # Features section
    st.markdown("<h2 style='text-align: center; margin-top: 2rem; color: white;'>⚡ Features</h2>", unsafe_allow_html=True)
    features = [
        ("🧠", "Generate tailored Queries", "Get SQL queries based on your DB & app, including joins, aggregations & data manipulation."),
        ("🧪", "Automated Query Testing", "Run AI-powered pipelines for auto SQL testing across different scenarios and datasets."),
        ("📘", "Explain SQL Queries", "Understand complex SQL with AI-generated explanations and query breakdowns."),
        ("🤝", "Collaborative Query Dev", "Refine SQL queries with team members for better accuracy and optimization.")
    ]
    cols = st.columns(2)
    for i, (icon, title, desc) in enumerate(features):
        with cols[i % 2]:
            st.markdown(f"""
            <div class='feature-card'>
                <span class='feature-icon'>{icon}</span>
                <div class='feature-title'>{title}</div>
                <div class='feature-desc'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # Testimonials section
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: white;'>💬 Testimonials</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0aec0;'>What our users say about SQL Whisperer</p>", unsafe_allow_html=True)
    testimonials = [
        ("Workik's SQL generator is a marvel! It turns complex data operations into a breeze. Our team's productivity has skyrocketed!", "Ava Harris", "Lead Data Engineer"),
        ("As someone who regularly deals with large datasets, SQL Whisperer's AI-driven assistance has simplified my workflow immensely.", "Elena Stanley", "Data Analyst"),
        ("From intricate joins to data manipulation, SQL Whisperer nails it every time. It's my go-to for efficient SQL development.", "Noah Taylor", "Backend Developer")
    ]
    cols = st.columns(3)
    for i, (quote, name, title) in enumerate(testimonials):
        with cols[i]:
            st.markdown(f"""
            <div class='testimonial-card'>
                <div class='testimonial-quote'>"{quote}"</div>
                <div class='testimonial-name'>{name}</div>
                <div class='testimonial-title'>{title}</div>
            </div>
            """, unsafe_allow_html=True)

    

    # GitHub Footer
    with st.container():
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; padding-bottom: 30px;">
            <h4 style="color: #ffffff;">🚀 Explore more projects on GitHub</h4>
            <a href="https://github.com/Bhanudahiyaa" target="_blank" style="text-decoration: none;">
                <button class="github-btn">
                    <img src="https://img.icons8.com/ios-filled/24/ffffff/github.png"
                         style="vertical-align: middle; margin-right: 8px;" />
                    Visit GitHub
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()