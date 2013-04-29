//MAIN FUNCTIONS


function accordionAction(panel){
	console.log($(panel).siblings());
	
	if($(panel).hasClass('open')){
	
		$(panel).siblings().removeClass('closed');
		$(panel).siblings().children('div:nth-child(2)').css('opacity', '1');
		$(panel).removeClass('open');
	}
	else if($(panel).hasClass('closed')){
		$(panel).removeClass('closed');
		$(panel).children('div:nth-child(2)').css('opacity', '1');
		$(panel).siblings().removeClass('open');
	}
	else{
		
		$(panel).siblings().children('div:nth-child(2)').css('opacity', '0');
		$(panel).addClass('open');
		$(panel).siblings().addClass('closed');
	}
}

function createSlugs(){
	// FIXME could be neater JS...
	$("#id_slug").each(function() {
		$(this).slugify("#id_" + $(this).data("slug-from"));
	})
}
$(function () {
    $('#actTab a:last').tab('show');
  })
  
  
$(document).ready(function(){
	$('.feature img').css('opacity','1');
	
	$("a[data-toggle=popover]").popover({ 
		html : true,
		content : function() {
	      return $('#popover_content_wrapper').html();
	    }	
	})
      .click(function(e) {
        e.preventDefault()
      });
      
    
    
});

$(function(){
	$(".activity li a").click(function(){
	    $(this).addClass('visited');
    });
})