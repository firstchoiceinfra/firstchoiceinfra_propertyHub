import streamlit as st


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 03 — POST PROPERTY
# ============================================================

st.set_page_config(
    page_title="Post Property | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM UI
# ============================================================

st.markdown("""
<style>

.stApp {

    background:
    radial-gradient(
        circle at 10% 10%,
        rgba(59,130,246,0.10),
        transparent 30%
    ),

    radial-gradient(
        circle at 90% 20%,
        rgba(168,85,247,0.10),
        transparent 30%
    ),

    linear-gradient(
        135deg,
        #F8FAFC,
        #EEF2FF,
        #FAF5FF,
        #F0FDFA
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
        #020617,
        #0F172A,
        #1E1B4B,
        #312E81
    );

}


[data-testid="stSidebar"] * {

    color:
    white !important;

}


/* HERO */

.post-hero {

    padding:
    55px;

    border-radius:
    40px;

    color:
    white;

    background:

    linear-gradient(
        135deg,
        #020617,
        #172554,
        #4338CA,
        #7E22CE,
        #BE185D
    );

    box-shadow:

    0 30px 80px
    rgba(30,41,59,0.30);

    margin-bottom:
    35px;

}


.post-hero h1 {

    font-size:
    48px;

    font-weight:
    900;

}


.post-hero p {

    font-size:
    19px;

    line-height:
    1.7;

}


/* SECTION */

.section-title {

    padding:
    22px 28px;

    border-radius:
    25px;

    color:
    white;

    background:

    linear-gradient(
        135deg,
        #1E3A8A,
        #4338CA,
        #7E22CE
    );

    box-shadow:

    0 15px 40px
    rgba(79,70,229,0.20);

    margin:
    30px 0 25px 0;

}


.section-title h2 {

    margin:
    0;

    font-size:
    28px;

    font-weight:
    900;

}


/* PREVIEW */

.preview-card {

    padding:
    35px;

    border-radius:
    30px;

    background:
    rgba(255,255,255,0.95);

    border:
    1px solid
    #E2E8F0;

    box-shadow:

    0 20px 50px
    rgba(15,23,42,0.10);

}


.preview-price {

    color:
    #047857;

    font-size:
    30px;

    font-weight:
    900;

}


/* FOOTER */

.fc-footer {

    margin-top:
    60px;

    padding:
    40px;

    border-radius:
    32px;

    color:
    white;

    text-align:
    center;

    background:

    linear-gradient(
        135deg,
        #020617,
        #1E1B4B,
        #312E81
    );

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE — CUSTOM AREAS
# ============================================================

if "custom_areas" not in st.session_state:

    st.session_state.custom_areas = {}


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:25px;
    ">

    <h1>🏠 FirstChoice</h1>

    <h3>Property Hub</h3>

    <hr>

    <p>
    India's Next-Generation<br>
    Real Estate Ecosystem
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("### 📌 Navigation")


    st.page_link(
        "app.py",
        label="🏠 Home"
    )


    st.page_link(
        "pages/01_Login_Register.py",
        label="🔐 Login & Registration"
    )


    st.page_link(
        "pages/02_Property_Search.py",
        label="🔎 Property Search"
    )


    st.page_link(
        "pages/03_Post_Property.py",
        label="🏡 Post Property"
    )


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="post-hero">

<h1>
🏡 Post Your Property
</h1>

<p>
List your property with photos, videos and exact location
so buyers and tenants can discover it easily.
</p>

<p>
📸 Photos
&nbsp; • &nbsp;
🎥 Video
&nbsp; • &nbsp;
📍 Google Location
&nbsp; • &nbsp;
🌍 Smart Area Discovery
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY PURPOSE
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🎯 Property Listing Purpose
</h2>

</div>
""", unsafe_allow_html=True)


purpose = st.selectbox(

    "What do you want to do?",

    [
        "Sell Property",
        "Rent Property",
        "Lease Property",
        "Post Upcoming Project",
        "Post Ongoing Project",
        "Post Ready-to-Move Project",
        "Post New Layout",
        "Post Plot / Land"
    ]

)


# ============================================================
# PROPERTY CATEGORY
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🏠 Property Category
</h2>

</div>
""", unsafe_allow_html=True)


category = st.selectbox(

    "Select Property Category",

    [
        "Residential",
        "Commercial",
        "Plot / Land",
        "Agricultural Land",
        "Industrial Property",
        "Farm House",
        "Upcoming Project",
        "Ongoing Project",
        "Ready to Move Project"
    ]

)


property_type = st.selectbox(

    "Property Type",

    [
        "Apartment",
        "Villa",
        "Independent House",
        "Builder Floor",
        "Studio Apartment",
        "Residential Plot",
        "Commercial Plot",
        "Farm Land",
        "Office",
        "Shop",
        "Showroom",
        "Warehouse",
        "Industrial Unit",
        "Other"
    ]

)


# ============================================================
# LOCATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🌍 Property Location
</h2>

<p>
Select your location. If your exact area is not available,
choose Other Area and add your locality.
</p>

</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)


with col1:

    country = st.selectbox(

        "🌍 Country",

        [
            "India",
            "Other Country"
        ]

    )


with col2:

    state = st.selectbox(

        "🗺️ State",

        [
            "Maharashtra",
            "Madhya Pradesh",
            "Gujarat",
            "Karnataka",
            "Telangana",
            "Rajasthan",
            "Uttar Pradesh",
            "Delhi",
            "Other State"
        ]

    )


col1, col2 = st.columns(2)


with col1:

    city = st.selectbox(

        "🏙️ City / District",

        [
            "Nagpur",
            "Mumbai",
            "Pune",
            "Nashik",
            "Aurangabad",
            "Indore",
            "Bhopal",
            "Ahmedabad",
            "Other City"
        ]

    )


with col2:

    locality_type = st.selectbox(

        "🏘️ Location Type",

        [
            "Village",
            "Town",
            "City Area",
            "Suburb",
            "Other"
        ]

    )


# ============================================================
# VILLAGE / TOWN
# ============================================================

village_town = st.text_input(

    "🏘️ Village / Town Name",

    placeholder=
    "Example: Nagpur, Hingna, Wardha Road etc."

)


# ============================================================
# AREA
# ============================================================

existing_areas = [

    "Select Area",

    "Civil Lines",

    "Dharampeth",

    "Manish Nagar",

    "Wardha Road",

    "Hingna",

    "Katol Road",

    "Koradi",

    "Other Area"

]


area = st.selectbox(

    "📍 Select Area",

    existing_areas

)


# ============================================================
# CUSTOM AREA
# ============================================================

custom_area = ""


if area == "Other Area":

    custom_area = st.text_input(

        "📍 Enter Your Exact Area Name",

        placeholder=
        "Example: Your locality / colony / village / layout"

    )


    if custom_area.strip():

        save_area = st.button(

            "💾 Save This Area"

        )


        if save_area:

            location_key = (

                country
                + "_"
                + state
                + "_"
                + city
                + "_"
                + village_town

            )


            if location_key not in st.session_state.custom_areas:

                st.session_state.custom_areas[
                    location_key
                ] = []


            if custom_area not in st.session_state.custom_areas[
                location_key
            ]:

                st.session_state.custom_areas[
                    location_key
                ].append(
                    custom_area
                )


                st.success(

                    f"Area '{custom_area}' saved successfully."

                )


# ============================================================
# SHOW SAVED CUSTOM AREAS
# ============================================================

location_key = (

    country
    + "_"
    + state
    + "_"
    + city
    + "_"
    + village_town

)


saved_areas = st.session_state.custom_areas.get(

    location_key,

    []

)


if saved_areas:

    st.info(

        "📍 Previously added areas for this location: "
        + ", ".join(saved_areas)

    )


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📐 Property Details
</h2>

</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)


with col1:

    property_area = st.number_input(

        "📐 Property Area (Sq.Ft.)",

        min_value=0,

        value=0

    )


with col2:

    price = st.number_input(

        "💰 Expected Price (₹)",

        min_value=0,

        value=0,

        step=100000

    )


with col3:

    bhk = st.selectbox(

        "🛏️ BHK",

        [
            "Not Applicable",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5+ BHK"
        ]

    )


# ============================================================
# PROJECT STATUS
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🏗️ Project & Property Status
</h2>

</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)


with col1:

    project_status = st.selectbox(

        "🏗️ Status",

        [
            "Ready to Move",
            "Under Construction",
            "Upcoming",
            "Ongoing",
            "New Launch"
        ]

    )


with col2:

    possession = st.selectbox(

        "📅 Possession",

        [
            "Immediate",
            "Within 6 Months",
            "Within 1 Year",
            "1-2 Years",
            "2+ Years"
        ]

    )


# ============================================================
# GOOGLE LOCATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📍 Google Location
</h2>

</div>
""", unsafe_allow_html=True)


