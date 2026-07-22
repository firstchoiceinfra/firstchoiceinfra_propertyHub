import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 21 - SMART SAVED PROPERTIES & WISHLIST
# ============================================================

st.set_page_config(
    page_title="My Wishlist | FirstChoice Property Hub",
    page_icon="❤️",
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

    padding: 48px;

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

    color:
    rgba(255,255,255,0.88);
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

    color:
    rgba(255,255,255,0.82);
}

/* PROPERTY CARD */

.property-card {

    padding: 30px;

    border-radius: 30px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    margin-bottom: 20px;
}

/* AI CARD */

.ai-card {

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

/* PRICE CARD */

.price-card {

    padding: 30px;

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
    0 18px 45px
    rgba(5,150,105,0.22);
}

/* COMPARE */

.compare-card {

    padding: 30px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F8FAFF,
        #FDF4FF
    );

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);
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
PROPERTY HUB • SMART WISHLIST • COMPARE • DECIDE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
❤️ My Smart Property Wishlist
</div>

<div class="hero-subtitle">
Save, compare, track prices and discover the best property
for your needs with intelligent property insights.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# WISHLIST OVERVIEW
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Wishlist Overview
</div>

<div class="section-subtitle">
Your complete property shortlist at a glance.
</div>

</div>
""", unsafe_allow_html=True)


w1, w2, w3, w4, w5 = st.columns(5)


with w1:

    st.metric(
        "❤️ Saved",
        "18"
    )


with w2:

    st.metric(
        "⚖️ Compare",
        "4"
    )


with w3:

    st.metric(
        "💰 Price Drops",
        "3"
    )


with w4:

    st.metric(
        "🛡️ Verified",
        "11"
    )


with w5:

    st.metric(
        "📅 Site Visits",
        "5"
    )


# ============================================================
# FILTER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Manage Saved Properties
</div>

<div class="section-subtitle">
Find the right property from your personal shortlist.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    search = st.text_input(
        "Search Saved Property",
        placeholder=
        "Search by name or location"
    )


with f2:

    property_filter = st.selectbox(
        "Property Type",
        [
            "All",
            "Apartment",
            "Villa",
            "Plot",
            "Independent House",
            "Commercial"
        ]
    )


with f3:

    sort_by = st.selectbox(
        "Sort By",
        [
            "Recently Saved",
            "Highest Match Score",
            "Lowest Price",
            "Price Drop",
            "Most Verified"
        ]
    )


# ============================================================
# SMART AI RECOMMENDATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 AI Property Decision Assistant
</div>

<div class="section-subtitle">
Intelligent insights based on your saved properties.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
🧠 Your Best Match Today
</h2>

<h1>
🏆 Premium 3 BHK Luxury Apartment
</h1>

<p>
📍 Civil Lines, Nagpur
</p>

<p>
🎯 AI Match Score: <b>94%</b>
</p>

<p>
💰 Excellent price-to-location ratio
</p>

<p>
🛡️ High property verification score
</p>

<p>
📈 Strong match with your saved preferences
</p>

<p>
💡 Recommendation: Schedule a site visit
before making your final decision.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "📅 SCHEDULE SITE VISIT",
    use_container_width=True
):

    st.success(
        "Site visit request initiated."
    )


# ============================================================
# SAVED PROPERTIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
❤️ Your Saved Properties
</div>

<div class="section-subtitle">
Review and manage your shortlisted properties.
</div>

</div>
""", unsafe_allow_html=True)


properties = [

    {
        "name":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "price":
        "₹1.25 Crore",

        "old_price":
        "₹1.35 Crore",

        "match":
        94,

        "verification":
        "98%",

        "type":
        "Apartment",

        "status":
        "💰 Price Reduced"
    },

    {
        "name":
        "Luxury Independent Villa",

        "location":
        "Baner, Pune",

        "price":
        "₹2.40 Crore",

        "old_price":
        "₹2.40 Crore",

        "match":
        88,

        "verification":
        "92%",

        "type":
        "Villa",

        "status":
        "🛡️ Verified"
    },

    {
        "name":
        "Premium Residential Plot",

        "location":
        "Wardha Road, Nagpur",

        "price":
        "₹65 Lakh",

        "old_price":
        "₹70 Lakh",

        "match":
        91,

        "verification":
        "95%",

        "type":
        "Plot",

        "status":
        "💰 Price Reduced"
    }

]


