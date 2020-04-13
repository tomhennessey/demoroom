<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Process Form</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<?php
	if(isset($_POST['name'])) {
	
		// define variables from _POST[]
		$name = $_POST['name'];
		$email_from = $_POST['email'];
		$demo_name = $_POST['demo-name'];
		$date_time = $_POST['dateTime'];
		$comments = $_POST['info'];
		
		// format date and time string
		$dateTimeNew = DateTime::createFromFormat('Y-m-d\TG\:i', $date_time);
		$dateTimeNew = $dateTimeNew->format('l F dS \a\t\ g\:ia \(m-d-Y \- H:i\)');
		
		// compose message that will be sent to demo room email
		$email_message = "$name ($email_from) has requested a demo:\n" . $demo_name . "\n" . $dateTimeNew . "\n" . $comments;
		
		// email and subject to send
		$email_to = "chem-demoroom@illinois.edu";
		$email_subject = "Demo Request from Website";
		
		// create email headers and send
		$headers = 'From: chem-demoroom@illinois.edu' . "\r\n" .
		'Reply-To: chem-demoroom@illinois.edu' . "\r\n" .
		'X-Mailer: PHP/' . phpversion();
		if (mail($email_to, $email_subject, $email_message, $headers)) {
		}
		else {
			echo "There was an error processing your request. Please send an email to chem-demoroom@illinois.edu with your demo request.";
		}
		
		// confirmation email for requester
		$email_confirmation_subject = "Demo Request Confirmation";
		$email_confirmation = "This email is to confirm you request of $demo_name on $dateTimeNew. If any of this information is incorrect, please reply to this email with the corrected information. Thank you!";
		if(mail($email_from, $email_confirmation_subject, $email_confirmation, $headers)) {
		}
		else {
			echo "There was an error processing your request. Please send an email to chem-demoroom@illinois.edu with your demo request."; 
		}
	}
  ?>
<body>
	
		<h1> Thank You</h1>
        <p> You should receive an email confirming your demonstration request shortly. If you do not, please email chemdemoroom@illinois.edu to request your demo.</p>

</body>
</html>