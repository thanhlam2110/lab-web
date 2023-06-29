
<?php
$data = "";
$url = 'http://192.168.107.133:5000/api/publicationAuthorId?id=Yt6EcJYAAAAJ';

// Send GET request and retrieve the response
$response = file_get_contents($url);

if ($response !== false) {
    // Decode the response from JSON to an associative array
    $data = json_decode($response, true);
    // foreach ($data as $item) {
    //     echo "Title: " . $item['bib']['title'] . "<br>";
    //     echo "Citation: " . $item['bib']['citation'] . "<br><br>";
    // }
} else {
    echo 'Failed';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>PUBLICATION</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container-fluid p-5 bg-primary text-white text-center">
  <h1>PUBLICATION PAPER</h1>
</div>
<style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    
    th, td {
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    th{
        text-align: center;
    }
    th {
        background-color: #f2f2f2;
    }
    
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    tr:hover {
        background-color: #f5f5f5;
    }
</style>
<table>
    <tr>
        <th>Number</th>
        <th>Title</th>
        <th>Publisher</th>
    </tr>
    <!-- <?php foreach ($data as $item) { ?>
        <tr>
            <td><?php echo $item['bib']['title']; ?></td>
            <td><?php echo $item['bib']['citation']; ?></td>
        </tr>
    <?php } ?> -->
    <?php foreach ($data as $index => $item): ?>
        <tr>
            <td><?php echo $index + 1; ?></td>
            <td><?php echo $item['bib']['title']; ?></td>
            <td><?php echo $item['bib']['citation']; ?></td>
        </tr>
    <?php endforeach; ?>
</table>
</body>
</html>
