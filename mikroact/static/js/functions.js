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
