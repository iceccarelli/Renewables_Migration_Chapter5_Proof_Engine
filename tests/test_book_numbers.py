import pytest
import pandas as pd
import os
import sys
import numpy as np

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chapter5_core import (
    calculate_swansons_law, 
    calculate_sovereignty_metric, 
    calculate_sovereignty_recovery_factor,
    BOOK_DATA
)

def test_sovereignty_metric_2026():
    """Verify the 28% independence claim for 2026 (Section 5.6)"""
    d_total = 0.96 # High dependency
    protocol_command = 0.2 # Low command
    alpha = BOOK_DATA.loc['Alpha Sovereignty', 'Value']
    s_2026 = calculate_sovereignty_metric(2026, d_total, protocol_command, alpha)
    # 1 - 0.96 + 1.2 * 0.2 = 0.04 + 0.24 = 0.28
    assert abs(s_2026 - 0.28) < 1e-5
    print("\n[PASS] 2026 Sovereignty Metric (28%) verified.")

def test_sovereignty_metric_2030():
    """Verify the 75% independence claim for 2030 (Section 5.6)"""
    d_total = 0.96 # Still high dependency
    protocol_command = 0.5916666666666667 # High command
    alpha = BOOK_DATA.loc['Alpha Sovereignty', 'Value']
    s_2030 = calculate_sovereignty_metric(2030, d_total, protocol_command, alpha)
    # 1 - 0.96 + 1.2 * 0.591666 = 0.04 + 0.71 = 0.75
    assert abs(s_2030 - 0.75) < 1e-5
    print("\n[PASS] 2030 Sovereignty Metric (75%) verified.")

def test_book_numbers_integrity():
    """Verify hardcoded numbers match book values in data/book_numbers.csv"""
    assert BOOK_DATA.loc['Polysilicon Control China', 'Value'] == 96
    assert BOOK_DATA.loc['Wafer Control China', 'Value'] == 98
    assert BOOK_DATA.loc['Silicon Import Dep', 'Value'] == 96
    assert BOOK_DATA.loc['Silicon Protocol Offset', 'Value'] == 45
    print("\n[PASS] Book numbers integrity verified.")

def test_sovereignty_recovery_factor():
    """Verify Section 5.5.1 logic"""
    res_mcp = 4.5
    res_legacy = 1.0
    dep_pv = 0.8
    r_mcp = calculate_sovereignty_recovery_factor(res_mcp, res_legacy, dep_pv)
    # (4.5 / 1.0) * (1 - 0.8) = 4.5 * 0.2 = 0.9
    assert abs(r_mcp - 0.9) < 1e-5
    print("\n[PASS] Sovereignty Recovery Factor logic verified.")

if __name__ == "__main__":
    pytest.main([__file__])
