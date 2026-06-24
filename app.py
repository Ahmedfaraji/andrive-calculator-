import streamlit as st
from datetime import date

st.set_page_config(page_title="حاسبة أندرايف برو", layout="centered")
st.title("🚕 حاسبة فاتورة أندرايف برو")

# ===== الإعدادات =====
col1, col2 = st.columns(2)
with col1:
    price = st.number_input("💵 الأجرة د.م", min_value=10.0, value=70.0, step=1.0)
    min_fare = st.number_input("📉 الميني/الحد الأدنى د.م", min_value=10.0, value=15.0, step=1.0)
with col2:
    commission_rate = st.slider("📊 نسبة عمولة أندرايف %", 5.0, 25.0, 10.9, step=0.1)
    trips_count = st.number_input("🔢 عدد الرحلات اليوم", min_value=1, value=3, step=1)

# ===== الحسابات =====
commission = price * (commission_rate / 100)
vat = commission * 0.20
total_paid = commission + vat
driver_income_trip = price - total_paid

# الميني: إلا الرباح قل من الميني، ناخدو الميني
driver_income_trip = max(driver_income_trip, min_fare)

# حساب اليوم كامل
daily_income = driver_income_trip * trips_count
daily_commission = commission * trips_count
daily_vat = vat * trips_count

st.divider()

# ===== عرض النتائج بحال inDrive =====
st.subheader("📊 إحصائيات الرحلة الواحدة")
col1, col2, col3 = st.columns(3)
col1.metric("الأجرة", f"{price} د.م")
col2.metric("العمولة + VAT", f"{round(total_paid, 2)} د.م")
col3.metric("💰 دخل السائق", f"{round(driver_income_trip, 2)} د.م")

st.divider()
st.subheader(f"📅 إحصائيات اليوم - {date.today()}")

col1, col2, col3 = st.columns(3)
col1.metric("عدد الطلبات", f"{trips_count}")
col2.metric("المجموع الصافي", f"{round(daily_income, 2)} د.م")
col3.metric("مصاريف المنصة", f"{round(daily_commission + daily_vat, 2)} د.م")

if driver_income_trip == min_fare:
    st.warning(f"⚠️ الرحلة وصلات للميني: {min_fare} د.م")
else:
    st.success(f"✅ السائق غادي يشد {round(driver_income_trip, 2)} درهم صافية فالرحلة")

st.info(f"🎯 الهدف اليومي: إلا درتي {trips_count} رحلات غادي تجمع {round(daily_income, 2)} درهم")
