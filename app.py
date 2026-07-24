import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# MAIN APP.PY — UPDATED MASTER HOME & NAVIGATION CENTER
# ============================================================

st.set_page_config(
    page_title="FirstChoice Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if "user_role" not in st.session_state:
    st.session_state["user_role"] = "guest"

if "user_name" not in st.session_state:
    st.session_state["user_name"] = "Guest User"


# ============================================================
# PREMIUM MULTINATIONAL UI
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


/* ============================================================
SIDEBAR
============================================================ */

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


/* ============================================================
BRAND
============================================================ */

.brand {

    padding: 42px;

    border-radius: 36px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 25px 70px
    rgba(37,99,235,0.25);

    margin-bottom: 30px;
}

.brand-title {

    font-size: 48px;

    font-weight: 900;

    line-height: 1.1;
}

.brand-subtitle {

    margin-top: 15px;

    font-size: 18px;

    line-height: 1.8;

    color:
    rgba(255,255,255,0.90);
}


/* ============================================================
SEARCH CARD
============================================================ */

.search-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 30px;
}


/* ============================================================
SECTION
============================================================ */

.section {

    margin-top: 30px;

    margin-bottom: 22px;

    padding: 28px 32px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 15px 40px
    rgba(37,99,235,0.18);
}

.section h2 {

    margin: 0;

    font-size: 29px;

    font-weight: 900;
}


/* ============================================================
FEATURE CARD
============================================================ */

.card {

    padding: 30px;

    min-height: 200px;

    border-radius: 28px;

    background: white;

    border:
    1px solid #E5E7EB;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    transition:
    transform 0.2s ease;
}

.card:hover {

    transform:
    translateY(-5px);
}


/* ============================================================
NAVIGATION CARD
============================================================ */

.nav-card {

    padding: 25px;

    min-height: 170px;

    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border:
    1px solid #E0E7FF;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    margin-bottom: 18px;
}


/* ============================================================
SMART CARD
============================================================ */

.smart-card {

    padding: 32px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #4C1D95,
        #7C3AED,
        #C026D3,
        #DB2777
    );

    box-shadow:
    0 20px 60px
    rgba(124,58,237,0.25);

    margin-bottom: 25px;
}


/* ============================================================
TRUST CARD
============================================================ */

.trust-card {

    padding: 28px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 18px 50px
    rgba(5,150,105,0.22);

}


/* ============================================================
FOOTER
============================================================ */

.footer {

    margin-top: 60px;

    padding: 45px;

    border-radius: 30px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B,
        #4C1D95
    );
}


/* ============================================================
BUTTON
============================================================ */

.stButton > button {

    border-radius: 14px;

    font-weight: 800;

    padding: 12px;

}


/* ============================================================
MOBILE
============================================================ */

