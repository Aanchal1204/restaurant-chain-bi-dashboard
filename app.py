import streamlit as st

st.set_page_config(
    page_title="Restaurant Chain BI Dashboard",
    layout="wide"
)

st.title("🍽 Restaurant Chain Business Intelligence Dashboard")

st.write("""
This project was built for a restaurant chain operating across 10 outlets in 5 cities.

The dashboard helps management monitor:
- Revenue performance
- Outlet rankings
- Menu performance
- Inventory wastage
- Growth trends
""")

st.header("Executive Performance Overview")

st.image("executive_overview.png")

st.markdown("""
### Key KPIs
- Annual Revenue: ₹12M+
- Gross Margin %
- Month-over-Month Growth
- Customer Ratings
""")

st.header("Outlet & Menu Performance")

st.image("outlet_performance.png")

st.markdown("""
### Insights
- Best performing outlets identified
- High revenue menu items highlighted
- Underperforming locations tracked
""")

st.header("Inventory & Wastage Monitoring")

st.image("inventory_wastage.png")

st.markdown("""
### Insights
- Inventory wastage tracked
- Stock health alerts implemented
- Actionable recommendations generated
""")

st.success("Built using Power BI, DAX, Power Query and Excel")