import streamlit as st
from datetime import datetime

# ============================================================
# PAGE 25 — PROPERTY COLLABORATION HUB
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Collaboration Hub | FirstChoice Property Hub",
    page_icon="💬",
    layout="wide"
)

# ============================================================
# PREMIUM MULTICOLOUR UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F5F7FF 0%,
        #FFF7ED 35%,
        #FDF4FF 70%,
        #ECFEFF 100%
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

.hero {
    padding: 52px;
    border-radius: 36px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1D4ED8,
        #7C3AED,
        #DB2777
    );

    box-shadow:
    0 24px 75px
    rgba(37,99,235,0.32);

    margin-bottom: 32px;
}

.hero h1 {
    font-size: 46px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
    line-height: 1.8;
}

.section {
    margin-top: 32px;
    margin-bottom: 22px;

    padding: 30px 34px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4F46E5,
        #9333EA,
        #EC4899
    );

    box-shadow:
    0 14px 40px
    rgba(79,70,229,0.22);
}

.section h2 {
    margin: 0;
    font-size: 29px;
    font-weight: 900;
}

.card {
    padding: 28px;
    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    margin-bottom: 20px;
}

.ai-card {
    padding: 32px;
    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #4C1D95,
        #7C3AED,
        #C026D3
    );

    box-shadow:
    0 18px 55px
    rgba(124,58,237,0.25);
}

.success-card {
    padding: 32px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );
}

.info-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0369A1,
        #0284C7,
        #06B6D4
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
💬 Property Collaboration Hub
</h1>

<p>
A property-specific communication and task management
workspace for buyers, sellers, builders and agents.
</p>

<p>
💬 Messages • 📌 Enquiries • ✅ Tasks • 📅 Follow-ups • 👥 Collaboration
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AI INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Communication Centre
</h2>

<p>
Keep every important property conversation and follow-up
connected to the property instead of losing information
across different messaging apps.
</p>

<p>
The platform can eventually connect communication,
property documents, site visits, negotiations and
transaction milestones in one unified workspace.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY PROFILE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Collaboration Property
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    property_name = st.text_input(
        "🏠 Property Name",
        value="My Property"
    )


with c2:

    property_id = st.text_input(
        "🆔 Property ID",
        value="FC-PROPERTY-001"
    )


c3, c4 = st.columns(2)


with c3:

    current_user = st.text_input(
        "👤 Your Name"
    )


with c4:

    user_role = st.selectbox(
        "👥 Your Role",
        [
            "Buyer",
            "Seller",
            "Builder",
            "Agent",
            "Executive",
            "Legal Consultant",
            "Loan Consultant"
        ]
    )


# ============================================================
# QUICK CONTACT
# ============================================================

st.markdown("""
<div class="section">

<h2>
📞 Property Contact
</h2>

</div>
""", unsafe_allow_html=True)


q1, q2, q3 = st.columns(3)


with q1:

    contact_name = st.text_input(
        "👤 Contact Person"
    )


with q2:

    contact_role = st.selectbox(
        "💼 Contact Role",
        [
            "Buyer",
            "Seller",
            "Builder",
            "Agent",
            "Executive",
            "Lawyer",
            "Loan Consultant"
        ]
    )


with q3:

    contact_mobile = st.text_input(
        "📱 Contact Mobile"
    )


# ============================================================
# MESSAGE CENTRE
# ============================================================

st.markdown("""
<div class="section">

<h2>
💬 Property Message Centre
</h2>

</div>
""", unsafe_allow_html=True)


if "property_messages" not in st.session_state:

    st.session_state.property_messages = []


message_type = st.selectbox(
    "📌 Message Type",
    [
        "General Enquiry",
        "Property Information",
        "Site Visit",
        "Price Discussion",
        "Document Request",
        "Loan Discussion",
        "Legal Query",
        "Booking Query"
    ]
)


message_text = st.text_area(
    "💬 Write Message",
    placeholder="Type your property-related message..."
)


if st.button(
    "📨 SEND PROPERTY MESSAGE",
    use_container_width=True
):

    if not message_text:

        st.warning(
            "⚠️ Please enter a message."
        )

    else:

        st.session_state.property_messages.append({

            "Time":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            ),

            "From":
            current_user,

            "Role":
            user_role,

            "Type":
            message_type,

            "Message":
            message_text

        })

        st.success(
            "✅ Message added to Property Communication Centre."
        )


# ============================================================
# MESSAGE HISTORY
# ============================================================

