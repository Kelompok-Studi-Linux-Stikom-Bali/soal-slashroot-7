<?php
    session_start();
    include("conn.php");
    if(isset($_SESSION['user'])){
        header('Location: index.php');
    }

    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = $connect->real_escape_string($_POST['username']);
        $password = $connect->real_escape_string($_POST['password']);
        
        $query = $connect->query("INSERT INTO admin (id_admin, username, password, role) VALUES (null,'$username','$password','user')");
        if($query){
            $_SESSION["message"] = 1;
            header('Location: login.php');
            die();
        }
        $_SESSION['message'] = "Error";
        
    }
    
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Register</h1>
        <?php if(isset($_SESSION['message'])) {?>
            <div class="alert alert-danger" role="alert">
                <?=$_SESSION['message']?>
            </div>
        <?php unset($_SESSION['message']); } ?>
        <form action='register.php' method="post">
            <div class="form-outline mb-4">
                <label class="form-label" for="form2Example1">Username</label>
                <input type="text" name="username" id="form2Example1" class="form-control" />
            </div>

            <div class="form-outline mb-4">
                <label class="form-label" for="form2Example2">Password</label>
                <input type="password" name="password" id="form2Example2" class="form-control" />
            </div>
            <button type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>
        </form>
    </div>
</body>
</html>