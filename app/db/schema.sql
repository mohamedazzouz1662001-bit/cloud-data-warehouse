CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(100) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    total_amount NUMERIC(10,2) NOT NULL,
    order_date DATE NOT NULL
);

INSERT INTO sales (order_id, customer_name, product_name, quantity, total_amount, order_date)
VALUES
    ('A1001', 'Ahmed', 'Laptop', 2, 3500.00, '2026-01-15'),
    ('A1002', 'Sara', 'Phone', 3, 2100.00, '2026-01-18'),
    ('A1003', 'Ali', 'Tablet', 1, 1200.00, '2026-01-22'),
    ('A1004', 'Nora', 'Monitor', 4, 2600.00, '2026-01-25'),
    ('A1005', 'Khalid', 'Keyboard', 10, 1500.00, '2026-01-28')
ON CONFLICT DO NOTHING;
