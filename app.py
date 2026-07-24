import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# MAIN APPLICATION
# ============================================================

st.set_page_config(
    page_title="FirstChoice Infra Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GLOBAL PREMIUM UI
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
        linear-gradient(
            135deg,
            #F8FAFC 0%,
            #EFF6FF 35%,
            #F5F3FF 70%,
            #ECFEFF 100%
        );
    }

    header {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    [data-testid="stSidebar"] {
        background:
        linear-gradient(
            180deg,
            #020617,
            #172554,
            #312E81,
            #4C1D95
        );
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .hero {
        padding: 55px;
        border-radius: 35px;
        color: white;

        background:
        linear-gradient(
            135deg,
            #020617,
            #1D4ED8,
            #7C3AED,
            #DB2777
        );

        box-shadow:
        0 25px 70px
        rgba(37, 99, 235, 0.25);

        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 48px;
        font-weight: 900;
    }

    .hero p {
        font-size: 19px;
        line-height: 1.8;
    }

    .section {
        padding: 28px 35px;
        border-radius: 28px;
        color: white;

        background:
        linear-gradient(
            135deg,
            #1E3A8A,
            #4F46E5,
            #7C3AED,
            #EC4899
        );

        box-shadow:
        0 15px 45px
        rgba(79, 70, 229, 0.20);

        margin-top: 30px;
        margin-bottom: 25px;
    }

    .card {
        padding: 30px;
        border-radius: 25px;
        background: white;

        box-shadow:
        0 12px 35px
        rgba(0,0,0,0.07);

        min-height: 180px;
    }

    .footer {
        margin-top: 60px;
        padding: 40px;
        border-radius: 30px;
        color: white;
        text-align: center;

        background:
        linear-gradient(
            135deg,
            #020617,
            #1E1B4B,
            #4C1D95
        );
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:20px;">

        <h1>🏠 FirstChoice</h1>

        <h3>Infra Property Hub</h3>

        <p>
        India's Next-Generation
        Real Estate Ecosystem
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🚀 Explore")

    st.info(
        "Use the Pages menu to open "
        "any section of FirstChoice Property Hub."
    )

    st.markdown("### 🏠 Property")

    st.markdown(
        """
        • Buy Property  
        • Sell Property  
        • Rent Property  
        • Land & Plot  
        • Commercial  
        • New Projects  
        """
    )

    st.markdown("### 🛠️ Services")

    st.markdown(
        """
        • Architects  
        • Builders  
        • Contractors  
        • Plumbers  
        • Carpenters  
        • Building Material  
        """
    )

    st.divider()

    st.caption(
        "© FirstChoice Infra Property Hub"
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

    <h1>
    🏠 FirstChoice Infra Property Hub
    </h1>

    <p>
    India's Next-Generation
    Real Estate Marketplace
    </p>

    <p>
    Buy • Sell • Rent • Invest • Build • Discover
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SEARCH
# ============================================================

st.markdown(
    """
    <div class="section">

    <h2>
    🔎 Find Your Perfect Property
    </h2>

    <p>
    Search properties, projects, land,
    commercial spaces and local property services.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3)


with c1:

    purpose = st.selectbox(
        "🏠 What are you looking for?",
        [
            "Buy",
            "Rent",
            "Sell",
            "Commercial",
            "Land & Plot",
            "Investment"
        ]
    )


with c2:

    location = st.text_input(
        "📍 Location",
        placeholder="City, Town, Village or Area"
    )


with c3:

    property_type = st.selectbox(
        "🏡 Property Type",
        [
            "Any Property",
            "Apartment",
            "Flat",
            "Villa",
            "Independent House",
            "Plot",
            "Farm Land",
            "Office",
            "Shop",
            "Warehouse",
            "New Project"
        ]
    )


if st.button(
    "🔎 SEARCH PROPERTY",
    use_container_width=True
):

    st.success(
        f"Searching {purpose} properties "
        f"in {location or 'all locations'}."
    )


# ============================================================
# PLATFORM FEATURES
# ============================================================

st.markdown(
    """
    <div class="section">

    <h2>
    🚀 One Platform. Complete Property Ecosystem.
    </h2>

    <p>
    Property discovery से लेकर property services तक,
    FirstChoice एक complete ecosystem बनाने के लिए designed है.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


f1, f2, f3, f4 = st.columns(4)


features = [

    ("🏠", "Buy & Sell",
     "Homes, flats, villas, plots and land."),

    ("🔑", "Rent",
     "Residential and commercial rental properties."),

    ("🎥", "Photo & Video",
     "Property photos, videos and location visibility."),

    ("🛠️", "Home Services",
     "Architects, contractors and construction services.")
]


for col, feature in zip(
    [f1, f2, f3, f4],
    features
):

    with col:

        icon, title, description = feature

        st.markdown(
            f"""
            <div class="card">

            <h1>{icon}</h1>

            <h2>{title}</h2>

            <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    <h2>
    🏠 FIRSTCHOICE INFRA PROPERTY HUB
    </h2>

    <p>
    Buy • Sell • Rent • Invest • Build • Discover
    </p>

    <p>
    © FirstChoice Infra Property Hub
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
