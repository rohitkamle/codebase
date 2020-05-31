<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>



<?php
$json_string = file_get_contents("https://jsonplaceholder.typicode.com/users");
$array = json_decode($json_string, true);

?>
<div class="container">
<div class="card">
<div class="card-body">
<table class="table table-bordered table-dark">
    <thead><tr><th>Id</th><th>Name</th><th>Email</th><th>Mobile</th></tr></thead>
    <tbody>
    <?php foreach($array as $key => $value): ?>
        <tr>
                <td><?php echo $value['id']; ?></td>
                <td><?php echo $value['name']; ?></td>
                <td><?php echo $value['email']; ?></td>
                <td><?php echo $value['phone']; ?></td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>
</div>
</div>
</div>
</body>
<html>