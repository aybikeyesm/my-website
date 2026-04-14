import streamlit as st


st.set_page_config(
    page_title="Aybike Yesim Eskibozkurt | Personal Website",
    page_icon="A",
    layout="wide",
)


PROFILE = {
    "name": "Aybike Yesim Eskibozkurt",
    "title": "Physiotherapy Student | Researcher | Coder",
    "tagline": (
        "I work across science, research, writing, and technology with a strong interest "
        "in turning ideas into meaningful impact."
    ),
    "location": "Istanbul, Turkey",
    "email": "aybikeeskibozkurt@gmail.com",
    "photo": "/Users/aybikeeskibozkurt/Desktop/1773172040834-1.jpg",
    "banner": "/Users/aybikeeskibozkurt/Desktop/1772722679133.jpg",
    "bio": (
        "I am especially focused on biomaterials, and I work on developing bioresponsive "
        "hydrogel systems that aim to mimic the regenerative properties of synovial fluid. "
        "My goal is to transform scientific research into healthcare solutions that can be "
        "applied in real life.\n\n"
        "Throughout my academic journey, I have taken part in international projects, won "
        "awards in chemistry, and contributed to science communication.\n\n"
        "For me, science begins with asking the right questions, and I continue to follow "
        "those questions with curiosity and commitment."
    ),
}

PROJECTS = [
    {
        "name": "AI Study Companion",
        "summary": (
            "A smart learning assistant concept designed to help students summarize notes, "
            "generate quizzes, and stay motivated throughout their study journey."
        ),
        "stack": "Python, Streamlit, OpenAI API",
    },
    {
        "name": "Sustainability Tracker",
        "summary": (
            "An interactive dashboard concept for visualizing habits, environmental impact, "
            "and long-term progress in sustainable living."
        ),
        "stack": "Python, Pandas, Plotly",
    },
]

EXPERIENCE = [
    {
        "role": "Program Participant - Nestle Youth Academy",
        "org": "Nestle",
        "meta": "Seasonal | Mar 2026 - Present | Remote",
        "details": [
            "Selected to participate in the Nestle Youth Academy, a program focused on developing young talents through training, mentorship, and real-world insights.",
            "Gained knowledge in professional development, leadership, and industry dynamics.",
            "Participated in workshops, seminars, and interactive learning sessions.",
            "Engaged with professionals and peers from diverse backgrounds.",
            "Strengthened communication, teamwork, and problem-solving skills.",
        ],
    },
    {
        "role": "Blogger",
        "org": "Medium",
        "meta": "Seasonal | Sep 2023 - Present | Remote",
        "details": [
            "Published periodical articles on science, education, and personal development.",
            "Focused on presenting complex ideas in a clear and accessible way while maintaining analytical depth.",
            "Strengthened structured writing, critical thinking, and effective communication skills.",
            "Skill focus: Copywriting.",
        ],
    },
    {
        "role": "Freelance Translator",
        "org": "Coursera",
        "meta": "Part-time | Aug 2022 - Present | Remote",
        "details": [
            "Contributed to the translation and localization of educational course content for a global audience.",
            "Translated academic materials between Turkish and English with attention to accuracy, clarity, and terminology consistency.",
            "Strengthened academic language, cross-cultural communication, and collaborative digital workflow skills.",
            "Skill focus: English and foreign languages.",
        ],
    },
    {
        "role": "Program Participant - Kodluyoruz",
        "org": "Kodluyoruz",
        "meta": "Seasonal | Dec 2025 - Feb 2026 | Remote",
        "details": [
            "Selected for the AI4Change Program, focusing on the application of artificial intelligence for social impact.",
            "Gained foundational knowledge in artificial intelligence and real-world applications.",
            "Explored how technology can address social and environmental challenges.",
            "Participated in collaborative learning and project-based discussions.",
            "Developed problem-solving, analytical thinking, and interdisciplinary perspective.",
        ],
    },
    {
        "role": "Trainee",
        "org": "Yetkin Gencler",
        "meta": "Full-time | Aug 2023 - Sep 2025 | Hybrid",
        "details": [
            "Developed core competencies such as critical thinking, communication, teamwork, and effective use of office and digital productivity tools through an intensive skills-based training program.",
            "Skill focus: Microsoft Office Programs.",
        ],
    },
    {
        "role": "Teaching Assistant - Habitat Association",
        "org": "Habitat Dernegi",
        "meta": "Seasonal | Sep 2022 - 2024 | On-site",
        "details": [
            "Delivered Scratch programming workshops for children, contributing to early coding education and digital literacy development.",
            "Taught fundamental programming concepts such as algorithms, sequencing, and logical thinking.",
            "Designed interactive, project-based activities to foster creativity and engagement.",
            "Adapted teaching approaches for different age groups, strengthening communication skills.",
            "Encouraged active participation and supported an inclusive learning environment.",
        ],
    },
    {
        "role": "Musician",
        "org": "Kadikoy Belediyesi",
        "meta": "Part-time | Sep 2016 - Jun 2021 | On-site",
        "details": [
            "Performed as a volunteer flutist in the municipality's orchestra, participating in rehearsals and public performances.",
            "Contributed to ensemble coordination and cultural events aimed at promoting artistic engagement within the community.",
            "Strengthened discipline, teamwork, and performance skills.",
            "Skill focus: Flute.",
        ],
    },
    {
        "role": "Flutist - Orchestra Member",
        "org": "Kadikoy Belediyesi Cocuk Sanat Merkezi",
        "meta": "Sep 2016 - Jun 2021 | On-site",
        "details": [
            "Performed as a flutist in the Children's Art Center Orchestra through rehearsals and live performances.",
            "Contributed to ensemble performances by maintaining rhythm, coordination, and musical harmony.",
            "Developed discipline, consistency, and time management through regular rehearsals.",
            "Strengthened teamwork and communication skills within a group setting.",
            "Participated in public performances, gaining stage experience and confidence.",
        ],
    },
]

