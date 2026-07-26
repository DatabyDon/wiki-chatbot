# Data Standards

## Naming Conventions
- Table names should be lowercase and use underscores: `customer_orders`
- Column names should be descriptive and avoid abbreviations.
- Date columns should always be named with a `_date` suffix: `created_date`

## Data Quality
- All datasets must have a primary key.
- Null values must be documented and intentional.
- Data pipelines must include row count validation at each step.

## Tools
- SQL is the standard query language across all teams.
- Snowflake is the primary data warehouse.
- Tableau is the standard visualization tool.