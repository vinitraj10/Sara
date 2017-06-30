$(document).on('click', '.browse', function(){
  var file = $(this).parent().parent().parent().find('.file');
  file.trigger('click');
});
$(document).on('change', '.file', function(){
  $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
});
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
$("a[rel='like']").on('click',function(event){
    event.preventDefault();
    like();
    function like(){
        console.log('We are in Like Function');
        url = $("a[rel='like']").attr('href');
        console.log(url);
        $.ajax({
            url:url,
            type:'GET',
        })
    }
})  
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
    function create_post() {
    $('#loading-image').show();
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : { 
            body : $('#id_text').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()

        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#id_text').val(' ');
            $('#loading-image').hide();
            $(json).hide().prependTo('#aj').fadeIn(2000);

        //html: json
    //}).hide().prependTo('#aj').fadeIn()
          /* $("ul").append(json).hide().fadeIn(2500);
          $('#id_text').val(' ');
           a = document.getElementById('rect').innerHTML;
            $('#id_text').val(' ');
            document.getElementById('rect').innerHTML = json + " " + a;
            
        */
        },


        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
});
/*window.onload = function() {
    get_json();

    function get_json() {
        $.ajax({
        url : "/blog/", // the endpoint
        type : "GET",
        success : function(json) {
            console.log("here");
            //console.log(json);
        }
    })

};
}
/*
$('body').on('load',function(event){
    get_json();
    function get_json() {
        $.ajax({
        url : "/blog/", // the endpoint
        type : "GET",
        success : function(json) {
            console.log("here");
            console.log(json);
        }
    })
}})*/