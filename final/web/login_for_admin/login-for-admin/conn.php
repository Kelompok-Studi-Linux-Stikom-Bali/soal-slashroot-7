<?php

$connect = new mysqli('mysql-db','root','291dcc71b79731f88b65cee99a9b5bf3edec2d9755e22af2746bf1784633a7b0338c2573167e4f7997f0c488a04d74c4e650','ctf_4');

if ($connect->connect_error) {
    die("Connection failed: " . $connect->connect_error);
}