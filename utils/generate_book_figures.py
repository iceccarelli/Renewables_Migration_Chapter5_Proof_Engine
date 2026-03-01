import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chapter5_core import calculate_swansons_law, calculate_protocol_dividend, get_dependency_manifold

def generate_figure_5_1():
    """Reproduces Figure 5.1: The Learning Curve Trap"""
    vol_range = np.logspace(0, 3, 100)
    prices = calculate_swansons_law(vol_range, learning_rate=0.2)
    effective_values = calculate_protocol_dividend(prices, mcp_unlock_factor=0.4)
    
    plt.figure(figsize=(10, 6))
    plt.loglog(vol_range, prices, 'r-', label='Physical Module Price (Swanson\'s Law)')
    plt.loglog(vol_range, effective_values, 'b-', label='Effective Value (Module + MCP Services)')
    plt.fill_between(vol_range, prices, effective_values, color='gray', alpha=0.2, label='The Protocol Dividend')
    
    plt.xlabel('Cumulative Global Volume (GW)')
    plt.ylabel('Module Price (€/Wp)')
    plt.title('Figure 5.1: The Learning Curve Trap')
    plt.legend()
    plt.grid(True, which="both", ls="-")
    
    plt.savefig('plots/learning_curve_vs_dependency.png')
    print("[PASS] Figure 5.1 generated.")

def generate_figure_5_2():
    """Reproduces Figure 5.2: The Dependency Manifold (3D view)"""
    dep_range = np.linspace(0.5, 1.0, 50)
    prot_range = np.linspace(0.0, 1.0, 50)
    D, P, S = get_dependency_manifold(dep_range, prot_range)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface
    surf = ax.plot_surface(D, P, S, cmap='viridis', alpha=0.8)
    
    ax.set_xlabel('Dependency (D)')
    ax.set_ylabel('Protocol Command (P)')
    ax.set_zlabel('Sovereignty (S)')
    ax.set_title('Figure 5.2: The Dependency Manifold')
    
    plt.savefig('plots/dependency_manifold_3d.png')
    print("[PASS] Figure 5.2 generated.")

def generate_silicon_sovereignty():
    """Generates Silicon Sovereignty Projection"""
    years = np.array([2026, 2027, 2028, 2029, 2030])
    s_vals = np.array([0.28, 0.35, 0.48, 0.62, 0.75])
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, s_vals, 'g-o', label='Sovereignty Metric (S)')
    plt.axhline(y=0.75, color='r', linestyle='--', label='2030 Sovereign Target')
    
    plt.xlabel('Year')
    plt.ylabel('Sovereignty Index')
    plt.title('Silicon Sovereignty Projection (Section 5.6)')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('plots/silicon_sovereignty_projection.png')
    print("[PASS] Silicon sovereignty projection generated.")

if __name__ == "__main__":
    os.makedirs('plots', exist_ok=True)
    generate_figure_5_1()
    generate_figure_5_2()
    generate_silicon_sovereignty()
