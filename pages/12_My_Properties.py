import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 12 - MY PROPERTIES / OWNER DASHBOARD
# ============================================================

st.set_page_config(
    page_title="My Properties | FirstChoice Property Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

/* BRAND */

.brand {
    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 22px 32px;

    border-radius: 24px;

    color: white;

    box-shadow:
    0 18px 50px
    rgba(37,99,235,0.22);
}

.brand-title {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 2px;
}

.brand-subtitle {
    font-size: 11px;
    letter-spacing: 4px;
    color: #FDE68A;
}

/* HERO */

.hero {
    margin-top: 28px;

    padding: 42px;

    border-radius: 32px;

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
}

.hero-title {
    font-size: 42px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 16px;
    color: rgba(255,255,255,0.88);
}

/* SECTION */

.section-header {
    margin-top: 35px;
    margin-bottom: 22px;

    padding: 22px 30px;

    border-radius: 22px;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    color: white;

    box-shadow:
    0 12px 35px
    rgba(37,99,235,0.18);
}

.section-title {
    font-size: 27px;
    font-weight: 900;
}

.section-subtitle {
    font-size: 13px;
    color: rgba(255,255,255,0.82);
}

/* STAT CARD */

.stat-card {
    padding: 25px;

    border-radius: 25px;

    background: white;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    min-height: 150px;
}

.stat-number {
    font-size: 34px;
    font-weight: 900;
    color: #4C1D95;
}

.stat-label {
    font-size: 14px;
    color: #64748B;
}

/* PROPERTY CARD */

.property-card {
    background: white;

    padding: 25px;

    border-radius: 28px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

.property-image {
    width: 100%;
    height: 230px;

    object-fit: cover;

    border-radius: 22px;
}

/* STATUS */

.status-active {
    color: #059669;
    font-weight: 800;
}

.status-pending {
    color: #D97706;
    font-weight: 800;
}

.status-draft {
    color: #64748B;
    font-weight: 800;
}

.status-sold {
    color: #2563EB;
    font-weight: 800;
}

/* PERFORMANCE */

.performance {
    padding: 35px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 22px 60px
    rgba(124,58,237,0.25);
}

/* CTA */

.cta {
    padding: 40px;

    border-radius: 30px;

    background:
    linear-gradient(
        135deg,
        #ECFDF5,
        #EFF6FF,
        #F5F3FF
    );

    border:
    1px solid #DDE7FF;
}

/* FOOTER */

.footer {
    margin-top: 60px;

    padding: 45px;

    border-radius: 28px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FIRSTCHOICE INFRA
</div>

<div class="brand-subtitle">
PROPERTY HUB • SMART REAL ESTATE MANAGEMENT
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
📊 My Properties Dashboard
</div>

<div class="hero-subtitle">
Manage your property listings, track performance,
respond to enquiries and grow your real estate business.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROFILE SUMMARY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👤 Welcome Back, Property Partner
</div>

<div class="section-subtitle">
Your personalised property management centre.
</div>

</div>
""", unsafe_allow_html=True)


profile1, profile2 = st.columns([2, 1])


with profile1:

    st.markdown("""
    <div class="stat-card">

    <h2>
    🏢 FirstChoice Property Partner
    </h2>

    <p>
    Account Type: Owner / Agent / Builder
    </p>

    <p>
    📱 Mobile: Verified
    </p>

    <p>
    🛡️ Identity Verification: Pending
    </p>

    </div>
    """, unsafe_allow_html=True)


with profile2:

    st.markdown("""
    <div class="stat-card">

    <h3>
    ⭐ Profile Strength
    </h3>

    <h1 style="color:#7C3AED;">
    75%
    </h1>

    <p>
    Complete your profile to build more trust.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# STATISTICS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📈 Listing Overview
</div>

<div class="section-subtitle">
Track your complete property portfolio.
</div>

</div>
""", unsafe_allow_html=True)


stats = [

    ("🏠", "Total Properties", "12"),

    ("🟢", "Active Listings", "7"),

    ("🟡", "Pending Verification", "2"),

    ("📝", "Draft Listings", "1"),

    ("🏷️", "Sold / Rented", "2"),

    ("👁️", "Total Views", "24,680")

]


stat_cols = st.columns(3)


for index, stat in enumerate(stats):

    with stat_cols[index % 3]:

        st.markdown(
            f"""
            <div class="stat-card">

            <div style="font-size:35px;">
            {stat[0]}
            </div>

            <div class="stat-number">
            {stat[2]}
            </div>

            <div class="stat-label">
            {stat[1]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    if index % 3 == 2:

        st.write("")


# ============================================================
# QUICK ACTIONS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⚡ Quick Actions
</div>

<div class="section-subtitle">
Manage your properties quickly.
</div>

</div>
""", unsafe_allow_html=True)


q1, q2, q3, q4 = st.columns(4)


with q1:

    if st.button(
        "➕ Add New Property",
        use_container_width=True
    ):

        st.success(
            "Opening property listing form."
        )


with q2:

    if st.button(
        "📊 View Analytics",
        use_container_width=True
    ):

        st.info(
            "Property analytics module will open."
        )


with q3:

    if st.button(
        "💬 View Enquiries",
        use_container_width=True
    ):

        st.info(
            "Your buyer enquiries will appear here."
        )


with q4:

    if st.button(
        "🚀 Promote Property",
        use_container_width=True
    ):

        st.info(
            "Premium promotion options will appear here."
        )


# ============================================================
# FILTER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Manage Your Listings
</div>

<div class="section-subtitle">
Filter and manage all your properties.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2 = st.columns(2)


with f1:

    status_filter = st.selectbox(
        "Filter by Status",
        [
            "All Properties",
            "Active",
            "Pending Verification",
            "Draft",
            "Sold",
            "Rented",
            "Rejected"
        ]
    )


with f2:

    search_property = st.text_input(
        "Search Property",
        placeholder="Search by property name or location"
    )


# ============================================================
# DEMO PROPERTY DATA
# ============================================================

properties = [

    {
        "name":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "price":
        "₹1.25 Crore",

        "status":
        "Active",

        "views":
        "8,420",

        "enquiries":
        "142",

        "image":
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=85"
    },

    {
        "name":
        "Luxury Independent Villa",

        "location":
        "Baner, Pune",

        "price":
        "₹2.80 Crore",

        "status":
        "Pending Verification",

        "views":
        "5,230",

        "enquiries":
        "76",

        "image":
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85"
    },

    {
        "name":
        "Premium Residential Plot",

        "location":
        "Wardha Road, Nagpur",

        "price":
        "₹48 Lakh",

        "status":
        "Draft",

        "views":
        "1,120",

        "enquiries":
        "18",

        "image":
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"
    }

]


# ============================================================
# PROPERTY LISTINGS
# ============================================================

for index, property_item in enumerate(properties):

    status = property_item["status"]

    if status_filter != "All Properties":

        if status != status_filter:

            continue


    st.markdown(
        f"""
        <div class="property-card">

        <div style="font-size:11px;
        color:#7C3AED;
        font-weight:800;">
        PROPERTY ID: FC-{10001 + index}
        </div>

        <h2>
        {property_item['name']}
        </h2>

        <p>
        📍 {property_item['location']}
        </p>

        <h2 style="color:#7C3AED;">
        {property_item['price']}
        </h2>

        <p>
        Status:
        <b>{property_item['status']}</b>
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    a1, a2, a3, a4 = st.columns(4)


    with a1:

        if st.button(
            "👁️ View",
            key=f"view_{index}",
            use_container_width=True
        ):

            st.info(
                f"Opening {property_item['name']}"
            )


    with a2:

        if st.button(
            "✏️ Edit",
            key=f"edit_{index}",
            use_container_width=True
        ):

            st.info(
                "Property editing module will open."
            )


    with a3:

        if st.button(
            "🚀 Boost",
            key=f"boost_{index}",
            use_container_width=True
        ):

            st.success(
                "Premium promotion options opened."
            )


    with a4:

        if st.button(
            "🗑️ Delete",
            key=f"delete_{index}",
            use_container_width=True
        ):

            st.warning(
                "Delete confirmation required."
            )


    st.write("")


# ============================================================
# PERFORMANCE ANALYTICS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📈 Property Performance
</div>

<div class="section-subtitle">
Understand how buyers interact with your listings.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="performance">

<h2>
🚀 Your Property Reach
</h2>

<p>
👁️ Total Property Views: 24,680
</p>

<p>
💬 Total Enquiries: 428
</p>

<p>
❤️ Total Saves: 1,240
</p>

<p>
📅 Site Visit Requests: 86
</p>

<p>
📈 Monthly Visibility Growth: +32%
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SMART RECOMMENDATIONS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 Smart Listing Recommendations
</div>

<div class="section-subtitle">
AI-powered suggestions to improve your property performance.
</div>

</div>
""", unsafe_allow_html=True)


r1, r2, r3 = st.columns(3)


with r1:

    st.info(
        """
        📸 **Add More Photos**

        Properties with high-quality
        photos generally attract more
        attention.
        """
    )


with r2:

    st.success(
        """
        🎥 **Add Property Video**

        A property video can help
        buyers understand the property
        before visiting.
        """
    )


with r3:

    st.warning(
        """
        🛡️ **Complete Verification**

        Verified listings can build
        greater buyer confidence.
        """
    )


# ============================================================
# PREMIUM CTA
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⭐ Grow Your Property Visibility
</div>

<div class="section-subtitle">
Reach more genuine buyers and investors.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="cta">

<h2>
🚀 Upgrade Your Listing
</h2>

<p>
Get better visibility with FirstChoice Premium.
</p>

<p>
⭐ Featured Placement
</p>

<p>
🔥 Top Search Position
</p>

<p>
📈 Advanced Analytics
</p>

<p>
🎯 Smart Buyer Matching
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "🚀 Explore Premium Promotion",
    use_container_width=True
):

    st.success(
        "Premium promotion module will open."
    )


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

<small>
© FirstChoice Infra Property Hub
</small>

</div>
""", unsafe_allow_html=True)
