import streamlit as st


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# COMMON NAVIGATION SYSTEM
# BACK | HOME | PAGE MENU
# ============================================================


APP_PAGES = {
    "🏠 Home / Dashboard": "01_admin_master_control.py",
    "🏡 Property Details": "03_property_details.py",
    "📢 Communication Center": "11_smart_communication_notification_center.py",
    "💰 Finance Calculator": "13_finance_calculator.py",
    "📊 Market Insights": "16_market_insights.py",
    "🤖 AI Property Intelligence": "17_AI_Property_Intelligence.py",
    "🎥 Virtual Property Tour": "19_virtual_property_tour.py",
    "📈 Investment Intelligence": "20_investment_intelligence.py",
    "⚖️ Legal Due Diligence": "22_property_legal_due_diligence.py",
    "🤝 Property Deal Room": "23_property_deal_room.py",
    "📁 Property Document Vault": "24_property_document_vault.py",
    "💬 Property Collaboration Hub": "25_property_collaboration_hub.py",
    "📅 Property Site Visit": "26_property_site_visit_manager.py",
    "⚖️ Property Comparison": "27_property_comparison_center.py",
    "💳 Investment Finance Center": "28_property_investment_finance_center.py",
    "🛡️ Legal Verification": "30_property_legal_verification.py",
    "👤 User Profile": "6_User_Profile.py",
    "🏡 My Listings": "7_My_Listings.py",
    "⭐ Saved Properties": "8_Saved_Properties.py",
    "🔍 Property Search": "9_Property_Search.py",
}


HOME_PAGE = "01_admin_master_control.py"


# ============================================================
# SET CURRENT PAGE
# ============================================================

def set_current_page(current_page):

    # Initialize navigation history
    if "navigation_history" not in st.session_state:
        st.session_state.navigation_history = []

    previous_page = st.session_state.get(
        "current_page",
        HOME_PAGE
    )

    # Avoid duplicate page entries
    if previous_page != current_page:

        if not st.session_state.navigation_history:

            st.session_state.navigation_history.append(
                previous_page
            )

        elif (
            st.session_state.navigation_history[-1]
            != previous_page
        ):

            st.session_state.navigation_history.append(
                previous_page
            )

    st.session_state.current_page = current_page


# ============================================================
# GO BACK
# ============================================================

def go_back():

    history = st.session_state.get(
        "navigation_history",
        []
    )

    if history:

        previous_page = history.pop()

        st.session_state.navigation_history = history

        st.session_state.current_page = previous_page

        try:

            st.switch_page(
                previous_page
            )

        except Exception:

            st.switch_page(
                HOME_PAGE
            )

    else:

        st.switch_page(
            HOME_PAGE
        )


# ============================================================
# COMMON NAVIGATION UI
# ============================================================

def show_navigation():

    st.markdown(
        """
        <style>

        .nav-title {
            padding: 14px 20px;
            border-radius: 16px;
            margin-bottom: 12px;

            background:
            linear-gradient(
                135deg,
                #071952,
                #2563EB,
                #7C3AED
            );

            color: white;

            font-size: 18px;
            font-weight: 800;

            text-align: center;

            box-shadow:
            0 8px 25px
            rgba(37,99,235,0.20);
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="nav-title">
        🏠 FirstChoice Infra Property Hub
        </div>
        """,
        unsafe_allow_html=True
    )


    back_col, home_col, menu_col = st.columns(
        [1, 1, 2]
    )


    # ========================================================
    # BACK
    # ========================================================

    with back_col:

        if st.button(
            "⬅️ BACK",
            use_container_width=True,
            key="common_back_button"
        ):

            go_back()


    # ========================================================
    # HOME
    # ========================================================

    with home_col:

        if st.button(
            "🏠 HOME",
            use_container_width=True,
            key="common_home_button"
        ):

            st.session_state.navigation_history = []

            st.session_state.current_page = HOME_PAGE

            st.switch_page(
                HOME_PAGE
            )


    # ========================================================
    # PAGE MENU
    # ========================================================

    with menu_col:

        selected_page = st.selectbox(

            "📋 PAGE MENU",

            list(APP_PAGES.keys()),

            index=None,

            placeholder="Select a page...",

            key="common_page_menu"

        )


        if selected_page:

            selected_file = APP_PAGES[
                selected_page
            ]

            current_page = st.session_state.get(
                "current_page",
                ""
            )

            if selected_file != current_page:

                st.switch_page(
                    selected_file
                )
