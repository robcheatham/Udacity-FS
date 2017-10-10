$(document).ready(function() {
    $('.toggle-nav').click(function(e) {
        $(this).toggleClass('active');
        $('.close-nav').toggleClass('active');
        $('.menu').toggleClass('active');
        $('.map-wrapper').toggleClass('open-menu')
        e.preventDefault();
    });
    $('.close-nav').click(function(e) {
    	$(this).toggleClass('active');
    	$('.toggle-nav').toggleClass('active');
    	$('.menu').toggleClass('active');
    	$('.map-wrapper').toggleClass('open-menu');
    	e.preventDefault();
    })
});