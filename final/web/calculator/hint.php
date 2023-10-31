<?php
if (isset($_POST['submit'])) {
    $inp = $_POST['kalkulator'];
    if (preg_match_all('/[a-z]|[A-Z]|,|@|#/', $inp)) {
        die('not printable');
    }
    $filter = eval('return $inp;');
?>
    <div class='alert alert-primary' role='alert'>
        <?= eval('return $filter'); ?>
    </div>
<?php
}
?>