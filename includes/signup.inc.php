<?php

// make sure the user accessed the page the correct way, else redirect to login page

if (isset($_POST["submit"])) { //check that the superglobal variable, which is a post method called 'submit', is set

    echo "it works! dfjgbdfkjgbdfkgjs";
    $uid = $_POST["uid"];
    // $pwd = $_POST["pwd"];

    require_once 'dbh.inc.php';
    require_once 'functions.inc.php';

    // check for errors in input
    if (emptyInput($uid) !== false) {
        header("location: ../login.html?error=emptyInput"); 
        exit();
    }
    if (invalidUid($uid) !== false) {
        header("location: ../login.html?error=invalidUid"); 
        exit();
    }
    // echo "now checking if uid already exists";
    // if (uidExists($conn, $uid) !== false) {
    //     echo "now redirecting";
    //     header("location: ../login.html?error=uidTaken"); 
    //     exit();
    // }

    echo "passed error handling functions";

    createUser($conn, $uid); 

    echo "ran all functions, created user";
}
else {
    header("location: ../login.html"); //redirects user to login page if this page was not accessed legally
}

?>