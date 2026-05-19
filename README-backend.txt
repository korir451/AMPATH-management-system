Safaricom Training Backend (PHP + MySQL)

1) Put this folder/files into your web root.
   - index.php (created)

2) Ensure your MySQL DB exists:
   - dbname: safaricom_db

3) Ensure tables exist (training schema expected):
   - bundles(bundle_id, bundle_name, data_gb, validity_days, price_kes)
   - transactions(transaction_id (auto), customer_id, service_id, amount_kes, status, created_at, note nullable)

4) Start PHP server:
   - php -S localhost:3000

5) Test endpoints:
   - http://localhost:3000/index.php?action=getBundles
   - Record transaction:
     curl -X POST -d "customer_id=1&service_id=2&amount_kes=50&status=SUCCESS&note=test" \
       http://localhost:3000/index.php?action=recordTransaction

Note:
- This backend returns JSON only.
- Your existing index.html is UI; you can submit forms to another endpoint or fetch JSON from backend.

