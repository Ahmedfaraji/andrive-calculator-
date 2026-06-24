import streamlit as st

st.set_page_config(page_title="حاسبة أندرايف", layout="centered")
st.title("🚕 حاسبة فاتورة أندرايف")

price = st.number_input("الأجرة د.م", min_value=10.0, value=70.0, step=1.0)
commission_rate = st.slider("نسبة عمولة أندرايف %", 5, 25, 10.9)

commission = price * (commission_rate / 100)
vat = commission * 0.20
total_paid = commission + vat
driver_income = price - total_paid

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.metric("الأجرة الكاملة", f"{price} د.م")
    st.metric("عمولة أندرايف", f"{round(commission, 2)} د.م")
with col2:
    st.metric("ضريبة VAT 20%", f"{round(vat, 2)} د.م")
    st.metric("💰 دخل السائق", f"{round(driver_income, 2)} د.م")

st.success(f"السائق غادي يشد {round(driver_income, 2)} درهم صافية")
