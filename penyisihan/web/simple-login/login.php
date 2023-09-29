<?php
session_start();
!isset($_POST["username"]) || !isset($_POST["password"]) ? header('Location: index.php') : "";

include("conn.php");

$username = $_POST['username'];
$password = $_POST['password'];

$query = $connect->query("SELECT * from user where username = '$username' and password = '$password'");
if($query->num_rows){
    $_SESSION["flag"] = 'slashroot7{s1mpl3_sql_1nj3cti0n}';
    header('Location: index.php');
    die();
}

$_SESSION["msg"] = "Login Failed";
header('Location: index.php');
