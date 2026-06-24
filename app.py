import streamlit as st

st.set_page_config(page_title="حاسبة أندرايف", layout="centered")
st.title("🚕 حاسبة فاتورة أندرايف")

price = st.number_input("الأجرة د.م", min_value=10.0, value=70.0, step=1.0)
عمولة_النسبة = st.slider("نسبة عمولة أندرايف %", 5, 25, 10.9)

عمولة_أندرايف = price * (عمولة_النسبة / 100)
VAT = عمولة_أندرايف * 0.20
إجمالي_المدفوع = عمولة_أندرايف + VAT
دخل_السائق = price - إجمالي_المدفوع

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.metric("الأجرة الكاملة", f"{price} د.م")
    st.metric("عمولة أندرايف", f"{round(عمولة_أندرايف, 2)} د.م")
with col2:
    st.metric("ضريبة VAT 20%", f"{round(VAT, 2)} د.م")
    st.metric("💰 دخل السائق", f"{round(دخل_السائق, 2)} د.م")

st.success(f"السائق غادي يشد {round(دخل_السائق, 2)} درهم صافية")
