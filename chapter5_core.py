import numpy as np
import pandas as pd
import os

# Load book numbers for verification
def load_book_numbers():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'book_numbers.csv')
    return pd.read_csv(data_path).set_index('Metric')

BOOK_DATA = load_book_numbers()

def calculate_swansons_law(cumulative_volume_gw, learning_rate=0.2, p0=100):
    """
    Figure 5.1: Swanson's Law Learning Curve
    P(V) = p0 * (V/V0) ^ (log2(1 - learning_rate))
    """
    # Simplified power law for learning curve
    price = p0 * (cumulative_volume_gw ** (np.log2(1 - learning_rate)))
    return price

def calculate_protocol_dividend(price, mcp_unlock_factor):
    """
    Figure 5.1: The Protocol Dividend
    Effective Value = Price + (Price * mcp_unlock_factor)
    """
    effective_value = price * (1 + mcp_unlock_factor)
    return effective_value

def calculate_sovereignty_recovery_factor(grid_resilience_mcp, grid_resilience_legacy, dependency_pv):
    """
    Section 5.5.1: Sovereignty Recovery Factor (R_MCP)
    R_MCP = (Resilience_MCP / Resilience_Legacy) * (1 - D_PV)
    """
    r_mcp = (grid_resilience_mcp / grid_resilience_legacy) * (1 - dependency_pv)
    return r_mcp

def calculate_sovereignty_metric(t, d_total, protocol_command, alpha=1.2):
    """
    Section 5.6: The Polynomial of Dependency
    S(t) = (1 - D_total) + alpha * Protocol_Command(t)
    """
    s_t = (1 - d_total) + alpha * protocol_command
    return s_t

def get_dependency_manifold(dependency_range, protocol_command_range):
    """
    Generates data for 3D Dependency Manifold
    """
    D, P = np.meshgrid(dependency_range, protocol_command_range)
    alpha = BOOK_DATA.loc['Alpha Sovereignty', 'Value']
    S = (1 - D) + alpha * P
    return D, P, S

def calculate_asp_sovereign_unlock(base_capacity, asp_factor):
    """
    Section 5.7: ASP Sovereign Silicon Calculator
    """
    sovereign_capacity = base_capacity * asp_factor
    return sovereign_capacity

def calculate_silicon_boomerang_dividend(import_value_bn, boomerang_factor):
    """
    Section 5.3: Silicon Boomerang Dividend
    """
    dividend = import_value_bn * boomerang_factor
    return dividend
