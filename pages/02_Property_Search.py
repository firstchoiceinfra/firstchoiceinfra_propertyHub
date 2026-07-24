import streamlit as st
from datetime import date

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 02 — PROPERTY SEARCH
# ============================================================

st.set_page_config(
    page_title="Property Search | FirstChoice Infra Property Hub",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
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

/* SIDEBAR */

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

/* HERO */

.search-hero {

    padding: 45px;

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

    margin-bottom: 30px;
}

.search-hero h1 {

    font-size: 44px;

    font-weight: 900;

    margin-bottom: 10px;
}

.search-hero p {

    font-size: 18px;

    line-height: 1.7;

}

/* SEARCH BOX */

.search-box {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 30px;
}

/* SECTION */

.section-title {

    padding: 22px 28px;

    border-radius: 24px;

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

    margin-top: 30px;

    margin-bottom: 25px;
}

/* PROPERTY CARD */

.property-card {

    padding: 25px;

    border-radius: 26px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    border:
    1px solid #E5E7EB;

    margin-bottom: 25px;
}

.property-title {

    font-size: 25px;

    font-weight: 800;

    color: #111827;
}

.property-location {

    color: #4F46E5;

    font-weight: 600;

}

.property-price {

    font-size: 25px;

    font-weight: 900;

    color: #059669;
}

.property-tag {

    display: inline-block;

    padding: 6px 12px;

    border-radius: 20px;

    background: #EEF2FF;

    color: #4338CA;

    font-weight: 600;

}

/* INFO CARD */

.info-card {

    padding: 25px;

    border-radius: 25px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.06);

}

/* FOOTER */

