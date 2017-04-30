$(document).ready(function(){
  var $content = $("#profile").hide();
  $("#image").on("click", function(e){
     $content.slideToggle();
  });
});