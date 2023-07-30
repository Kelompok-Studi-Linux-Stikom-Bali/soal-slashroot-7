<?php
session_start();
!isset($_POST["username"]) || !isset($_POST["password"]) ? header('Location: index.php') : "";

include("conn.php");

$username = $_POST['username'];
$password = $_POST['password'];

$query = $connect->query("SELECT * from user where username = '$username' and password = '$password'");
if($query->num_rows){
    $_SESSION["flag"] = 'CTF{y0u_g0t_me}';
    header('Location: index.php');
    die();
}

$_SESSION["msg"] = "Login Failed";
header('Location: index.php');
