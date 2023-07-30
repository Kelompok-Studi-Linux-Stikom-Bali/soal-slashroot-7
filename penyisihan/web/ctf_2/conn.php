<?php

$connect = new mysqli('localhost','root','','ctf_2');

if ($connect->connect_error) {
    die("Connection failed: " . $connect->connect_error);
}