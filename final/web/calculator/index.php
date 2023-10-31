<!-- hint: source.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>
   <div class="container mt-5">
    <?php
    if(isset($_POST['submit'])){
        $inp = $_POST['kalkulator'];
        if(preg_match_all('/[a-z]|[A-Z]|@|#/',$inp)){
            die("not printable");
        }
        $filter = eval("return $inp;");
    ?>
        <div class="alert alert-primary" role="alert">
            <?=eval("return $filter;");?>
        </div>
    <?php
    }
    ?>
        <form method="post" action="index.php">
            <div class="mb-3">
                <label for="kalkulator" class="form-label">Kalkulator</label>
                <input type="text" class="form-control" name="kalkulator">
            </div>
            <button type="submit" name="submit" class="btn btn-primary mb-3">Submit</button>
        </form>
    </div>
</body>
</html>