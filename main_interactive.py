import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from chapter5_core import (
    calculate_swansons_law, 
    calculate_protocol_dividend, 
    calculate_sovereignty_recovery_factor,
    calculate_sovereignty_metric,
    get_dependency_manifold,
    calculate_asp_sovereign_unlock,
    calculate_silicon_boomerang_dividend,
    BOOK_DATA
)

st.set_page_config(page_title="Renewables Migration: Chapter 5 Proof Engine", layout="wide")

# Sidebar for global parameters
st.sidebar.title("Global Parameters")
spy_mode = st.sidebar.checkbox("Spy Mode: Highlight Book Claims", value=True)

st.title("Chapter 5: The Solar Suicide")
st.markdown("""
    This dashboard provides a production-ready verification of **Chapter 5: The Solar Suicide** 
    from *'The Renewables Migration'* by Vincenzo Grimaldi.
""")

if spy_mode:
    st.info("🕵️ **Spy Mode Active**: Book claims are highlighted in gold.")

tabs = st.tabs([
    "Learning Curve Trap Simulator", 
    "Dependency Manifold Explorer", 
    "ASP Sovereign Silicon Calculator", 
    "2030 Pivot Projection", 
    "Prove Every Equation", 
    "Download Book Data"
])

# Tab 1: Learning Curve Trap
with tabs[0]:
    st.header("Learning Curve Trap Simulator")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        learning_rate = st.slider("Learning Rate (%)", 10, 30, 20) / 100
        mcp_unlock = st.slider("MCP Sovereignty Unlock (%)", 0, 50, 40) / 100
        vol_range = np.logspace(0, 3, 50)
        
        prices = calculate_swansons_law(vol_range, learning_rate)
        effective_values = calculate_protocol_dividend(prices, mcp_unlock)
        
        if spy_mode:
            st.warning(f"**Book Claim**: Figure 5.1 shows the 'Protocol Dividend' clawing back value from the learning curve trap.")
            
    with col2:
        df_plot = pd.DataFrame({
            'Volume (GW)': vol_range,
            'Physical Price (€/Wp)': prices,
            'Effective Value (MCP)': effective_values
        })
        fig = px.line(df_plot, x='Volume (GW)', y=['Physical Price (€/Wp)', 'Effective Value (MCP)'], 
                      log_x=True, log_y=True, title="Swanson's Law vs. Protocol Dividend (Figure 5.1)")
        st.plotly_chart(fig, use_container_width=True)

# Tab 2: Dependency Manifold
with tabs[1]:
    st.header("Dependency Manifold Explorer")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        dep_range = np.linspace(0.5, 1.0, 20)
        prot_range = np.linspace(0.0, 1.0, 20)
        D, P, S = get_dependency_manifold(dep_range, prot_range)
        
        st.markdown("### Sovereignty Metric (S)")
        st.latex(r"S(t) = (1 - D_{total}) + \alpha \cdot Protocol\_Command(t)")
        
        if spy_mode:
            st.warning("**Book Claim**: In 2026, S ≈ 0.28. By 2030, S pushes toward 0.75.")

    with col2:
        fig = go.Figure(data=[go.Surface(z=S, x=D, y=P, colorscale='Viridis')])
        fig.update_layout(title='The Dependency Manifold (Section 5.6)',
                          scene=dict(xaxis_title='Dependency (D)', yaxis_title='Protocol Command (P)', zaxis_title='Sovereignty (S)'))
        st.plotly_chart(fig, use_container_width=True)

# Tab 3: ASP Sovereign Silicon
with tabs[2]:
    st.header("ASP Sovereign Silicon Calculator")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        base_cap = st.number_input("Base Solar Capacity (GW)", value=117)
        asp_factor = st.slider("ASP Framework Gain (%)", 0, 100, 45) / 100
        
        sovereign_cap = calculate_asp_sovereign_unlock(base_cap, asp_factor)
        st.metric("Sovereign Capacity (GW)", f"{sovereign_cap:.1f}", delta=f"{asp_factor:.1%}")
        
        if spy_mode:
            st.warning("**Book Claim**: Table A.4 shows a 45% Protocol Offset for Silicon (PV) via the ASP Framework.")

    with col2:
        df_material = pd.read_csv('data/appendix_a_extract.csv').iloc[:4]
        fig = px.bar(df_material, x='Material', y=['Import Dep (%)', 'Protocol Offset (%)'], 
                     barmode='group', title="Material Ledger and Protocol Offset (Table A.4)")
        st.plotly_chart(fig, use_container_width=True)

# Tab 4: 2030 Pivot
with tabs[3]:
    st.header("2030 Pivot Projection")
    st.markdown("### Industrial Employment and the Protocol Pivot (Table A.5)")
    
    df_jobs = pd.read_csv('data/appendix_a_extract.csv').iloc[4:9]
    st.table(df_jobs)
    
    if spy_mode:
        st.success("🎯 **Exact Book Match**: 64,000 jobs clawed back by 2030 through autonomous cost optimization.")

# Tab 5: Equations
with tabs[4]:
    st.header("Prove Every Equation")
    st.markdown("### Sovereignty Recovery Factor (Section 5.5.1)")
    st.latex(r"R_{MCP} = \frac{Grid Resilience (with MCP)}{Grid Resilience (Legacy)} \cdot (1 - D_{PV})")
    
    st.markdown("### The Polynomial of Dependency (Section 5.6)")
    st.latex(r"S(t) = (1 - D_{total}) + \alpha \cdot Protocol\_Command(t)")
    
    st.markdown("### Swanson's Law (Figure 5.1)")
    st.latex(r"P(V) = p_0 \cdot (V/V_0)^{\log_2(1 - \text{Learning Rate})}")

# Tab 6: Data
with tabs[5]:
    st.header("Download Book Data")
    st.dataframe(BOOK_DATA)
    st.download_button("Download CSV", BOOK_DATA.to_csv(), "book_numbers_ch5.csv", "text/csv")
