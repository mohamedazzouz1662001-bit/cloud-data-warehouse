# Cloud Data Warehouse Starter

This repository contains a starter setup for a large-scale cloud data warehouse connected to a database service.

## Project Structure

```text
.
├── README.md
├── docker-compose.yml
├── .env.example
├── infrastructure/
│   ├── terraform/
│   └── scripts/
├── app/
│   ├── db/
│   ├── warehouse/
│   ├── etl/
│   └── api/
├── docs/
│   └── architecture.md
└── .github/
    └── workflows/
```

## Included

- Cloud database connection example
- Data warehouse configuration
- ETL pipeline starter
- Infrastructure scripts
- Deployment examples

## Quick Start

1. Copy `.env.example` to `.env`
2. Configure database credentials
3. Run docker-compose
4. Start the ETL pipeline

## Example .env

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=appdb
DB_USER=postgres
DB_PASSWORD=postgres
WAREHOUSE_HOST=warehouse.example.com
WAREHOUSE_PORT=5432
WAREHOUSE_NAME=analytics
WAREHOUSE_USER=warehouse_user
WAREHOUSE_PASSWORD=your_secret
```

## Main Technologies

- PostgreSQL
- dbt
- Docker
- Terraform
- Python

## Notes

This repository is a starting template and should be adapted to your specific cloud provider and architecture.