if st.session_state.property_messages:

    st.markdown("""
    <div class="section">

    <h2>
    🕒 Property Communication History
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.dataframe(
        st.session_state.property_messages,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "💬 No property communication history yet."
    )


# ============================================================
# TASK MANAGEMENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
✅ Property Transaction Task Board
</h2>

<p>
Create and track important tasks related to this property.
</p>

</div>
""", unsafe_allow_html=True)


if "property_tasks" not in st.session_state:

    st.session_state.property_tasks = []


t1, t2 = st.columns(2)


with t1:

    task_title = st.text_input(
        "📌 Task Name",
        placeholder="Example: Collect Sale Agreement"
    )


with t2:

    task_owner = st.text_input(
        "👤 Assigned To"
    )


t3, t4 = st.columns(2)


with t3:

    task_priority = st.selectbox(
        "🚦 Priority",
        [
            "Low",
            "Medium",
            "High",
            "Urgent"
        ]
    )


with t4:

    task_status = st.selectbox(
        "📊 Task Status",
        [
            "Pending",
            "In Progress",
            "Completed"
        ]
    )


if st.button(
    "➕ ADD PROPERTY TASK",
    use_container_width=True
):

    if not task_title:

        st.warning(
            "⚠️ Please enter a task name."
        )

    else:

        st.session_state.property_tasks.append({

            "Task":
            task_title,

            "Assigned To":
            task_owner,

            "Priority":
            task_priority,

            "Status":
            task_status,

            "Created":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        st.success(
            "✅ Task added successfully."
        )


# ============================================================
# TASK LIST
# ============================================================

if st.session_state.property_tasks:

    st.dataframe(
        st.session_state.property_tasks,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "📌 No tasks created yet."
    )


# ============================================================
# FOLLOW-UP REMINDER
# ============================================================

st.markdown("""
<div class="section">

<h2>
📅 Follow-Up Reminder
</h2>

</div>
""", unsafe_allow_html=True)


r1, r2 = st.columns(2)


with r1:

    reminder_title = st.text_input(
        "🔔 Reminder Title"
    )


with r2:

    reminder_date = st.date_input(
        "📅 Follow-Up Date"
    )


reminder_notes = st.text_area(
    "📝 Reminder Notes"
)


if st.button(
    "🔔 CREATE FOLLOW-UP REMINDER",
    use_container_width=True
):

    st.success(
        f"✅ Follow-up reminder created for {reminder_date}."
    )


# ============================================================
# COLLABORATION MEMBERS
# ============================================================

st.markdown("""
<div class="section">

<h2>
👥 Collaboration Members
</h2>

</div>
""", unsafe_allow_html=True)


members = st.multiselect(
    "Select people involved in this property transaction",
    [
        "Buyer",
        "Seller",
        "Builder",
        "Agent",
        "Sales Executive",
        "Legal Consultant",
        "Loan Consultant",
        "Property Manager",
        "Admin"
    ]
)


if members:

    st.markdown(
        f"""
        <div class="info-card">

        <h2>
        👥 Active Collaboration Team
        </h2>

        <p>
        {", ".join(members)}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ACTIVITY SUMMARY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Collaboration Activity
</h2>

</div>
""", unsafe_allow_html=True)


m1, m2, m3, m4 = st.columns(4)


with m1:

    st.metric(
        "💬 Messages",
        len(
            st.session_state.property_messages
        )
    )


with m2:

    st.metric(
        "✅ Tasks",
        len(
            st.session_state.property_tasks
        )
    )


with m3:

    completed_tasks = len(
        [
            x
            for x in st.session_state.property_tasks
            if x["Status"] == "Completed"
        ]
    )

    st.metric(
        "🎯 Completed",
        completed_tasks
    )


with m4:

    st.metric(
        "👥 Members",
        len(members)
    )


# ============================================================
# SMART COLLABORATION FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future Smart Collaboration Features
</h2>

<p>
The production version can integrate:
</p>

<p>
💬 Real-Time Chat
&nbsp; • &nbsp;
📞 Voice / Video Calls
&nbsp; • &nbsp;
📎 Document Sharing
&nbsp; • &nbsp;
🔔 Push Notifications
&nbsp; • &nbsp;
📅 Calendar Integration
&nbsp; • &nbsp;
🤖 AI Conversation Summary
&nbsp; • &nbsp;
🌐 Multi-Language Chat
</p>

<p>
AI can automatically summarise long property conversations,
extract important action items and create follow-up tasks.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NOTICE
# ============================================================

st.markdown("""
<div class="success-card">

<h2>
🏠 One Property — One Collaboration Space
</h2>

<p>
Keep property enquiries, communication, tasks and follow-ups
connected to the same property record.
</p>

</div>
""", unsafe_allow_html=True)
