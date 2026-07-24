import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# SINGLE APP.PY — MASTER NAVIGATION SYSTEM
# ============================================================

st.set_page_config(
    page_title="FirstChoice Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM GLOBAL UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F7F9FF 0%,
        #FFF7F3 35%,
        #F7F1FF 70%,
        #EFFCFF 100%
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


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #071952,
        #1E1B4B,
        #4C1D95
    );

}

[data-testid="stSidebar"] * {
    color: white !important;
}


/* =========================================================
SIDEBAR BRAND
========================================================= */

.sidebar-brand {

    padding: 22px;

    border-radius: 22px;

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    margin-bottom: 25px;

    text-align: center;

}

.sidebar-brand h2 {

    margin: 0;

    font-size: 24px;

    font-weight: 900;

}

.sidebar-brand p {

    margin-top: 8px;

    font-size: 13px;

}


/* =========================================================
HERO
========================================================= */

.hero {

    padding: 50px;

    border-radius: 36px;

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
    0 24px 75px
    rgba(37,99,235,0.30);

    margin-bottom: 30px;

}

.hero h1 {

    font-size: 46px;

    font-weight: 900;

}

.hero p {

    font-size: 18px;

    line-height: 1.8;

}


/* =========================================================
SECTION
========================================================= */

.section {

    margin-top: 30px;

    margin-bottom: 22px;

    padding: 28px 32px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4F46E5,
        #9333EA,
        #EC4899
    );

    box-shadow:
    0 14px 40px
    rgba(79,70,229,0.22);

}

.section h2 {

    margin: 0;

    font-size: 29px;

    font-weight: 900;

}


/* =========================================================
CARD
========================================================= */

.card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    border:
    1px solid #E0E7FF;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    margin-bottom: 20px;

}


/* =========================================================
BACK BUTTON AREA
========================================================= */

.back-area {

    margin-top: 60px;

    padding: 30px;

    border-radius: 28px;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #EFF6FF,
        #F5F3FF,
        #FDF2F8
    );

    border:
    1px solid #E0E7FF;

}


/* =========================================================
FOOTER
========================================================= */

.footer {

    margin-top: 60px;

    padding: 40px;

    border-radius: 30px;

    text-align: center;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B,
        #4C1D95
    );

}


/* =========================================================
BUTTONS
========================================================= */

.stButton > button {

    border-radius: 14px;

    font-weight: 800;

    min-height: 45px;

}


/* =========================================================
MOBILE
========================================================= */

