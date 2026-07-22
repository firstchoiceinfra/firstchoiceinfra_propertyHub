import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 14 - SAVED PROPERTIES / WISHLIST / COMPARE
# ============================================================

st.set_page_config(
    page_title="Saved Properties | FirstChoice Property Hub",
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

    background: white;

    padding: 25px;

    border-radius: 28px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;

    min-height: 420px;
}

/* COMPARE */

.compare-card {

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F8FAFF,
        #FDF4FF
    );

    padding: 30px;

    border-radius: 30px;

    box-shadow:
    0 18px 45px
    rgba(0,0,0,0.08);

    border:
    1px solid #E2E8F0;
}

/* AI */

.ai-card {

    padding: 38px;

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
PROPERTY HUB • SMART PROPERTY DISCOVERY
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
❤️ My Saved Properties
</div>

<div class="hero-subtitle">
Save your favourite properties, compare your best choices
and discover personalised recommendations.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# QUICK SUMMARY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Your Property Shortlist
</div>

<div class="section-subtitle">
Everything you are interested in, organised in one place.
</div>

</div>
""", unsafe_allow_html=True)


s1, s2, s3, s4 = st.columns(4)


with s1:

    st.metric(
        "❤️ Saved",
        "18"
    )


with s2:

    st.metric(
        "⚖️ Compare",
        "4"
    )


with s3:

    st.metric(
        "📅 Site Visits",
        "3"
    )


with s4:

    st.metric(
        "💬 Enquiries",
        "7"
    )


# ============================================================
# SEARCH
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Find Saved Property
</div>

<div class="section-subtitle">
Search and organise your saved properties.
</div>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    search = st.text_input(
        "Search",
        placeholder=
        "Search by property name or location"
    )


with c2:

    sort_by = st.selectbox(
        "Sort By",
        [
            "Recently Saved",
            "Price: Low to High",
            "Price: High to Low",
            "Largest Area",
            "Most Popular"
        ]
    )


# ============================================================
# SAVED PROPERTY DATA
# ============================================================

properties = [

    {
        "name":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "price":
        "₹1.25 Crore",

        "area":
        "1,850 Sq.Ft",

        "type":
        "Apartment",

        "status":
        "Ready to Move",

        "verified":
        "Verified",

        "rating":
        "4.8 / 5",

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

        "area":
        "3,200 Sq.Ft",

        "type":
        "Villa",

        "status":
        "Ready to Move",

        "verified":
        "Verified",

        "rating":
        "4.9 / 5",

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

        "area":
        "2,000 Sq.Ft",

        "type":
        "Residential Plot",

        "status":
        "New Launch",

        "verified":
        "Verified",

        "rating":
        "4.7 / 5",

        "image":
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"
    }

]


# ============================================================
# SAVED PROPERTIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏡 Your Favourite Properties
</div>

<div class="section-subtitle">
Compare, enquire or schedule a site visit.
</div>

</div>
""", unsafe_allow_html=True)


cols = st.columns(3)


