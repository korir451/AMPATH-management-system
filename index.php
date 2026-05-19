<?php
// index.php - Safaricom Training Backend (PHP + MySQL)
// Provides an endpoint to fetch bundles and optionally record a transaction.

header('Content-Type: application/json; charset=utf-8');

$DB_HOST = 'localhost';
$DB_NAME = 'safaricom_db';
$DB_USER = 'root';
$DB_PASS = 'Brian3943*';

$dsn = "mysql:host={$DB_HOST};dbname={$DB_NAME};charset=utf8mb4";
$options = [
  PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
  PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
  PDO::ATTR_EMULATE_PREPARES => false,
];

try {
  $pdo = new PDO($dsn, $DB_USER, $DB_PASS, $options);
} catch (Throwable $e) {
  http_response_code(500);
  echo json_encode(['ok' => false, 'error' => 'DB connection failed']);
  exit;
}

$action = $_GET['action'] ?? 'getBundles';

if ($action === 'getBundles') {
  $stmt = $pdo->query('SELECT bundle_id, bundle_name, data_gb, validity_days, price_kes FROM bundles ORDER BY bundle_id');
  $rows = $stmt->fetchAll();
  echo json_encode(['ok' => true, 'action' => 'getBundles', 'bundles' => $rows]);
  exit;
}

if ($action === 'recordTransaction') {
  // Expected POST fields: customer_id, service_id, amount_kes, status, note(optional)
  $customerId = isset($_POST['customer_id']) ? (int)$_POST['customer_id'] : 0;
  $serviceId  = isset($_POST['service_id']) ? (int)$_POST['service_id'] : 0;
  $amountKes  = isset($_POST['amount_kes']) ? (float)$_POST['amount_kes'] : 0;
  $status     = $_POST['status'] ?? 'PENDING';
  $note       = $_POST['note'] ?? null;

  if ($customerId <= 0 || $serviceId <= 0 || $amountKes <= 0) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'Invalid input']);
    exit;
  }

  $sql = 'INSERT INTO transactions (customer_id, service_id, amount_kes, status, created_at, note)
          VALUES (:customer_id, :service_id, :amount_kes, :status, NOW(), :note)';
  $stmt = $pdo->prepare($sql);
  $stmt->execute([
    ':customer_id' => $customerId,
    ':service_id' => $serviceId,
    ':amount_kes' => $amountKes,
    ':status' => $status,
    ':note' => $note
  ]);

  echo json_encode([
    'ok' => true,
    'action' => 'recordTransaction',
    'transaction_id' => (int)$pdo->lastInsertId()
  ]);
  exit;
}

http_response_code(400);
echo json_encode(['ok' => false, 'error' => 'Unknown action']);

