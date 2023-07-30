<?php
session_start();
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  </head>
  <body>
        <div class="vh-100 d-flex justify-content-center align-items-center">
            <div class="col-md-4 p-5 shadow-sm border rounded-3">
                <h2 class="text-center mb-4 text-primary">Login</h2>
                <form action="login.php" method="post">
                    <?php if(isset($_SESSION['msg'])) {?>
                        <div class="alert alert-danger">
                            <?=$_SESSION['msg']?>
                        </div>
                    <?php }else if(isset($_SESSION['flag'])){ ?>
                        <div class="alert alert-success">
                            <?=$_SESSION['flag']?>
                        </div>
                    <?php } session_destroy();?>
                    <div class="mb-3">
                        <label for="form-username" class="form-label">Username</label>
                        <input type="text" class="form-control border border-primary" id="form-username" name="username">
                    </div>
                    <div class="mb-3">
                        <label for="form-password" class="form-label">Password</label>
                        <input type="password" class="form-control border border-primary" id="form-password" name="password">
                    </div>
                    <div class="d-grid">
                        <button class="btn btn-primary" type="submit">Login</button>
                    </div>
                </form>
            </div>
        </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
  </body>
</html>