function deleteBlog(id){
    if(confirm("Are you sure?")){
        $.ajax({
            url: '/blog/delete/'+id,
            method: 'delete',
            contentType: 'application/json',
            success: function(response, textStatus, jqXHR) {
                console.log(jqXHR);
                if (jqXHR.status == 200) {
                    $('<div class = "col-sm-12">').addClass('success').prependTo('.container .message').text('Blog deleted successfully!');
                    setTimeout(window.location.reload(), 10000);
                } else {
                    $('<div class = "col-sm-12">').addClass('error').prependTo('.container .message').text('Something is wrong!');
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
}

