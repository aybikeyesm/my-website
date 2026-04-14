import streamlit as st


st.set_page_config(
    page_title="Aybike | Personal Website",
    page_icon="A",
    layout="wide",
)


PROFILE = {
    "name": "Aybike Eskibozkurt",
    "title": "Computer Engineering Student | Researcher | Builder",
    "tagline": "I design thoughtful digital experiences and turn curiosity into projects, research, and social impact.",
    "location": "Turkey",
    "email": "aybike@example.com",
    "phone": "+90 5xx xxx xx xx",
    "bio": (
        "I am a curious and disciplined learner who enjoys blending design, software, "
        "research, and community work. My focus is building meaningful products while "
        "growing as a developer and researcher."
    ),
}

PROJECTS = [
    {
        "name": "AI Study Companion",
        "summary": "A smart learning assistant that helps students summarize notes, generate quizzes, and stay motivated.",
        "stack": "Python, Streamlit, OpenAI API",
    },
    {
        "name": "Campus Event Hub",
        "summary": "A student-focused platform for discovering events, clubs, and networking opportunities in one place.",
        "stack": "Python, Flask, SQLite",
    },
    {
        "name": "Sustainability Tracker",
        "summary": "An interactive dashboard that visualizes habits, impact, and progress around sustainable living.",
        "stack": "Python, Pandas, Plotly",
    },
]

RESEARCH = [
    "Human-centered AI and ethical system design",
    "Educational technologies that improve student engagement",
    "Data-driven approaches for sustainable decision-making",
]

JOURNEY = [
    ("2022", "Started focusing seriously on software, design, and academic growth."),
    ("2023", "Built student projects, joined communities, and strengthened my Python foundation."),
    ("2024", "Became more active in research, teamwork, and real product thinking."),
    ("2025+", "Aiming to create impactful technology, publish meaningful work, and grow internationally."),
]

PLATFORMS = [
    ("GitHub", "https://github.com/yourusername"),
    ("LinkedIn", "https://www.linkedin.com/in/yourusername"),
    ("Email", "mailto:aybike@example.com"),
]

VISION_POINTS = [
    "Build technology that is elegant, useful, and socially meaningful.",
    "Contribute to research that improves how people learn and interact with digital systems.",
    "Keep growing into a developer who combines technical depth with empathy and creativity.",
]

SKILLS = {
    "Programming": ["Python", "SQL", "HTML", "CSS", "JavaScript"],
    "Tools": ["Git", "GitHub", "Streamlit", "Figma", "VS Code"],
    "Strengths": ["Research", "Problem Solving", "Presentation", "Teamwork", "Fast Learning"],
}

VOLUNTEER = [
    "Supported student communities through event organization and peer collaboration.",
    "Contributed to awareness and educational activities focused on social benefit.",
    "Helped peers with technical onboarding, presentations, and project planning.",
]