@media (max-width: 768px) {

    .brand {
        padding: 28px;
    }

    .brand-title {
        font-size: 32px;
    }

    .section {
        padding: 22px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR — MASTER NAVIGATION
# ============================================================

with st.sidebar:

    st.markdown("""
    <h1>
    🏠 FirstChoice
    </h1>

    <h3>
    Property Hub
    </h3>

    <hr>
    """, unsafe_allow_html=True)


    # ========================================================
    # USER PROFILE
    # ========================================================

    st.markdown(
        f"""
        👤 **{st.session_state["user_name"]}**

        <br>

        🔐 Role:
        <b>{st.session_state["user_role"].upper()}</b>
        """,
        unsafe_allow_html=True
    )


    st.markdown("---")


    # ========================================================
    # QUICK NAVIGATION
    # ========================================================

    st.markdown(
        "### 🚀 Quick Navigation"
    )


    quick_page = st.selectbox(

        "Open Module",

        [

            "🏠 Home",

            "🔎 Property Search",

            "🏡 Buy Property",

            "🔑 Rent Property",

            "🏢 Commercial Property",

            "🌳 Land & Plot",

            "🚀 New Projects",

            "📈 Investment Planner",

            "📊 ROI & Rental Yield",

            "🏦 Loan & EMI Center",

            "⚖️ Property Comparison",

            "🤖 Investment Intelligence",

            "❤️ Investment Watchlist",

            "🛡️ Verified Properties",

            "👤 User Dashboard",

            "📢 Post Property",

            "💼 Partner / Agent Portal",

            "👑 Admin Master Control Center"

        ],

        key="main_quick_navigation"

    )


    if st.button(
        "🚀 OPEN SELECTED MODULE",
        use_container_width=True
    ):

        st.session_state["selected_module"] = quick_page

        st.success(
            f"Selected: {quick_page}"
        )


    st.markdown("---")


    # ========================================================
    # PROPERTY NAVIGATION
    # ========================================================

    st.markdown(
        "### 🏠 Property"
    )

    st.markdown("""
    • 🔎 Property Search

    • 🏡 Buy Property

    • 🔑 Rent Property

    • 🏢 Commercial

    • 🌳 Land & Plot

    • 🚀 New Projects

    • 📍 Location Search
    """)


    # ========================================================
    # INVESTMENT NAVIGATION
    # ========================================================

    st.markdown(
        "### 📈 Investment & Finance"
    )

    st.markdown("""
    • 📊 ROI Analyzer

    • 🏠 Rental Yield

    • 🔮 Future Value

    • 💰 Investment Planner

    • 🏦 Loan & EMI

    • ⚖️ Loan Comparison

    • 📊 Property Comparison

    • 🤖 Investment Intelligence
    """)


    # ========================================================
    # TRUST NAVIGATION
    # ========================================================

    st.markdown(
        "### 🛡️ Trust & Safety"
    )

    st.markdown("""
    • ✅ Verified Listings

    • 👤 Verified Owners

    • 🏢 Verified Builders

    • 🤝 Verified Agents

    • 🛡️ Property Verification

    • 🔐 Secure Enquiry
    """)


    # ========================================================
    # ACCOUNT NAVIGATION
    # ========================================================

    st.markdown(
        "### 👤 Account"
    )

    st.markdown("""
    • 👤 My Dashboard

    • ❤️ My Watchlist

    • 📢 My Properties

    • 📩 My Enquiries

    • 💳 Subscription

    • ⚙️ Account Settings
    """)


    # ========================================================
    # ADMIN ONLY
    # ========================================================

    if st.session_state["user_role"] == "admin":

        st.markdown("---")

        st.markdown(
            "### 👑 Admin Control"
        )

        st.markdown("""
        • 👥 User Management

        • 🏠 Property Approvals

        • 📢 Advertisement Control

        • 💳 Revenue Management

        • 👨‍💼 Manager & Staff

        • 📊 Company Reports

        • 🔐 Audit Logs

        • ⚙️ System Settings
        """)


# ============================================================
# MAIN HERO
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FirstChoice Property Hub
</div>

<div class="brand-subtitle">

India's Next-Generation Real Estate Marketplace

<br><br>

🏠 Buy
&nbsp; • &nbsp;
🔑 Rent
&nbsp; • &nbsp;
📢 Sell
&nbsp; • &nbsp;
📈 Invest
&nbsp; • &nbsp;
🏦 Finance
&nbsp; • &nbsp;
🤖 Compare

<br><br>

A complete digital property ecosystem for
Buyers, Owners, Agents, Builders and Investors.

</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# WELCOME STATUS
# ============================================================

if st.session_state.get("selected_module"):

    st.info(
        f"🚀 Selected Module: "
        f"{st.session_state['selected_module']}"
    )


# ============================================================
# SMART SEARCH
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔎 Find Your Perfect Property
</h2>

<p>
Search homes, plots, commercial spaces, new projects
and investment opportunities across India.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="search-card">',
    unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3)


with c1:

    looking_for = st.selectbox(

        "What are you looking for?",

        [

            "🏠 Buy",

            "🔑 Rent",

            "🏢 Commercial",

            "🌳 Land & Plot",

            "🚀 New Project",

            "📈 Investment"

        ]

    )


with c2:

    location = st.text_input(

        "📍 Location",

        placeholder=
        "City, Locality or PIN Code"

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


search_col1, search_col2 = st.columns([3, 1])


with search_col1:

    budget = st.select_slider(

        "💰 Approximate Budget",

        options=[

            "Any Budget",

            "Under ₹25 Lakh",

            "₹25–50 Lakh",

            "₹50 Lakh–₹1 Crore",

            "₹1–2 Crore",

            "₹2–5 Crore",

            "₹5 Crore+"

        ]

    )


with search_col2:

    st.write("")

    st.write("")

    search_clicked = st.button(

        "🔎 SEARCH PROPERTY",

        use_container_width=True

    )


if search_clicked:

    st.success(
        "✅ Property search request submitted."
    )

    st.info(
        f"Searching for {looking_for} "
        f"properties in {location or 'All Locations'} "
        f"under {budget}."
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# QUICK ACTION CENTER
# ============================================================

st.markdown("""
<div class="section">

<h2>
⚡ Quick Property Actions
</h2>

<p>
Start your property journey with one click.
</p>

</div>
""", unsafe_allow_html=True)


q1, q2, q3, q4 = st.columns(4)


with q1:

    st.markdown("""
    <div class="nav-card">

    <h2>🏠 Buy</h2>

    <p>
    Find your dream home,
    villa, apartment or plot.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "🔎 Explore Buy",
        use_container_width=True
    ):

        st.info(
            "Open Buy Property from the Pages menu."
        )


with q2:

    st.markdown("""
    <div class="nav-card">

    <h2>🔑 Rent</h2>

    <p>
    Find residential and
    commercial rental properties.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "🔎 Explore Rent",
        use_container_width=True
    ):

        st.info(
            "Open Rent Property from the Pages menu."
        )


with q3:

    st.markdown("""
    <div class="nav-card">

    <h2>📢 Sell</h2>

    <p>
    Upload property photos,
    videos and listing details.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "📢 Post Property",
        use_container_width=True
    ):

        st.info(
            "Open Post Property from the Pages menu."
        )


with q4:

    st.markdown("""
    <div class="nav-card">

    <h2>📈 Invest</h2>

    <p>
    Analyze ROI, rental yield,
    appreciation and finance.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "📊 Investment Center",
        use_container_width=True
    ):

        st.info(
            "Open Investment Planner / ROI & Finance Center."
        )


# ============================================================
# INVESTMENT & FINANCE CENTER
# ============================================================

st.markdown("""
<div class="section">

<h2>
📈 Smart Investment & Finance Center
</h2>

<p>
Analyze property returns, compare investment opportunities,
calculate EMI and evaluate loan offers.
</p>

</div>
""", unsafe_allow_html=True)


i1, i2, i3, i4 = st.columns(4)


with i1:

    st.markdown("""
    <div class="card">

    <h2>
    📊 ROI Analyzer
    </h2>

    <p>
    Calculate estimated ROI,
    capital gain and total return.
    </p>

    <p>
    📈 Investment Performance
    </p>

    </div>
    """, unsafe_allow_html=True)


with i2:

    st.markdown("""
    <div class="card">

    <h2>
    🏠 Rental Yield
    </h2>

    <p>
    Compare gross and net rental
    yield after vacancy and expenses.
    </p>

    <p>
    💰 Rental Income Analysis
    </p>

    </div>
    """, unsafe_allow_html=True)


with i3:

    st.markdown("""
    <div class="card">

    <h2>
    🏦 Loan Comparison
    </h2>

    <p>
    Compare multiple lenders,
    EMI, interest and total loan cost.
    </p>

    <p>
    💳 Smart Finance
    </p>

    </div>
    """, unsafe_allow_html=True)


with i4:

    st.markdown("""
    <div class="card">

    <h2>
    ⚖️ Property Comparison
    </h2>

    <p>
    Compare multiple properties based
    on price, ROI, rental yield and value.
    </p>

    <p>
    🤖 Decision Support
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SMART PROPERTY COMPARISON
# ============================================================

st.markdown("""
<div class="section">

<h2>
⚖️ Smart Property Comparison
</h2>

<p>
Compare properties before making a purchase decision.
</p>

</div>
""", unsafe_allow_html=True)


comp1, comp2, comp3 = st.columns(3)


with comp1:

    st.markdown("""
    <div class="card">

    <h2>
    🏠 Compare Price
    </h2>

    <p>
    Compare purchase price,
    location and property type.
    </p>

    </div>
    """, unsafe_allow_html=True)


with comp2:

    st.markdown("""
    <div class="card">

    <h2>
    📈 Compare Returns
    </h2>

    <p>
    Compare ROI, rental yield,
    appreciation and future value.
    </p>

    </div>
    """, unsafe_allow_html=True)


with comp3:

    st.markdown("""
    <div class="card">

    <h2>
    🏦 Compare Finance
    </h2>

    <p>
    Compare EMI affordability,
    loan cost and down payment.
    </p>

    </div>
    """, unsafe_allow_html=True)


if st.button(
    "⚖️ OPEN PROPERTY COMPARISON CENTER",
    use_container_width=True
):

    st.info(
        "Open the Property Comparison page from the Pages menu."
    )


# ============================================================
# TRUST ECOSYSTEM
# ============================================================

st.markdown("""
<div class="section">

<h2>
🛡️ FirstChoice Trust Ecosystem
</h2>

<p>
Our platform vision is designed around transparency,
verification and safer property discovery.
</p>

</div>
""", unsafe_allow_html=True)


t1, t2, t3, t4 = st.columns(4)


with t1:

    st.markdown("""
    <div class="trust-card">

    <h2>
    ✅ Verified Listings
    </h2>

    <p>
    Property listing verification
    and trust signals.
    </p>

    </div>
    """, unsafe_allow_html=True)


with t2:

    st.markdown("""
    <div class="trust-card">

    <h2>
    👤 Verified Owners
    </h2>

    <p>
    Owner identity and profile
    verification ecosystem.
    </p>

    </div>
    """, unsafe_allow_html=True)


with t3:

    st.markdown("""
    <div class="trust-card">

    <h2>
    🏢 Verified Builders
    </h2>

    <p>
    Builder and project verification
    for greater transparency.
    </p>

    </div>
    """, unsafe_allow_html=True)


with t4:

    st.markdown("""
    <div class="trust-card">

    <h2>
    🤝 Verified Agents
    </h2>

    <p>
    Agent profile and professional
    trust ecosystem.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SMART PLATFORM
# ============================================================

st.markdown("""
<div class="smart-card">

<h2>
🤖 FirstChoice Smart Property Ecosystem
</h2>

<p>
FirstChoice Property Hub is designed to connect the complete
real estate journey in one digital ecosystem.
</p>

<p>

🏠 Property Discovery
&nbsp; • &nbsp;

📍 Location Search
&nbsp; • &nbsp;

📸 Photos & Videos
&nbsp; • &nbsp;

🛡️ Verification
&nbsp; • &nbsp;

📈 Investment Analysis
&nbsp; • &nbsp;

🏦 Loan Comparison
&nbsp; • &nbsp;

⚖️ Property Comparison
&nbsp; • &nbsp;

❤️ Watchlist
&nbsp; • &nbsp;

📢 Property Listing
&nbsp; • &nbsp;

🤝 Partner Ecosystem

</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# WHY FIRSTCHOICE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🌟 Why FirstChoice Property Hub?
</h2>

<p>
We are building more than a property listing website.
We are building a complete digital property ecosystem.
</p>

</div>
""", unsafe_allow_html=True)


w1, w2, w3 = st.columns(3)


with w1:

    st.markdown("""
    <div class="card">

    <h2>
    🤖 Smart Technology
    </h2>

    <p>
    AI-powered recommendations,
    smart search, ROI analysis,
    loan comparison and property intelligence.
    </p>

    </div>
    """, unsafe_allow_html=True)


with w2:

    st.markdown("""
    <div class="card">

    <h2>
    🛡️ Trusted Ecosystem
    </h2>

    <p>
    Identity verification,
    property verification,
    trust signals and safer enquiries.
    </p>

    </div>
    """, unsafe_allow_html=True)


with w3:

    st.markdown("""
    <div class="card">

    <h2>
    🇮🇳 India-Wide Vision
    </h2>

    <p>
    Designed to scale from local property
    discovery to a nationwide real estate marketplace.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# USER JOURNEY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🧭 Complete Property Journey
</h2>

<p>
From property discovery to investment decision.
</p>

</div>
""", unsafe_allow_html=True)


j1, j2, j3, j4, j5 = st.columns(5)


with j1:

    st.markdown("""
    <div class="nav-card">

    <h2>1️⃣ Discover</h2>

    <p>
    Search property
    </p>

    </div>
    """, unsafe_allow_html=True)


with j2:

    st.markdown("""
    <div class="nav-card">

    <h2>2️⃣ Shortlist</h2>

    <p>
    Save to Watchlist
    </p>

    </div>
    """, unsafe_allow_html=True)


with j3:

    st.markdown("""
    <div class="nav-card">

    <h2>3️⃣ Compare</h2>

    <p>
    Compare properties
    </p>

    </div>
    """, unsafe_allow_html=True)


with j4:

    st.markdown("""
    <div class="nav-card">

    <h2>4️⃣ Analyze</h2>

    <p>
    ROI & Finance
    </p>

    </div>
    """, unsafe_allow_html=True)


with j5:

    st.markdown("""
    <div class="nav-card">

    <h2>5️⃣ Decide</h2>

    <p>
    Enquiry / Visit / Deal
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CALL TO ACTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Ready to Find Your Next Property?
</h2>

<p>
Use the sidebar Pages menu or Quick Navigation to explore
property search, investment planning, ROI analysis,
loan comparison and other FirstChoice Property Hub modules.
</p>

</div>
""", unsafe_allow_html=True)


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
Buy • Sell • Rent • Invest • Compare • Finance • Discover
</p>

<hr>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
