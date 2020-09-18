$(document).ready(function(){
	$(".form2").hide();
	$(".form3").hide();
	$(".form4").hide();
	$(".form5").hide();
	$(".form6").hide();


	$("#form1").click(function(event){
		event.preventDefault();
		if($('#id_first_name').val() == "" || $('#id_last_name').val() == "" || $('#id_email').val() == ""
			|| $('#id_date_of_birth').val() == "" || $('#id_phone_number').val() == ""
			 || $('#id_address').val() == "" || $('#id_location').val() == "" || $('#id_projects_link').val() == ""
			 || $('#id_resume_summary').val() == "" || $('#id_professional_title').val() == ""
		){
			$(".msg1").addClass("noti");
			$(".msg1").text("There is/are Empty Field(s)");
		}
		else{
			// CHECK INPUT VALIDATION
			if(form1_valid() != false){
				postForm1();
			}
		}

	});
	$("#form2").click(function(event){
		event.preventDefault();
		if($('#id_school_name').val() == "" && $('#id_studied').val() == "" )
		{
			$(".form2").hide();
			$(".form3").show();
		}
		else{
			if(form2_valid() != false){
				postForm2();
				$(".form2").hide();
				$(".form3").show();
			}
		}
	});

	$("#form3").click(function(event){
		event.preventDefault();
		if($('#id_name').val() == "")
		{
			$(".form3").hide();
			$(".form4").show();
		}
		else{
			if(form3_valid() != false){
				postForm3();
				$(".form3").hide();
				$(".form4").show();
			}
		}
	});


	$("#form4").click(function(event){
		event.preventDefault();
		if($('#id_school').val() == "" && $('#id_year').val() == "")
		{
			$(".form4").hide();
			$(".form5").show();
		}
		else{
			if(form4_valid() != false){
				postForm4();
				$(".form4").hide();
				$(".form5").show();
			}
		}

	});

	$("#form5").click(function(event){
		event.preventDefault();
		if($('#id_interest').val() == "")
		{
			$(".form5").hide();
			$(".form6").show();
		}
		else{
			if(form5_valid() != false){
				postForm5();
				$(".form5").hide();
				$(".form6").show();
			}
		}
	});

	$("#form6").click(function(event){
		event.preventDefault();
		if($('#id_title').val() == "" && $('#id_description').val() == ""){
			$.ajax({
				type: 'POST',
				url: '/done/'+parseInt(sessionStorage.getItem('id'))+'/False',
				data: {
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
				},
				success: function(res){
					if(res.status == 404){
						$(".msg6").addClass("noti");
						$(".msg6").text("User id not found. You'll have to start from beginning. ");
					}
					else{
						$(".msg6").addClass("noti");
						$(".msg6").text("Redirecting now...");

						setTimeout(() =>{console.log("Redirecting...")}, 8000);
						window.location.assign("/done/"+parseInt(sessionStorage.getItem('id'))+"/False/");
					}

				},
				error: function(){
					$(".msg6").addClass("noti");
					$(".msg6").text("There's error with saving data, please try again");
				}
			});
		}
		else{
			if(form6_valid() != false){
				postForm6();
				$.ajax({
					type: 'POST',
					url: '/done/'+parseInt(sessionStorage.getItem('id'))+'/False',
					data: {
						csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
					},
					success: function(res){
						if(res.status == 404){
							$(".msg2").addClass("noti");
							$(".msg2").text("User id not found. You'll have to start from beginning. ");
						}
						else{
							$(".msg2").addClass("noti");
							$(".msg2").text("Redirecting now...");

							setTimeout(() =>{console.log("Redirecting...")}, 8000);
							window.location.assign("/done/"+parseInt(sessionStorage.getItem('id'))+"/False");
						}
					},
					error: function(){
						$(".msg2").addClass("noti");
						$(".msg2").text("There's error with saving data, please try again");
					}
				});
			}
		}
		
		
		
	});


	$("#addNewForm2").click(function(event){
		event.preventDefault();
		if($('#id_school_name').val() == "" && $('#id_studied').val() == "" )
		{
			$(".msg2").addClass("noti");
			$(".msg2").text("There is/are Empty field(s)");
		}
		else{
			if(form2_valid() != false){
				postForm2();
				$('#id_school_name').val("");
				$('#id_studied').val("");
			}
			
		}
	});


	$("#addNewForm3").click(function(event){
		event.preventDefault();	
		if($('#id_percentage').val() == "" || $('#id_name').val() == ""){
			$(".msg3").addClass("noti");
			$(".msg3").text("There is/are Empty field(s)");
		}
		else{
			if(form3_valid() != false){
				 postForm3();
				 // $('#id_percentage').val("");
				 // $('#id_percentage').val("");
				 $('#id_name').val("");
			}
			 
		}  
		
	});

	$("#addNewForm4").click(function(event){
		event.preventDefault();
		if($('#id_school').val() == "" && $('#id_year').val() == ""){
			$(".msg4").addClass("noti");
			$(".msg4").text("There is/are Empty field(s)");
		}
		else{
			if(form4_valid() != false){
				postForm4();
			    $('#id_school').val("");
				$('#id_year').val("");
			}
		}
		
		
	});

	$("#addNewForm5").click(function(event){
		event.preventDefault();	
		if( $('#id_interest').val() == ""){
			$(".msg5").addClass("noti");
			$(".msg5").text("There is/are Empty field(s)");
		}
		else{
			if(form5_valid() != false){
					postForm5();
	    			$('#id_interest').val("");
			}
		}
	
	    
	});

	$("#addNewForm6").click(function(event){
		event.preventDefault();	
		if($('#id_title').val() == "" && $('#id_description').val() == ""){
			$(".msg6").addClass("noti");
			$(".msg6").text("There is/are Empty field(s)");
		}
		else{
			if(form6_valid() != false){
				postForm6();
			    $('#id_title').val("");
				$('#id_description').val("");
			}
		}
	
	});

	// SEND DATA TO DJANGO VIEWS TO PROCESS
	function postForm1(){
				$.ajax({
					type: 'POST',
					url: '/form1',
					data: {
						first_name: $('#id_first_name').val(),
						last_name: $('#id_last_name').val(),
						email: $('#id_email').val(),
						date_of_birth: $('#id_date_of_birth').val(),
						phone_number: $('#id_phone_number').val(),
						address: $('#id_address').val(),
						location: $('#id_location').val(),
						projects_link: $('#id_projects_link').val(),
						resume_summary: $('#id_resume_summary').val(),
						professional_title: $('#id_professional_title').val(),
						csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
					},
					success: function(response){
						sessionStorage.setItem('id', response.id);
						$(".form1").hide();
						$(".form2").show();
					},
					error: function(){
		 				$(".msg2").addClass("noti");
						$(".msg2").text("There's error with saving data, please try again");
		 			}				
				});
	}			
	

	function postForm2(){
			$.ajax({
				type: 'POST',
				url: '/form2',
				data: {
					school_name: $('#id_school_name').val(),
					degree: $('#id_degree').val(),
					studied: $('#id_studied').val(),
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
					id:  parseInt(sessionStorage.getItem('id'))
				},
				success: function(){
					$(".msg2").addClass("noti");
					$(".msg2").text("Saved successfully.");
				},
				error: function(){
					$(".msg2").addClass("noti");
					$(".msg2").text("There's error with saving data, please try again");
				}
			});	
	}

	function postForm3(){

			$.ajax({
				type: 'POST',
				url: '/form3',
				data: {
					percentage: $('#id_percentage').val(),
					name: $('#id_name').val(),
					id: parseInt(sessionStorage.getItem('id')),
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				},
				success: function(){
					$(".msg3").addClass("noti");
					$(".msg3").text("Saved successfully.");
				},
				error: function(){
					$(".msg3").addClass("noti");
					$(".msg3").text("There's error with saving data, please try again");
				}
			});
			
	}

	function postForm4(){
			$.ajax({
				type: 'POST',
				url: '/form4',
				data: {
					school: $('#id_school').val(),
					year: $('#id_year').val(),
					id: parseInt(sessionStorage.getItem('id')),
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				},
				success: function(){
					$(".msg4").addClass("noti");
					$(".msg4").text("Saved successfully.");
				},
				error: function(){
					$(".msg4").addClass("noti");
					$(".msg4").text("There's error with saving data, please try again");
				}
			});
		
	}

	function postForm5(){
			$.ajax({
				type: 'POST',
				url: '/form5',
				data: {
					interest: $('#id_interest').val(),
					id: parseInt(sessionStorage.getItem('id')),
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				},
				success: function(){
					$(".msg5").addClass("noti");
					$(".msg5").text("Saved successfully.");
				},
				error: function(){
					$(".msg5").addClass("noti");
					$(".msg5").text("There's error with saving data, please try again");
				}
			});	
	}

	function postForm6(){
			$.ajax({
				type: 'POST',
				url: '/form6',
				data: {
					title: $('#id_title').val(),
					description: $('#id_description').val(),
					id: parseInt(sessionStorage.getItem('id')),
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				},
				success: function(){
					$(".msg6").addClass("noti");
					$(".msg6").text("Saved successfully.");
				},
				error: function(){
					$(".msg6").addClass("noti");
					$(".msg6").text("There's error with saving data, please try again");
				}
			});	
	}


        // VALIDATIONS CHECK
	function form1_valid(){
		 if(validate_name($('#id_first_name').val()) == false) {
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("First Name field is not valid"); 
		 	return false;
		 }
		 else if(validate_name($('#id_last_name').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Last Name field is not valid");
		 	return false;
		 }
		 else if(validate_email($('#id_email').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Email field is not valid");
		 	return false;
		 }
		 else if(validate_phone_num($('#id_phone_number').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Phone number field is not valid");
		 	return false;
		 }
		 else if(validate_long_name($('#id_resume_summary').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Resume summary field is not valid");
		 	return false;
		 }
		 else if(validate_dob($('#id_date_of_birth').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Date of Birth field is not valid");
		 	return false;
		 }
		 else if(validate_long_name($('#id_professional_title').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Professional Title field is not valid");
		 	return false;
		 }
		 else if(validate_long_name($('#id_address').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Address field is not valid");
		 	return false;
		 }
		 else if(validate_long_name($('#id_location').val()) == false){
		 	$(".msg1").addClass("noti");
		 	$(".msg1").text("Address field is not valid");
		 	return false;
		 }
		
	}
	function form2_valid(){
		if(validate_long_name($('#id_school_name').val()) == false){
			$(".msg2").addClass("noti");
		 	$(".msg2").text("School Name field is not valid");
			return false;
		}
		else if(validate_long_name($('#id_studied').val()) == false){
			$(".msg2").addClass("noti");
		 	$(".msg2").text("Studied field is not valid");
			return false;
		}
	}

	function form3_valid(){
		if(validate_long_name($('#id_name').val()) == false){
			$(".msg3").addClass("noti");
		 	$(".msg3").text("Name field is not valid");
			return false;
		}
	}

	function form4_valid(){
		if(validate_long_name($('#id_school').val()) == false){
			$(".msg4").addClass("noti");
		 	$(".msg4").text("School field is not valid");
			return false;
		}
		else if(validate_year($('#id_year').val()) == false){
			$(".msg4").addClass("noti");
		 	$(".msg4").text("Year field is not valid");
			return false;
		}
		
	}

	function form5_valid(){
		if(validate_long_name($('#id_interest').val()) == false){
			$(".msg5").addClass("noti");
		 	$(".msg5").text("Interest field is not valid");
			return false;
		}
		
	}
	function form6_valid(){
		if(validate_long_name($('#id_title').val()) == false){
			$(".msg6").addClass("noti");
		 	$(".msg6").text("Title field is not valid");
			return false;
		}
		else if(validate_long_name($('#id_description').val()) == false){
			$(".msg6").addClass("noti");
		 	$(".msg6").text("Description field is not valid");
			return false;
		}
		
	}



	// VALIDATE USING REGEX
	function validate_email(email){
		return email.length < 50 && /^[^@]+@[^@]{2,}\.[^@]{3,}$/.test(email);
	}
	function validate_phone_num(phone){
		return /^(\+234)\d{10}$/.test(phone);
	}
	function validate_name(name){
		return /^([a-zA-Z.]){3,20}$/.test(name);
	}

	function validate_long_name(name){
		return name.length < 400
	}
	function validate_year(year){
		return /^([0-9]){4}$/.test(year);
	}
	function validate_dob(dob){
		return /(\d{4})-(\d{2})-(\d{2})/.test(dob);
	}


				// SKILL BOX LEVELS FUNCTION
	let $listItems = $(".sk").find(".s").find("h3").find("span");
   	$($listItems).each(function(index){

		$spa = $(this).attr("class");
		for(var j=1; j <= parseInt($spa); j++){
			let add = index+1
			$(".sk>.s>h3>span#"+add).append("<div class='box'>"+j+"</div>").css("display", "flex");
		}

   	});

				//PDF BUTTON FUNCTION
	$(".pdf-btn>span.pdf-download").click(function(){
		let path =window.location.pathname;
		let matches = path.match(/\d+/g);
		let getId = matches[0];

		$.ajax({
				type: 'GET',
				url: '/generatePdf/'+getId,
				data: {	
				},
				success: function(res){
					console.log(res);
				},
				error: function(res){
					console.log(res.responseJSON.error);
				}
		});
	});

				//DELETE BUTTON FUNCTION
	$("span.delete").click(function(){
		let path =window.location.pathname;
		let matches = path.match(/\d+/g);
		let getId = matches[0];

		$.ajax({
				type: 'GET',
				url: '/delete/'+getId,
				data: {
				},
				success: function(res){
					window.location.assign("/create");
				},
				error: function(){
				}
		});
	});

	if($.cookie("clear") == "False"){
			$(".pdf-btn").show();
	}
});