EDUCATION = [
    {
        "school": "Yeditepe University",
        "degree": "Bachelor's Degree, Physiotherapy and Rehabilitation",
        "date": "Aug 2025 - Jun 2029",
        "details": [
            "Biotechnology Society - Member",
            "Participated in biotechnology-focused academic events and seminars.",
            "Assisted with event logistics and communication during academic symposiums.",
            "Sanitas Health Club - Member",
            "Actively involved in health-related student initiatives and events.",
            "Contributed to the organization of conferences and seminars on healthcare and wellbeing.",
            "Supported event coordination and participant engagement during academic activities.",
        ],
    },
    {
        "school": "ISTEK Acibadem Schools",
        "degree": "High School, IB DP Programme (International Baccalaureate)",
        "date": "Sep 2021 - Jun 2024",
        "details": [
            "Wrote 'To What Extent Soil Type Affects CO2 Concentration, Temperature and pH in Mesocosm'.",
            "Participated in the Young Reporters for the Environment competition with the article 'TWEETING TROUBLE: CLIMATE CHANGE. ARE WE SILENCING OUR BIRDS?' and became world champion in the International Collaboration, Article, 15-18 Years category.",
            "Completed the IB DP Programme.",
            "Placed 4th in the Istanbul interschool archery competition for young women.",
            "Attended the Pera International Music Festival as a flutist.",
            "Skills: Biology, Chemistry, and interdisciplinary research.",
        ],
    },
]

PUBLICATIONS = [
    {
        "title": "TWEETING TROUBLE: CLIMATE CHANGE. ARE WE SILENCING OUR BIRDS?",
        "publisher": "Young Reporters For The Environment",
        "date": "May 31, 2023",
        "description": "Show publication",
    },
    {
        "title": "To What Extent Soil Type Affects CO2 Concentration, Temperature and pH",
        "publisher": "Robert College Science Symposium",
        "date": "Jun 10, 2022",
        "description": (
            "Due to global climate change and the demands of a growing population, land use "
            "and ecosystem sustainability have become increasingly important. This study "
            "used mesocosms, small artificial ecosystems where variables can be manipulated, "
            "to observe changes in CO2 concentration, pH, and temperature across two soil "
            "types: regular potting soil and succulent soil. Although differences were "
            "observed in CO2 concentration and pH, air and water temperatures remained "
            "similar in both mesocosms."
        ),
    },
]

COURSES = [
    "Bogazici University - Physics, Biology, Medicine, Machine Learning",
    "Duke University - Introduction to Chemistry: Reactions and Ratios",
    "EGG (Early Entrepreneur Development) Program",
    "GWC-Morgan Stanley JavaScript-p5.js",
    "Girls Who Code - Introduction to Data",
    "Sabanci University - Astrophysics and Exoplanets",
    "Sabanci University - Quantum Physics",
    "The School of The New York Times Summer Camp - Photojournalism As Art",
    "YetGen",
]

