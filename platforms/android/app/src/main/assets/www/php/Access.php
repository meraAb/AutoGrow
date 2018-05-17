<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
</head>
<body>
    <?php
	require "/opendb.php";
        // Elegxos an exoun dwthei times sto email kai sto password
        if(isset($_POST["Email"]) && isset($_POST["Password"])){
            $email = $_POST["Email"];
            $password = $_POST["Password"];
			// Elegxos an uparxei o user
			$sql = "SELECT Email,Password FROM users WHERE Email ='$email' AND Password = '$password'";
			$result = $conn->query($sql);
			if ($result->num_rows > 0) {
                // output data of each row
                while($row = $result->fetch_assoc()) {
                   // Elegxos an dothike to email kai to password tou diaxeiristh
                    if (strcmp($row["Email"], $email) == 0 && strcmp($row["Password"], $password) == 0){
                        session_start();
						// Ekxwrhsh email kai password stis session metablhtes email1 kai pass1 antistoixa
                        $_SESSION["email1"] = $email;
                        $_SESSION["pass1"] = $password;
				?>
				<script>
					window.alert("Welcome");
					window.location.href = '../index.html';
				</script>
					<?php
                    }
                }
			} else {
				?>
				<script>
					window.alert("Try again");
					window.location.href = '../login.html';
				</script>
			<?php
			}
				
					$conn->close();
			}
					?>
</body>
</html>