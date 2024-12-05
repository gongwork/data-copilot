-- Generated on: 2024-12-04 19:35:10
-- Dataset: stocks

-- Original Excel sheet: market_cap
CREATE TABLE IF NOT EXISTS market_cap (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    marketcap REAL  -- Original column: marketcap,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original Excel sheet: p_e_ratio
CREATE TABLE IF NOT EXISTS p_e_ratio (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    pe_ratio_ttm REAL  -- Original column: pe_ratio_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original Excel sheet: dividend_yield
CREATE TABLE IF NOT EXISTS dividend_yield (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    dividend_yield_ttm REAL  -- Original column: dividend_yield_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original Excel sheet: earnings
CREATE TABLE IF NOT EXISTS earnings (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    earnings_ttm REAL  -- Original column: earnings_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original Excel sheet: country_region
CREATE TABLE IF NOT EXISTS country_region (
    country TEXT  -- Original column: country,
    region TEXT  -- Original column: region,
    sub_region TEXT  -- Original column: sub_region
);

-- Original Excel sheet: revenue
CREATE TABLE IF NOT EXISTS revenue (
    rank INTEGER  -- Original column: Rank,
    name TEXT  -- Original column: Name,
    symbol TEXT  -- Original column: Symbol,
    revenue_ttm INTEGER  -- Original column: revenue_ttm,
    price_gbp REAL  -- Original column: price (GBP),
    country TEXT  -- Original column: country
);

-- Original Excel sheet: bus_term
CREATE TABLE IF NOT EXISTS bus_term (
    business_term TEXT  -- Original column: business_term,
    business_description TEXT  -- Original column: business_description,
    related_tables REAL  -- Original column: related_tables,
    related_columns REAL  -- Original column: related_columns
);
