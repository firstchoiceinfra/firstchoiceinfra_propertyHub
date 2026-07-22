import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 7 - MY LISTINGS MANAGEMENT
# PREMIUM MULTINATIONAL REAL ESTATE DASHBOARD
# ============================================================

st.set_page_config(
    page_title="My Listings | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
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

    padding: 20px 32px;

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

/* PAGE HEADER */

.page-header {

    margin-top: 28px;

    padding: 38px 42px;

    border-radius: 30px;

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
    0 22px 60px
    rgba(124,58,237,0.25);

    position: relative;

    overflow: hidden;
}

.page-header::after {

    content: "";

    position: absolute;

    width: 280px;

    height: 280px;

    right: -90px;

    top: -140px;

    border-radius: 50%;

    background:
    rgba(255,255,255,0.13);
}

.page-title {

    font-size: 42px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.page-subtitle {

    font-size: 16px;

    color:
    rgba(255,255,255,0.86);

    position: relative;

    z-index: 2;
}

/* SECTION HEADER */

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

    position: relative;

    overflow: hidden;
}

.section-header::after {

    content: "";

    position: absolute;

    width: 150px;

    height: 150px;

    right: -50px;

    top: -75px;

    border-radius: 50%;

    background:
    rgba(255,255,255,0.12);
}

.section-title {

    font-size: 27px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.section-subtitle {

    font-size: 13px;

    color:
    rgba(255,255,255,0.82);

    position: relative;

    z-index: 2;
}

/* STAT CARDS */

.stat-card {

    padding: 25px;

    border-radius: 24px;

    color: white;

    min-height: 145px;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.10);
}

.blue {

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #06B6D4
    );
}

