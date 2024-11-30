-- Generated on: 2024-11-23 19:01:27
-- Dataset: company_rank

-- Original CSV file: Companies_ranked_by_Dividend_Yield.csv
CREATE TABLE IF NOT EXISTS companies_ranked_by_dividend_yield (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    dividend_yield_ttm REAL  -- Original column: dividend_yield_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original CSV file: Companies_ranked_by_Earnings.csv
CREATE TABLE IF NOT EXISTS companies_ranked_by_earnings (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    earnings_ttm REAL  -- Original column: earnings_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original CSV file: Companies_ranked_by_Market_Cap.csv
CREATE TABLE IF NOT EXISTS companies_ranked_by_market_cap (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    marketcap REAL  -- Original column: marketcap,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original CSV file: Companies_ranked_by_P_E_ratio.csv
CREATE TABLE IF NOT EXISTS companies_ranked_by_p_e_ratio (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    pe_ratio_ttm REAL  -- Original column: pe_ratio_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original CSV file: Companies_ranked_by_Revenue.csv
CREATE TABLE IF NOT EXISTS companies_ranked_by_revenue (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    revenue_ttm INTEGER  -- Original column: revenue_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original CSV file: country_region.csv
CREATE TABLE IF NOT EXISTS country_region (
    country TEXT  -- Original column: country,
    region TEXT  -- Original column: region,
    sub_region TEXT  -- Original column: sub_region
);
