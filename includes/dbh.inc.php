<?php

$serverName = "localhost";
$dBUsername = "root";
$dBPassword = "";
$dBName = "cvimagehandling";

$conn = mysqli_connect($serverName, $dBUsername, $dBPassword, $dBName);

if (!conn) { // ie if connection fails
    die("Connection failed: " . mysqli_connect_error()); 
    // ( . (period) is string concatenation operator in php)
}

// THIS IS INCOMPLETE