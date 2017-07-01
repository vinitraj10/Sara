(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $(document).on('click', 'a.page-scroll', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 100
    });
    $(window).on('scroll',function(){
        var Top = $(window).scrollTop();
        if (Top==0){
            $('#mainNav').removeClass('affix');
        }
        else{
            $('#mainNav').addClass('affix');
        }
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

  

})(jQuery); // End of use strict
// JavaScript
window.sr = ScrollReveal({reset:true});
sr.reveal('.foo-1', { duration: 1500 }, 50);
sr.reveal('.foo-2', { duration: 1600 }, 50);
sr.reveal('.foo-3', { duration: 1700 }, 50);
sr.reveal('.bar-1', { duration: 1800 }, 50);
sr.reveal('.bar-2', { duration: 1900 }, 50);
sr.reveal('.bar-3', { duration: 2000 }, 50);
/* activate sidebar */
/* activate sidebar */
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})