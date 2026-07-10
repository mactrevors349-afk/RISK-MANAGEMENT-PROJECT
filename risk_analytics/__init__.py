"""
Risk Analytics Package

A comprehensive suite of quantitative risk analysis tools for financial portfolios,
including volatility analysis, Value at Risk (VaR), Conditional Value at Risk (CVaR),
and portfolio performance metrics.

Modules:
    portfolio_risk_analysis: Portfolio VaR, CVaR, and volatility analysis tools

Author: RISK MANAGEMENT PROJECT
Version: 1.0.0
"""

from .portfolio_risk_analysis import (
    generate_portfolio_data,
    calculate_portfolio_metrics,
    visualize_portfolio_analysis,
    main
)

__version__ = "1.0.0"
__author__ = "RISK MANAGEMENT PROJECT"

__all__ = [
    'generate_portfolio_data',
    'calculate_portfolio_metrics',
    'visualize_portfolio_analysis',
    'main'
]
