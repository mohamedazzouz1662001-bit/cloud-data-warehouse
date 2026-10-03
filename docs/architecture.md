# Architecture Overview

This project provides a starter architecture for a cloud data warehouse integrated with a production database.

## Components

- Operational Database: PostgreSQL
- ETL/ELT layer: Python scripts and orchestration tools
- Data Warehouse: cloud analytics layer
- Reporting: BI and dashboards

## Flow

1. Application writes data to the operational database
2. ETL jobs extract data from the database
3. Data is cleaned and transformed
4. Data is loaded into the warehouse
5. Analysts query the warehouse for reporting

## Best Practices

- Use environment variables for secrets
- Separate dev, staging, and production
- Encrypt data at rest and in transit
- Enable backups and monitoring
- Use incremental ETL processing
