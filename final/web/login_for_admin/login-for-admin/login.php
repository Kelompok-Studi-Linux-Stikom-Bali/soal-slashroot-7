<?php
    session_start();
    include "conn.php";
    if(isset($_SESSION['user'])){
        header('Location: index.php');
    }
    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = $connect->real_escape_string($_POST['username']);
        $password = $connect->real_escape_string($_POST['password']);
        
        $query = $connect->query("SELECT * FROM admin WHERE username = '$username' && password = '$password' ");
        if($query->num_rows){
            $_SESSION["user"] = $username;
            header('Location: index.php');
            die();
        }
        $_SESSION['message'] = "Invalid Credentials";
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Login</h1>
        <?php if(isset($_SESSION['message'])) {?>
            <div class="alert <?php if($_SESSION['message'] == 1){ echo "alert-success"; }else{ echo "alert-danger";} ?>" role="alert">
                <?php if($_SESSION['message'] == 1){ echo "Successfuly create account"; }else{ echo "Invalid Credentials";} ?>
            </div>
        <?php unset($_SESSION['message']); } ?>
        <form action='login.php' method="post">
            <div class="form-outline mb-4">
                <label class="form-label" for="form2Example1">Username</label>
                <input type="text" name="username" id="form2Example1" class="form-control" />
            </div>

            <div class="form-outline mb-4">
                <label class="form-label" for="form2Example2">Password</label>
                <input type="password" name="password" id="form2Example2" class="form-control" />
            </div>
            <div class="flex">
                <button type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>
                <a href="register.php" class="btn btn-primary btn-block mb-4">Register</a>
            </div>
        </form>
    </div>
</body>
</html>