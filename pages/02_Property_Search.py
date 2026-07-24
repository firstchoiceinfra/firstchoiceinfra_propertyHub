import streamlit as st

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)

from core.Database import (
    get_properties,
    get_custom_areas,
    add_property_view
)


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 02 — PROPERTY SEARCH
# ============================================================

st.set_page_config(
    page_title="Property Search | FirstChoice Property Hub",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM UI
# ============================================================

load_premium_ui()


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
# HERO
# ============================================================

hero(
    "🔎 Discover Your Perfect Property",
    "Search homes, plots, land, commercial spaces and upcoming projects across locations."
)


# ============================================================
# SEARCH SECTION
# ============================================================

section(
    "🔍 Smart Property Search",
    "Use multiple filters to find the property that matches your requirement."
)


# ============================================================
# SEARCH FILTERS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    purpose = st.selectbox(

        "🎯 Looking For",

        [
            "All",
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


with col2:

    property_type = st.selectbox(

        "🏠 Property Type",

        [
            "All",
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
            "Industrial Unit"
        ]

    )


with col3:

    city = st.selectbox(

        "🏙️ City",

        [
            "All",
            "Nagpur",
            "Mumbai",
            "Pune",
            "Nashik",
            "Aurangabad",
            "Indore",
            "Bhopal",
            "Ahmedabad"
        ]

    )


# ============================================================
# AREA SEARCH
# ============================================================

st.markdown("### 📍 Location & Area")


col1, col2 = st.columns(2)


with col1:

    village_town = st.text_input(

        "🏘️ Village / Town",

        placeholder=
        "Enter village or town name"

    )


with col2:

    area_name = st.text_input(

        "📍 Area / Locality",

        placeholder=
        "Enter area, locality, colony or layout"

    )


# ============================================================
# PRICE FILTER
# ============================================================

st.markdown("### 💰 Budget")


col1, col2 = st.columns(2)


with col1:

    min_price = st.number_input(

        "Minimum Budget (₹)",

        min_value=0,

        value=0,

        step=100000

    )


with col2:

    max_price = st.number_input(

        "Maximum Budget (₹)",

        min_value=0,

        value=0,

        step=100000

    )


# ============================================================
# PROPERTY AREA
# ============================================================

st.markdown("### 📐 Property Size")


col1, col2 = st.columns(2)


with col1:

    min_area = st.number_input(

        "Minimum Area (Sq.Ft.)",

        min_value=0,

        value=0

    )


with col2:

    max_area = st.number_input(

        "Maximum Area (Sq.Ft.)",

        min_value=0,

        value=0

    )


# ============================================================
# SEARCH BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)


search_button = st.button(

    "🔎 SEARCH PROPERTIES",

    use_container_width=True

)


# ============================================================
# SEARCH RESULTS
# ============================================================

if search_button:

    selected_city = (

        None

        if city == "All"

        else city

    )


    selected_type = (

        None

        if property_type == "All"

        else property_type

    )


    selected_purpose = (

        None

        if purpose == "All"

        else purpose

    )


    # --------------------------------------------------------
    # GET DATABASE RESULTS
    # --------------------------------------------------------

    properties = get_properties(

        city=selected_city,

        area_name=area_name.strip()

        if area_name.strip()

        else None,

        property_type=selected_type,

        purpose=selected_purpose

    )


    # --------------------------------------------------------
    # ADDITIONAL FILTERING
    # --------------------------------------------------------

    filtered_properties = []


    for property_item in properties:

        # -----------------------------------------------
        # Village / Town Filter
        # -----------------------------------------------

        if village_town.strip():

            if village_town.lower() not in (

                property_item["village_town"]

                or ""

            ).lower():

                continue


        # -----------------------------------------------
        # Minimum Price
        # -----------------------------------------------

        if min_price > 0:

            if (

                property_item["price"]

                or 0

            ) < min_price:

                continue


        # -----------------------------------------------
        # Maximum Price
        # -----------------------------------------------

        if max_price > 0:

            if (

                property_item["price"]

                or 0

            ) > max_price:

                continue


        # -----------------------------------------------
        # Minimum Area
        # -----------------------------------------------

        if min_area > 0:

            if (

                property_item["property_area"]

                or 0

            ) < min_area:

                continue


        # -----------------------------------------------
        # Maximum Area
        # -----------------------------------------------

        if max_area > 0:

            if (

                property_item["property_area"]

                or 0

            ) > max_area:

                continue


        filtered_properties.append(

            property_item

        )


    # ========================================================
    # RESULTS COUNT
    # ========================================================

    st.markdown(
        f"""
        <div class="fc-section">

        <h2>
        🏡 {len(filtered_properties)}
        Properties Found
        </h2>

        <p>
        Matching properties available on FirstChoice Property Hub.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # NO RESULTS
    # ========================================================

    if not filtered_properties:

        st.warning(

            "No matching properties found."

        )

        st.info(

            "Try changing your location, budget or property type."

        )


    # ========================================================
    # PROPERTY RESULTS
    # ========================================================

    for property_item in filtered_properties:

        property_id = property_item["id"]


        title = (

            property_item["property_type"]

            or "Property"

        )


        location = (

            f"{property_item['city']}, "

            f"{property_item['village_town']}, "

            f"{property_item['area_name']}"

        )


        price = (

            property_item["price"]

            or 0

        )


        views = (

            property_item["views"]

            or 0

        )


        st.markdown(

            f"""
            <div class="property-card">

            <div class="property-info">

            <div class="property-title">

            🏡 {title}

            </div>

            <div class="property-location">

            📍 {location}

            </div>

            <div class="property-price">

            ₹ {price:,.0f}

            </div>

            <hr>

            <p>

            🎯 <b>Purpose:</b>
            {property_item["purpose"]}

            </p>

            <p>

            🏠 <b>Category:</b>
            {property_item["category"]}

            </p>

            <p>

            📐 <b>Area:</b>
            {property_item["property_area"] or 0}
            Sq.Ft.

            </p>

            <p>

            🛏️ <b>BHK:</b>
            {property_item["bhk"] or "N/A"}

            </p>

            <p>

            🏗️ <b>Status:</b>
            {property_item["project_status"] or "N/A"}

            </p>

            <p>

            👀 <b>Views:</b>
            {views}

            </p>

            </div>

            </div>
            """,

            unsafe_allow_html=True

        )


        # ====================================================
        # PROPERTY ACTIONS
        # ====================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            if st.button(

                "👁️ View Details",

                key=f"view_{property_id}",

                use_container_width=True

            ):

                add_property_view(

                    property_id

                )

                st.session_state[

                    "selected_property_id"

                ] = property_id

                st.rerun()


        with col2:

            if st.button(

                "📍 Location",

                key=f"location_{property_id}",

                use_container_width=True

            ):

                location_url = (

                    property_item[

                        "google_location"

                    ]

                )


                if location_url:

                    st.markdown(

                        f"[📍 Open Google Maps]({location_url})"

                    )

                else:

                    st.info(

                        "Location not available."

                    )


        with col3:

            if st.button(

                "📞 Contact",

                key=f"contact_{property_id}",

                use_container_width=True

            ):

                st.info(

                    f"Contact: "

                    f"{property_item['contact_name']}"

                )

                st.write(

                    f"📱 "

                    f"{property_item['contact_mobile']}"

                )


# ============================================================
# PROPERTY DETAILS
# ============================================================

if "selected_property_id" in st.session_state:

    selected_id = (

        st.session_state[

            "selected_property_id"

        ]

    )


    section(

        "🏡 Property Details",

        "Detailed information about the selected property."

    )


    selected_properties = get_properties()


    selected_property = None


    for item in selected_properties:

        if item["id"] == selected_id:

            selected_property = item

            break


    if selected_property:

        st.markdown(

            f"""
            <div class="fc-card">

            <h2>

            🏡 {selected_property["property_type"]}

            </h2>

            <p>

            📍

            {selected_property["country"]},

            {selected_property["state"]},

            {selected_property["city"]},

            {selected_property["village_town"]},

            {selected_property["area_name"]}

            </p>

            <p>

            💰

            <b>
            ₹ {selected_property["price"] or 0:,.0f}
            </b>

            </p>

            <p>

            📐

            {selected_property["property_area"] or 0}

            Sq.Ft.

            </p>

            <p>

            📝

            {selected_property["description"] or "No description available."}

            </p>

            </div>
            """,

            unsafe_allow_html=True

        )


        # ----------------------------------------------------
        # GOOGLE LOCATION
        # ----------------------------------------------------

        if selected_property["google_location"]:

            st.markdown(

                f"""
                ### 📍 Property Location

                [Open Property Location on Google Maps](
                {selected_property["google_location"]}
                )
                """

            )


        # ----------------------------------------------------
        # CLOSE DETAILS
        # ----------------------------------------------------

        if st.button(

            "⬅️ Back to Search Results",

            use_container_width=True

        ):

            del st.session_state[

                "selected_property_id"

            ]

            st.rerun()


# ============================================================
# QUICK NAVIGATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

section(
    "🚀 Quick Navigation",
    "Continue exploring FirstChoice Property Hub."
)


col1, col2, col3 = st.columns(3)


with col1:

    if st.button(

        "🏠 Home",

        use_container_width=True

    ):

        st.switch_page(

            "app.py"

        )


with col2:

    if st.button(

        "🏡 Post Property",

        use_container_width=True

    ):

        st.switch_page(

            "pages/03_Post_Property.py"

        )


with col3:

    if st.button(

        "🔐 Login / Register",

        use_container_width=True

    ):

        st.switch_page(

            "pages/01_Login_Register.py"

        )


# ============================================================
# FOOTER
# ============================================================

footer()