for index, property_item in enumerate(properties):

    with cols[index % 3]:

        st.markdown(
            f"""
            <div class="property-card">

            <img
            src="{property_item['image']}"
            style="
            width:100%;
            height:200px;
            object-fit:cover;
            border-radius:20px;
            "
            >

            <h3>
            {property_item['name']}
            </h3>

            <p>
            📍 {property_item['location']}
            </p>

            <h2 style="color:#7C3AED;">
            {property_item['price']}
            </h2>

            <p>
            📐 {property_item['area']}
            </p>

            <p>
            🏠 {property_item['type']}
            </p>

            <p>
            🛡️ {property_item['verified']}
            </p>

            <p>
            ⭐ {property_item['rating']}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        b1, b2 = st.columns(2)


        with b1:

            if st.button(
                "❤️ Saved",
                key=f"save_{index}",
                use_container_width=True
            ):

                st.success(
                    "Property removed from wishlist."
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


        if st.button(
            "📅 Schedule Site Visit",
            key=f"visit_{index}",
            use_container_width=True
        ):

            st.info(
                "Site visit scheduling module will open."
            )


# ============================================================
# COMPARE PROPERTIES
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


st.markdown("""
<div class="compare-card">

<h2>
🏆 Compare Your Top Choices
</h2>

<p>
The production version will allow buyers to compare
multiple properties side-by-side.
</p>

</div>
""", unsafe_allow_html=True)


compare_data = {

    "Feature": [

        "Property Type",

        "Location",

        "Price",

        "Area",

        "Property Status",

        "Verification",

        "Rating"

    ],

    "Property A": [

        "Apartment",

        "Civil Lines, Nagpur",

        "₹1.25 Crore",

        "1,850 Sq.Ft",

        "Ready to Move",

        "Verified",

        "4.8 / 5"

    ],

    "Property B": [

        "Villa",

        "Baner, Pune",

        "₹2.80 Crore",

        "3,200 Sq.Ft",

        "Ready to Move",

        "Verified",

        "4.9 / 5"

    ],

    "Property C": [

        "Residential Plot",

        "Wardha Road, Nagpur",

        "₹48 Lakh",

        "2,000 Sq.Ft",

        "New Launch",

        "Verified",

        "4.7 / 5"

    ]

}


st.table(compare_data)


# ============================================================
# SMART RECOMMENDATIONS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 Properties Recommended For You
</div>

<div class="section-subtitle">
Discover properties based on your saved preferences.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
🧠 FirstChoice Smart Match
</h2>

<p>
Based on your saved properties, you may be interested in
premium residential projects around Nagpur and Pune.
</p>

<p>
🎯 Your preferred property type:
Residential + Premium Homes
</p>

<p>
💰 Your observed budget range:
₹40 Lakh – ₹3 Crore
</p>

<p>
📍 Your preferred locations:
Nagpur • Pune
</p>

<p>
⭐ Your preferred listings:
Verified Properties
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY ALERTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔔 Smart Property Alerts
</div>

<div class="section-subtitle">
Get notified when a property matching your interests appears.
</div>

</div>
""", unsafe_allow_html=True)


alert1, alert2 = st.columns(2)


with alert1:

    alert_location = st.text_input(
        "Preferred Location",
        placeholder="Example: Nagpur"
    )


with alert2:

    alert_budget = st.selectbox(
        "Budget Range",
        [
            "Any Budget",
            "Under ₹50 Lakh",
            "₹50 Lakh – ₹1 Crore",
            "₹1 Crore – ₹3 Crore",
            "Above ₹3 Crore"
        ]
    )


if st.button(
    "🔔 CREATE PROPERTY ALERT",
    use_container_width=True
):

    st.success(
        "Your smart property alert has been created."
    )


# ============================================================
# SMART DECISION SUPPORT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💡 Smart Decision Support
</div>

<div class="section-subtitle">
Compare more than just price.
</div>

</div>
""", unsafe_allow_html=True)


d1, d2, d3 = st.columns(3)


with d1:

    st.info(
        """
        📍 **Location Score**

        Compare connectivity,
        neighbourhood and nearby facilities.
        """
    )


with d2:

    st.success(
        """
        🛡️ **Trust Score**

        Check owner verification,
        property verification and listing quality.
        """
    )


with d3:

    st.warning(
        """
        📈 **Investment Potential**

        Future versions will provide
        market and investment insights.
        """
    )


# ============================================================
# NEXT LEVEL FEATURE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Coming Next
</div>

<div class="section-subtitle">
A completely new property investment experience.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
📊 Property Investment Intelligence
</h2>

<p>
Analyse a property before investing.
</p>

<p>
📈 Estimated Rental Yield
</p>

<p>
💰 EMI & Cash Flow
</p>

<p>
📊 Price Comparison
</p>

<p>
📍 Location Growth Indicators
</p>

<p>
🏗️ Development Potential
</p>

<p>
🎯 Investment Score
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
Buy • Sell • Rent • Invest • Discover
</p>

<hr>

<small>
© FirstChoice Infra Property Hub
</small>

</div>
""", unsafe_allow_html=True)
