<?php
session_start();
if(isset($_POST['feedback'])){
    $feedback = $_POST['feedback'];
    $_SESSION["feedback"] = $feedback;
    echo shell_exec("python bot.py $feedback");

    header('Location: feedback.php');
}