for index, property_data in enumerate(properties):

    st.markdown(
        f"""
        <div class="property-card">

        <h2>
        🏠 {property_data["name"]}
        </h2>

        <p>
        📍 {property_data["location"]}
        </p>

        <h2>
        💰 {property_data["price"]}
        </h2>

        <p>
        Previous Price:
        <s>{property_data["old_price"]}</s>
        </p>

        <p>
        🎯 AI Match Score:
        <b>{property_data["match"]}%</b>
        </p>

        <p>
        🛡️ Verification:
        <b>{property_data["verification"]}</b>
        </p>

        <p>
        {property_data["status"]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    b1, b2, b3, b4, b5 = st.columns(5)


    with b1:

        if st.button(
            "👁️ View",
            key=f"view_{index}",
            use_container_width=True
        ):

            st.info(
                "Property details page selected."
            )


    with b2:

        if st.button(
            "⚖️ Compare",
            key=f"compare_{index}",
            use_container_width=True
        ):

            st.success(
                "Property added to comparison."
            )


    with b3:

        if st.button(
            "📅 Visit",
            key=f"visit_{index}",
            use_container_width=True
        ):

            st.info(
                "Site visit booking opened."
            )


    with b4:

        if st.button(
            "🔔 Price Alert",
            key=f"alert_{index}",
            use_container_width=True
        ):

            st.success(
                "Price alert activated."
            )


    with b5:

        if st.button(
            "❤️ Remove",
            key=f"remove_{index}",
            use_container_width=True
        ):

            st.warning(
                "Property removed from wishlist."
            )


# ============================================================
# PRICE DROP TRACKER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💰 Smart Price Drop Tracker
</div>

<div class="section-subtitle">
Track price movements of properties you are watching.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="price-card">

<h2>
📉 Price Drop Detected
</h2>

<h1>
Premium 3 BHK Luxury Apartment
</h1>

<p>
📍 Civil Lines, Nagpur
</p>

<p>
Previous Price:
<s>₹1.35 Crore</s>
</p>

<p>
New Price:
<b>₹1.25 Crore</b>
</p>

<p>
🔥 You could save ₹10 Lakh
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "🔔 KEEP TRACKING PRICE",
    use_container_width=True
):

    st.success(
        "Price tracking activated."
    )


# ============================================================
# PROPERTY COMPARISON
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⚖️ Smart Property Comparison
</div>

<div class="section-subtitle">
Compare your shortlisted properties before making a decision.
</div>

</div>
""", unsafe_allow_html=True)


compare_property = st.multiselect(
    "Select Properties to Compare",
    [
        "Premium 3 BHK Luxury Apartment",
        "Luxury Independent Villa",
        "Premium Residential Plot",
        "FirstChoice Premium Township"
    ],
    default=[
        "Premium 3 BHK Luxury Apartment",
        "Premium Residential Plot"
    ]
)


if len(compare_property) >= 2:

    st.markdown(
        """
        <div class="compare-card">

        <h2>
        ⚖️ Comparison Dashboard
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    comparison_data = {

        "Feature": [
            "Price",
            "AI Match",
            "Verification",
            "Location",
            "Property Type",
            "Price Trend"
        ],

        "Premium 3 BHK Luxury Apartment": [
            "₹1.25 Cr",
            "94%",
            "98%",
            "Civil Lines, Nagpur",
            "Apartment",
            "📉 Reduced"
        ],

        "Premium Residential Plot": [
            "₹65 Lakh",
            "91%",
            "95%",
            "Wardha Road, Nagpur",
            "Plot",
            "📉 Reduced"
        ]

    }


    st.table(
        comparison_data
    )


# ============================================================
# PROPERTY SCORE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🎯 Property Decision Score
</div>

<div class="section-subtitle">
Understand why a property may be suitable for you.
</div>

</div>
""", unsafe_allow_html=True)


score1, score2, score3, score4 = st.columns(4)


with score1:

    st.metric(
        "📍 Location",
        "92 / 100"
    )


with score2:

    st.metric(
        "💰 Value",
        "89 / 100"
    )


with score3:

    st.metric(
        "🛡️ Trust",
        "96 / 100"
    )


with score4:

    st.metric(
        "🎯 Overall",
        "94 / 100"
    )


# ============================================================
# SAVED SEARCH
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔔 Saved Search Alerts
</div>

<div class="section-subtitle">
Get notified automatically when matching properties are listed.
</div>

</div>
""", unsafe_allow_html=True)


saved_search = st.text_input(
    "Saved Search Name",
    placeholder=
    "Example: 3 BHK Under ₹1.5 Cr in Nagpur"
)


alert_frequency = st.selectbox(
    "Alert Frequency",
    [
        "Instant",
        "Daily",
        "Weekly"
    ]
)


if st.button(
    "🔔 CREATE SAVED SEARCH",
    use_container_width=True
):

    if saved_search:

        st.success(
            f"Saved search '{saved_search}' created."
        )

    else:

        st.warning(
            "Please enter a saved search name."
        )


# ============================================================
# SMART INSIGHTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🧠 Smart Wishlist Insights
</div>

<div class="section-subtitle">
Personalized intelligence from your saved properties.
</div>

</div>
""", unsafe_allow_html=True)


i1, i2, i3 = st.columns(3)


with i1:

    st.info(
        """
        📍 **Location Insight**

        Most of your saved properties
        are in Nagpur.
        """
    )


with i2:

    st.success(
        """
        💰 **Price Insight**

        3 saved properties recently
        received price reductions.
        """
    )


with i3:

    st.warning(
        """
        🎯 **Decision Insight**

        Your strongest match currently
        scores 94%.
        """
    )


# ============================================================
# FUTURE FEATURES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Advanced Property Intelligence — Coming Next
</div>

<div class="section-subtitle">
Technology that helps buyers make smarter property decisions.
</div>

</div>
""", unsafe_allow_html=True)


x1, x2, x3 = st.columns(3)


with x1:

    st.info(
        """
        🤖 **AI Property Advisor**

        Personalized property recommendations
        based on your requirements.
        """
    )


with x2:

    st.success(
        """
        📈 **Price Prediction**

        Estimate potential future
        price movement.
        """
    )


with x3:

    st.warning(
        """
        🗺️ **Location Intelligence**

        Compare connectivity,
        amenities and neighbourhood data.
        """
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
