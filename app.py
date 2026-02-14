import streamlit as st
import pickle
import pandas as pd

# ================= LOAD MODELS =================
with open("kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("product_similarity.pkl", "rb") as f:
    product_similarity_df = pickle.load(f)

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.big-font {
    font-size: 20px;
    font-weight: 600;
}
.subtle {
    color: #6c757d;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("🛒 Shopper Spectrum")
st.sidebar.markdown("**E-Commerce Analytics Dashboard**")
st.sidebar.markdown("---")
st.sidebar.info(
    "This application provides:\n"
    "- 📦 Product Recommendations\n"
    "- 👥 Customer Segmentation\n\n"
    "Built using ML & Streamlit."
)

# ================= MAIN HEADER =================
st.markdown(
    "<h1 style='text-align: center;'>🛒 Shopper Spectrum</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;' class='subtle'>Customer Segmentation & Product Recommendation System</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ================= TABS =================
tab1, tab2 = st.tabs(["🎯 Product Recommendation", "👥 Customer Segmentation"])

# ================= TAB 1: PRODUCT RECOMMENDATION =================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎯 Product Recommendation Engine")
    st.markdown(
        "<p class='subtle'>Enter a product name to discover similar items frequently bought together.</p>",
        unsafe_allow_html=True
    )

    product_name = st.text_input("🔍 Product Name")

    if st.button("✨ Get Recommendations"):
        if product_name in product_similarity_df.index:
            similarity_scores = (
                product_similarity_df[product_name]
                .sort_values(ascending=False)[1:6]
            )

            st.success("✅ Recommended Products")
            for i, prod in enumerate(similarity_scores.index, start=1):
                st.markdown(f"**{i}.** {prod}")
        else:
            st.error("❌ Product not found. Please check spelling or try another product.")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 2: CUSTOMER SEGMENTATION =================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 👥 Customer Segmentation (RFM Analysis)")
    st.markdown(
        "<p class='subtle'>Predict customer type using Recency, Frequency, and Monetary values.</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input("📅 Recency (days)", min_value=0)

    with col2:
        frequency = st.number_input("🛍️ Frequency", min_value=0)

    with col3:
        monetary = st.number_input("💰 Monetary Value", min_value=0.0)

    if st.button("🔮 Predict Customer Segment"):
        input_scaled = scaler.transform([[recency, frequency, monetary]])
        cluster = kmeans.predict(input_scaled)[0]

        segment_map = {
            0: ("Regular Customer", "🙂 Consistent but moderate buyer"),
            1: ("High-Value Customer", "🌟 Loyal & high spender"),
            2: ("Occasional Customer", "🛒 Infrequent purchases"),
            3: ("At-Risk Customer", "⚠️ Needs retention strategy")
        }

        segment, description = segment_map.get(cluster, ("Unknown", ""))

        st.success(f"**Segment:** {segment}")
        st.info(description)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px;' class='subtle'>"
    "Built with ❤️ using Python, Machine Learning & Streamlit"
    "</p>",
    unsafe_allow_html=True
)
