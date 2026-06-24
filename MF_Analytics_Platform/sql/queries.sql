-- =====================================================
-- QUERY 1
-- Top 5 Funds by AUM
-- =====================================================

SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- QUERY 2
-- Average NAV Per Month
-- =====================================================

SELECT
strftime('%Y-%m', nav_date) AS Month,
ROUND(AVG(nav),2) AS Average_NAV
FROM fact_nav
GROUP BY Month
ORDER BY Month;


-- =====================================================
-- QUERY 3
-- Total Transactions by State
-- =====================================================

SELECT
state,
COUNT(*) AS Total_Transactions
FROM fact_transactions
GROUP BY state
ORDER BY Total_Transactions DESC;


-- =====================================================
-- QUERY 4
-- Funds with Expense Ratio less than 1%
-- =====================================================

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- QUERY 5
-- Average 3-Year Return
-- =====================================================

SELECT
ROUND(AVG(return_3yr_pct),2) AS Average_3Y_Return
FROM fact_performance;


-- =====================================================
-- QUERY 6
-- Highest Sharpe Ratio
-- =====================================================

SELECT
amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- =====================================================
-- QUERY 7
-- Total Investment by Transaction Type
-- =====================================================

SELECT
transaction_type,
SUM(amount_inr) AS Total_Investment
FROM fact_transactions
GROUP BY transaction_type;


-- =====================================================
-- QUERY 8
-- Average Transaction Amount by State
-- =====================================================

SELECT
state,
ROUND(AVG(amount_inr),2) AS Average_Amount
FROM fact_transactions
GROUP BY state
ORDER BY Average_Amount DESC;


-- =====================================================
-- QUERY 9
-- Top 10 Performing Funds (5-Year Return)
-- =====================================================

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- =====================================================
-- QUERY 10
-- Number of Schemes per Fund House
-- =====================================================

SELECT
fund_house,
COUNT(*) AS Total_Schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY Total_Schemes DESC;