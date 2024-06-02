var addBlog = function () {
    // Private functions
    var validator;
	var initValidation = function () {
        validator = $( "#addEmailForm" ).validate({
            // define validation rules
            rules: {
				'subject': {
					required: true,
					minlength: 2
				},
				'body': {
					required: true
				},
				'emails': {
					required: true
				},
			},messages:{
				'subject': {
					required: "Please enter your subject",
					minlength: "Your name must be at least 2 characters long"
				},
				'body': {
					required: "Please write something about your blog",
				},
				'emails': {
					required: "Please add email ids",
				}
			},
            errorPlacement: function(error, element) {
				error.insertAfter(element);
			},
            submitHandler: function (form) {
				// let data = {"subject" : $('#subject').val(), "body" : $('#body').val(), "attachment" : $('#attachment').val(), "emails" : $('#emails').val()};
				// console.log(data);

				const fileInput = document.getElementById('attachment');
				const file = fileInput.files[0];
				const formData = new FormData();
				if(file){
					formData.append('attachment', file);
				}
				formData.append('subject', $('#subject').val());
				formData.append('body', $('#body').val());
				formData.append('emails', $('#emails').val());
				
				$.ajax({
					url: '/email/html/',
					type: 'POST',
					data: formData,
					processData: false,
    				contentType: false,
					success: function(response, textStatus, jqXHR) {
						console.log(jqXHR);
						if (jqXHR.status == 200) {
							$('<div class = "col-sm-12">').addClass('success').prependTo('.container .row .message').text('New blog successfully added!');
							form.reset();
						} else {
							$('<div class = "col-sm-12">').addClass('error').prependTo('.container .row .message').text('Something is wrong!');
						}
					},
					error: function(response, textStatus, jqXHR) {
						console.log(response);
						// let errors = $.parseJSON(data.responseText);
						// $.each(errors.errors, function(index, value) {
						// 	alert(index);
						// });
					}
				});
            }
        });       
    }

    return {
        // public functions
        init: function() {
            initValidation();
        }
    };
}();

jQuery(document).ready(function() {    
    addBlog.init();
});

