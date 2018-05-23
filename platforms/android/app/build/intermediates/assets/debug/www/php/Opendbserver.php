<?php
    // Stoixeia bashs kai administrator bashs
    $servername = "192.168.1.50";
    $username = "chris";
    $password = "cdelis1994";
    $dbname = "precision_agriculture";
    
    // sundesh me thn bash
    $connserver = mysqli_connect($servername, $username, $password, $dbname);
    
    // elenxos an egine h sundesh
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    
    // gia thn uposthriksh ellhnikwn    
    mysqli_set_charset($connserver,"utf8");
?>