CERTIFICATES = [
    "Python Programming Certificate",
    "Introduction to Artificial Intelligence",
    "Research Methods and Academic Writing",
    "Web Development Fundamentals",
]


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Manrope:wght@400;500;700;800&display=swap');

        :root {
            --bg: #f6efe5;
            --bg-soft: #fffaf4;
            --text: #1b1a17;
            --muted: #5f5a52;
            --accent: #c96f3b;
            --accent-deep: #7e3f22;
            --card: rgba(255, 250, 244, 0.82);
            --line: rgba(27, 26, 23, 0.08);
            --shadow: 0 24px 60px rgba(88, 61, 43, 0.12);
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(201, 111, 59, 0.18), transparent 30%),
                radial-gradient(circle at top right, rgba(89, 126, 107, 0.14), transparent 28%),
                linear-gradient(180deg, #f9f1e7 0%, #f4ebdf 45%, #efe4d7 100%);
        }

        [data-testid="stHeader"] { background: transparent; }
        .block-container {
            padding-top: 1.4rem;
            padding-bottom: 4rem;
            max-width: 1180px;
        }

        html, body, [class*="css"] {
            font-family: "Manrope", sans-serif;
            color: var(--text);
        }

        h1, h2, h3 {
            font-family: "Space Grotesk", sans-serif !important;
            letter-spacing: -0.03em;
        }

        .nav-wrap {
            position: sticky;
            top: 0.6rem;
            z-index: 10;
            background: rgba(255, 250, 244, 0.72);
            backdrop-filter: blur(12px);
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: 0.8rem 1.1rem;
            margin-bottom: 1.2rem;
            box-shadow: var(--shadow);
        }

        .nav-wrap a {
            color: var(--muted);
            text-decoration: none;
            margin-right: 1rem;
            font-size: 0.92rem;
            font-weight: 700;
        }

        .hero {
            padding: 4rem 2rem;
            border-radius: 32px;
            background:
                linear-gradient(135deg, rgba(255, 250, 244, 0.92), rgba(246, 229, 211, 0.72)),
                linear-gradient(120deg, rgba(201,111,59,0.08), rgba(89,126,107,0.08));
            border: 1px solid rgba(27, 26, 23, 0.08);
            box-shadow: var(--shadow);
        }

        .eyebrow {
            display: inline-block;
            padding: 0.45rem 0.85rem;
            border-radius: 999px;
            background: rgba(201, 111, 59, 0.10);
            color: var(--accent-deep);
            font-size: 0.86rem;
            font-weight: 800;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .hero h1 {
            font-size: clamp(2.5rem, 7vw, 5.2rem);
            line-height: 0.95;
            margin: 1rem 0 0.8rem 0;
        }

        .hero p {
            font-size: 1.08rem;
            color: var(--muted);
            max-width: 700px;
            line-height: 1.8;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }

        .stat-card, .section-card, .timeline-card, .project-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 24px;
            box-shadow: var(--shadow);
            backdrop-filter: blur(8px);
        }

        .stat-card {
            padding: 1.1rem 1.2rem;
        }

        .stat-value {
            font-family: "Space Grotesk", sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
        }

        .stat-label {
            color: var(--muted);
            font-size: 0.92rem;
        }

        .section-title {
            font-size: 2rem;
            margin: 0 0 0.4rem 0;
        }

        .section-copy {
            color: var(--muted);
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        .section-card, .timeline-card, .project-card {
            padding: 1.35rem;
            height: 100%;
        }

        .project-title {
            font-family: "Space Grotesk", sans-serif;
            font-size: 1.2rem;
            margin-bottom: 0.35rem;
        }

        .chip {
            display: inline-block;
            padding: 0.42rem 0.7rem;
            margin: 0.25rem 0.35rem 0 0;
            border-radius: 999px;
            background: rgba(27, 26, 23, 0.05);
            border: 1px solid rgba(27, 26, 23, 0.08);
            color: var(--text);
            font-size: 0.88rem;
            font-weight: 700;
        }

        .platform-link {
            display: block;
            padding: 0.95rem 1rem;
            border-radius: 18px;
            background: rgba(255,255,255,0.46);
            border: 1px solid var(--line);
            text-decoration: none;
            color: var(--text) !important;
            font-weight: 700;
            margin-bottom: 0.8rem;
        }

        .small-muted {
            color: var(--muted);
            font-size: 0.94rem;
            line-height: 1.7;
        }

        .footer-box {
            margin-top: 1.5rem;
            padding: 1.5rem;
            border-radius: 26px;
            background: linear-gradient(135deg, rgba(201,111,59,0.12), rgba(89,126,107,0.10));
            border: 1px solid var(--line);
        }

        @media (max-width: 900px) {
            .stat-grid {
                grid-template-columns: 1fr;
            }
            .nav-wrap {
                border-radius: 24px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def section_header(anchor: str, title: str, subtitle: str) -> None:
    st.markdown(f"<div id='{anchor}'></div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='section-title'>{title}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='section-copy'>{subtitle}</p>", unsafe_allow_html=True)


inject_styles()

st.markdown(
    """
    <div class="nav-wrap">
        <a href="#hero">Hero</a>
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#research">Research</a>
        <a href="#journey">Journey</a>
        <a href="#platforms">Platforms</a>
        <a href="#vision">Vision</a>
        <a href="#skills">Skills</a>
        <a href="#volunteer">Volunteer</a>
        <a href="#certificates">Certificates</a>
        <a href="#contact">Contact</a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown(
    f"""
    <section class="hero">
        <span class="eyebrow">Personal Website</span>
        <h1>{PROFILE["name"]}</h1>
        <p><strong>{PROFILE["title"]}</strong></p>
        <p>{PROFILE["tagline"]}</p>
        <div class="stat-grid">
            <div class="stat-card">
                <div class="stat-value">3+</div>
                <div class="stat-label">Core focus areas: software, research, design</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">10+</div>
                <div class="stat-label">Skills and tools across product building</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">100%</div>
                <div class="stat-label">Motivation to keep learning and contributing</div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.write("")
section_header("about", "About Me", "A short introduction that gives visitors your personality, focus, and direction.")
left, right = st.columns([1.35, 1])
with left:
    st.markdown(
        f"""
        <div class="section-card">
            <p class="small-muted">{PROFILE["bio"]}</p>
            <p class="small-muted">
                I care about creating work that feels both intentional and useful. I enjoy
                exploring how code, design, and research can come together to solve real problems.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="section-card">
            <div class="chip">Creative</div>
            <div class="chip">Analytical</div>
            <div class="chip">Curious</div>
            <div class="chip">Collaborative</div>
            <div class="chip">Disciplined</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
section_header("projects", "Projects", "Selected works that show what you build and how you think.")
project_cols = st.columns(3)
for col, project in zip(project_cols, PROJECTS):
    with col:
        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-title">{project["name"]}</div>
                <p class="small-muted">{project["summary"]}</p>
                <div class="chip">{project["stack"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("research", "Research", "Topics I want to study more deeply and contribute to over time.")
research_cols = st.columns(3)
for col, item in zip(research_cols, RESEARCH):
    with col:
        st.markdown(
            f"""
            <div class="section-card">
                <p class="small-muted">{item}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("journey", "Journey", "A simple timeline of how my path is evolving.")
timeline_cols = st.columns(len(JOURNEY))
for col, (year, text) in zip(timeline_cols, JOURNEY):
    with col:
        st.markdown(
            f"""
            <div class="timeline-card">
                <div class="project-title">{year}</div>
                <p class="small-muted">{text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("platforms", "Other Platforms", "Places where my work, network, and updates can be followed.")
platform_left, platform_right = st.columns([1, 1.2])
with platform_left:
    cards = "".join(
        [
            f"<a class='platform-link' href='{url}' target='_blank'>{name}</a>"
            for name, url in PLATFORMS
        ]
    )
    st.markdown(f"<div class='section-card'>{cards}</div>", unsafe_allow_html=True)
with platform_right:
    st.markdown(
        """
        <div class="section-card">
            <p class="small-muted">
                This section can later be expanded with Behance, Medium, Kaggle, Google Scholar,
                or any other platform where you publish work and build your professional presence.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
section_header("vision", "Vision", "The kind of future I want to build through my work.")
vision_cols = st.columns(3)
for col, item in zip(vision_cols, VISION_POINTS):
    with col:
        st.markdown(
            f"""
            <div class="section-card">
                <p class="small-muted">{item}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("skills", "Skills", "Technical skills, tools, and strengths that support my journey.")
skill_cols = st.columns(3)
for col, (group, items) in zip(skill_cols, SKILLS.items()):
    chips = "".join([f"<div class='chip'>{item}</div>" for item in items])
    with col:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="project-title">{group}</div>
                {chips}
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("volunteer", "Volunteer", "Community-oriented experiences that matter to me.")
volunteer_cols = st.columns(3)
for col, item in zip(volunteer_cols, VOLUNTEER):
    with col:
        st.markdown(
            f"""
            <div class="section-card">
                <p class="small-muted">{item}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("certificates", "Certificates", "Courses and credentials that supported my development.")
cert_cols = st.columns(2)
for index, cert in enumerate(CERTIFICATES):
    with cert_cols[index % 2]:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="project-title">{cert}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("contact", "Contact", "If you want to collaborate, connect, or ask about my work, reach out.")
st.markdown(
    f"""
    <div class="footer-box">
        <div class="project-title">Let's build something meaningful.</div>
        <p class="small-muted">Location: {PROFILE["location"]}</p>
        <p class="small-muted">Email: {PROFILE["email"]}</p>
        <p class="small-muted">Phone: {PROFILE["phone"]}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
