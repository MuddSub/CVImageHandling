<?php

function emptyInput($uid) {
    $result;
    if (empty($uid)) {
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
    echo "inside uidExists function";
    $sql = "SELECT * FROM users WHERE usersUid = ?;"; # this is a sql statement that we will submit to the database
    $stmt = mysqli_stmt_init($conn); #this is a prepared statement. the func intiializes a new prepared statement

    echo "check if there are mistakes in stmt";
    // check if there are mistakes in the statement
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../login.html?error=validationstmtfailed"); 
        exit();
    }

    echo "\n now starting bind param";
    myqsli_stmt_bind_param($stmt, "s", $uid);
    echo "\n finish bind now start execute";
    mysqli_stmt_execute($stmt);
    echo "finish execute";
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

function createUser($conn, $uid) {
    echo "\n now creating user in databse";
    $sql = "INSERT INTO users (usersUid) VALUES (?);"; # this is a sql statement that we will submit to the database
    echo "\r\n init sql var";
    $stmt = mysqli_stmt_init($conn); #this is a prepared statement. the func intiializes a new prepared statement
    // something is going wrong here in this initialization
    
    echo "\n init stmt, now checking for mistakes";
    // check if there are mistakes in the statement
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        echo "mistake ! >:(";
        header("location: ../login.html?error=createuserstmtfailed"); 
        exit();
    }
    echo "\n no mistakes, now creating user";
    // $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);

    myqsli_stmt_bind_param($stmt, "s", $uid); /////STUCK HERE
    echo "\n finish bind start execute";
    mysqli_stmt_execute($stmt);
    echo "executed";
    mysqli_stmt_close($stmt);
    header("location: ../login.html?error=none"); 
    exit();

}