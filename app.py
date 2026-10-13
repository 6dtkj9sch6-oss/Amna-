
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Textile Quality Studio",
    page_icon="🧵",
    layout="wide",
)

# Textile color palette
NAVY = "#17324D"
TEAL = "#168C8C"
MINT = "#DDF3EC"
GOLD = "#E8B04A"
CREAM = "#F7F5EF"
INK = "#243746"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {CREAM};
        color: {INK};
    }}
    [data-testid="stSidebar"] {{
        background: {NAVY};
    }}
    [data-testid="stSidebar"] * {{
        color: white;
    }}
    .hero {{
        padding: 25px;
        border-radius: 16px;
        background: linear-gradient(120deg, {NAVY}, {TEAL});
        color: white;
        margin-bottom: 20px;
    }}
    .hero h1 {{
        color: white;
    }}
    .metric-card {{
        background: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #E3E8E6;
    }}
    .metric-value {{
        color: {NAVY};
        font-size: 28px;
        font-weight: bold;
    }}
    .section-title {{
        color: {NAVY};
        font-size: 22px;
        font-weight: bold;
        margin: 12px 0;
    }}
    .stButton button {{
        background: {TEAL};
        color: white;
        border-radius: 8px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Demonstration fabric data
if "fabric_data" not in st.session_state:
    st.session_state.fabric_data = pd.DataFrame([
        {
            "Sample": "FAB-001",
            "Cotton %": 100,
            "Polyester %": 0,
            "Yarn Count": 30,
            "GSM": 120,
            "Strength (N)": 350,
            "Defect": "None",
            "Quality": "Good",
        },
        {
            "Sample": "FAB-002",
            "Cotton %": 80,
            "Polyester %": 20,
            "Yarn Count": 30,
            "GSM": 125,
            "Strength (N)": 340,
            "Defect": "None",
            "Quality": "Good",
        },
        {
            "Sample": "FAB-003",
            "Cotton %": 60,
            "Polyester %": 40,
            "Yarn Count": 28,
            "GSM": 130,
            "Strength (N)": 320,
            "Defect": "Slight stain",
            "Quality": "Poor",
        },
        {
            "Sample": "FAB-004",
            "Cotton %": 50,
            "Polyester %": 50,
            "Yarn Count": 28,
            "GSM": 135,
            "Strength (N)": 310,
            "Defect": "None",
            "Quality": "Good",
        },
        {
            "Sample": "FAB-005",
            "Cotton %": 100,
            "Polyester %": 0,
            "Yarn Count": 40,
            "GSM": 110,
            "Strength (N)": 280,
            "Defect": "Hole",
            "Quality": "Poor",
        },
        {
            "Sample": "FAB-006",
            "Cotton %": 70,
            "Polyester %": 30,
            "Yarn Count": 30,
            "GSM": 128,
            "Strength (N)": 335,
            "Defect": "None",
            "Quality": "Good",
        },
        {
            "Sample": "FAB-007",
            "Cotton %": 60,
            "Polyester %": 40,
            "Yarn Count": 30,
            "GSM": 132,
            "Strength (N)": 300,
            "Defect": "Broken yarn",
            "Quality": "Poor",
        },
        {
            "Sample": "FAB-008",
            "Cotton %": 90,
            "Polyester %": 10,
            "Yarn Count": 32,
            "GSM": 118,
            "Strength (N)": 345,
            "Defect": "None",
            "Quality": "Good",
        },
    ])

# Sidebar navigation
with st.sidebar:
    st.markdown("## 🧵 Textile Studio")
    st.caption("Fabric Quality Dashboard")

    page = st.radio(
        "Navigate",
        [
            "Dashboard",
            "Fabric Samples",
            "Color Palette",
            "About",
        ],
    )

    st.markdown("---")
    st.markdown("### Filter Samples")

    quality_filter = st.multiselect(
        "Select quality",
        ["Good", "Poor"],
        default=["Good", "Poor"],
    )

df = st.session_state.fabric_data.copy()

filtered = df[
    df["Quality"].isin(quality_filter)
]

# Dashboard
if page == "Dashboard":
    st.markdown(
        f"""
        <div class="hero">
            <h1>Textile Quality Studio</h1>
            <p>
                Explore fabric composition, testing results,
                and quality trends in one simple workspace.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    total = len(filtered)
    good = (filtered["Quality"] == "Good").sum()
    poor = (filtered["Quality"] == "Poor").sum()

    average_gsm = (
        filtered["GSM"].mean()
        if total > 0 else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        ("Samples Shown", total),
        ("Good Quality", good),
        ("Poor Quality", poor),
        (
            "Average GSM",
            f"{average_gsm:.1f}" if total else "—",
        ),
    ]

    for col, (label, value) in zip(
        [col1, col2, col3, col4], metrics
    ):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div>{label}</div>
                    <div class="metric-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("")
    left, right = st.columns([1.3, 1])

    with left:
        st.markdown(
            '<div class="section-title">'
            'Fabric Strength by Sample</div>',
            unsafe_allow_html=True,
        )

        if total:
            fig = px.bar(
                filtered,
                x="Sample",
                y="Strength (N)",
                color="Quality",
                text="Strength (N)",
                color_discrete_map={
                    "Good": TEAL,
                    "Poor": GOLD,
                },
                template="plotly_white",
            )

            fig.update_layout(
                margin=dict(l=10, r=10, t=15, b=10)
            )

            st.plotly_chart(
                fig, use_container_width=True
            )
        else:
            st.info("Select a quality type in the sidebar.")

    with right:
        st.markdown(
            '<div class="section-title">'
            'Quality Breakdown</div>',
            unsafe_allow_html=True,
        )

        if total:
            counts = (
                filtered["Quality"]
                .value_counts()
                .rename_axis("Quality")
                .reset_index(name="Samples")
            )

            fig2 = px.pie(
                counts,
                names="Quality",
                values="Samples",
                hole=0.55,
                color="Quality",
                color_discrete_map={
                    "Good": TEAL,
                    "Poor": GOLD,
                },
                template="plotly_white",
            )

            st.plotly_chart(
                fig2, use_container_width=True
            )
        else:
            st.info("No samples match the selected filter.")

    st.markdown(
        '<div class="section-title">Fabric Sample Records</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
    )

# Fabric samples page
elif page == "Fabric Samples":
    st.markdown(
        f"""
        <div class="hero">
            <h1>Fabric Samples</h1>
            <p>Review, edit, and export fabric test records.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    edited = st.data_editor(
        st.session_state.fabric_data,
        use_container_width=True,
        hide_index=True,
        num_rows="dynamic",
        key="fabric_editor",
        column_config={
            "Cotton %": st.column_config.NumberColumn(
                min_value=0, max_value=100, step=1
            ),
            "Polyester %": st.column_config.NumberColumn(
                min_value=0, max_value=100, step=1
            ),
            "Yarn Count": st.column_config.NumberColumn(
                min_value=1, step=1
            ),
            "GSM": st.column_config.NumberColumn(
                min_value=1, step=1
            ),
            "Strength (N)": st.column_config.NumberColumn(
                min_value=0, step=1
            ),
            "Quality": st.column_config.SelectboxColumn(
                options=["Good", "Poor"]
            ),
        },
    )

    if st.button("Save Table Changes"):
        st.session_state.fabric_data = edited.copy()
        st.success("Changes saved for this session.")

    st.download_button(
        label="Download CSV",
        data=edited.to_csv(index=False).encode("utf-8"),
        file_name="textile_fabric_samples.csv",
        mime="text/csv",
    )

    st.caption(
        "Reminder: Cotton % + Polyester % should usually equal 100%."
    )

# Color palette page
elif page == "Color Palette":
    st.markdown(
        f"""
        <div class="hero">
            <h1>Textile Color Palette</h1>
            <p>
                A professional color scheme inspired by
                fabrics, dyes, and natural fibers.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    palette = [
        ("Deep Navy", NAVY, "Headings and navigation"),
        ("Textile Teal", TEAL, "Buttons and charts"),
        ("Soft Mint", MINT, "Soft accent"),
        ("Warm Gold", GOLD, "Highlights"),
        ("Cotton Cream", CREAM, "Page background"),
        ("Ink", INK, "Body text"),
    ]

    cols = st.columns(3)

    for i, (name, color, purpose) in enumerate(palette):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div style="
                        background:{color};
                        height:50px;
                        border-radius:8px;">
                    </div>
                    <h4 style="color:{NAVY};">{name}</h4>
                    <code>{color}</code>
                    <p>{purpose}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# About page
else:
    st.markdown(
        f"""
        <div class="hero">
            <h1>About This Project</h1>
            <p>A beginner-friendly application for textile students.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("""
    ### Features
    - View fabric quality records.
    - Compare fabric strength and quality.
    - Edit and download sample data.
    - Explore the application's color palette.

    ### Textile Terms
    - **GSM:** Grams per square metre.
    - **Yarn Count:** A measure of yarn fineness.
    - **Strength (N):** Force measured in newtons.
    - **Defect:** An issue found in the fabric.

    **Note:** This application uses demonstration data.
    Replace it with verified production or laboratory data
    before making real quality decisions.
    """)
    
    st.caption("Built with Streamlit, pandas, and Plotly.")
