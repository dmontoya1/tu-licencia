
function scroll_to_class(element_class, removed_height) {
	var scroll_to = $(element_class).offset().top - removed_height;
	if($(window).scrollTop() != scroll_to) {
		$('html, body').stop().animate({scrollTop: scroll_to}, 0);
	}
}

function bar_progress(progress_line_object, direction) {
	var number_of_steps = progress_line_object.data('number-of-steps');
	var now_value = progress_line_object.data('now-value');
	var new_value = 0;
	if(direction == 'right') {
		new_value = now_value + ( 100 / number_of_steps );
	}
	else if(direction == 'left') {
		new_value = now_value - ( 100 / number_of_steps );
	}
	progress_line_object.attr('style', 'width: ' + new_value + '%;').data('now-value', new_value);
}

jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */

    $.backstretch("/static/images/fondo.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
    
    /*
        Form
    */
    $('.f1 fieldset:first').fadeIn('slow');
    
    $('.f1 input[type="text"], .f1 input[type="password"], .f1 textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    // next step 1
    $('.f1 .btn-step-1').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
		

		
		/* 
		if ($('#cities').val() == "" || $('#cities').val() == null){
			next_step = false;
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar tu ubicación (Departamento y ciudad)',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			})
		}

		if (age == ""){
			next_step = false;
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar tu fecha de nacimiento',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			}).then((result) => {
				if (result.value) {
					$('html, body, #licence-request-form').animate({
						scrollTop: $('#birthdate-select').offset().top
					}, 1000);
				}
			})
		}

		if (gender == ""){
			next_step = false;			
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar tu género',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			  }).then((result) => {
				if (result.value) {
					scroll_to_class( $('.choice-gender'), 20 );
				}
			  })

		}
		*/

    	if( next_step ) {
    		parent_fieldset.fadeOut(400, function() {
    			// change icons
    			current_active_step.removeClass('active').addClass('activated').next().addClass('active');
    			// progress bar
    			bar_progress(progress_line, 'right');
    			// show next step
	    		$(this).next().fadeIn();
	    		// scroll window to beginning of the form
    			scroll_to_class( $('.f1'), 20 );
	    	});
    	}
    	
	});
	
	// next step 2
    $('.f1 .btn-step-2').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');

		if (runt == ""){
			next_step = false;
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar si estas inscrito en el RUNT',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			}).then((result) => {
				if (result.value) {
					$('html, body, #licence-request-form').animate({
						scrollTop: $('#birthdate-select').offset().top
					}, 1000);
				}
			})
		}

		if (car){
			if (!('car' in licences)){
				next_step = false;			
				swal({
					title: 'Atención',
					text: 'Debes seleccionar la licencia para carro que vas a tramitar',
					type: 'error',
					showCancelButton: false,
					confirmButtonText: 'Ok'
				})
			}
		}
		if (bike){
			if (!('bike' in licences)){
				next_step = false;			
				swal({
					title: 'Atención',
					text: 'Debes seleccionar la licencia para moto que vas a tramitar',
					type: 'error',
					showCancelButton: false,
					confirmButtonText: 'Ok'
				})
			}
		}
		if (!(bike) && !(car)){
			next_step = false;			
			swal({
				title: 'Atención',
				text: 'Debes seleccionar el tipo de licencia que vas a tramitar',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			})
		}
		if (tramit == ""){
			next_step = false;
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar el trámite que deseas realizar',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			}).then((result) => {
				if (result.value) {
					$('html, body, #licence-request-form').animate({
						scrollTop: $('#birthdate-select').offset().top
					}, 1000);
				}
			})
		}

    	if( next_step ) {
			
    		parent_fieldset.fadeOut(400, function() {
    			// change icons
    			current_active_step.removeClass('active').addClass('activated').next().addClass('active');
    			// progress bar
    			bar_progress(progress_line, 'right');
    			// show next step
	    		$(this).next().fadeIn();
	    		// scroll window to beginning of the form
    			scroll_to_class( $('.f1'), 20 );
	    	});
    	}
    	
    });
    
    // previous step
    $('.f1 .btn-previous').on('click', function() {
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
    	
    	$(this).parents('fieldset').fadeOut(400, function() {
    		// change icons
    		current_active_step.removeClass('active').prev().removeClass('activated').addClass('active');
    		// progress bar
    		bar_progress(progress_line, 'left');
    		// show previous step
    		$(this).prev().fadeIn();
    		// scroll window to beginning of the form
			scroll_to_class( $('.f1'), 20 );
    	});
    });
    
    // submit
    
});
