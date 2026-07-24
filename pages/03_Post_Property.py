import streamlit as st
import json
import os
import uuid
from datetime import datetime

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 03 — POST PROPERTY
# ============================================================

st.set_page_config(
    page_title="Post Property | FirstChoice Infra Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CONFIGURATION
# ============================================================

DATA_FILE = "property_data.json"
AREA_FILE = "custom_areas.json"

MAX_IMAGE_SIZE_MB = 10
MAX_VIDEO_SIZE_MB = 100


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

.post-hero {

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

.post-hero h1 {

    font-size: 44px;

    font-weight: 900;

}

.post-hero p {

    font-size: 18px;

    line-height: 1.7;

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

    margin-top: 35px;

    margin-bottom: 25px;
}

/* FORM CARD */

.form-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 30px;

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

/* SUCCESS */

.success-card {

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
    0 20px 50px
    rgba(5,150,105,0.25);

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
# HELPER FUNCTIONS
# ============================================================

def load_json_file(file_path, default_value):

    if not os.path.exists(file_path):

        return default_value

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return default_value


def save_json_file(file_path, data):

    try:

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except Exception:

        return False


def file_size_mb(uploaded_file):

    if uploaded_file is None:

        return 0

    return uploaded_file.size / (
        1024 * 1024
    )


# ============================================================
# LOGIN CHECK
# ============================================================

# Temporary development login
# Production version will use OTP authentication.

is_logged_in = st.session_state.get(
    "logged_in",
    True
)

current_user = st.session_state.get(
    "user_email",
    "demo_user@firstchoiceinfra.com"
)


if not is_logged_in:

    st.warning(
        "Please login before posting a property."
    )

    st.stop()


# ============================================================
# LOAD DATA
# ============================================================

property_data = load_json_file(
    DATA_FILE,
    []
)

custom_areas = load_json_file(
    AREA_FILE,
    {}
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <h1>🏠 FirstChoice</h1>

    <p>Property Hub</p>

    <hr>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 📝 Post Property

    Add your property with complete
    location, pricing, media and
    contact information.
    """)

    st.markdown("""
    ### 📍 Location

    Country

    State

    City / Town

    Area / Locality
    """)

    st.markdown("""
    ### 🎥 Media

    Property Photos

    Property Video

    Nearby Location Video

    Google Location
    """)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="post-hero">

<h1>
🏠 Post Your Property
</h1>

<p>
List your property on FirstChoice Infra Property Hub
and reach buyers, tenants, investors and businesses.
</p>

<p>
📸 Photos • 🎥 Video • 📍 Google Location • 🛡️ Verified Listing
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# BASIC PROPERTY INFORMATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🏠 Property Basic Information
</h2>

<p>
Tell us about the property you want to list.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


b1, b2, b3 = st.columns(3)


with b1:

    listing_purpose = st.selectbox(

        "Property Purpose",

        [
            "Buy",
            "Rent",
            "Sell",
            "Lease",
            "Investment"
        ]

    )


with b2:

    property_category = st.selectbox(

        "Property Category",

        [
            "Residential",
            "Commercial",
            "Land & Plot",
            "New Project"
        ]

    )


with b3:

    property_type = st.selectbox(

        "Property Type",

        [
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
            "Industrial Property",
            "Other"
        ]

    )


property_title = st.text_input(

    "Property Title",

    placeholder=
    "Example: Premium Residential Plot Near Nagpur Highway"

)


property_description = st.text_area(

    "Property Description",

    placeholder=
    "Describe the property, location advantages, nearby facilities and other important information.",

    height=180

)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOCATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📍 Property Location
</h2>

<p>
Provide the exact property location.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


l1, l2 = st.columns(2)


with l1:

    country = st.selectbox(

        "Country",

        [
            "India",
            "Other"
        ]

    )


with l2:

    if country == "Other":

        state = st.text_input(
            "State / Province"
        )

    else:

        state = st.selectbox(

            "State",

            [
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


l3, l4 = st.columns(2)


with l3:

    city = st.text_input(

        "City / Town / Village",

        placeholder=
        "Example: Nagpur"

    )


with l4:

    existing_areas = custom_areas.get(

        f"{country}_{state}_{city}",

        []

    )


    area_options = [

        "Select Area",

        "Others"

    ] + sorted(

        list(
            set(existing_areas)
        )

    )


    selected_area = st.selectbox(

        "Area / Locality",

        area_options

    )


# ============================================================
# OTHERS — CUSTOM AREA
# ============================================================

custom_area = ""


if selected_area == "Others":

    custom_area = st.text_input(

        "Enter Your Area / Locality Name",

        placeholder=
        "Example: Shankar Nagar Extension"

    )


elif selected_area != "Select Area":

    custom_area = selected_area


st.info(
    "If your area is not available, select 'Others'. "
    "Your new area will be saved and may appear automatically "
    "for future property listings in the same location."
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PRICE & PROPERTY SIZE
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
💰 Price & Property Size
</h2>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


p1, p2, p3 = st.columns(3)


with p1:

    price = st.number_input(

        "Property Price (₹)",

        min_value=0,

        value=0,

        step=100000

    )


with p2:

    property_area = st.number_input(

        "Property Area",

        min_value=0.0,

        value=0.0,

        step=100.0

    )


with p3:

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


p4, p5, p6 = st.columns(3)


with p4:

    bedrooms = st.selectbox(

        "Bedrooms",

        [
            "Not Applicable",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5+ BHK"
        ]

    )


with p5:

    property_status = st.selectbox(

        "Property Status",

        [
            "Ready to Move",
            "Under Construction",
            "Upcoming Project",
            "New Launch",
            "Ready to Build",
            "Other"
        ]

    )


with p6:

    furnishing = st.selectbox(

        "Furnishing",

        [
            "Not Applicable",
            "Fully Furnished",
            "Semi Furnished",
            "Unfurnished"
        ]

    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# AMENITIES
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
✨ Property Amenities
</h2>

</div>
""", unsafe_allow_html=True)


amenities = st.multiselect(

    "Select Available Amenities",

    [
        "Parking",
        "Lift",
        "Security",
        "CCTV",
        "Swimming Pool",
        "Gym",
        "Club House",
        "Garden",
        "Children Play Area",
        "Power Backup",
        "Water Supply",
        "Road Connectivity",
        "Gated Community",
        "Electricity",
        "Internet Connectivity"
    ]

)


# ============================================================
# GOOGLE MAP LOCATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🗺️ Google Location
</h2>

<p>
Add the exact location of the property.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


g1, g2 = st.columns(2)


with g1:

    latitude = st.text_input(

        "Latitude",

        placeholder=
        "Example: 21.1458"

    )


with g2:

    longitude = st.text_input(

        "Longitude",

        placeholder=
        "Example: 79.0882"

    )


google_maps_url = st.text_input(

    "Google Maps Link",

    placeholder=
    "Paste Google Maps property location link here"

)


st.info(
    "Future version will include an interactive Google Maps picker."
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY MEDIA
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📸 Property Photos & Videos
</h2>

<p>
Add high-quality media to increase property visibility.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


property_images = st.file_uploader(

    "📸 Upload Property Photos",

    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ],

    accept_multiple_files=True

)


property_video = st.file_uploader(

    "🎥 Upload Property Video",

    type=[
        "mp4",
        "mov",
        "avi",
        "webm"
    ],

    accept_multiple_files=False

)


nearby_video = st.file_uploader(

    "🎥 Upload Nearby Location Video",

    type=[
        "mp4",
        "mov",
        "avi",
        "webm"
    ],

    accept_multiple_files=False

)


st.info(
    "Nearby location video can show roads, schools, hospitals, "
    "markets, transport and other important surroundings."
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MEDIA VALIDATION
# ============================================================

media_error = False


if property_images:

    for image in property_images:

        if file_size_mb(image) > MAX_IMAGE_SIZE_MB:

            st.error(
                f"Image '{image.name}' exceeds "
                f"{MAX_IMAGE_SIZE_MB} MB limit."
            )

            media_error = True


if property_video:

    if file_size_mb(property_video) > MAX_VIDEO_SIZE_MB:

        st.error(

            f"Property video exceeds "
            f"{MAX_VIDEO_SIZE_MB} MB limit."

        )

        media_error = True


if nearby_video:

    if file_size_mb(nearby_video) > MAX_VIDEO_SIZE_MB:

        st.error(

            f"Nearby location video exceeds "
            f"{MAX_VIDEO_SIZE_MB} MB limit."

        )

        media_error = True


# ============================================================
# CONTACT INFORMATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📞 Contact Information
</h2>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


c1, c2 = st.columns(2)


with c1:

    contact_name = st.text_input(

        "Contact Person Name",

        placeholder=
        "Enter owner / agent / builder name"

    )


with c2:

    contact_mobile = st.text_input(

        "Mobile Number",

        placeholder=
        "Enter 10-digit mobile number"

    )


contact_email = st.text_input(

    "Email Address",

    placeholder=
    "Enter contact email address"

)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY VERIFICATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🛡️ Property Verification
</h2>

</div>
""", unsafe_allow_html=True)


verification_type = st.selectbox(

    "Property Ownership / Verification Status",

    [
        "Not Verified",
        "Owner Documents Available",
        "Agent Documents Available",
        "Builder Documents Available",
        "Verification Requested"
    ]

)


# ============================================================
# TERMS AND CONDITIONS
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📜 Listing Terms & Conditions
</h2>

</div>
""", unsafe_allow_html=True)


terms_accepted = st.checkbox(

    "I confirm that the information provided in this property listing is accurate and I have the legal right or authorization to list this property on FirstChoice Infra Property Hub."

)


# ============================================================
# POST PROPERTY
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)


submit_property = st.button(

    "🚀 POST PROPERTY",

    use_container_width=True,

    type="primary"

)


# ============================================================
# SUBMIT LOGIC
# ============================================================

if submit_property:

    validation_errors = []


    if not property_title.strip():

        validation_errors.append(
            "Property title is required."
        )


    if not property_description.strip():

        validation_errors.append(
            "Property description is required."
        )


    if not city.strip():

        validation_errors.append(
            "City / Town / Village is required."
        )


    if not custom_area.strip():

        validation_errors.append(
            "Area / Locality is required."
        )


    if price <= 0:

        validation_errors.append(
            "Please enter a valid property price."
        )


    if property_area <= 0:

        validation_errors.append(
            "Please enter a valid property area."
        )


    if not contact_name.strip():

        validation_errors.append(
            "Contact person name is required."
        )


    if not contact_mobile.strip():

        validation_errors.append(
            "Mobile number is required."
        )


    if len(
        contact_mobile.strip()
    ) != 10:

        validation_errors.append(
            "Please enter a valid 10-digit mobile number."
        )


    if not terms_accepted:

        validation_errors.append(
            "You must accept the property listing terms and conditions."
        )


    if media_error:

        validation_errors.append(
            "Please fix media upload errors before posting."
        )


    # ========================================================
    # SHOW VALIDATION ERRORS
    # ========================================================

    if validation_errors:

        st.error(
            "Please fix the following issues:"
        )

        for error in validation_errors:

            st.warning(
                f"• {error}"
            )


    else:

        # ====================================================
        # SAVE CUSTOM AREA
        # ====================================================

        location_key = (
            f"{country}_{state}_{city}"
        )


        if location_key not in custom_areas:

            custom_areas[
                location_key
            ] = []


        if custom_area not in custom_areas[
            location_key
        ]:

            custom_areas[
                location_key
            ].append(
                custom_area
            )


        save_json_file(

            AREA_FILE,

            custom_areas

        )


        # ====================================================
        # GENERATE PROPERTY ID
        # ====================================================

        property_id = (

            "FC-"

            +

            datetime.now().strftime(
                "%Y%m%d"
            )

            +

            "-"

            +

            uuid.uuid4().hex[:8].upper()

        )


        # ====================================================
        # PROPERTY RECORD
        # ====================================================

        new_property = {

            "property_id":
            property_id,

            "created_at":
            datetime.now().isoformat(),

            "posted_by":
            current_user,

            "listing_purpose":
            listing_purpose,

            "property_category":
            property_category,

            "property_type":
            property_type,

            "property_title":
            property_title,

            "property_description":
            property_description,

            "country":
            country,

            "state":
            state,

            "city":
            city,

            "area":
            custom_area,

            "price":
            price,

            "property_area":
            property_area,

            "area_unit":
            area_unit,

            "bedrooms":
            bedrooms,

            "property_status":
            property_status,

            "furnishing":
            furnishing,

            "amenities":
            amenities,

            "latitude":
            latitude,

            "longitude":
            longitude,

            "google_maps_url":
            google_maps_url,

            "verification_type":
            verification_type,

            "contact_name":
            contact_name,

            "contact_mobile":
            contact_mobile,

            "contact_email":
            contact_email,

            "has_property_images":
            bool(property_images),

            "property_image_count":
            len(property_images)
            if property_images
            else 0,

            "has_property_video":
            bool(property_video),

            "has_nearby_video":
            bool(nearby_video),

            "status":
            "Pending Approval"

        }


        # ====================================================
        # SAVE PROPERTY
        # ====================================================

        property_data.append(
            new_property
        )


        save_success = save_json_file(

            DATA_FILE,

            property_data

        )


        if save_success:

            st.markdown(
                f"""
                <div class="success-card">

                <h2>
                🎉 Property Submitted Successfully
                </h2>

                <p>
                Your property has been submitted
                for verification and approval.
                </p>

                <h3>
                Property ID: {property_id}
                </h3>

                <p>
                Status: Pending Approval
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


            st.balloons()


        else:

            st.error(

                "Unable to save property data. "
                "Please try again."

            )


# ============================================================
# BACK BUTTON
# ============================================================

st.markdown(
    "<br><br>",
    unsafe_allow_html=True
)


if st.button(

    "⬅️ BACK TO PROPERTY SEARCH",

    use_container_width=True

):

    st.switch_page(

        "pages/02_Property_Search.py"

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