PLATFORMS = [
    ("GitHub", "https://github.com/aybikeyesm"),
    ("LinkedIn", "https://www.linkedin.com/in/aybikeyesimeskibozkurt"),
    ("Email", "mailto:aybikeeskibozkurt@gmail.com"),
]

VISION_POINTS = [
    "To build bridges between scientific research and practical healthcare applications.",
    "To develop biomaterial-based systems that can contribute to regenerative medicine.",
    "To keep combining research, communication, and technology in ways that create real social value.",
]

SKILLS = [
    "Copywriting",
    "English",
    "Photography",
    "Research Skills",
    "Microsoft Office Programs",
    "JavaScript",
    "Chemistry",
    "Biology",
    "Python",
]

VOLUNTEER = [
    {
        "role": "Volunteer Translator",
        "org": "Coursera",
        "meta": "Aug 2022 - Present | Education",
        "description": (
            "Contributed to the translation and localization of course materials to improve "
            "global accessibility for learners. Assisted in translating and editing "
            "educational content between Turkish and English, ensuring clarity, accuracy, "
            "and consistency. Gained experience in academic terminology, digital "
            "collaboration, and community-driven knowledge sharing."
        ),
    },
    {
        "role": "Yarini Kodlayanlar Project Volunteer Trainer",
        "org": "Habitat Dernegi",
        "meta": "Sep 2022 - 2024",
        "description": (
            "Contributed to digital inclusion by providing coding education to children "
            "through Scratch-based workshops. Supported equal access to technology and "
            "inspired young learners to explore creativity and problem-solving through coding."
        ),
    },
    {
        "role": "Blogger",
        "org": "Medium",
        "meta": "Sep 2023 - Present",
        "description": "I write on areas that interest me and publish them for everyone to see.",
    },
    {
        "role": "Local Community Initiative",
        "org": "Beth Israel Deaconess Medical Center",
        "meta": "Dec 2021 - Jan 2022 | Health",
        "description": (
            "Designed and distributed handmade postcards for long-term hospital patients "
            "to offer emotional support and encouragement. The project reached dozens of "
            "patients, bringing moments of joy and connection during treatment while "
            "strengthening empathy-driven communication."
        ),
    },
    {
        "role": "Event Volunteer",
        "org": "International Baccalaureate",
        "meta": "Dec 2023 | Education",
        "description": (
            "Supported participant guidance, booth assistance, and event organization during "
            "the International Baccalaureate Day event. Strengthened communication, teamwork, "
            "and event coordination skills."
        ),
    },
    {
        "role": "Event Volunteer",
        "org": "Yeditepe University",
        "meta": "Nov 2025 | Science and Technology",
        "description": (
            "Supported participant guidance during the Sci4Future event and contributed to "
            "the seamless execution of the program while gaining access to biotechnology-focused "
            "academic presentations and industry representatives."
        ),
    },
    {
        "role": "Volunteer Music Performer - Community Outreach Program",
        "org": "Kadikoy Belediyesi",
        "meta": "Jun 2019 | Veteran Support",
        "description": (
            "Performed flute pieces for Darulaceze Elderly Care Institution as part of "
            "community outreach activities. Engaged with elderly individuals and helped create "
            "a warm, uplifting social environment."
        ),
    },
    {
        "role": "Kadikoy Municipality Children's Art Center Flutist",
        "org": "Kadikoy Belediyesi",
        "meta": "Sep 2016 - Jun 2021 | Arts and Culture",
        "description": (
            "Performed as a volunteer flutist in the center's youth orchestra, supporting "
            "musical events, rehearsals, and cultural programs aimed at fostering artistic engagement."
        ),
    },
    {
        "role": "Event Volunteer",
        "org": "Yeditepe University",
        "meta": "Dec 2025 | Forensic Sciences",
        "description": (
            "Served as a volunteer at the 6th Forensic Sciences Congress, supporting session "
            "organization, participant coordination, and on-site logistics."
        ),
    },
    {
        "role": "Event Volunteer",
        "org": "Yeditepe University",
        "meta": "Dec 2025 | Health",
        "description": (
            "Served as a speaker helper during the Sports Health Congress, supporting "
            "communication and coordination between speakers and the organizing team while "
            "gaining practical exposure to physiotherapy-related topics."
        ),
    },
]