.footer {

    margin-top: 60px;

    padding: 40px;

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

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <h1>🏠 FirstChoice</h1>

    <p>Property Hub</p>

    <hr>
    """, unsafe_allow_html=True)

    st.markdown("### 🔎 Property Search")

    st.info(
        "Use the filters to find properties "
        "according to your requirements."
    )

    st.markdown("""
    ### Search Categories

    🏠 Residential

    🏢 Commercial

    🌳 Land & Plot

    🔑 Rental

    🚀 New Projects

    📈 Investment
    """)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="search-hero">

<h1>
🔎 Find Your Perfect Property
</h1>

<p>
Search verified homes, apartments, villas, plots,
land, commercial spaces and new projects across India.
</p>

<p>
Buy • Rent • Invest • Discover
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH FILTER SECTION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🔍 Property Search Filters
</h2>

<p>
Select your preferred location and property requirements.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="search-box">',
    unsafe_allow_html=True
)


# ============================================================
# PURPOSE
# ============================================================

c1, c2, c3 = st.columns(3)


with c1:

    purpose = st.selectbox(
        "Property Purpose",
        [
            "Buy",
            "Rent",
            "Sell",
            "Lease",
            "Investment"
        ]
    )


with c2:

    property_category = st.selectbox(
        "Property Category",
        [
            "All Categories",
            "Residential",
            "Commercial",
            "Land & Plot",
            "New Project"
        ]
    )


with c3:

    property_type = st.selectbox(
        "Property Type",
        [
            "Any Property",
            "Apartment",
            "Flat",
            "Villa",
            "Independent House",
            "Row House",
            "Farm House",
            "Plot",
            "Residential Plot",
            "Commercial Plot",
            "Farm Land",
            "Office",
            "Shop",
            "Showroom",
            "Warehouse",
            "Factory",
            "Industrial Property"
        ]
    )


# ============================================================
# LOCATION
# ============================================================

st.markdown("### 📍 Property Location")


l1, l2, l3, l4 = st.columns(4)


with l1:

    country = st.selectbox(
        "Country",
        [
            "India"
        ]
    )


with l2:

    state = st.selectbox(
        "State",
        [
            "All States",
            "Maharashtra",
            "Madhya Pradesh",
            "Gujarat",
            "Delhi",
            "Karnataka",
            "Telangana",
            "Tamil Nadu",
            "Uttar Pradesh",
            "Rajasthan",
            "Goa",
            "Other"
        ]
    )


with l3:

    city = st.text_input(
        "City / Town",
        placeholder="Example: Nagpur"
    )


with l4:

    area = st.text_input(
        "Area / Locality",
        placeholder="Example: Wardha Road"
    )


# ============================================================
# PRICE
# ============================================================

st.markdown("### 💰 Budget Range")


p1, p2 = st.columns(2)


with p1:

    min_price = st.number_input(
        "Minimum Budget (₹)",
        min_value=0,
        value=0,
        step=100000
    )


with p2:

    max_price = st.number_input(
        "Maximum Budget (₹)",
        min_value=0,
        value=50000000,
        step=100000
    )


# ============================================================
# PROPERTY SIZE
# ============================================================

st.markdown("### 📐 Property Size")


s1, s2, s3 = st.columns(3)


with s1:

    min_area = st.number_input(
        "Minimum Area",
        min_value=0,
        value=0,
        step=100
    )


with s2:

    max_area = st.number_input(
        "Maximum Area",
        min_value=0,
        value=100000,
        step=100
    )


with s3:

    area_unit = st.selectbox(
        "Area Unit",
        [
            "Sq. Ft.",
            "Sq. Yard",
            "Sq. Meter",
            "Acre",
            "Hectare",
            "Guntha"
        ]
    )


# ============================================================
# ADVANCED FILTERS
# ============================================================

with st.expander(
    "⚙️ Advanced Search Filters"
):

    a1, a2, a3 = st.columns(3)


    with a1:

        bedrooms = st.selectbox(
            "Bedrooms",
            [
                "Any",
                "1 BHK",
                "2 BHK",
                "3 BHK",
                "4 BHK",
                "5+ BHK"
            ]
        )


    with a2:

        possession = st.selectbox(
            "Property Status",
            [
                "Any Status",
                "Ready to Move",
                "Under Construction",
                "Upcoming Project",
                "New Launch"
            ]
        )


    with a3:

        furnished = st.selectbox(
            "Furnishing",
            [
                "Any",
                "Fully Furnished",
                "Semi Furnished",
                "Unfurnished"
            ]
        )


    a4, a5, a6 = st.columns(3)


    with a4:

        verified_only = st.checkbox(
            "🛡️ Verified Listings Only"
        )


    with a5:

        video_only = st.checkbox(
            "🎥 Properties With Video"
        )


    with a6:

        map_only = st.checkbox(
            "📍 Properties With Google Location"
        )


# ============================================================
# SEARCH BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)


search_button = st.button(
    "🔎 SEARCH PROPERTIES",
    use_container_width=True,
    type="primary"
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SEARCH VALIDATION
# ============================================================

if search_button:

    if min_price > max_price:

        st.error(
            "Minimum budget cannot be greater than maximum budget."
        )

    elif min_area > max_area:

        st.error(
            "Minimum property area cannot be greater than maximum area."
        )

    else:

        st.success(
            "Property search completed successfully."
        )

        st.session_state["property_search"] = {

            "purpose": purpose,

            "category": property_category,

            "property_type": property_type,

            "country": country,

            "state": state,

            "city": city,

            "area": area,

            "min_price": min_price,

            "max_price": max_price,

            "min_area": min_area,

            "max_area": max_area,

            "area_unit": area_unit,

            "bedrooms": bedrooms,

            "possession": possession,

            "furnished": furnished,

            "verified_only": verified_only,

            "video_only": video_only,

            "map_only": map_only

        }


# ============================================================
# SAMPLE PROPERTY DATA
# ============================================================

properties = [

    {
        "title": "Premium 3 BHK Apartment",
        "location": "Wardha Road, Nagpur, Maharashtra",
        "type": "Apartment",
        "category": "Residential",
        "purpose": "Buy",
        "price": 7500000,
        "area": 1450,
        "unit": "Sq. Ft.",
        "status": "Ready to Move",
        "verified": True,
        "video": True,
        "description":
        "Premium residential apartment with modern amenities and excellent connectivity."
    },

    {
        "title": "Residential Plot Near Highway",
        "location": "Katol Road, Nagpur, Maharashtra",
        "type": "Residential Plot",
        "category": "Land & Plot",
        "purpose": "Buy",
        "price": 3500000,
        "area": 2000,
        "unit": "Sq. Ft.",
        "status": "Ready to Build",
        "verified": True,
        "video": True,
        "description":
        "Residential plot located near major road connectivity and upcoming development."
    },

    {
        "title": "Modern Commercial Office",
        "location": "Civil Lines, Nagpur, Maharashtra",
        "type": "Office",
        "category": "Commercial",
        "purpose": "Rent",
        "price": 85000,
        "area": 2200,
        "unit": "Sq. Ft.",
        "status": "Ready to Move",
        "verified": True,
        "video": False,
        "description":
        "Premium commercial office space suitable for corporate and professional businesses."
    }

]


# ============================================================
# FILTER SAMPLE DATA
# ============================================================

filtered_properties = []


for property_data in properties:

    match = True


    if property_category != "All Categories":

        if property_data["category"] != property_category:

            match = False


    if property_type != "Any Property":

        if property_data["type"] != property_type:

            match = False


    if purpose != "Investment":

        if property_data["purpose"] != purpose:

            match = False


    if city:

        if city.lower() not in property_data["location"].lower():

            match = False


    if area:

        if area.lower() not in property_data["location"].lower():

            match = False


    if not (
        min_price
        <=
        property_data["price"]
        <=
        max_price
    ):

        match = False


    if not (
        min_area
        <=
        property_data["area"]
        <=
        max_area
    ):

        match = False


    if verified_only:

        if not property_data["verified"]:

            match = False


    if video_only:

        if not property_data["video"]:

            match = False


    if match:

        filtered_properties.append(
            property_data
        )


# ============================================================
# RESULTS HEADER
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🏠 Property Search Results
</h2>

</div>
""", unsafe_allow_html=True)


