import streamlit as st
import os
import uuid

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)

from core.database import (
    get_custom_areas,
    save_custom_area,
    create_property,
    save_property_media
)
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

load_premium_ui()


# ============================================================
# MEDIA DIRECTORY
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MEDIA_DIR = os.path.join(
    BASE_DIR,
    "data",
    "property_media"
)

os.makedirs(
    MEDIA_DIR,
    exist_ok=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )

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
# LOGIN CHECK
# ============================================================

if not is_logged_in():

    hero(
        "🔐 Login Required",
        "Please login or create your FirstChoice Property Hub account before posting a property."
    )

    st.warning(
        "You must be logged in to post a property."
    )

    if st.button(
        "🔐 Login / Register",
        use_container_width=True
    ):

        st.switch_page(
            "pages/01_Login_Register.py"
        )

    footer()

    st.stop()


# ============================================================
# HERO
# ============================================================

hero(
    "🏡 List Your Property",
    "Reach genuine buyers, tenants, investors and property seekers through FirstChoice Infra Property Hub."
)


# ============================================================
# INTRODUCTION
# ============================================================

section(
    "🚀 Create Your Property Listing",
    "Provide accurate property details to create a professional listing."
)


st.markdown(
    """
    <div class="fc-card">

    <h3>
    🌟 Increase Your Property Visibility
    </h3>

    <p>
    Add accurate location details, photographs, videos,
    Google Maps location and complete property information.
    </p>

    <p>
    Your listing will be submitted for verification before
    appearing publicly on the Property Search platform.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY PURPOSE
# ============================================================

section(
    "🎯 Property Listing Purpose",
    "Select what you want to do with your property."
)


purpose = st.selectbox(

    "What would you like to do?",

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

section(
    "🏠 Property Category",
    "Choose the category that best describes your property."
)


category = st.selectbox(

    "Property Category",

    [

        "Residential",

        "Commercial",

        "Industrial",

        "Agricultural",

        "Land & Plot",

        "Mixed Use",

        "Other"

    ]

)


# ============================================================
# PROPERTY TYPE
# ============================================================

property_type_options = [

    "Apartment",

    "Villa",

    "Independent House",

    "Builder Floor",

    "Studio Apartment",

    "Residential Plot",

    "Commercial Plot",

    "Farm Land",

    "Agricultural Land",

    "Office",

    "Shop",

    "Showroom",

    "Warehouse",

    "Industrial Unit",

    "Other"

]


property_type = st.selectbox(

    "🏡 Property Type",

    property_type_options

)


# ============================================================
# LOCATION
# ============================================================

section(
    "📍 Property Location",
    "Select the exact location of your property."
)


col1, col2 = st.columns(2)


with col1:

    country = st.selectbox(

        "🌍 Country",

        [

            "India",

            "Other"

        ]

    )


with col2:

    state = st.selectbox(

        "🗺️ State",

        [

            "Maharashtra",

            "Madhya Pradesh",

            "Gujarat",

            "Rajasthan",

            "Delhi",

            "Karnataka",

            "Telangana",

            "Tamil Nadu",

            "Uttar Pradesh",

            "Other"

        ]

    )


col1, col2 = st.columns(2)


with col1:

    city = st.text_input(

        "🏙️ City",

        placeholder="Example: Nagpur"

    )


with col2:

    village_town = st.text_input(

        "🏘️ Village / Town",

        placeholder="Example: Hingna"

    )


# ============================================================
# AREA MANAGEMENT
# ============================================================

st.markdown(
    "### 📍 Area / Locality"
)


custom_areas = []


if (

    country.strip()

    and state.strip()

    and city.strip()

    and village_town.strip()

):

    custom_areas = get_custom_areas(

        country,

        state,

        city,

        village_town

    )


area_options = [

    "Select Area"

]


area_options.extend(

    custom_areas

)


area_options.append(

    "Others"

)


area_selection = st.selectbox(

    "Select Area / Locality",

    area_options

)


custom_area_name = ""


if area_selection == "Others":

    custom_area_name = st.text_input(

        "✏️ Enter Your Area Name",

        placeholder=
        "Example: Green Valley Layout"

    )

    st.info(

        "This new area will automatically be saved for future property listings in the same Village / Town."

    )


if area_selection != "Select Area" and area_selection != "Others":

    area_name = area_selection

else:

    area_name = custom_area_name.strip()


# ============================================================
# PROPERTY DETAILS
# ============================================================

section(
    "📐 Property Details",
    "Enter the size, price and other important property information."
)


col1, col2, col3 = st.columns(3)


with col1:

    property_area = st.number_input(

        "📐 Property Area (Sq.Ft.)",

        min_value=0.0,

        value=0.0,

        step=100.0

    )


with col2:

    price = st.number_input(

        "💰 Price (₹)",

        min_value=0.0,

        value=0.0,

        step=100000.0

    )


with col3:

    bhk = st.selectbox(

        "🛏️ BHK",

        [

            "N/A",

            "1 BHK",

            "2 BHK",

            "3 BHK",

            "4 BHK",

            "5 BHK",

            "6+ BHK"

        ]

    )


# ============================================================
# PROJECT STATUS
# ============================================================

col1, col2 = st.columns(2)


with col1:

    project_status = st.selectbox(

        "🏗️ Project Status",

        [

            "Ready to Move",

            "Under Construction",

            "Upcoming",

            "New Launch",

            "Ready Plot",

            "New Layout",

            "N/A"

        ]

    )


with col2:

    possession = st.text_input(

        "📅 Possession / Availability",

        placeholder=
        "Example: December 2026"

    )


# ============================================================
# GOOGLE LOCATION
# ============================================================

section(
    "📍 Google Maps Location",
    "Add the Google Maps link so property seekers can easily find the exact location."
)


google_location = st.text_input(

    "🔗 Google Maps URL",

    placeholder=
    "Paste Google Maps share link here"

)


st.info(

    "Tip: Open Google Maps → Select your property location → Share → Copy Link → Paste it here."

)


# ============================================================
# DESCRIPTION
# ============================================================

section(
    "📝 Property Description",
    "Describe your property, nearby facilities, road access and important highlights."
)


description = st.text_area(

    "Property Description",

    placeholder=
    "Describe the property, nearby schools, hospitals, markets, roads, transport, surroundings and other important information.",

    height=180

)


# ============================================================
# MEDIA UPLOAD
# ============================================================

section(
    "📸 Photos & 🎥 Property Video",
    "Upload high-quality photographs and a short property video."
)


photos = st.file_uploader(

    "📸 Upload Property Photos",

    type=[

        "jpg",

        "jpeg",

        "png",

        "webp"

    ],

    accept_multiple_files=True

)


video = st.file_uploader(

    "🎥 Upload Property Video",

    type=[

        "mp4",

        "mov",

        "avi",

        "mkv"

    ]

)


st.info(

    "For best performance, upload compressed images and a compressed property video."

)


# ============================================================
# CONTACT DETAILS
# ============================================================

section(
    "📞 Contact Information",
    "Enter the contact details that property seekers can use."
)


col1, col2 = st.columns(2)


with col1:

    contact_name = st.text_input(

        "👤 Contact Person Name",

        placeholder=
        "Enter contact person's name"

    )


with col2:

    contact_mobile = st.text_input(

        "📱 Contact Mobile Number",

        placeholder=
        "Enter 10-digit mobile number"

    )


# ============================================================
# PREVIEW
# ============================================================

section(
    "👁️ Listing Preview",
    "Review your basic property information before submitting."
)


st.markdown(

    f"""
    <div class="property-card">

    <div class="property-info">

    <div class="property-title">

    🏡 {property_type}

    </div>

    <div class="property-location">

    📍 {country} • {state} • {city} •
    {village_town} • {area_name or "Area not selected"}

    </div>

    <div class="property-price">

    ₹ {price:,.0f}

    </div>

    <hr>

    <p>
    🎯 <b>Purpose:</b> {purpose}
    </p>

    <p>
    🏠 <b>Category:</b> {category}
    </p>

    <p>
    📐 <b>Area:</b> {property_area:,.0f} Sq.Ft.
    </p>

    <p>
    🛏️ <b>BHK:</b> {bhk}
    </p>

    <p>
    🏗️ <b>Status:</b> {project_status}
    </p>

    </div>

    </div>
    """,

    unsafe_allow_html=True

)


# ============================================================
# SUBMIT PROPERTY
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)


submit_property = st.button(

    "🚀 SUBMIT PROPERTY FOR VERIFICATION",

    use_container_width=True

)


if submit_property:

    # ========================================================
    # VALIDATION
    # ========================================================

    if not city.strip():

        st.error(

            "Please enter city name."

        )

        st.stop()


    if not village_town.strip():

        st.error(

            "Please enter Village / Town."

        )

        st.stop()


    if not area_name:

        st.error(

            "Please select an area or enter a new area."

        )

        st.stop()


    if property_area <= 0:

        st.error(

            "Please enter property area."

        )

        st.stop()


    if price <= 0:

        st.error(

            "Please enter property price."

        )

        st.stop()


    if not contact_name.strip():

        st.error(

            "Please enter contact person name."

        )

        st.stop()


    if not contact_mobile.strip():

        st.error(

            "Please enter contact mobile number."

        )

        st.stop()


    # ========================================================
    # SAVE CUSTOM AREA
    # ========================================================

    if area_selection == "Others":

        save_custom_area(

            country=country,

            state=state,

            city=city.strip(),

            village_town=village_town.strip(),

            area_name=area_name,

            created_by=st.session_state.get(

                "user_id",

                None

            )

        )


    # ========================================================
    # CREATE PROPERTY
    # ========================================================

    property_id = create_property(

        owner_id=st.session_state.get(

            "user_id",

            None

        ),

        purpose=purpose,

        category=category,

        property_type=property_type,

        country=country,

        state=state,

        city=city.strip(),

        village_town=village_town.strip(),

        area_name=area_name,

        property_area=property_area,

        price=price,

        bhk=bhk,

        project_status=project_status,

        possession=possession.strip(),

        google_location=google_location.strip(),

        description=description.strip(),

        contact_name=contact_name.strip(),

        contact_mobile=contact_mobile.strip()

    )


    # ========================================================
    # SAVE PHOTOS
    # ========================================================

    photo_count = 0


    if photos:

        for photo in photos:

            extension = os.path.splitext(

                photo.name

            )[1].lower()


            unique_name = (

                f"{property_id}_"

                f"{uuid.uuid4().hex}"

                f"{extension}"

            )


            file_path = os.path.join(

                MEDIA_DIR,

                unique_name

            )


            with open(

                file_path,

                "wb"

            ) as file:

                file.write(

                    photo.getbuffer()

                )


            save_property_media(

                property_id=property_id,

                media_type="image",

                file_path=file_path

            )


            photo_count += 1


    # ========================================================
    # SAVE VIDEO
    # ========================================================

    video_saved = False


    if video:

        extension = os.path.splitext(

            video.name

        )[1].lower()


        unique_name = (

            f"{property_id}_"

            f"{uuid.uuid4().hex}"

            f"{extension}"

        )


        file_path = os.path.join(

            MEDIA_DIR,

            unique_name

        )


        with open(

            file_path,

            "wb"

        ) as file:

            file.write(

                video.getbuffer()

            )


        save_property_media(

            property_id=property_id,

            media_type="video",

            file_path=file_path

        )


        video_saved = True


    # ========================================================
    # SUCCESS
    # ========================================================

    st.success(

        "🎉 Property submitted successfully!"

    )


    st.info(

        f"""
        Property ID: {property_id}

        Status: Pending Verification

        Photos Uploaded: {photo_count}

        Video Uploaded: {"Yes" if video_saved else "No"}

        Your property will appear publicly after verification.
        """

    )


# ============================================================
# BACK BUTTON
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)


if st.button(

    "⬅️ Back to Property Search",

    use_container_width=True

):

    st.switch_page(

        "pages/02_Property_Search.py"

    )


# ============================================================
# FOOTER
# ============================================================

footer()