google_location = st.text_input(

    "🔗 Google Maps Location Link",

    placeholder=
    "Paste your Google Maps location link here"

)


st.caption(

    "Tip: Google Maps में property location खोलें → Share → Copy Link → यहाँ paste करें."

)


# ============================================================
# PHOTOS
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📸 Property Photos
</h2>

</div>
""", unsafe_allow_html=True)


photos = st.file_uploader(

    "Upload Property Photos",

    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ],

    accept_multiple_files=True

)


# ============================================================
# VIDEO
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🎥 Property Video Advertisement
</h2>

<p>
Show buyers what is around the property through video.
</p>

</div>
""", unsafe_allow_html=True)


video = st.file_uploader(

    "Upload Property Video",

    type=[
        "mp4",
        "mov",
        "avi",
        "webm"
    ]

)


# ============================================================
# DESCRIPTION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📝 Property Description
</h2>

</div>
""", unsafe_allow_html=True)


description = st.text_area(

    "Describe Your Property",

    placeholder=
    "Describe property features, nearby locations, roads, schools, hospitals, markets and other important information.",

    height=180

)


# ============================================================
# CONTACT DETAILS
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
👤 Contact Information
</h2>

</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)


with col1:

    contact_name = st.text_input(

        "👤 Contact Person Name",

        placeholder=
        "Enter contact person name"

    )


with col2:

    contact_mobile = st.text_input(

        "📱 Contact Mobile Number",

        placeholder=
        "Enter 10-digit mobile number"

    )


# ============================================================
# LISTING PREVIEW
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
👀 Listing Preview
</h2>

</div>
""", unsafe_allow_html=True)


