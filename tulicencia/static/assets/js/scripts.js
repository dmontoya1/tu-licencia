
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
	toastr.options = {
		"closeButton": false,
		"debug": false,
		"newestOnTop": false,
		"progressBar": false,
		"positionClass": "toast-top-full-width",
		"preventDuplicates": false,
		"onclick": null,
		"showDuration": "300",
		"hideDuration": "1000",
		"timeOut": "5000",
		"extendedTimeOut": "1000",
		"showEasing": "swing",
		"hideEasing": "linear",
		"showMethod": "fadeIn",
		"hideMethod": "fadeOut"
	  }
    
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
		switch(tramits['licence_1']['tramit']) {
			case 'FL':
				$('.resume-T1').text(`Primera licencia - ${tramits['licence_1']['licence']}`)
				break;
			case 'SL':
				$('.resume-T1').text(`Segunda licencia - ${tramits['licence_1']['licence']}`)
				break;
			case 'RN':
				$('.resume-T1').text(`Renovar licencia - ${tramits['licence_1']['licence']}`)
				break;
			case 'RC':
				$('.resume-T1').text(`Recategorizar licencia - ${tramits['licence_1']['licence']}`)
				break;
			default:
				console.log('Default')
		}
		switch(tramits['licence_2']['tramit']) {
			case 'FL':
				$('.resume-T2').text(`Primera licencia - ${tramits['licence_2']['licence']}`)
				break;
			case 'SL':
				$('.resume-T2').text(`Segunda licencia - ${tramits['licence_2']['licence']}`)
				break;
			case 'RN':
				$('.resume-T2').text(`Renovar licencia - ${tramits['licence_2']['licence']}`)
				break;
			case 'RC':
				$('.resume-T2').text(`Recategorizar licencia - ${tramits['licence_2']['licence']}`)
				break;
			default:
				console.log('Default')
		}
		var licence = ""
    	if( next_step ) {
			$.each(licences, function(i, v){
				licence += (`${v},`)
			})
			var params_crc = {
				state: $('#states').val(),
				age: age,
				gender: gender,
				licences: licence
			}
			crc_filter(params_crc)
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
	
	// next step 3
    $('.f1 .btn-step-3').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
		var next_step = true;
		var cea_trigger = false;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
		var licence = ""
		if (crc == ""){
			next_step = false;
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar un Centro de reconocimiento para hacerte los exámenes',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			})
		}
    	if( next_step ) {
			$.each(licences, function(i, v){
				licence += (`${v},`)
			})

			var params_cea = {
				tramit_1: tramit_type1,
				tramit_2: tramit_type2,
				state: $('#states').val(),
				age: age,
				gender: gender,
				licences: licence,
				licences__licence__category__in: licence,
			}
			loadVehicleSelect(licence)
			cea_filter(params_cea)
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
			if (tramit_type1 === 'RN' && (tramit_type2 === 'RN' || tramit_type2 == '')){
				$('.f1 .btn-step-4').trigger('click')
			}
    	}
    	
	});
	
	// next step 4
    $('.f1 .btn-step-4').on('click', function() {
		function next_step_fn(){
			var params = {
				state: $('#states').val(),
			}
			transit_filter(params)
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
    	var parent_fieldset = $(this).parents('fieldset');
		var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
		var progress_line = $(this).parents('.f1').find('.f1-progress-line');
		if (tramit_type1 === 'RN' && (tramit_type2 === 'RN' || tramit_type2 == '')){
			setTimeout(function(){
				next_step_fn();
				current_active_step.removeClass('active').addClass('activated').next().addClass('active');
				// progress bar
				bar_progress(progress_line, 'right');
				// show next step
				$(this).next().fadeIn();
			}, 700);
		}
		else if (cea == ""){
			next_step = false;
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar un Centro de enseñanza para hacer tu curso',
				type: 'error',
				showCancelButton: false,
				confirmButtonText: 'Ok'
			});
		}
    	if( next_step ) {
			next_step_fn();
    	}
    	
	});

	// next step 5
    $('.f1 .btn-step-5').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
		var progress_line = $(this).parents('.f1').find('.f1-progress-line');
		if (transit == ""){
			next_step = false;
			swal({
				title: 'Atención',
				text: 'Para continuar debes seleccionar un Organismo de tránsito ',
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
