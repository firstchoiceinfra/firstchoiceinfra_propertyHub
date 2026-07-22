import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 8 - SAVED PROPERTIES / FAVORITES
# PREMIUM MULTINATIONAL REAL ESTATE MARKETPLACE
# ============================================================

st.set_page_config(
    page_title="Saved Properties | FirstChoice Property Hub",
    page_icon="❤️",
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

/* ============================================================
BRAND
============================================================ */

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


/* ============================================================
PAGE HEADER
============================================================ */

.page-header {

    margin-top: 28px;

    padding: 42px;

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

    width: 300px;

    height: 300px;

    right: -100px;

    top: -150px;

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


/* ============================================================
SECTION HEADER
============================================================ */

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


/* ============================================================
STAT CARDS
============================================================ */

.stat-card {

    padding: 25px;

    border-radius: 24px;

    color: white;

    min-height: 140px;

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

.pink {

    background:
    linear-gradient(
        135deg,
        #EC4899,
        #F43F5E
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

.green {

    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}


/* ============================================================
PROPERTY CARD
============================================================ */

.property-card {

    background: white;

    border-radius: 28px;

    overflow: hidden;

    margin-bottom: 25px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    transition:
    transform 0.2s ease;
}

.property-image {

    width: 100%;

    height: 245px;

    object-fit: cover;
}

.property-content {

    padding: 25px;
}


/* ============================================================
BADGES
============================================================ */

.badge {

    display: inline-block;

    padding: 7px 14px;

    border-radius: 30px;

    font-size: 11px;

    font-weight: 800;

    color: white;

    margin-right: 5px;
}

.badge-verified {

    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.badge-premium {

    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}


/* ============================================================
COMPARE
============================================================ */

.compare-box {

    background: white;

    padding: 28px;

    border-radius: 25px;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);
}


/* ============================================================
PREMIUM
============================================================ */

.premium-card {

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
    0 20px 55px
    rgba(124,58,237,0.25);
}


/* ============================================================
FOOTER
============================================================ */

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
❤️ My Saved Properties
</div>

<div class="page-subtitle">
Keep your favourite properties in one place,
compare your shortlisted options and plan your next move.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# STATS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Your Property Shortlist
</div>

<div class="section-subtitle">
A quick overview of your saved real estate opportunities.
</div>

</div>
""", unsafe_allow_html=True)

s1,s2,s3,s4 = st.columns(4)

stats = [

    ("❤️","Saved Properties","18","pink"),

    ("👁️","Recently Viewed","32","blue"),

    ("📅","Site Visits","5","purple"),

    ("💬","Active Enquiries","8","green")

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
# SEARCH & FILTER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Find Your Saved Property
</div>

<div class="section-subtitle">
Search and filter your favourite properties.
</div>

</div>
""", unsafe_allow_html=True)

f1,f2,f3,f4 = st.columns(4)

with f1:

    search = st.text_input(
        "Search",
        placeholder="Property name or location"
    )

with f2:

    property_type = st.selectbox(
        "Property Type",
        [
            "All",
            "Apartment",
            "Villa",
            "Plot",
            "Commercial"
        ]
    )

with f3:

    city = st.selectbox(
        "City",
        [
            "All Cities",
            "Nagpur",
            "Mumbai",
            "Pune",
            "Bengaluru",
            "Delhi"
        ]
    )

with f4:

    price_range = st.selectbox(
        "Budget",
        [
            "Any Budget",
            "Under ₹50 Lakh",
            "₹50 Lakh - ₹1 Crore",
            "₹1 Crore - ₹3 Crore",
            "Above ₹3 Crore"
        ]
    )


# ============================================================
# SAVED PROPERTIES DATA
# ============================================================

properties = [

    {

        "name":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "price":
        "₹1.25 Cr",

        "type":
        "Apartment",

        "verified":
        True,

        "premium":
        True,

        "image":
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=85"

    },

    {

        "name":
        "Modern Luxury Villa",

        "location":
        "Baner, Pune",

        "price":
        "₹2.80 Cr",

        "type":
        "Villa",

        "verified":
        True,

        "premium":
        True,

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

        "type":
        "Plot",

        "verified":
        True,

        "premium":
        False,

        "image":
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"

    },

    {

        "name":
        "Premium Commercial Office",

        "location":
        "Andheri, Mumbai",

        "price":
        "₹4.50 Cr",

        "type":
        "Commercial",

        "verified":
        True,

        "premium":
        True,

        "image":
        "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=85"

    }

]


# ============================================================
# FILTER FUNCTION
# ============================================================

filtered_properties = []

for property_item in properties:

    if search:

        search_text = search.lower()

        if (
            search_text not in
            property_item["name"].lower()
            and
            search_text not in
            property_item["location"].lower()
        ):

            continue

    if property_type != "All":

        if property_item["type"] != property_type:

            continue

    if city != "All Cities":

        if city.lower() not in property_item["location"].lower():

            continue

    filtered_properties.append(
        property_item
    )


# ============================================================
# PROPERTY DISPLAY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
❤️ Your Favourite Properties
</div>

<div class="section-subtitle">
Shortlisted properties you may want to visit or purchase.
</div>

</div>
""", unsafe_allow_html=True)


if not filtered_properties:

    st.warning(
        "No saved properties match your selected filters."
    )


for index, property_item in enumerate(
    filtered_properties
):

    st.markdown(
        f"""
        <div class="property-card">

        <img
        class="property-image"
        src="{property_item['image']}"
        >

        <div class="property-content">

        <span class="badge badge-verified">
        🛡️ Verified
        </span>

        {
        '<span class="badge badge-premium">⭐ Premium</span>'
        if property_item["premium"]
        else ""
        }

        <h2>
        {property_item["name"]}
        </h2>

        <p>
        📍 {property_item["location"]}
        </p>

        <h2 style="color:#7C3AED;">
        {property_item["price"]}
        </h2>

        <p>
        🏠 {property_item["type"]}
        </p>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    b1,b2,b3,b4 = st.columns(4)


    with b1:

        if st.button(
            "🏡 View Property",
            key=f"view_{index}",
            use_container_width=True
        ):

            st.info(
                f"Opening {property_item['name']}"
            )


    with b2:

        if st.button(
            "📅 Site Visit",
            key=f"visit_{index}",
            use_container_width=True
        ):

            st.success(
                "Site visit request initiated."
            )


    with b3:

        if st.button(
            "💬 Contact",
            key=f"contact_{index}",
            use_container_width=True
        ):

            st.info(
                "Owner / Agent contact module will open here."
            )


    with b4:

        if st.button(
            "🗑️ Remove",
            key=f"remove_{index}",
            use_container_width=True
        ):

            st.warning(
                "Property removed from saved list."
            )


# ============================================================
# COMPARE PROPERTIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⚖️ Compare Your Shortlist
</div>

<div class="section-subtitle">
Compare multiple properties before making your final decision.
</div>

</div>
""", unsafe_allow_html=True)


compare_options = [

    "Premium 3 BHK Luxury Apartment",

    "Modern Luxury Villa",

    "Premium Residential Plot",

    "Premium Commercial Office"

]

selected_compare = st.multiselect(

    "Select properties to compare",

    compare_options,

    max_selections=3

)


if selected_compare:

    st.markdown(
        '<div class="compare-box">',
        unsafe_allow_html=True
    )

    comparison_data = {

        "Premium 3 BHK Luxury Apartment":
        ["Nagpur","₹1.25 Cr","Apartment","3 BHK","4,850"],

        "Modern Luxury Villa":
        ["Pune","₹2.80 Cr","Villa","4 BHK","3,240"],

        "Premium Residential Plot":
        ["Nagpur","₹48 Lakh","Plot","N/A","2,190"],

        "Premium Commercial Office":
        ["Mumbai","₹4.50 Cr","Commercial","N/A","5,420"]

    }


    for property_name in selected_compare:

        data = comparison_data[
            property_name
        ]

        st.markdown(
            f"""
            ### 🏡 {property_name}

            📍 **Location:** {data[0]}

            💰 **Price:** {data[1]}

            🏠 **Type:** {data[2]}

            🛏️ **Configuration:** {data[3]}

            👁️ **Views:** {data[4]}

            ---
            """
        )


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SITE VISIT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📅 Plan a Property Visit
</div>

<div class="section-subtitle">
Schedule a visit with the owner, agent or builder.
</div>

</div>
""", unsafe_allow_html=True)


v1,v2 = st.columns(2)


with v1:

    visit_property = st.selectbox(

        "Select Property",

        compare_options

    )


with v2:

    visit_date = st.date_input(

        "Preferred Visit Date"

    )


visit_time = st.selectbox(

    "Preferred Time",

    [

        "10:00 AM",

        "11:00 AM",

        "12:00 PM",

        "2:00 PM",

        "4:00 PM",

        "5:00 PM"

    ]

)


if st.button(

    "📅 Request Site Visit",

    use_container_width=True

):

    st.success(

        f"""
        Site visit request submitted for
        {visit_property} on
        {visit_date} at {visit_time}.
        """

    )


# ============================================================
# PREMIUM FEATURE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⭐ FirstChoice Smart Shortlist
</div>

<div class="section-subtitle">
Get intelligent recommendations based on your saved properties.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="premium-card">

<h2>
🤖 Smart Property Recommendations
</h2>

<p>
FirstChoice Property Hub will analyse your saved properties,
preferred locations, budget and property type to recommend
relevant opportunities.
</p>

<h3>
🎯 Your Personalised Real Estate Discovery
</h3>

<p>
Discover properties that match your investment and lifestyle goals.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(

    "🚀 Explore Recommended Properties",

    use_container_width=True

):

    st.info(

        "AI-powered property recommendations will be connected in the production version."

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