final_area = (

    custom_area

    if area == "Other Area"

    else area

)


st.markdown(
    f"""
    <div class="preview-card">

    <h2>
    🏡 {property_type}
    </h2>

    <p>
    <b>Purpose:</b>
    {purpose}
    </p>

    <p>
    <b>Category:</b>
    {category}
    </p>

    <p>
    <b>Location:</b>
    {country},
    {state},
    {city},
    {village_town},
    {final_area}
    </p>

    <p>
    <b>Area:</b>
    {property_area} Sq.Ft.
    </p>

    <p>
    <b>BHK:</b>
    {bhk}
    </p>

    <p>
    <b>Status:</b>
    {project_status}
    </p>

    <p>
    <b>Google Location:</b>
    {google_location if google_location else "Not Added"}
    </p>

    <div class="preview-price">
    ₹ {price:,}
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# POST PROPERTY
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)


if st.button(

    "🚀 POST PROPERTY",

    use_container_width=True

):

    if not village_town.strip():

        st.error(

            "Please enter Village / Town name."

        )

    elif area == "Other Area" and not custom_area.strip():

        st.error(

            "Please enter your exact Area name."

        )

    elif property_area <= 0:

        st.error(

            "Please enter valid property area."

        )

    elif price <= 0:

        st.error(

            "Please enter valid property price."

        )

    else:

        st.success(

            "🎉 Property listing submitted successfully!"

        )

        st.info(

            "Database integration के बाद यह listing automatically Property Search में दिखाई देगी."

        )


# ============================================================
# QUICK NAVIGATION
# ============================================================

st.markdown("### 🚀 Quick Navigation")


c1, c2, c3 = st.columns(3)


with c1:

    if st.button(
        "🔎 Property Search",
        use_container_width=True
    ):

        st.switch_page(
            "pages/02_Property_Search.py"
        )


with c2:

    if st.button(
        "🔐 Login / Register",
        use_container_width=True
    ):

        st.switch_page(
            "pages/01_Login_Register.py"
        )


with c3:

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.switch_page(
            "app.py"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="fc-footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
Buy • Sell • Rent • Invest • Build • Discover
</p>

<p>
India's Next-Generation Real Estate Ecosystem
</p>

<hr>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
