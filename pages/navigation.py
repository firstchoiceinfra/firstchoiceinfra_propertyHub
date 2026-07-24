import streamlit as st


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# COMMON NAVIGATION SYSTEM
# ============================================================


# ============================================================
# PAGE LIST
# ============================================================

PAGES = {

    "🏠 Home": "app.py",

    "🔎 Property Search": "pages/02_Property_Search.py",

    "🏡 Buy Property": "pages/03_Buy_Property.py",

    "🔑 Rent Property": "pages/04_Rent_Property.py",

    "🏢 Commercial Property": "pages/05_Commercial_Property.py",

    "🌳 Land & Plot": "pages/06_Land_And_Plot.py",

    "🚀 New Projects": "pages/07_New_Projects.py",

    "📢 Post Property": "pages/08_Post_Property.py",

    "❤️ My Watchlist": "pages/09_Watchlist.py",

    "🛡️ Verified Properties": "pages/10_Verified_Properties.py",

    "📈 Investment & Finance": "pages/28_Investment_Finance_Center.py",

    "⚖️ Property Comparison": "pages/29_Property_Comparison.py",

    "🏦 Loan & EMI Comparison": "pages/30_Loan_EMI_Comparison.py",

    "👤 User Dashboard": "pages/50_User_Dashboard.py",

    "💼 Partner Portal": "pages/51_Partner_Portal.py",

    "👑 Admin Master Control": "pages/99_Admin_Master_Control.py"

}


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div style="
                padding:20px;
                border-radius:20px;
                background:linear-gradient(
                    135deg,
                    #071952,
                    #2563EB,
                    #7C3AED,
                    #EC4899
                );
                color:white;
                margin-bottom:20px;
            ">

            <h2>
            🏠 FirstChoice
            </h2>

            <p>
            Property Hub
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            "## 📚 Main Navigation"
        )


        selected_page = st.radio(

            "Select Page",

            list(PAGES.keys()),

            key="main_navigation"

        )


        if st.button(
            "🚀 OPEN SELECTED PAGE",
            use_container_width=True
        ):

            page_path = PAGES[selected_page]

            try:

                st.switch_page(page_path)

            except Exception:

                st.error(
                    f"Page not found: {page_path}"
                )


        st.divider()


        st.markdown(
            """
            ### 🏠 Property

            Buy • Sell • Rent • Invest
            """
        )


        st.markdown(
            """
            ### 🛡️ Trust

            Verified Properties
            Verified Owners
            Secure Enquiry
            """
        )


        st.divider()


        st.caption(
            "FirstChoice Infra Property Hub"
        )


# ============================================================
# BOTTOM NAVIGATION
# ============================================================

def render_bottom_navigation(
    current_page
):

    page_names = list(
        PAGES.keys()
    )


    if current_page not in PAGES:

        return


    current_index = page_names.index(
        current_page
    )


    st.divider()


    st.markdown(
        "## 🧭 Page Navigation"
    )


    col1, col2, col3 = st.columns(3)


    # ========================================================
    # PREVIOUS
    # ========================================================

    with col1:

        if current_index > 0:

            previous_page = page_names[
                current_index - 1
            ]


            if st.button(
                "⬅️ Previous Page",
                use_container_width=True
            ):

                st.switch_page(
                    PAGES[
                        previous_page
                    ]
                )


    # ========================================================
    # HOME
    # ========================================================

    with col2:

        if st.button(
            "🏠 Back to Main Menu",
            use_container_width=True
        ):

            st.switch_page(
                "app.py"
            )


    # ========================================================
    # NEXT
    # ========================================================

    with col3:

        if current_index < len(
            page_names
        ) - 1:

            next_page = page_names[
                current_index + 1
            ]


            if st.button(
                "➡️ Next Page",
                use_container_width=True
            ):

                st.switch_page(
                    PAGES[
                        next_page
                    ]
                )


    st.markdown(
        """
        <div style="
            text-align:center;
            padding:15px;
            margin-top:15px;
            border-radius:15px;
            background:#EEF2FF;
        ">

        🏠 FirstChoice Property Hub
        <br>
        <small>
        All modules are connected through the main navigation.
        </small>

        </div>
        """,
        unsafe_allow_html=True
    )