st.write(
    f"Found **{len(filtered_properties)}** matching properties."
)


# ============================================================
# PROPERTY RESULTS
# ============================================================

if len(filtered_properties) == 0:

    st.warning(
        "No properties found matching your search criteria."
    )

else:

    for index, property_data in enumerate(
        filtered_properties
    ):

        st.markdown(
            '<div class="property-card">',
            unsafe_allow_html=True
        )


        r1, r2 = st.columns(
            [2, 1]
        )


        with r1:

            st.markdown(
                f"""
                <div class="property-title">
                🏠 {property_data["title"]}
                </div>

                <div class="property-location">
                📍 {property_data["location"]}
                </div>

                <br>

                <span class="property-tag">
                {property_data["category"]}
                </span>

                &nbsp;

                <span class="property-tag">
                {property_data["type"]}
                </span>

                &nbsp;

                <span class="property-tag">
                {property_data["status"]}
                </span>
                """,
                unsafe_allow_html=True
            )


            st.write(
                property_data["description"]
            )


            st.write(
                f"📐 Area: **{property_data['area']:,} "
                f"{property_data['unit']}**"
            )


            if property_data["verified"]:

                st.success(
                    "🛡️ Verified Property"
                )


        with r2:

            st.markdown(
                f"""
                <div class="property-price">
                ₹{property_data["price"]:,}
                </div>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "📍 View Location",
                key=f"location_{index}",
                use_container_width=True
            ):

                st.info(
                    "Google Maps integration will open here."
                )


            if property_data["video"]:

                if st.button(
                    "🎥 Watch Property Video",
                    key=f"video_{index}",
                    use_container_width=True
                ):

                    st.info(
                        "Property video player will open here."
                    )


            if st.button(
                "📞 Contact Owner",
                key=f"contact_{index}",
                use_container_width=True
            ):

                st.success(
                    "Owner contact request submitted."
                )


            if st.button(
                "❤️ Save Property",
                key=f"save_{index}",
                use_container_width=True
            ):

                st.success(
                    "Property saved to your favourites."
                )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# FUTURE PLATFORM FEATURES
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🚀 Advanced Property Discovery
</h2>

<p>
Future versions will include AI recommendations,
property comparison, map-based search,
360° property tours, video listings,
EMI calculations and investment intelligence.
</p>

</div>
""", unsafe_allow_html=True)


x1, x2, x3, x4 = st.columns(4)


with x1:

    st.markdown("""
    <div class="info-card">

    <h3>🤖 AI Recommendations</h3>

    <p>
    Discover properties based on your
    search behaviour and preferences.
    </p>

    </div>
    """, unsafe_allow_html=True)


with x2:

    st.markdown("""
    <div class="info-card">

    <h3>🗺️ Map Search</h3>

    <p>
    Explore properties directly
    on an interactive map.
    </p>

    </div>
    """, unsafe_allow_html=True)


with x3:

    st.markdown("""
    <div class="info-card">

    <h3>🎥 Video Properties</h3>

    <p>
    Watch property videos and
    nearby location videos.
    </p>

    </div>
    """, unsafe_allow_html=True)


with x4:

    st.markdown("""
    <div class="info-card">

    <h3>📊 Investment Insights</h3>

    <p>
    Analyze property value,
    rental yield and investment potential.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# BACK BUTTON
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)


if st.button(
    "⬅️ BACK TO HOME",
    use_container_width=True
):

    st.switch_page(
        "app.py"
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

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