@media (max-width: 768px) {

    .hero {

        padding: 30px;

    }

    .hero h1 {

        font-size: 32px;

    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PAGE LIST
# ============================================================

PAGES = {

    "🏠 Home": "home",

    "👑 Admin / Boss Control Center": "admin",

    "🏡 Property Search": "property_search",

    "📢 Property Listing": "property_listing",

    "🏠 Buy Property": "buy_property",

    "🔑 Rent Property": "rent_property",

    "🏢 Commercial Property": "commercial",

    "🌳 Land & Plot": "land_plot",

    "🏗️ New Projects": "new_projects",

    "📈 Investment & ROI Center": "investment",

    "🏦 Loan & EMI Center": "loan_emi",

    "🤖 Investment Intelligence": "investment_ai",

    "👤 User Management": "users",

    "👨‍💼 Partner / Agent Management": "partners",

    "👥 Downline & Team Management": "downline",

    "💰 Revenue & Subscription": "revenue",

    "📊 Reports & Analytics": "reports",

    "⚙️ System Settings": "settings"

}


# ============================================================
# SESSION STATE
# ============================================================

if "current_page" not in st.session_state:

    st.session_state.current_page = "home"


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">

    <h2>
    🏠 FirstChoice
    </h2>

    <p>
    Property Hub
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown(
        "### 📚 All Platform Pages"
    )


    page_names = list(PAGES.keys())


    selected_page_name = st.radio(

        "Navigate",

        page_names,

        index=page_names.index(
            next(
                name
                for name, value in PAGES.items()
                if value == st.session_state.current_page
            )
        ),

        label_visibility="collapsed"

    )


    selected_page = PAGES[
        selected_page_name
    ]


    if selected_page != st.session_state.current_page:

        st.session_state.current_page = selected_page

        st.rerun()


    st.divider()


    st.markdown("""
    ### 🚀 Quick Navigation

    सभी modules एक ही navigation system से
    connected हैं।

    किसी भी page पर जाएँ और नीचे
    **Back to Main Menu** button से वापस आएँ।
    """)


# ============================================================
# CURRENT PAGE
# ============================================================

current_page = st.session_state.current_page


# ============================================================
# HOME PAGE
# ============================================================

if current_page == "home":

    st.markdown("""
    <div class="hero">

    <h1>
    🏠 FirstChoice Property Hub
    </h1>

    <p>
    India's Next-Generation Real Estate Marketplace
    </p>

    <p>
    Buy • Sell • Rent • Invest • Discover
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="section">

    <h2>
    🔎 Find Your Perfect Property
    </h2>

    <p>
    Search homes, apartments, plots,
    commercial properties and investment opportunities.
    </p>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns(3)


    with c1:

        looking_for = st.selectbox(
            "What are you looking for?",
            [
                "🏠 Buy",
                "🔑 Rent",
                "🏢 Commercial",
                "🌳 Land & Plot",
                "📈 Investment"
            ]
        )


    with c2:

        location = st.text_input(
            "📍 Location",
            placeholder="City, Locality or PIN Code"
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
                "Warehouse"
            ]
        )


    if st.button(
        "🔎 SEARCH PROPERTY",
        use_container_width=True
    ):

        st.session_state.current_page = "property_search"

        st.rerun()


    st.markdown("""
    <div class="section">

    <h2>
    🚀 One Platform. Every Property Need.
    </h2>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.markdown("""
        <div class="card">

        <h2>🏠 Buy</h2>

        <p>
        Discover apartments, villas,
        houses and plots.
        </p>

        </div>
        """, unsafe_allow_html=True)


    with c2:

        st.markdown("""
        <div class="card">

        <h2>🔑 Rent</h2>

        <p>
        Find homes and commercial
        spaces for rent.
        </p>

        </div>
        """, unsafe_allow_html=True)


    with c3:

        st.markdown("""
        <div class="card">

        <h2>🚀 Sell</h2>

        <p>
        List properties with photos
        and videos.
        </p>

        </div>
        """, unsafe_allow_html=True)


    with c4:

        st.markdown("""
        <div class="card">

        <h2>🛡️ Trust</h2>

        <p>
        Verified properties and
        trusted ecosystem.
        </p>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# ADMIN PAGE
# ============================================================

elif current_page == "admin":

    st.markdown("""
    <div class="hero">

    <h1>
    👑 Admin / Boss Master Control Center
    </h1>

    <p>
    Complete control over users, properties,
    advertisements, subscriptions and company operations.
    </p>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "👥 Total Users",
            "12,480"
        )


    with c2:

        st.metric(
            "🏠 Properties",
            "3,245"
        )


    with c3:

        st.metric(
            "📢 Total Ads",
            "4,860"
        )


    with c4:

        st.metric(
            "⭐ Subscribers",
            "1,240"
        )


    st.markdown("""
    <div class="section">

    <h2>
    🚨 Pending Admin Actions
    </h2>

    </div>
    """, unsafe_allow_html=True)


    p1, p2, p3, p4 = st.columns(4)


    with p1:

        st.metric(
            "👤 User Requests",
            "27"
        )


    with p2:

        st.metric(
            "🏠 Property Approvals",
            "18"
        )


    with p3:

        st.metric(
            "📢 Ad Approvals",
            "35"
        )


    with p4:

        st.metric(
            "💳 Payment Reviews",
            "6"
        )


# ============================================================
# PROPERTY SEARCH PAGE
# ============================================================

elif current_page == "property_search":

    st.markdown("""
    <div class="hero">

    <h1>
    🔎 Property Search Center
    </h1>

    <p>
    Search and discover properties across India.
    </p>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns(3)


    with c1:

        st.text_input(
            "📍 Location"
        )


    with c2:

        st.selectbox(
            "🏡 Property Type",
            [
                "Any",
                "Apartment",
                "Villa",
                "House",
                "Plot",
                "Commercial"
            ]
        )


    with c3:

        st.selectbox(
            "💰 Purpose",
            [
                "Buy",
                "Rent",
                "Investment"
            ]
        )


    if st.button(
        "🔎 SEARCH",
        use_container_width=True
    ):

        st.success(
            "Search request submitted."
        )


# ============================================================
# PROPERTY LISTING
# ============================================================

elif current_page == "property_listing":

    st.markdown("""
    <div class="hero">

    <h1>
    📢 Property Listing Center
    </h1>

    <p>
    Create and manage premium property listings.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.text_input(
        "🏠 Property Name"
    )

    st.text_input(
        "📍 Location"
    )

    st.number_input(
        "💰 Price",
        min_value=0
    )

    st.text_area(
        "📝 Property Description"
    )


    if st.button(
        "📢 PUBLISH PROPERTY",
        use_container_width=True
    ):

        st.success(
            "Property listing submitted."
        )


# ============================================================
# BUY PROPERTY
# ============================================================

elif current_page == "buy_property":

    st.markdown("""
    <div class="hero">

    <h1>
    🏠 Buy Property
    </h1>

    <p>
    Explore properties available for purchase.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "🏠 Buy Property marketplace module."
    )


# ============================================================
# RENT PROPERTY
# ============================================================

elif current_page == "rent_property":

    st.markdown("""
    <div class="hero">

    <h1>
    🔑 Rent Property
    </h1>

    <p>
    Find residential and commercial rental properties.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "🔑 Rental Property marketplace module."
    )


# ============================================================
# COMMERCIAL
# ============================================================

elif current_page == "commercial":

    st.markdown("""
    <div class="hero">

    <h1>
    🏢 Commercial Property
    </h1>

    <p>
    Offices, shops, warehouses and commercial investments.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "🏢 Commercial Property module."
    )


# ============================================================
# LAND & PLOT
# ============================================================

elif current_page == "land_plot":

    st.markdown("""
    <div class="hero">

    <h1>
    🌳 Land & Plot
    </h1>

    <p>
    Discover residential plots, farm land and land investments.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "🌳 Land & Plot module."
    )


# ============================================================
# NEW PROJECTS
# ============================================================

elif current_page == "new_projects":

    st.markdown("""
    <div class="hero">

    <h1>
    🏗️ New Projects
    </h1>

    <p>
    Explore new and upcoming real estate projects.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "🏗️ New Projects module."
    )


# ============================================================
# INVESTMENT
# ============================================================

elif current_page == "investment":

    st.markdown("""
    <div class="hero">

    <h1>
    📈 Smart Property Investment & ROI Center
    </h1>

    <p>
    Analyze rental yield, ROI, capital appreciation
    and long-term investment potential.
    </p>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns(3)


    with c1:

        st.number_input(
            "🏷️ Property Price",
            min_value=0,
            value=5000000
        )


    with c2:

        st.number_input(
            "💵 Monthly Rent",
            min_value=0,
            value=25000
        )


    with c3:

        st.number_input(
            "📈 Annual Appreciation %",
            min_value=0.0,
            value=7.0
        )


    st.info(
        "📊 Full Page 28 Investment Planner can be connected here."
    )


# ============================================================
# LOAN EMI
# ============================================================

elif current_page == "loan_emi":

    st.markdown("""
    <div class="hero">

    <h1>
    🏦 Loan & EMI Comparison Center
    </h1>

    <p>
    Compare multiple lenders and calculate EMI
    for loan tenures up to 30 years.
    </p>

    </div>
    """, unsafe_allow_html=True)


    principal = st.number_input(
        "💰 Loan Amount",
        min_value=0,
        value=3500000
    )


    rate = st.number_input(
        "📊 Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=8.5
    )


    tenure = st.number_input(
        "📅 Loan Tenure (Years)",
        min_value=1,
        max_value=30,
        value=20
    )


    months = int(
        tenure * 12
    )


    monthly_rate = (
        rate / 12 / 100
    )


    if principal > 0:

        if monthly_rate == 0:

            emi = principal / months

        else:

            emi = (

                principal
                *
                monthly_rate
                *
                (1 + monthly_rate) ** months

                /

                (
                    (1 + monthly_rate) ** months
                    - 1
                )

            )


        total_payment = (
            emi * months
        )


        total_interest = (
            total_payment
            - principal
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "💳 Monthly EMI",
                f"₹{emi:,.0f}"
            )


        with c2:

            st.metric(
                "💸 Total Interest",
                f"₹{total_interest:,.0f}"
            )


        with c3:

            st.metric(
                "💰 Total Payment",
                f"₹{total_payment:,.0f}"
            )


# ============================================================
# INVESTMENT AI
# ============================================================

elif current_page == "investment_ai":

    st.markdown("""
    <div class="hero">

    <h1>
    🤖 Investment Intelligence
    </h1>

    <p>
    Smart investment insights and decision support.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "🤖 AI Investment Intelligence module."
    )


# ============================================================
# USERS
# ============================================================

elif current_page == "users":

    st.markdown("""
    <div class="hero">

    <h1>
    👤 User Management
    </h1>

    <p>
    Manage buyers, owners, agents, builders and users.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "👤 User Management module."
    )


# ============================================================
# PARTNERS
# ============================================================

elif current_page == "partners":

    st.markdown("""
    <div class="hero">

    <h1>
    👨‍💼 Partner / Agent Management
    </h1>

    <p>
    Manage agents, builders, partners and business profiles.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "👨‍💼 Partner Management module."
    )


# ============================================================
# DOWNLINE
# ============================================================

elif current_page == "downline":

    st.markdown("""
    <div class="hero">

    <h1>
    👥 Downline & Team Management
    </h1>

    <p>
    Manage managers, executives and team hierarchy.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "👥 Downline Management module."
    )


# ============================================================
# REVENUE
# ============================================================

elif current_page == "revenue":

    st.markdown("""
    <div class="hero">

    <h1>
    💰 Revenue & Subscription Center
    </h1>

    <p>
    Monitor subscription plans and company revenue.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.metric(
        "💰 Total Revenue",
        "₹24,85,600"
    )


# ============================================================
# REPORTS
# ============================================================

elif current_page == "reports":

    st.markdown("""
    <div class="hero">

    <h1>
    📊 Reports & Analytics
    </h1>

    <p>
    Business performance and platform analytics.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "📊 Reports & Analytics module."
    )


# ============================================================
# SETTINGS
# ============================================================

elif current_page == "settings":

    st.markdown("""
    <div class="hero">

    <h1>
    ⚙️ System Settings
    </h1>

    <p>
    Configure FirstChoice Property Hub.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.info(
        "⚙️ System Settings module."
    )


# ============================================================
# BACK TO MAIN MENU
# ============================================================

if current_page != "home":

    st.markdown("""
    <div class="back-area">

    <h2>
    🔙 Navigation
    </h2>

    <p>
    क्या आप वापस सभी pages वाले Main Menu पर जाना चाहते हैं?
    </p>

    </div>
    """, unsafe_allow_html=True)


    if st.button(
        "⬅️ BACK TO MAIN MENU",
        use_container_width=True
    ):

        st.session_state.current_page = "home"

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Discover
</p>

<hr>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
