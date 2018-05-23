<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
</head>
<body>
    <?php
	require "/opendb.php";
        // Elegxos an exoun dwthei times sto email kai sto password
        if(isset($_POST["UserName"]) && isset($_POST["UserLastName"]) && isset($_POST["Email"]) && isset($_POST["Password"])){
            $username = $_POST["UserName"];
            $userlastname = $_POST["UserLastName"];
            $email = $_POST["Email"];
			$password = $_POST["Password"];
			// Eisagwgh twn timwn autwn ston pinaka sub_node
			$sql = "INSERT INTO users (Name,LastName,Password,Email) VALUES ('$username','$userlastname','$password','$email')";
			if ($conn->query($sql) === TRUE) {
				?>
					<script>
					window.alert("Επιτυχής εγγραφή");
					window.location.href = '../login.html';
					</script>
				<?php
		} else {
				?>
					<script>
					window.alert("Το e-mail έχει δoθεί!");
					window.location.href = '../login.html';
					</script>
				<?php
				}
					$conn->close();
			}
					?>
</body>
</html>