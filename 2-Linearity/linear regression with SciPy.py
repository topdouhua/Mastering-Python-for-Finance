
""" Linear regression with SciPy """
from scipy import stats

stock_returns = [0.065, 0.0265, -0.0593, -0.001, 0.0346]
mkt_returns = [0.055, -0.09, -0.041, 0.045, 0.022]

beta, alpha, r_value, p_value, std_err = \
    stats.linregress(stock_returns, mkt_returns)
print ('beta = ', beta)
print ('alpha = ',alpha)
print ('r_value + ', alpha)
print ('p_value = ', p_value)
print ('std_errr = ', std_err )

""" Calculating the SML """
rf = 0.05
mrisk_prem = 0.085
risk_prem = mrisk_prem * beta
print ("Risk premium:", risk_prem)

expected_stock_return = rf + risk_prem
print ("Expected stock return:", expected_stock_return)
