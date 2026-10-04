# Cloud Data Warehouse Starter

هذا المشروع هو قالب عملي لبدء بناء مخزن بيانات سحابي/محلي متكامل مع قاعدة بيانات تشغيلية، ETL، ونظام تحميل بيانات إلى مستودع تحليلي.

## المكونات

- PostgreSQL: قاعدة البيانات التشغيلية
- Python: ETL وملفات معالجة البيانات
- Docker Compose: تشغيل بيئة التطوير محلياً
- SQL Scripts: إنشاء الجداول والبيانات التجريبية
- Warehouse Loader: مثال لتحميل البيانات إلى طبقة التحليل

## هيكل المشروع

```text
cloud-data-warehouse/
├── .gitignore
├── .env.example
├── docker-compose.yml
├── README.md
├── app/
│   ├── db/
│   │   ├── connect.py
│   │   └── schema.sql
│   ├── etl/
│   │   └── extract_sales.py
│   └── warehouse/
│       └── load_to_warehouse.py
└── docs/
    └── architecture.md
```

## المتطلبات

- Docker
- Docker Compose
- Python 3.11+
- pip

## التشغيل السريع

1. انسخ ملف `.env.example` إلى `.env`
2. شغّل قاعدة البيانات:

```bash
docker-compose up -d
```

3. تثبيت الحزم:

```bash
python -m pip install psycopg2-binary pandas python-dotenv
```

4. إنشاء الجداول:

```bash
psql -h localhost -U postgres -d appdb -f app/db/schema.sql
```

5. تشغيل ETL:

```bash
python app/etl/extract_sales.py
```

6. تحميل البيانات إلى طبقة المستودع:

```bash
python app/warehouse/load_to_warehouse.py
```

## إعداد متغيرات البيئة

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=appdb
DB_USER=postgres
DB_PASSWORD=postgres

APP_ENV=development
LOG_LEVEL=INFO
```

## مثال قاعدة بيانات

```sql
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(100),
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    total_amount NUMERIC(10,2),
    order_date DATE
);
```

## مثال ETL

```python
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="appdb",
    user="postgres",
    password="postgres",
    port="5432",
)

df = pd.read_sql("SELECT * FROM sales", conn)
print(df.head())
```

## الخطوة التالية

- ربط بياناتك بواجهة برمجة أو تطبيق
- تحويل هذا القالب إلى AWS / Azure / GCP
- إضافة dbt أو Airflow
- تشغيل تقارير BI

## ملاحظات

هذا المشروع يعد نقطة انطلاق، ويمكن توسيعه لاحقاً ليصبح مستودع بيانات كامل جاهز للإنتاج.