.green {

    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.purple {

    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

.orange {

    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

/* LISTING CARD */

.listing-card {

    background: white;

    border-radius: 28px;

    overflow: hidden;

    margin-bottom: 25px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);
}

.listing-image {

    width: 100%;

    height: 240px;

    object-fit: cover;
}

.listing-content {

    padding: 28px;
}

/* BADGE */

.badge {

    display: inline-block;

    padding: 7px 14px;

    border-radius: 30px;

    font-size: 12px;

    font-weight: 800;

    color: white;
}

.badge-green {

    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.badge-orange {

    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

.badge-purple {

    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

/* ANALYTICS */

.analytics-card {

    background: white;

    padding: 25px;

    border-radius: 24px;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.06);
}

/* PREMIUM */

.premium-card {

    padding: 35px;

    border-radius: 28px;

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
    0 20px 55px
    rgba(124,58,237,0.25);
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
PROPERTY HUB • INDIA'S SMART REAL ESTATE MARKETPLACE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown("""
<div class="page-header">

<div class="page-title">
🏡 My Property Listings
</div>

<div class="page-subtitle">
Manage, monitor and grow your property listings from one
powerful real estate dashboard.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# LISTING STATS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Listing Performance Overview
</div>

<div class="section-subtitle">
A quick view of your property marketplace performance.
</div>

</div>
""", unsafe_allow_html=True)

s1,s2,s3,s4 = st.columns(4)

stats = [
    ("🏡","Total Listings","6","blue"),
    ("🟢","Active Listings","4","green"),
    ("👁️","Total Views","12,845","purple"),
    ("💬","Total Enquiries","186","orange")
]

for col, item in zip(
    [s1,s2,s3,s4],
    stats
):

    with col:

        st.markdown(
            f"""
            <div class="stat-card {item[3]}">

            <div style="font-size:38px;">
            {item[0]}
            </div>

            <div style="font-size:15px;">
            {item[1]}
            </div>

            <div style="font-size:30px;font-weight:900;">
            {item[2]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
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
Search and filter properties to quickly manage your portfolio.
</div>

</div>
""", unsafe_allow_html=True)

f1,f2,f3 = st.columns(3)

with f1:

    search = st.text_input(
        "Search Property",
        placeholder="Search by property name..."
    )

with f2:

    status_filter = st.selectbox(
        "Listing Status",
        [
            "All",
            "Active",
            "Paused",
            "Sold",
            "Rented"
        ]
    )

with f3:

    property_filter = st.selectbox(
        "Property Type",
        [
            "All",
            "Apartment",
            "Villa",
            "Plot",
            "Commercial"
        ]
    )


# ============================================================
# PROPERTY DATA
# ============================================================

properties = [

    {
        "name":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "price":
        "₹1.25 Cr",

        "status":
        "Active",

        "views":
        "4,850",

        "enquiries":
        "72",

        "image":
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=85"
    },

    {
        "name":
        "Modern Independent Villa",

        "location":
        "Baner, Pune",

        "price":
        "₹2.80 Cr",

        "status":
        "Active",

        "views":
        "3,240",

        "enquiries":
        "51",

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
        "Active",

        "views":
        "2,190",

        "enquiries":
        "34",

        "image":
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"
    }
]


# ============================================================
# DISPLAY LISTINGS
# ============================================================

for index, property_item in enumerate(properties):

    if search:

        if search.lower() not in property_item["name"].lower():

            continue

    if status_filter != "All":

        if property_item["status"] != status_filter:

            continue

    st.markdown(
        f"""
        <div class="listing-card">

        <img
        class="listing-image"
        src="{property_item['image']}"
        >

        <div class="listing-content">

        <span class="badge badge-green">
        🟢 {property_item['status']}
        </span>

        <h2>
        {property_item['name']}
        </h2>

        <p>
        📍 {property_item['location']}
        </p>

        <h2 style="color:#7C3AED;">
        {property_item['price']}
        </h2>

        <hr>

        <b>
        👁️ {property_item['views']} Views
        </b>

        &nbsp;&nbsp;&nbsp;

        <b>
        💬 {property_item['enquiries']} Enquiries
        </b>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    a1,a2,a3,a4,a5 = st.columns(5)

    with a1:

        if st.button(
            "✏️ Edit",
            key=f"edit_{index}",
            use_container_width=True
        ):

            st.info(
                "Property editing module will open here."
            )

    with a2:

        if st.button(
            "📊 Analytics",
            key=f"analytics_{index}",
            use_container_width=True
        ):

            st.info(
                f"""
                Views: {property_item['views']}
                
                Enquiries: {property_item['enquiries']}
                """
            )

    with a3:

        if st.button(
            "⏸️ Pause",
            key=f"pause_{index}",
            use_container_width=True
        ):

            st.warning(
                "Listing paused."
            )

    with a4:

        if st.button(
            "⭐ Feature",
            key=f"feature_{index}",
            use_container_width=True
        ):

            st.success(
                "Featured listing option selected."
            )

    with a5:

        if st.button(
            "🗑️ Delete",
            key=f"delete_{index}",
            use_container_width=True
        ):

            st.error(
                "Delete confirmation required."
            )


# ============================================================
# PROPERTY STATUS MANAGEMENT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔄 Update Property Status
</div>

<div class="section-subtitle">
Keep your listing information accurate for buyers and tenants.
</div>

</div>
""", unsafe_allow_html=True)

u1,u2 = st.columns(2)

with u1:

    selected_property = st.selectbox(
        "Select Property",
        [
            "Premium 3 BHK Luxury Apartment",
            "Modern Independent Villa",
            "Premium Residential Plot"
        ]
    )

with u2:

    new_status = st.selectbox(
        "Change Status",
        [
            "Active",
            "Paused",
            "Sold",
            "Rented",
            "Under Negotiation"
        ]
    )

if st.button(
    "🔄 Update Property Status",
    use_container_width=True
):

    st.success(
        f"{selected_property} status updated to {new_status}."
    )


# ============================================================
# ANALYTICS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📈 Property Analytics
</div>

<div class="section-subtitle">
Understand how buyers interact with your listings.
</div>

</div>
""", unsafe_allow_html=True)

an1,an2,an3 = st.columns(3)

with an1:

    st.markdown(
        """
        <div class="analytics-card">

        <h3>
        👁️ Property Views
        </h3>

        <h1 style="color:#2563EB;">
        12,845
        </h1>

        <p>
        +18.5% compared with last month
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with an2:

    st.markdown(
        """
        <div class="analytics-card">

        <h3>
        ❤️ Saved Properties
        </h3>

        <h1 style="color:#EC4899;">
        642
        </h1>

        <p>
        Buyers who saved your properties
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with an3:

    st.markdown(
        """
        <div class="analytics-card">

        <h3>
        💬 Enquiries
        </h3>

        <h1 style="color:#7C3AED;">
        186
        </h1>

        <p>
        Potential buyers and tenants
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ENQUIRY MANAGEMENT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💬 Buyer & Tenant Enquiries
</div>

<div class="section-subtitle">
Manage conversations and respond to potential customers.
</div>

</div>
""", unsafe_allow_html=True)

enquiries = [
    "Rahul Sharma — Interested in 3 BHK Apartment",
    "Priya Verma — Requested Site Visit",
    "Amit Patel — Asked for Price Negotiation",
    "Sneha Joshi — Interested in Residential Plot"
]

selected_enquiry = st.selectbox(
    "Select Enquiry",
    enquiries
)

reply = st.text_area(
    "Your Reply",
    placeholder="Write your response..."
)

if st.button(
    "📤 Send Reply",
    use_container_width=True
):

    st.success(
        "Reply sent successfully."
    )


# ============================================================
# PREMIUM LISTING
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⭐ Grow Your Property Visibility
</div>

<div class="section-subtitle">
Give your best properties premium visibility.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="premium-card">

<h2>
🚀 FirstChoice Featured Properties
</h2>

<p>
Promote your property with premium placement,
featured badges and increased visibility.
</p>

<h3>
✨ Premium Visibility
</h3>

<p>
Your property can be promoted to relevant buyers
across the FirstChoice Property Hub marketplace.
</p>

</div>
""", unsafe_allow_html=True)

if st.button(
    "⭐ Explore Featured Listing Plans",
    use_container_width=True
):

    st.info(
        "Premium plans and payment gateway will be connected in the production version."
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
