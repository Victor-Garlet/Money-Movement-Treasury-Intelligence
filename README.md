# Money Movement & Treasury Intelligence

An analytical project focused on payment reliability, open finance infrastructure, treasury, liquidity and funding risk in financial services.

The goal is to build a practical portfolio project for Senior Data Analyst, Product Analyst, Treasury Analytics and Analytics Engineering roles in European fintechs and banks.

## Project Idea

Financial institutions such as fintechs, digital banks and payment companies depend on reliable money movement infrastructure and disciplined treasury management.

Small operational issues can become material at scale:

- API failures or degraded open banking availability;
- delayed or failed payment flows;
- additional support and operational costs;
- higher liquidity buffers;
- interest rate exposure;
- funding cost changes;
- FX and settlement risk.

This project aims to turn public financial infrastructure data into useful analytical models, metrics and dashboards that explain how money movement reliability and treasury conditions affect business decisions.

## Initial Scope

The first version of the project will focus on three analytical modules:

1. **Payment Reliability**
   - Open Banking API availability;
   - successful and failed API calls;
   - provider-level reliability metrics;
   - estimated customer and operational impact.

2. **Treasury & Funding Risk**
   - yield curves;
   - interest rate changes;
   - liquidity buffer analysis;
   - simple interest rate shock scenarios.

3. **Instant Payments & Open Finance**
   - Pix and Open Finance adoption;
   - payment infrastructure growth;
   - comparison between Brazil, the UK and Europe where public data allows it.

## Planned Data Sources

- UK Open Banking API Performance;
- ECB Data Portal;
- Bank of England yield curve data;
- Banco Central do Brasil Pix statistics;
- Open Finance Brasil public data;
- FRED, BIS, Companies House, GLEIF and OpenSanctions in later phases.

## Planned Stack

- Python;
- SQL;
- DuckDB;
- dbt;
- Jupyter;
- Git and GitHub;
- PostgreSQL;
- Streamlit, Evidence.dev, Superset or Power BI;
- GitHub Actions;
- Docker.

## Current Status

Project setup is in progress.

The first milestones are:

- create the local development structure;
- learn and document the Git/GitHub workflow;
- build the first API extraction script;
- load the first public dataset into DuckDB;
- write the first SQL metrics for payment reliability.

## Repository Philosophy

This is a learning-first project. The repository will not start as a polished final product.

Each phase should add one practical capability:

- one new data source;
- one new technical skill;
- one new financial concept;
- one new business question;
- one clear analytical output.

## License

This project is licensed under the MIT License.