CERTIFICATES = [
    {
        "title": "Sabanci University Online Winter School Astrophysics and Extrasolar Planets Quantum Physics",
        "issuer": "Sabanci University",
        "date": "Issued Jan 2021",
        "description": "Sabanci University Online Winter School.",
    },
    {
        "title": "Mobile Photography Training",
        "issuer": "Habitat Dernegi",
        "date": "Issued Aug 2022",
        "description": "Credential ID 56729917140952",
    },
    {
        "title": "Women in Technology Online Training",
        "issuer": "Habitat Dernegi",
        "date": "Issued Aug 2022",
        "description": "Credential ID 48186649352597",
    },
    {
        "title": "Financial Literacy Training for Individuals",
        "issuer": "Habitat Dernegi",
        "date": "Issued Aug 2022",
        "description": "Credential ID 08051850904435",
    },
    {
        "title": "3rd Traditional Sports Health Symposium",
        "issuer": "Yeditepe Universitesi Saglik Kulubu Sanitas",
        "date": "Issued Dec 2025",
        "description": (
            "Supported the organization of the Sports Health Symposium as part of the "
            "conference staff team and assisted with session logistics, participant "
            "coordination, and speaker support."
        ),
    },
    {
        "title": "3rd SCI4Future Industry Summit",
        "issuer": "Yeditepe University Biotechnology Society",
        "date": "Issued Nov 2025",
        "description": (
            "Supported the organization of the Sci4Future Summit as a conference staff member "
            "and gained experience in scientific event organization."
        ),
    },
    {
        "title": "6th Forensic Sciences Congress",
        "issuer": "Yeditepe University Biotechnology Society",
        "date": "Issued Dec 2025",
        "description": (
            "Volunteered as conference staff, supported session coordination, participant "
            "guidance, and on-site event logistics."
        ),
    },
    {
        "title": "AI4Change Program 6th Term Participation Certificate",
        "issuer": "Kodluyoruz",
        "date": "Issued Mar 2026",
        "description": "Credential ID 97481064981018",
    },
    {
        "title": "Intro to Data Science",
        "issuer": "Girls Who Code",
        "date": "Issued Jul 2024",
        "description": "Credential ID 83a79daf-41de-4346-a2d3-459fcda1b7c2",
    },
    {
        "title": "Girls Who Code: Basic Neural Nets",
        "issuer": "Girls Who Code",
        "date": "Issued Jul 2024",
        "description": "Credential ID 77b0f670-d55e-45f5-a5da-cab92a767b8c",
    },
    {
        "title": "YetGen Trainee",
        "issuer": "Yetkin Gencler",
        "date": "Issued Jan 2024",
        "description": "YetGen",
    },
    {
        "title": "Girls Who Code: Morgan Stanley Summer Immersion Program",
        "issuer": "Girls Who Code",
        "date": "Issued Aug 2023",
        "description": "Credential ID 4e2dfdb2-449c-4a46-b3f2-f9b94f7b5262",
    },
    {
        "title": "Girls Who Code: Morgan Stanley p5.js",
        "issuer": "Girls Who Code",
        "date": "Issued Aug 2023",
        "description": "Credential ID e377a882-6f2f-4f54-be33-0a443c4f6481",
    },
    {
        "title": "Girls Who Code: Morgan Stanley Game Design",
        "issuer": "Girls Who Code",
        "date": "Issued Aug 2023",
        "description": "Credential ID 0d421638-2257-4a71-9188-7c901a28cf40 | Skills: JavaScript",
    },
    {
        "title": "Yarini Kodlayanlar Egitmen Egitimi",
        "issuer": "Habitat Dernegi",
        "date": "Issued Sep 2022",
        "description": "Credential ID 74692177895354",
    },
    {
        "title": "YetGen x Habitat Dernegi Kariyerin Icin Ilk Adim",
        "issuer": "Habitat Dernegi",
        "date": "Issued Sep 2022",
        "description": "Credential ID 72728422896635",
    },
    {
        "title": "Introduction to Chemistry: Reactions and Ratios",
        "issuer": "Duke University | Coursera",
        "date": "Issued Aug 2022",
        "description": "Skills: Chemistry",
    },
    {
        "title": "Photojournalism as Art",
        "issuer": "The School of the New York Times",
        "date": "Issued Aug 2022",
        "description": "Credential ID 56715521 | Skills: Photography",
    },
]


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Manrope:wght@400;500;700;800&display=swap');

        :root {
            --text: #1a1714;
            --muted: #665f58;
            --accent: #af5a3c;
            --card: rgba(255, 250, 244, 0.84);
            --line: rgba(26, 23, 20, 0.08);
            --shadow: 0 24px 60px rgba(88, 61, 43, 0.12);
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(193, 96, 56, 0.18), transparent 30%),
                radial-gradient(circle at top right, rgba(109, 153, 138, 0.14), transparent 26%),
                linear-gradient(180deg, #f9f2e8 0%, #f4ebdf 50%, #efe5da 100%);
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
            padding: 1.2rem 1.2rem 3rem 1.2rem;
            border-radius: 32px;
            background:
                linear-gradient(135deg, rgba(255, 250, 244, 0.92), rgba(246, 229, 211, 0.72)),
                linear-gradient(120deg, rgba(201,111,59,0.08), rgba(89,126,107,0.08));
            border: 1px solid rgba(27, 26, 23, 0.08);
            box-shadow: var(--shadow);
        }

        .hero-banner {
            overflow: hidden;
            border-radius: 26px;
            margin-bottom: 1.4rem;
            border: 1px solid var(--line);
            box-shadow: var(--shadow);
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 170px 1fr;
            gap: 1.4rem;
            align-items: center;
        }

        .avatar-shell {
            width: 170px;
            height: 170px;
            border-radius: 28px;
            background: linear-gradient(135deg, rgba(175,90,60,0.16), rgba(109,153,138,0.18));
            border: 1px solid var(--line);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .avatar-shell img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .avatar-fallback {
            font-family: "Space Grotesk", sans-serif;
            font-size: 3rem;
            font-weight: 700;
            color: var(--accent);
        }

        .eyebrow {
            display: inline-block;
            padding: 0.45rem 0.85rem;
            border-radius: 999px;
            background: rgba(175, 90, 60, 0.10);
            color: #7d3a23;
            font-size: 0.86rem;
            font-weight: 800;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .hero h1 {
            font-size: clamp(2.4rem, 7vw, 5rem);
            line-height: 0.95;
            margin: 1rem 0 0.7rem 0;
        }

        .hero p {
            font-size: 1.05rem;
            color: var(--muted);
            max-width: 760px;
            line-height: 1.8;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 1.8rem;
        }

        .section-card, .project-card, .timeline-card, .stat-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 24px;
            box-shadow: var(--shadow);
            backdrop-filter: blur(8px);
            padding: 1.25rem;
            height: 100%;
        }

        .stat-value {
            font-family: "Space Grotesk", sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
        }

        .stat-label, .small-muted {
            color: var(--muted);
        }

        .small-muted {
            font-size: 0.95rem;
            line-height: 1.75;
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

        .project-title {
            font-family: "Space Grotesk", sans-serif;
            font-size: 1.15rem;
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

        ul.clean-list {
            padding-left: 1.1rem;
            margin: 0.4rem 0 0 0;
        }

        ul.clean-list li {
            margin-bottom: 0.45rem;
            color: var(--muted);
            line-height: 1.6;
        }

        .footer-box {
            margin-top: 1.3rem;
            padding: 1.5rem;
            border-radius: 26px;
            background: linear-gradient(135deg, rgba(201,111,59,0.12), rgba(89,126,107,0.10));
            border: 1px solid var(--line);
        }

        @media (max-width: 900px) {
            .stat-grid {
                grid-template-columns: 1fr;
            }
            .hero-grid {
                grid-template-columns: 1fr;
            }
            .avatar-shell {
                width: 140px;
                height: 140px;
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


def render_bullet_list(items: list[str]) -> str:
    return "<ul class='clean-list'>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


inject_styles()

st.markdown(
    """
    <div class="nav-wrap">
        <a href="#hero">Hero</a>
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#experience">Experience</a>
        <a href="#education">Education</a>
        <a href="#publications">Publications</a>
        <a href="#courses">Courses</a>
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
st.markdown("<section class='hero'>", unsafe_allow_html=True)
if PROFILE["banner"]:
    st.markdown("<div class='hero-banner'>", unsafe_allow_html=True)
    st.image(PROFILE["banner"], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
hero_left, hero_right = st.columns([0.28, 0.72], vertical_alignment="center")
with hero_left:
    if PROFILE["photo"]:
        st.image(PROFILE["photo"], use_container_width=True)
    else:
        st.markdown(
            """
            <div class="avatar-shell">
                <div class="avatar-fallback">AY</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
with hero_right:
    st.markdown(
        f"""
        <span class="eyebrow">Personal Website</span>
        <h1>{PROFILE["name"]}</h1>
        <p><strong>{PROFILE["title"]}</strong></p>
        <p>{PROFILE["tagline"]}</p>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="stat-grid">
        <div class="stat-card">
            <div class="stat-value">Biomaterials</div>
            <div class="stat-label">Focused on regenerative and bioresponsive systems</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">Science + Code</div>
            <div class="stat-label">Blending research, communication, and digital tools</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">Global Outlook</div>
            <div class="stat-label">International projects, academic events, and interdisciplinary growth</div>
        </div>
    </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.write("")
section_header("about", "About Me", "A closer look at my scientific interests, motivation, and academic direction.")
st.markdown(
    f"""
    <div class="section-card">
        <p class="small-muted">{PROFILE["bio"].replace(chr(10), "<br><br>")}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
section_header("projects", "Projects", "Selected project directions that reflect my interests in technology and impact.")
project_cols = st.columns(2)
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
section_header("experience", "Experience", "Programs, writing, teaching, translation, and creative work that shaped my professional growth.")
for item in EXPERIENCE:
    st.markdown(
        f"""
        <div class="section-card" style="margin-bottom: 1rem;">
            <div class="project-title">{item["role"]}</div>
            <p class="small-muted"><strong>{item["org"]}</strong> | {item["meta"]}</p>
            {render_bullet_list(item["details"])}
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
section_header("education", "Education", "My academic background and student community involvement.")
edu_cols = st.columns(2)
for col, item in zip(edu_cols, EDUCATION):
    with col:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="project-title">{item["school"]}</div>
                <p class="small-muted"><strong>{item["degree"]}</strong><br>{item["date"]}</p>
                {render_bullet_list(item["details"])}
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("publications", "Publications", "Writing and research outputs that reflect my academic interests.")
for item in PUBLICATIONS:
    st.markdown(
        f"""
        <div class="section-card" style="margin-bottom: 1rem;">
            <div class="project-title">{item["title"]}</div>
            <p class="small-muted"><strong>{item["publisher"]}</strong> | {item["date"]}</p>
            <p class="small-muted">{item["description"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
section_header("courses", "Courses", "Additional learning experiences that expanded my interdisciplinary perspective.")
course_cols = st.columns(2)
for idx, course in enumerate(COURSES):
    with course_cols[idx % 2]:
        st.markdown(
            f"""
            <div class="section-card" style="margin-bottom: 1rem;">
                <p class="small-muted">{course}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("platforms", "Other Platforms", "Places where my work, writing, and professional profile can be found.")
platform_left, platform_right = st.columns([1, 1.2])
with platform_left:
    cards = "".join(
        f"<a class='platform-link' href='{url}' target='_blank'>{name}</a>"
        for name, url in PLATFORMS
    )
    st.markdown(f"<div class='section-card'>{cards}</div>", unsafe_allow_html=True)
with platform_right:
    st.markdown(
        """
        <div class="section-card">
            <p class="small-muted">
                These platforms connect my scientific interests, writing practice, coding work,
                and professional development in one visible digital identity.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
section_header("vision", "Vision", "The direction I want my work to take in science, health, and innovation.")
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
section_header("skills", "Skills", "A selection of technical, academic, and creative skills.")
skill_html = "".join(f"<div class='chip'>{skill}</div>" for skill in SKILLS)
st.markdown(f"<div class='section-card'>{skill_html}</div>", unsafe_allow_html=True)

st.write("")
section_header("volunteer", "Volunteering", "Community work and service experiences that matter to me.")
for item in VOLUNTEER:
    st.markdown(
        f"""
        <div class="section-card" style="margin-bottom: 1rem;">
            <div class="project-title">{item["role"]}</div>
            <p class="small-muted"><strong>{item["org"]}</strong> | {item["meta"]}</p>
            <p class="small-muted">{item["description"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
section_header("certificates", "Certificates", "Selected certificates, participation records, and training credentials.")
cert_cols = st.columns(2)
for index, cert in enumerate(CERTIFICATES):
    with cert_cols[index % 2]:
        st.markdown(
            f"""
            <div class="section-card" style="margin-bottom: 1rem;">
                <div class="project-title">{cert["title"]}</div>
                <p class="small-muted"><strong>{cert["issuer"]}</strong><br>{cert["date"]}</p>
                <p class="small-muted">{cert["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
section_header("contact", "Contact", "If you would like to collaborate, connect, or discuss research, I would be glad to hear from you.")
st.markdown(
    f"""
    <div class="footer-box">
        <div class="project-title">Let's connect.</div>
        <p class="small-muted">Location: {PROFILE["location"]}</p>
        <p class="small-muted">Email: {PROFILE["email"]}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
