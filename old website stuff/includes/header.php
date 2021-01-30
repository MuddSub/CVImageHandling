<?php
    session_start();
    echo "<script>console.log('skdjfsjdf')</script>";

?>

<!doctype html>


<html>
    <head>
        <title>MuddSub Image Labeling</title>
        <link href="style.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
        <header>

            <?php 
                if ($_SESSION["uid"]) {
                    echo "<span id='login'>logged in as " . $_SESSION["uid"] . "</a></span>";
                }
                else {
                    echo "<span id='login'><a href='login.html'>not logged in</a></span>";
                }
            ?>
            
        </header>
