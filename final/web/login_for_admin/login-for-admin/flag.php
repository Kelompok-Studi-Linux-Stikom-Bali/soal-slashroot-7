<?php
    session_start();
    include("conn.php");
    $flag = '';

    if(isset($_SESSION['user'])){
        $user = stripslashes($_SESSION['user']);
        $query = $connect->query("SELECT count(id_admin) as ttl from admin where role = 'admin' && username = '$user'");
        $flag = 'Admin only can see the flag';
        
        if($query->fetch_array()['ttl']){
            $flag = 'slashroot7{w0w_n0w_y0u_Are_admIn}';
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flag</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" aria-current="page" href="index.php">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="flag.php">Flag</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="logout.php">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-5">
        <?=$flag?>
    </div>
</body>
</html>