<?php

function emptyInput($uid, $pwd) {
    $result;
    if (empty($uid) || empty($pwd)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}

function invalidUid($uid) {
    $result;
    if (!preg_match("/^[a-z]*$/", $uid)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}
function uidExists($conn, $uid) {
    $sql = "SELECT * FROM users WHERE usersUid = ?;"; # this is a sql statement that we will submit to the database
    $stmt = mysqli_stmt_init($conn); #this is a prepared statement. the func intiializes a new prepared statement

    // check if there are mistakes in the statement
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../login.html?error=validationstmtfailed"); 
        exit();
    }

    mysqli_stmt_bind_param($stmt, "s", $uid);
    mysqli_stmt_execute($stmt);
    $resultData = mysqli_stmt_get_result($stmt);
    // check if there is a result from this particular statemetn
    if ($row = mysqli_fetch_assoc($resultData)){
        return $row; // return all data from database if the user exists

    }
    else {
        $result = false;
        return $result;
    }
    mysqli_stmt_close($stmt);
}

function createUser($conn, $uid, $pwd) {
    $sql = "INSERT INTO users (usersUid, usersPwd) VALUES (?, ?);"; # this is a sql statement that we will submit to the database
    $stmt = mysqli_stmt_init($conn); #this is a prepared statement. the func intiializes a new prepared statement
    // something is going wrong here in this initialization
    
    // check if there are mistakes in the statement
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../login.html?error=createuserstmtfailed"); 
        exit();
    }
    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);

    mysqli_stmt_bind_param($stmt, "ss", $uid, $hashedPwd);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    header("location: ../login.html?error=none"); 
    exit();
}

function loginUser($conn, $uid, $pwd) {
    $sql = "SELECT * FROM users WHERE usersUid = ?;"; # this is a sql statement that we will submit to the database
    $stmt = mysqli_stmt_init($conn); #this is a prepared statement. the func intiializes a new prepared statement
    // something is going wrong here in this initialization
    
    // check if there are mistakes in the statement
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../login.html?error=createuserstmtfailed"); 
        exit();
    }

    mysqli_stmt_bind_param($stmt, "ss", $uid);
    mysqli_stmt_execute($stmt);
    $resultData = mysqli_stmt_get_result($stmt);
    $row = mysqli_fetch_assoc($resultData); # this is an associated array - instead of indexing by number, it indexes by the column name

    $pwdHashed = $row["usersPwd"];
    $checkPwd = password_verify($pwd, $pwdHashed);

    if ($checkPwd === false) { //////// SOMETHING IS GOING WRONG HERE
        //////////// CORRECT PASSWORDS ARE BEING MARKED AS FALSE
        header("location: ../login.html?error=wrongPwd"); 
        exit();
    }
    else if ($checkPwd === true) {
        session_start();
        $_SESSION["uid"] = $row["usersUid"];
        header("location: ../index.php"); 
        exit();
    }

    mysqli_stmt_close($stmt);
    header("location: ../login.html?error=none"); 
    exit();

}