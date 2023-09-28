<?php

if (empty($_SESSION['name'])) {
    header('Location: ?page=login.php');
    die;
}

?>

<div class="flex flex-col items-center justify-center px-6 mx-auto pt:mt-0 dark:bg-gray-900">
    <h1 class="text-3xl font-bold text-center dark:text-white">Welcome, <?php echo $_SESSION['name']; ?></h1>
</div>
