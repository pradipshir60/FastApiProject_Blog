var addBlog = function () {
    // Private functions
    var validator;
	var initValidation = function () {
        validator = $( "#addBlogForm" ).validate({
            // define validation rules
            rules: {
				'title': {
					required: true,
					minlength: 2
				},
				'body': {
					required: true
				},
			},messages:{
				'title': {
					required: "Please enter your title",
					minlength: "Your name must be at least 2 characters long"
				},
				'body': {
					required: "Please write something about your blog",
				}
			},
            errorPlacement: function(error, element) {
				error.insertAfter(element);
			},
            submitHandler: function (form) {
				let data = {"title" : $('#title').val(), "body" : $('#body').val()};
				$.ajax({
					url: '/blog/store/',
					method: 'post',
					data: JSON.stringify(data),
					contentType: 'application/json',
					success: function(response, textStatus, jqXHR) {
						console.log(jqXHR);
						if (jqXHR.status == 200) {
							$('<div class = "col-sm-12">').addClass('success').prependTo('.container .row .message').text('New blog successfully added!');
							form.reset();
						} else {
							$('<div class = "col-sm-12">').addClass('error').prependTo('.container .row .message').text('Something is wrong!');
						}
					},
					error: function(data) {
						console.log(data);
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

