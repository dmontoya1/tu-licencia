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

licences_car = ['B1', 'C1', 'C2', 'C2']
licences_bike = ['A1', 'A2']

function initMap(lat1, lon1) {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 20,
        center: {lat: user_lat, lng: user_lon}
    });
    directionsDisplay.setMap(map);

    calculateAndDisplayRoute(directionsService, directionsDisplay, lat1, lon1);
}

function initMap2(lat1, lon1) {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map2'), {
        zoom: 20,
        center: {lat: user_lat, lng: user_lon}
    });
    directionsDisplay.setMap(map);

    calculateAndDisplayRoute(directionsService, directionsDisplay, lat1, lon1);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay, lat, lon) {
    var start = `${user_lat}, ${user_lon}`;
    var end = `${lat}, ${lon}`;
    directionsService.route({
        origin: start,
        destination: end,
        travelMode: 'DRIVING'
    }, function(response, status) {
        if (status === 'OK') {
        directionsDisplay.setDirections(response);
        } else {
            console.log('Directions request failed due to ' + status)
        }
    });
}

function loadStatesSelect(){
    $.ajax({
        type: "GET",
        url:"/api/manager/states",
        success:function(data)
        {   
            $('select#states').empty()
            $(data).each(function(i, v){
                $('select#states').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select#states').prepend(
                `<option value="" selected disabled>Seleccione un Departamento</option>`
            )
        },
    });
        
}

function loadCitiesSelect(state_id){
    $.ajax({
        type: "GET",
        url:"/api/manager/city/"+state_id+"/",
        success:function(data)
        {   
            $('#cities').empty()
            $(data).each(function(i, v){
                $('#cities').append(
                    `<li class="col-12 col-md-6"> <span>*</span> ${v.name} </li>`
                )
            })

            $('select.city-select').empty()
            $(data).each(function(i, v){
                $('select.city-select').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.city-select').prepend(
                `<option value="" disabled selected>Filtro por ciudad</option>`+
                `<option value="0"> Ver todos</option>`
            )
            $('#city-user').empty()
            $(data).each(function(i, v){
                $('#city-user').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('#city-user').prepend(
                `<option value="" disabled selected>Selecciona tu ciudad de residencia</option>`
            )
            $('.content-municip').removeClass('d-none')
        },
    });     
}

function loadCRCSectorSelect(cityId){
    $.ajax({
        type: "GET",
        url:"/api/manager/sector/"+cityId+"/",
        success:function(data)
        {   
            $('select.sector-crc').empty()
            $(data).each(function(i, v){
                $('select.sector-crc').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.sector-crc').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`+
                `<option value="0"> Ver todos</option>`
            )
        },
    });     
}

function loadCRCSectorSelect1(cityId){
    $.ajax({
        type: "GET",
        url:"/api/manager/sector/"+cityId+"/",
        success:function(data)
        {   
            $('select.sector-crc-1').empty()
            $(data).each(function(i, v){
                $('select.sector-crc-1').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.sector-crc-1').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`+
                `<option value="0"> Ver todos</option>`
            )
        },
    });     
}

function loadCEASectorSelect(cityId){
    $.ajax({
        type: "GET",
        url:"/api/manager/sector/"+cityId+"/",
        success:function(data)
        {   
            $('select.sector-cea').empty()
            $(data).each(function(i, v){
                $('select.sector-cea').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.sector-cea').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`+
                `<option value="0"> Ver todos</option>`
            )
        },
    });
}

function loadCEASectorSelect1(cityId){
    $.ajax({
        type: "GET",
        url:"/api/manager/sector/"+cityId+"/",
        success:function(data)
        {   
            $('select.sector-cea-1').empty()
            $(data).each(function(i, v){
                $('select.sector-cea-1').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.sector-cea-1').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`+
                `<option value="0"> Ver todos</option>`
            )
        },
    });
}

function loadTransitSectorSelect(cityId){
    $.ajax({
        type: "GET",
        url:"/api/manager/sector/"+cityId+"/",
        success:function(data)
        {   
            $('select.sector-transit').empty()
            $(data).each(function(i, v){
                $('select.sector-transit').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.sector-transit').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`+
                `<option value="0"> Ver todos</option>`
            )
        },
    });
}

function loadTransitSectorSelect1(cityId){
    $.ajax({
        type: "GET",
        url:"/api/manager/sector/"+cityId+"/",
        success:function(data)
        {   
            $('select.sector-transit-1').empty()
            $(data).each(function(i, v){
                $('select.sector-transit-1').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.sector-transit-1').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`+
                `<option value="0"> Ver todos</option>`
            )
        },
    });
        
}

loadStatesSelect();

function clearLicences(){
    $('#toggleA1')[0].checked = false;
    $('#toggleA1').removeAttr('selected')
    $('#toggleA2')[0].checked = false;
    $('#toggleA2').removeAttr('selected')
    $('#toggleB1')[0].checked = false;
    $('#toggleB1').removeAttr('selected')
    $('#toggleC1')[0].checked = false;
    $('#toggleC1').removeAttr('selected')
    $('#toggleC2')[0].checked = false;
    $('#toggleC2').removeAttr('selected')
    $('#toggleC3')[0].checked = false;
    $('#toggleC3').removeAttr('selected')
    $('.check-A1').removeClass('check-pass--selected')
    $('.check-A2').removeClass('check-pass--selected')
    $('.check-B1').removeClass('check-pass--selected')
    $('.check-C1').removeClass('check-pass--selected')
    $('.check-C2').removeClass('check-pass--selected')
    $('.check-C3').removeClass('check-pass--selected')
    $('.title-bike').addClass('d-none')
    $('.toggleA1').addClass('d-none')
    $('.toggleA2').addClass('d-none')
    $('.title-car').addClass('d-none')
    $('.toggleB1').addClass('d-none')
    $('.toggleC1').addClass('d-none')
    $('.toggleC2').addClass('d-none')
    $('.toggleC3').addClass('d-none')
    $('.option-SL').removeClass('option--selected')
    $('.option-RN').removeClass('option--selected')
    $('.option-RC').removeClass('option--selected')
    $('.option-DU').removeClass('option--selected')
    $('#car-licence').removeClass('choose--selected')
    $('#bike-licence').removeClass('choose--selected')
    $('.content-car').removeClass('d-none')
    $('.content-bike').removeClass('d-none')
    $('.si-runt').removeClass('d-none')
    $('.no-runt').removeClass('d-none')
    $('li.option-SL').removeClass('d-none')
    $('li.option-RN').removeClass('d-none')
    if (age >= 18){
        $('li.option-RC').removeClass('d-none')
    }
    $('.no-more-tramit').removeClass('choose--selected')
    $('.new-tramit').removeClass('choose--selected')
    clearCart()
    licences = {}
    bike = false
    car = false
    tramit_type1 = ""
    tramit_type2 = ""
    runt = ""
    crc = ""
    cea = ""
    transit = ""
    tramits['licence_1'] = ""
    tramits['licence_2'] = ""
    cea_price = ""
    crc_price = ""
    transit_price = ""
    tramits = {'licence_1':'', 'licence_2':''}
    tramit_type1 = ""
    tramit_type2 = ""
    paper = ""
    aditional_tramit = false
    actual_tramit = ''
    confirm_t1 = false
    confirm_l1 = ""
    confirm_t2 = false
    confirm_l2 = ""
}

function clearTramit(tramit){
    var licence = ""
    if(tramit != 'SL' ){
        $('.toggleC1').addClass('d-none')
        $('.row-C3').addClass('d-none')
    }
    switch (tramit) { 
        case 'SL': 
            if (tramit_type1 == tramit && tramit_type2 == ""){
                tramit_type1 = ""
            }
            else{
                if (tramit_type1 == tramit){
                    tramit_type1 = tramit_type2
                    tramit_type2 = ""
                }
                else{
                    tramit_type2 = ""
                }
            }
            if (tramits['licence_1']['tramit'] == tramit && tramits['licence_2'] == ""){
                licence = tramits['licence_1']['licence']
                tramits['licence_1'] = ""
                tramit_type1 = ""
                $('.licence-vehicle').toggleClass('d-none')
            }
            else {
                if (tramits['licence_1']['tramit'] == tramit){
                    licence = tramits['licence_1']['licence']
                    tramits['licence_1'] = tramits['licence_2']
                    tramits['licence_2'] = ""
                }
                else {
                    if (tramits['licence_2']['tramit'] == tramit){
                        licence = tramits['licence_2']['licence']
                        tramits['licence_2'] = ""
                    }
                }
            }
            if (licence != ""){
                bike = jQuery.inArray( licence, ['A1', 'A2'] )
                car = jQuery.inArray( licence, ['B1', 'C1', 'C2', 'C3'] )
                if (bike != -1){
                    $('ul.bike-licences').addClass('d-none')
                    $('li.bikelicence span.imgCheckbox0').removeClass('imgChked');
                    $('li.carlicence').removeClass('disabled');
                }
                else{
                    if (car != -1){
                        $('ul.car-licences').addClass('d-none')
                        $('li.carlicence span.imgCheckbox0').removeClass('imgChked');
                        $('li.bikelicence').removeClass('disabled');
                    }
                }
                $('#toggle'+licence)[0].checked = false;
                $('.check-'+licence).removeClass('check-pass--selected')
            }
            else{
                $('.licence-vehicle').addClass('d-none')
            }
            break;
        case 'RN': 
            if (tramit_type1 == tramit && tramit_type2 == ""){
                clearLicences()
            }
            else{
                if (tramit_type1 == tramit){
                    tramit_type1 = tramit_type2
                    tramit_type2 = ""
                }
                else{
                    tramit_type2 = ""
                }
            }
            if ((tramits['licence_1']['tramit'] == tramit && tramits['licence_2']['tramit'] == tramit) ||
                (tramits['licence_1']['tramit'] == tramit && tramits['licence_2'] == "")){
                    clearLicences()
            }
            else{
                if (tramits['licence_1']['tramit'] == tramit && tramits['licence_2'] != ""){
                    licence = tramits['licence_1']['licence']
                    tramits['licence_1'] = ""
                    tramit_type1 = ""
                    $('.licence-vehicle').toggleClass('d-none')
                }
                else {
                    if (tramits['licence_1']['tramit'] == tramit){
                        licence = tramits['licence_1']['licence']
                        tramits['licence_1'] = tramits['licence_2']
                        tramits['licence_2'] = ""
                    }
                    else {
                        if (tramits['licence_2']['tramit'] == tramit){
                            licence = tramits['licence_2']['licence']
                            tramits['licence_2'] = ""
                        }
                    }
                }
                if (licence != ""){
                    bike = jQuery.inArray( licence, ['A1', 'A2'] )
                    car = jQuery.inArray( licence, ['B1', 'C1', 'C2', 'C3'] )
                    if (bike != -1){
                        $('ul.bike-licences').addClass('d-none')
                        $('li.bikelicence span.imgCheckbox0').removeClass('imgChked');
                        $('li.carlicence').removeClass('disabled');
                    }
                    else{
                        if (car != -1){
                            $('ul.car-licences').addClass('d-none')
                            $('li.carlicence span.imgCheckbox0').removeClass('imgChked');
                            $('li.bikelicence').removeClass('disabled');
                        }
                    }
                    $('#toggle'+licence)[0].checked = false;
                }
            }
            break;
        case 'RC': 
            $('.bikelicence').removeClass('disabled')
            $('.toggleB1').removeClass('d-none')
            if (tramit_type1 == tramit && tramit_type2 == ""){
                clearLicences()
            }
            else{
                if (tramit_type1 == tramit){
                    tramit_type1 = tramit_type2
                    tramit_type2 = ""
                }
                else{
                    tramit_type2 = ""
                }
            }
            if ((tramits['licence_1']['tramit'] == tramit && tramits['licence_2']['tramit'] == tramit) ||
                (tramits['licence_1']['tramit'] == tramit && tramits['licence_2'] == "")){
                    clearLicences()
            }
            else{
                if (tramits['licence_1']['tramit'] == tramit && tramits['licence_2'] != ""){
                    licence = tramits['licence_1']['licence']
                    tramits['licence_1'] = ""
                    tramit_type1 = ""
                    $('.licence-vehicle').toggleClass('d-none')
                }
                else {
                    if (tramits['licence_1']['tramit'] == tramit){
                        licence = tramits['licence_1']['licence']
                        tramits['licence_1'] = tramits['licence_2']
                        tramits['licence_2'] = ""
                    }
                    else {
                        if (tramits['licence_2']['tramit'] == tramit){
                            licence = tramits['licence_2']['licence']
                            tramits['licence_2'] = ""
                        }
                    }
                }
                if (licence != ""){
                    bike = jQuery.inArray( licence, ['A1', 'A2'] )
                    car = jQuery.inArray( licence, ['B1', 'C1', 'C2', 'C3'] )
                    if (bike != -1){
                        $('ul.bike-licences').addClass('d-none')
                        $('li.bikelicence span.imgCheckbox0').removeClass('imgChked');
                        $('li.carlicence').removeClass('disabled');
                    }
                    else{
                        if (car != -1){
                            $('ul.car-licences').addClass('d-none')
                            $('li.carlicence span.imgCheckbox0').removeClass('imgChked');
                            $('li.bikelicence').removeClass('disabled');
                        }
                    }
                    $('#toggle'+licence)[0].checked = false;
                }
            }
            break;
        default:
            console.log('Default');
    }
}

function loadVehicleSelect(licences){
    axios.get('/api/vehicles/vehicles/', {
        params: {
            licences: licences
        }
    })
    .then(function (response) {
        data = response.data;
        $('.vehicle-select').empty()
        if (data.length > 0){
            $.each(data, function(i, v){
                $('.vehicle-select').append(
                    `
                        <option value="${v.line}">${v.brand.name} - ${v.line}</option>
                    `
                )
            })
            $('.vehicle-select').append(
                `
                    <option value="" disabled selected>Filtro vehículos</option>
                `
            )
        }
        else {
            $('.vehicle-select').empty()
            $('.vehicle-select').append(
                '<option value="" disabled> No hay vehículos disponibles</option>'
            )
        }
    })
    .catch(function (error) {
        console.log(error);
    })
}

function clearCart(){
    cea = ""
    crc = ""
    transit = ""
    cea_price = ""
    crc_price = ""
    transit_price = ""
    $('.content-summary').empty()
    $('.content-summary').append(
        `
            <div class="header-summary"> 
                <img src="/static/assets/img/car.svg" width="25" class="mr-2" alt="">Resumen del servicio
                <div class="licences-resume">
                    <span class="resume-T1">
                    </span>
                    <span class="resume-T2">
                    </span>
                </div>
            </div>
            <div class="without-adding">No se han añadido elementos al carrito de compras </div>
            <ul class="list-summary d-none">
                <li class="d-flex flex-row cart-crc" data-value="0">
                </li>
                <li class="d-flex flex-row cart-cea" data-value="0">
                </li>
                <li class="d-flex flex-row cart-transit" data-value="0">
                </li>
            </ul>
            <p class="mb-0 pl-3 pr-3 pb-2 text-right"><strong>Total: $<span class="total-price">0</span></strong></p>
        `
    )
}

var gender = ""
var birth_date = ""
var age = ""
var tramit = ""
var licences = {}
var bike = false
var car = false
var runt = ""
var crc = ""
var cea = ""
var transit = ""
var cea_price = ""
var crc_price = ""
var transit_price = ""
var tramits = {'licence_1':'', 'licence_2':''}
var tramit_type1 = ""
var tramit_type2 = ""
var paper = ""
var payment_type = ""
var aditional_tramit = false
var actual_tramit = ''
var confirm_t1 = false
var confirm_t2 = false

function crc_filter(params){
    axios.get('/api/companies/crc', {
        params: params
    })
    .then(function (response) {
        data = response.data;
        if (data.length > 0){
            $('.crc-list').empty()
            $.each(data, function(i, v){
                if(v.logo == null){
                    logo = "/static/images/logo1.png"
                }
                else{
                    logo = v.logo
                }
                $('.crc-list').append(
                    `
                    <div class="col-12 col-xl-6">
                        <button type="button" class="company-detail-crc" data-id="${v.id}" data-company="crc" style="background-color: #fff; border: 1px solid #ddd;">
                            <div class="d-flex flex-row content-result rounded mb-2">
                                <div class="thumbnail mr-2 mb-4">
                                    <div class="img" style="background-image: url(${logo});background-size: contain;"></div>
                                        <div class="qualification">
                                            <span class="subtitle d-block">Calificación</span>
                                            <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>                            
                                        </div>
                                    </div>
                                    <div class="result-body">
                                        <h4 class="text-small"><span>${v.name}</span></h4>
                                        <div class="d-flex flex-row">
                                            <div class="price  pr-2">
                                                <span class="subtitle d-block">Valor examen</span>
                                                <p class="weigh-5 crc-price">${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                            <span class="subtitle d-block pb-1">Horarios de atención</span>
                                            <div class="d-flex flex-row d-normal">
                                                <div class="pr-2">
                                                <p class="text mb-1">${v.schedule}
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="subtitle d-block">Dirección:</span>
                                <p class="p-text">${v.address}</p>
                                </div>
                            </button>
                        </div>
                    </div> 
                    `
                )
            })
            $('.crc-price').priceFormat({
                centsLimit: 0,
                prefix: '$',
                thousandsSeparator: '.',
            });
            $('.company-detail-crc').on('click', function(){
                var licence = ""
                $.each(licences, function(i, v){
                    licence += (`${v},`)
                })
                id = $(this).data('id')
                company = $(this).data('company')
                url = `api/companies/${company}/${id}`
                axios.get(url, {
                    params: {
                      age: age,
                      gender: gender,
                      licences:licence,
                    }
                })
                .then(function (response) {
                    data = response.data
                    if(data.logo == null){
                        logo = "/static/images/logo1.png"
                    }
                    else{
                        logo = data.logo
                    }

                    $('.company-logo').attr('src', logo)
                    $('.company-name').text(data.name)
                    $('.company-address').text(data.address)
                    $('.company-sector').text(data.sector.name)
                    $('.company-location').text(`${data.city.name}, ${data.city.state.name}`)
                    $('.company-schedule').text(data.schedule)
                    $('.company-phone').text(data.cellphone)
                    $('.company-rating').text(data.rating)
                    $('.company-rating-count').text(`(${data.count_rating})`)
                    $('.company-price').text(`$ ${data.final_price}`)
                    $('.price-title').text('Valor examen')
                    $('.add-cart').data('id', data.id);
                    $('.add-cart').data('name', data.name);
                    $('.add-cart').data('price', data.final_price);
                    $('.add-cart').data('company', company);

                    initMap(data.lat, data.lon)
                    $('.company-price').priceFormat({
                        centsLimit: 0,
                        prefix: '$',
                        thousandsSeparator: '.',
                    });
                    $('.DetailModal').modal('show')

                })
                .catch(function (error) {
                    console.log(error);
                })
            })
        
        }

        else {
            $('.crc-list').empty()
            $('.crc-list').append(
                '<h3 style="padding:25px;">No se han encontrado Centros de reconocimientos de conductores en tu localidad. '+
                'Intenta nuevamente con un nuevo departamento o ciudad</h3>'
            )
        }
    })
    .catch(function (error) {
        console.log(error);
    })
}

function cea_filter(params){
    axios.get('/api/companies/cea', {
        params : params
    })
    .then(function (response) {
        data = response.data;
        if (data.length > 0){
            $('.cea-list').empty()
            $.each(data, function(i, v){
                if(v.logo == null){
                    logo = '/static/images/logo1.png'
                }
                else{
                    logo = v.logo
                }
                $('.cea-list').append(
                    `

                    <div class="col-12 col-xl-6">
                        <button type="button" class="company-detail-cea" data-id="${v.id}" data-company="cea" style="background-color: #fff; border: 1px solid #ddd;">
                            <div class="d-flex flex-row content-result rounded mb-2">
                                <div class="thumbnail mr-2 mb-4">
                                    <div class="img" style="background-image: url(${logo});background-size: contain;"></div>
                                        <div class="qualification">
                                            <span class="subtitle d-block">Calificación</span>
                                            <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>                            
                                        </div>
                                    </div>
                                    <div class="result-body">
                                        <h4 class="text-small"><span>${v.name}</span></h4>
                                        <div class="d-flex flex-row">
                                            <div class="price  pr-2">
                                                <span class="subtitle d-block">Valor curso de conducción</span>
                                                <p class="weigh-5 cea-price">${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                            <span class="subtitle d-block pb-1">Horarios de atención</span>
                                            <div class="d-flex flex-row d-normal">
                                                <div class="pr-2">
                                                    <p class="text mb-1">${v.schedule}
                                                    </p>
                                                </div>
                                                <div class="saturday">
                                                    <span class="subtitle d-block">horarios de cursos:</span>
                                                    <p class="text mb-0">${v.courses_schedule}</p>
                                                </div>
                                            </div>
                                     </div>
                                    </div>
                                    <span class="subtitle d-block">Dirección:</span>
                                    <p class="p-text">${v.address}</p>
                                </div>
                            </button>
                        </div>
                    </div>

                    `
                )
            })
            $('.cea-price').priceFormat({
                centsLimit: 0,
                prefix: '$',
                thousandsSeparator: '.',
            });
            $('.company-detail-cea').on('click', function(){
                var licence = ""
                $.each(licences, function(i, v){
                    licence += (`${v},`)
                })
                id = $(this).data('id')
                company = $(this).data('company')
                url = `api/companies/${company}/${id}`
                axios.get(url, {
                    params: {
                      age: age,
                      gender: gender,
                      licences:licence,
                      tramit_1:tramit_type1,
                      tramit_2: tramit_type2,
                    }
                })
                .then(function (response) {
                    data = response.data
                    if(data.logo == null){
                        logo = "/static/images/logo1.png"
                    }
                    else{
                        logo = data.logo
                    }
                    $('.company-logo').attr('src', logo)
                    $('.company-name').text(data.name)
                    $('.company-address').text(data.address)
                    $('.company-sector').text(data.sector.name)
                    $('.company-location').text(`${data.city.name}, ${data.city.state.name}`)
                    $('.company-schedule-atention').text(data.schedule)
                    $('.company-schedule-classes').text(data.courses_schedule)
                    $('.company-phone').text(data.cellphone)
                    $('.company-rating').text(data.rating)
                    $('.company-rating-count').text(`(${data.count_rating})`)
                    $('.company-price').text(`$ ${data.final_price}`)
                    $('.add-cart').data('id', data.id);
                    $('.add-cart').data('name', data.name);
                    $('.add-cart').data('price', data.final_price);
                    $('.add-cart').data('company', company);
                    $('.vehicle-list').empty()
                    $.each(data.vehicles, function(i, v){
                        try{
                            logo_vehicle = v.vehicle.images[0].image
                        }
                        catch(error){
                            logo_vehicle = '/static/vehicles/car1.png'
                        }
                        $('.vehicle-list').append(
                            `
                            <div class=" col-12 col-md-6 col-lg-2 vehicle-detail">
                                <div class="card">
                                    <div class="card-img">
                                        <img class="card-img-top" src="${logo_vehicle}" alt="Card image cap">
                                    </div>
                                    <div class="card-body card-body-detail">
                                        <p class="card-text">${v.vehicle.brand.name} ${v.vehicle.line}</p>
                                    </div>
                                </div>
                            </div>
        
                            `
                        )
                    })
                    initMap2(data.lat, data.lon)
                    $('.company-price').priceFormat({
                        centsLimit: 0,
                        prefix: '$',
                        thousandsSeparator: '.',
                    });
                    $('.DetailModal1').modal('show')

                })
                .catch(function (error) {
                    console.log(error);
                })
            })
        }
        else {
            $('.cea-list').empty()
            $('.cea-list').append(
                '<h3 style="padding:25px;">No se han encontrado Centros de enseñanza en tu localidad. '+
                'Intenta nuevamente con un nuevo departamento y ciudad</h3>'
            )
        }
    })
    .catch(function (error) {
        console.log(error);
    })
}

function transit_filter(params){
    axios.get('/api/companies/transit', {
        params: params
    })
    .then(function (response) {
        data = response.data;
        $('.transit-list').empty()
        if (data.length > 0){
            const starTotal = 5;
            $.each(data, function(i, v){
                if(v.logo == null){
                    logo = '/static/logos/movilidad.png'
                }
                else{
                    logo = v.logo
                }
                $('.transit-list').append(
                    `
                    <div class="col-12 col-xl-6">
                        <button type="button" class="company-detail" data-id="${v.id}" data-company="transit" style="background-color: #fff; border: 1px solid #ddd;">
                            <div class="d-flex flex-row content-result rounded mb-2">
                                <div class="thumbnail mr-2 mb-4">
                                    <div class="img" style="background-image: url(${logo});background-size: contain;"></div>
                                        <div class="qualification">
                                            <span class="subtitle d-block">Calificación</span>
                                            <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>                            
                                        </div>
                                    </div>
                                    <div class="result-body">
                                        <h4 class="text-small"><span>${v.name}</span></h4>
                                        <div class="d-flex flex-row">
                                            <div class="price  pr-2">
                                                <span class="subtitle d-block">Valor expedición</span>
                                                <p class="weigh-5 transit-price">${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                            <span class="subtitle d-block pb-1">Horarios</span>
                                            <div class="d-flex flex-row d-normal">
                                                <div class="pr-2">
                                                <p class="text mb-1">${v.schedule}
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="subtitle d-block">Dirección:</span>
                                <p class="p-text">${v.address}</p>
                                </div>
                            </button>
                        </div>
                    </div>
                    `
                )
            })
            $('.transit-price').priceFormat({
                centsLimit: 0,
                prefix: '$',
                thousandsSeparator: '.',
            });
            $('.company-detail').on('click', function(){
                var licence = ""
                $.each(licences, function(i, v){
                    licence += (`${v},`)
                })
                id = $(this).data('id')
                company = $(this).data('company')
                url = `api/companies/${company}/${id}`
                axios.get(url, {
                    params: {
                        licences:licence,
                        tramit_1:tramit_type1,
                        tramit_2: tramit_type2,
                    }
                })
                .then(function (response) {
                    data = response.data
                    if(data.logo == null){
                        logo = "/static/images/logo1.png"
                    }
                    else{
                        logo = data.logo
                    }
                    $('.company-logo').attr('src', logo)
                    $('.company-name').text(data.name)
                    $('.company-address').text(data.address)
                    $('.company-sector').text(data.sector.name)
                    $('.company-location').text(`${data.city.name}, ${data.city.state.name}`)
                    $('.company-schedule').text(data.schedule)
                    $('.company-phone').text(data.cellphone)
                    $('.company-rating').text(data.rating)
                    $('.company-rating-count').text(`(${data.count_rating})`)
                    $('.company-price').text(`$ ${data.final_price}`)
                    $('.add-cart').data('id', data.id);
                    $('.price-title').text('Valor expedición')
                    $('.add-cart').data('name', data.name);
                    $('.add-cart').data('price', data.final_price);
                    $('.add-cart').data('company', company);

                    initMap(data.lat, data.lon)
                    $('.company-price').priceFormat({
                        centsLimit: 0,
                        prefix: '$',
                        thousandsSeparator: '.',
                    });
                    $('.DetailModal').modal('show')

                })
                .catch(function (error) {
                    console.log(error);
                })
            })
        }
        else {
            $('.transit-list').empty()
            $('.transit-list').append(
                '<h3 style="padding:25px;">No se han encontrado organismos de tránsito en tu localidad. '+
                'Intenta nuevamente con un nuevo departamento y ciudad</h3>'
            )
        }
    })
    .catch(function (error) {
        console.log(error);
    })
}

$('select#states').on('change', function() {
    selected = $(this)
    loadCitiesSelect(selected.val())
    $('#toggle4').attr("href", `/transits/${selected.val()}`);
})

$('.continue-location').on('click', function(){
    if($('select#states').val() === null){
        swal({
            title: 'Atención',
            text: 'Debes seleccionar un departamento antes de continuar',
            type: 'error',
            showCancelButton: false,
            confirmButtonText: 'Aceptar'
        })
    }
    else{
        $('.element--location').addClass('d-none')
        $('.element--gender').addClass('animated fadeInRight')
        $('.element--gender').removeClass('d-none')
    }
})

$('.back-gender').on('click', function(){
    $('.element--gender').addClass('d-none')
    $('.element--location').addClass('animated fadeInRight')
    $('.element--location').removeClass('d-none')
})

$('.male').on('click', function(e){
    
    if ($('.female').hasClass('choose--selected')){
        $('.female').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    gender = 'M'

    setTimeout(function(){ 
        $('.element--gender').addClass('d-none')
        $('.element--birth-date').addClass('animated fadeInRight')
        $('.element--birth-date').removeClass('d-none')
    }, 700);
    

})

$('.female').on('click', function(e){
    
    if ($('.male').hasClass('choose--selected')){
        $('.male').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    gender = 'F'
    
    setTimeout(function(){ 
        $('.element--gender').addClass('d-none')
        $('.element--birth-date').addClass('animated fadeInRight')
        $('.element--birth-date').removeClass('d-none')
    }, 700);
})

$('.back-birth-date').on('click', function(){
    $('.element--birth-date').addClass('d-none')
    $('.element--gender').addClass('animated fadeInRight')
    $('.element--gender').removeClass('d-none')
    loadCitiesSelect(selected.val())

})

$('.continue-birth-date').click(() => {
    if($('#day').val() === '' || $('#month').val() === '' || $('#year').val() === '' ){
        swal({
            title: 'Atención',
            text: 'Ingresa tu fecha de nacimiento para continuar',
            type: 'error',
            showCancelButton: false,
            confirmButtonText: 'Aceptar'
        })
    }
    else {

        birth_date = `${$('#month').val()}/${$('#day').val()}/${$('#year').val()}`
        dob = new Date(birth_date);
        var today = new Date();
        age = Math.floor((today-dob) / (365.25 * 24 * 60 * 60 * 1000));
        if (isNaN(age)){
            swal({
                title: 'Error',
                text: 'Debes introducir una fecha de nacimiento válida',
                type: 'error',
                showCancelButton: false,
                confirmButtonText: 'Aceptar'
            })
        }
        else {
            $('#day-1').val($('#day').val())
            $('#month-1').val($('#month').val())
            $('#year-1').val($('#year').val())
    
            if (age == 18){
                swal({
                    title: 'Atención',
                    text: 'Tienes 18 años. Para sacar tu licencia es necesario tu documento original. No se aceptan contraseñas',
                    type: 'info',
                    showCancelButton: false,
                    confirmButtonText: 'Aceptar'
                }).then(function(){
                    $('.btn-step-1').trigger('click')
                })
            }
            else if (age < 18 && age >= 16){
                $(".toggleC1").hide();
                $(".toggleC2").hide();
                $(".toggleC3").hide();
                $('li.option-RC').hide()
                swal({
                    title: 'Atención',
                    text: 'Los menores de 18 años podrán adquirir únicamente licencias de servicio particular ( A1, A2 y B1), estarán restringidas las de servicio público (C1, C2 y C3).',
                    type: 'info',
                    showCancelButton: false,
                    confirmButtonText: 'Aceptar'
                }).then(function(){
                    $('.btn-step-1').trigger('click')
                })
            }
            else if (age < 16) {
                swal({
                    title: 'Atención',
                    text: 'La edad mínima permitida para adquirir la licencia de conducción colombiana son 16 años, no podrás continuar con el proceso hasta que no cumplas este requisito',
                    type: 'info',
                    showCancelButton: false,
                    confirmButtonText: 'Aceptar'
                })
            }
            else{
                $('.btn-step-1').trigger('click')
            }
        }   
    }
})

$('.back-tramit-type').on('click', function(){
    $('.element--birth-date').removeClass('d-none')
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
})

$('#licence-1').on('click', function(ev){
    clearLicences()
    tramit_type1 = "FL"
    $('#licence-1').addClass('choose--selected')
    if ($('#licence-2').hasClass('choose--selected')){
        $('#licence-2').removeClass('choose--selected')
    }
    setTimeout(function(){ 
        $('.element--tramit-type').addClass('d-none')
        $('.element--vehicle-type').removeClass('d-none')
    }, 700);
})

$('#licence-2').on('click', function(ev){
    clearLicences()
    tramit_type1 = ""
    $('#licence-2').addClass('choose--selected')
    if ($('#licence-1').hasClass('choose--selected')){
        $('#licence-1').removeClass('choose--selected')
    }
    setTimeout(function(){ 
        $('.element--tramit-type').addClass('d-none')
        $('.element--second-licence').removeClass('d-none')
    }, 700);
})

$('.back-vehicle-type').on('click', function(){
    $('.element--vehicle-type').addClass('d-none')
    if(tramit_type1 == 'FL'){
        $('.element--tramit-type').removeClass('d-none')
    }
    else{
        $('.option-'+tramit_type2).removeClass('option--selected')
        $('.element--second-licence').removeClass('d-none')
    }
})

$('.back-second-licence').on('click', function(){
    $('.element--second-licence').addClass('d-none')
    if (aditional_tramit){
        aditional_tramit = false
        $('.element--aditional-tramit').removeClass('d-none')
    }
    else{
        $('.element--tramit-type').removeClass('d-none')
    }
})

$('.element--second-licence input').on('click', function(ev){
    if (!($('.option-' + $(this).val()).hasClass('option--selected'))){
        
        switch($(this).val()) {
            case 'SL':
                actual_tramit = 'SL'
                if (!confirm_t1){
                    tramit_type1 = $(this).val()
                    if($('.option-RN').hasClass('option--selected')){
                        $('.option-RN').removeClass('option--selected')
                        clearTramit('RN')
                    }
                    if($('.option-RC').hasClass('option--selected')){
                        $('.option-RC').removeClass('option--selected')
                        clearTramit('RC')
                    }
                    $('#car-licence').removeClass('choose--selected')
                    $('#bike-licence').removeClass('choose--selected')
                    $('.content-car').removeClass('d-none')
                    $('.content-bike').removeClass('d-none')
                    car = false
                    bike = false
                    $('.option-' + tramit_type1).addClass('option--selected');
                    swal({
                        title: 'Atención',
                        type: 'info',
                        html:
                            'Selecciona  la nueva categoría que quieres aprender a conducir, podrás elegir entre moto categorías A1 y A2 y carro categorías B1 y C1.<br>'+
                            'Para categorías C2 y C3 consulta la opción “Subir la categoría de mi actual licencia”',
                        showCancelButton: true,
                        cancelButtonText: 'Cancelar',
                        confirmButtonText: 'Aceptar'
                    }).then((result) => {
                        if (result.value) {
                            $('.element--second-licence').addClass('d-none');
                            $('.element--vehicle-type').removeClass('d-none');
                            $('.sl-text').text('Selecciona el nuevo tipo de vehículo que quieres agregar a tu licencia de conducción')
                        } else {
                            tramit_type1 = ''
                            $('.option-SL').removeClass('option--selected');
                        }
                    })
                }
                else if (!confirm_t2){
                    if($('.option-RN').hasClass('option--selected') && tramit_type1 != 'RN'){
                        $('.option-RN').removeClass('option--selected')
                        clearTramit('RN')
                    }
                    if($('.option-RC').hasClass('option--selected') && tramit_type1 != 'RC'){
                        $('.option-RC').removeClass('option--selected')
                        clearTramit('RC')
                    }
                    tramit_type2 = $(this).val()
                    $('.option-' + tramit_type2).addClass('option--selected');
                    swal({
                        title: 'Atención',
                        type: 'info',
                        html:
                            'Selecciona  la nueva categoría que quieres aprender a conducir, podrás elegir entre moto categorías A1 y A2 y carro categorías B1 y C1.<br>'+
                            'Para categorías C2 y C3 consulta la opción “Subir la categoría de mi actual licencia”',
                        showCancelButton: false,
                        confirmButtonText: 'Aceptar'
                    }).then((result) => {
                        if (result.value) {
                            if (jQuery.inArray( confirm_l1, licences_bike ) >= 0){
                                $('.content-bike').addClass('d-none')
                                $('.licences-bikes').addClass('d-none')
                            }
                            else {
                                $('.content-bike').removeClass('d-none')
                                $('.licences-bikes').removeClass('d-none')
                            }
                            if (jQuery.inArray( confirm_l1, licences_car ) >= 0){
                                $('.content-car').addClass('d-none')
                                $('.licences-cars').addClass('d-none')
                            }
                            else {
                                $('.content-car').removeClass('d-none')
                                $('.licences-cars').removeClass('d-none')
                            }
                            $('.sl-text').text('Selecciona el nuevo tipo de vehículo que quieres agregar a tu licencia de conducción')
                            $('.element--second-licence').addClass('d-none');
                            $('.element--vehicle-type').removeClass('d-none');
                        } else {
                            tramit_type2 = ''
                            $('.option-SL').removeClass('option--selected');
                        }
                    })
                }
                break;
            case 'RC':
                actual_tramit = 'RC'
                $('.licences-bikes').addClass('d-none')
                $('.title-car').removeClass('d-none')
                $('.toggleB1').addClass('d-none')
                $('.toggleC1').removeClass('d-none')
                $('.toggleC2').removeClass('d-none')
                $('.toggleC3').removeClass('d-none')
                
                if (!confirm_t1){
                    if($('.option-SL').hasClass('option--selected')){
                        $('.option-SL').removeClass('option--selected')
                        clearTramit('SL')
                    }
                    if($('.option-RN').hasClass('option--selected')){
                        $('.option-RN').removeClass('option--selected')
                        clearTramit('RN')
                    }
                    if (!($('.content-bike').hasClass('d-none'))){
                        $('.content-bike').addClass('d-none')
                    }
                    
                    tramit_type1 = $(this).val()
                    $('.option-' + tramit_type1).addClass('option--selected');
                    swal({
                        title: 'Atención',
                        type: 'info',
                        html:
                            'Solo puedes recategorizar licencias de carros, de la siguiente manera: ' +
                            '<ul class="recat-info"> ' +
                                '<li>De B1 a C1</li>'+
                                '<li>De C1 a C2</li>'+
                                '<li>De C2 a C3</li>'+
                            '</ul>' +
                            'Debes seleccionar la licencia a la cual quieres recategorizar',
                        showCancelButton: false,
                        confirmButtonText: 'Aceptar'
                    }).then((result) => {
                        if (result.value) {
                            car = true
                            actual_tramit = 'RC'
                            $('.licences-cars').removeClass('d-none')
                            $('.title-car').removeClass('d-none')
                            $('.toggleC1').removeClass('d-none')
                            $('.toggleC2').removeClass('d-none')
                            $('.toggleC3').removeClass('d-none')
                            $('.element--second-licence').addClass('d-none');
                            $('.element--licence-type').removeClass('d-none');
                        } else {
                            $('.option-' + tramit_type1).removeClass('option--selected');
                            tramit_type1 = ''
                        }
                    })
                }
                else if (!(confirm_t2)){
                    if($('.option-RN').hasClass('option--selected') && tramit_type1 != 'RN'){
                        $('.option-RN').removeClass('option--selected')
                        clearTramit('RN')
                    }
                    if($('.option-SL').hasClass('option--selected') && tramit_type1 != 'SL'){
                        $('.option-SL').removeClass('option--selected')
                        clearTramit('SL')
                    }
                    if (jQuery.inArray( confirm_l1, licences_car ) >= 0){
                        swal({
                            title: 'Atención',
                            type: 'error',
                            text: 'Ya tienes una licencia de automóvil en proceso, no puedes realizar la recategorización',
                            showCancelButton: false,
                            confirmButtonText: 'Aceptar'
                        })
                    }
                    else{
                        tramit_type2 = $(this).val()
                        $('.option-' + tramit_type2).addClass('option--selected');
                        swal({
                            title: 'Atención',
                            type: 'info',
                            html:
                                'Solo puedes recategorizar licencias de carros, de la siguiente manera: ' +
                                '<ul class="recat-info"> ' +
                                    '<li>De B1 a C1</li>'+
                                    '<li>De C1 a C2</li>'+
                                    '<li>De C2 a C3</li>'+
                                '</ul>' +
                                'Debes seleccionar la licencia a la cual quieres recategorizar',
                            showCancelButton: false,
                            confirmButtonText: 'Aceptar'
                        }).then((result) => {
                            if (result.value) {
                                car = true
                                $('.element--second-licence').addClass('d-none');
                                $('.element--licence-type').removeClass('d-none');
                            } else {
                                $('.option-' + tramit_type1).removeClass('option--selected');
                                tramit_type1 = ''
                            }
                        })
                    }
                }
                break;
            case 'RN':
                actual_tramit = 'RN'
                if (!(confirm_t1)){
                    if($('.option-SL').hasClass('option--selected')){
                        $('.option-SL').removeClass('option--selected')
                        clearTramit('SL')
                    }
                    if($('.option-RC').hasClass('option--selected')){
                        $('.option-RC').removeClass('option--selected')
                        clearTramit('RC')
                    }
                    $('.content-car').removeClass('d-none')
                    $('.content-bike').removeClass('d-none')
                    car = false
                    bike = false
                    $('#car-licence').removeClass('choose--selected')
                    $('#bike-licence').removeClass('choose--selected')
                    tramit_type1 = $(this).val()
                    $('.option-' + tramit_type1).addClass('option--selected');
                    setTimeout(function(){
                        $('.element--second-licence').addClass('d-none');
                        $('.element--vehicle-type').removeClass('d-none'); 
                    },700);
                    
                }
                else if (!(confirm_t2)){
                    if($('.option-SL').hasClass('option--selected') && tramit_type1 != 'SL'){
                        $('.option-SL').removeClass('option--selected')
                        clearTramit('SL')
                    }
                    if($('.option-RC').hasClass('option--selected') && tramit_type1 != 'RC'){
                        $('.option-RC').removeClass('option--selected')
                        clearTramit('RC')
                    }
                    tramit_type2 = $(this).val()
                    $('.option-' + tramit_type2).addClass('option--selected');
                    
                    if (jQuery.inArray( confirm_l1, licences_bike ) >= 0){
                        $('.content-bike').addClass('d-none')
                        $('.licences-bikes').addClass('d-none')
                    }
                    else {
                        $('.content-bike').removeClass('d-none')
                        $('.licences-bikes').removeClass('d-none')
                    }
                    if (jQuery.inArray( confirm_l1, licences_car ) >= 0){
                        $('.content-car').addClass('d-none')
                        $('.licences-cars').addClass('d-none')
                    }
                    else {
                        $('.content-car').removeClass('d-none')
                        $('.licences-cars').removeClass('d-none')
                        $('.toggleC2').removeClass('d-none')
                        $('.toggleC3').removeClass('d-none')
                    }
                    setTimeout(function(){
                        $('.element--second-licence').addClass('d-none');
                        $('.element--vehicle-type').removeClass('d-none'); 
                    },700);
                }
                break;
            default:
                console.log('default')
          }
    }
    else {
        $('.option-' + $(this).val()).removeClass('option--selected');
        clearTramit($(this).val())
    }
})

$('.male').on('click', function(e){
    
    if ($('.female').hasClass('choose--selected')){
        $('.female').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    gender = 'M'

    setTimeout(function(){ 
        $('.element--gender').addClass('d-none')
        $('.element--birth-date').addClass('animated fadeInRight')
        $('.element--birth-date').removeClass('d-none')
    }, 700);
    

})

$('#bike-licence').on('click', function(ev){
    bike = !bike;
    if(tramit_type1 == 'SL' && actual_tramit == 'SL'){
        if ($('#car-licence').hasClass('choose--selected')){
            $('#car-licence').removeClass('choose--selected')
            car = false
        }
        if (!bike){
            $('#bike-licence').removeClass('choose--selected')
            if ('bike' in licences){
                delete licences['bike']
            }
            $('.title-bike').addClass('d-none')
            $('.toggleA1').addClass('d-none')
            $('.toggleA2').addClass('d-none')
            
        }
        else{
            $('#bike-licence').addClass('choose--selected')
            $('.licences-bikes').removeClass('d-none')
            $('.title-bike').removeClass('d-none')
            $('.toggleA1').removeClass('d-none')
            $('.toggleA2').removeClass('d-none')
            $('.title-car').addClass('d-none')
            $('.toggleB1').addClass('d-none')
            $('.toggleC1').addClass('d-none')
            $('.toggleC2').addClass('d-none')
            $('.toggleC3').addClass('d-none')
        }
    }
    else {
        if (!bike){
            $('#bike-licence').removeClass('choose--selected')
            if ('bike' in licences){
                delete licences['bike']
            }
            $('.title-bike').addClass('d-none')
            $('.toggleA1').addClass('d-none')
            $('.toggleA2').addClass('d-none')
            
        }
        else{
            $('#bike-licence').addClass('choose--selected')
            $('.licences-bikes').removeClass('d-none')
            $('.title-bike').removeClass('d-none')
            $('.toggleA1').removeClass('d-none')
            $('.toggleA2').removeClass('d-none')
            
        }
    }
    
})

$('#car-licence').on('click', function(ev){
    car = !car;
    if(tramit_type1 == 'SL' && actual_tramit == 'SL'){
        if ($('#bike-licence').hasClass('choose--selected')){
            $('#bike-licence').removeClass('choose--selected')
            bike = false
        }
    
        if (!(car)){
            $('#car-licence').removeClass('choose--selected')
            if ('car' in licences){
                delete licences['car']
            }
            $('.title-car').addClass('d-none')
            $('.toggleB1').addClass('d-none')
            $('.toggleC1').addClass('d-none')
            $('.toggleC2').addClass('d-none')
            $('.toggleC3').addClass('d-none')
            
        }
        else{
            $('#car-licence').addClass('choose--selected')
            $('.licences-cars').removeClass('d-none')
            $('.title-car').removeClass('d-none')
            $('.toggleB1').removeClass('d-none')
            $('.toggleC1').removeClass('d-none')
            $('.title-bike').addClass('d-none')
            $('.toggleA1').addClass('d-none')
            $('.toggleA2').addClass('d-none')
        }
    }
    else {
        if (!car){
            $('#car-licence').removeClass('choose--selected')
            if ('car' in licences){
                delete licences['car']
            }
            $('.title-car').addClass('d-none')
            $('.toggleB1').addClass('d-none')
            $('.toggleC1').addClass('d-none')
            $('.toggleC2').addClass('d-none')
            $('.toggleC3').addClass('d-none')
            
        }
        else{
            $('#car-licence').addClass('choose--selected')
            $('.licences-cars').removeClass('d-none')
            $('.title-car').removeClass('d-none')
            $('.toggleB1').removeClass('d-none')
            $('.toggleC1').removeClass('d-none')
            if(tramit_type1 == 'RN' || tramit_type2 == 'RN' || tramit_type1 == 'RC' || tramit_type2 == 'RC'){
                $('.toggleC2').removeClass('d-none')
                $('.toggleC3').removeClass('d-none')
            }
        }
    }
    
})

$('.continue-vehicle-type').on('click', function(){
    if (bike === false && car === false){
        swal({
            title: 'Atención',
            text: 'Selecciona el tipo de vehículo para continuar',
            type: 'error',
            showCancelButton: false,
            confirmButtonText: 'Aceptar'
        })
    }
    else if (tramits['licence_1'] != '' && (bike === false || car === false)){
        swal({
            title: 'Atención',
            text: 'Selecciona el tipo de vehículo para continuar',
            type: 'error',
            showCancelButton: false,
            confirmButtonText: 'Aceptar'
        })
    }
    else{
        $('.element--vehicle-type').addClass('d-none')
        $('.element--licence-type').removeClass('d-none')
    }
})

$('.back-licence-type').on('click', function(){
    if (!confirm_t1){
        deleteTramit('A1')
        deleteTramit('A2')
        deleteTramit('B1')
        deleteTramit('C1')
        deleteTramit('C2')
        deleteTramit('C3')
        $('#toggleA1')[0].checked = false;
        $('#toggleA1').removeAttr('selected')
        $('#toggleA2')[0].checked = false;
        $('#toggleA2').removeAttr('selected')
        $('#toggleB1')[0].checked = false;
        $('#toggleB1').removeAttr('selected')
        $('#toggleC1')[0].checked = false;
        $('#toggleC1').removeAttr('selected')
        $('#toggleC2')[0].checked = false;
        $('#toggleC2').removeAttr('selected')
        $('#toggleC3')[0].checked = false;
        $('#toggleC3').removeAttr('selected')
        $('.check-A1').removeClass('check-pass--selected')
        $('.check-A2').removeClass('check-pass--selected')
        $('.check-B1').removeClass('check-pass--selected')
        $('.check-C1').removeClass('check-pass--selected')
        $('.check-C2').removeClass('check-pass--selected')
        $('.check-C3').removeClass('check-pass--selected')
        $('#car-licence').removeClass('choose--selected')
        $('#bike-licence').removeClass('choose--selected')
        $('.licences-cars').addClass('d-none')
        $('.licences-bikes').addClass('d-none')
        bike = false
        car = false
        $('.no-more-tramit').removeClass('choose--selected')
        $('.new-tramit').removeClass('choose--selected')
    }
    else if (!confirm_t2){
        if (jQuery.inArray( confirm_l1, licences_bike ) >= 0){
            $('.content-bike').addClass('d-none')
            $('.licences-bikes').addClass('d-none')
            deleteTramit('B1')
            deleteTramit('C1')
            deleteTramit('C2')
            deleteTramit('C3')
            $('#toggleB1')[0].checked = false;
            $('#toggleB1').removeAttr('selected')
            $('#toggleC1')[0].checked = false;
            $('#toggleC1').removeAttr('selected')
            $('#toggleC2')[0].checked = false;
            $('#toggleC2').removeAttr('selected')
            $('#toggleC3')[0].checked = false;
            $('#toggleC3').removeAttr('selected')
            $('.check-B1').removeClass('check-pass--selected')
            $('.check-C1').removeClass('check-pass--selected')
            $('.check-C2').removeClass('check-pass--selected')
            $('.check-C3').removeClass('check-pass--selected')
        }
        else {
            $('.content-bike').removeClass('d-none')
            $('.licences-bikes').removeClass('d-none')
        }
        if (jQuery.inArray( confirm_l1, licences_car) >= 0){
            $('.content-car').addClass('d-none')
            $('.licences-cars').addClass('d-none')
            deleteTramit('A1')
            deleteTramit('A2')
            $('#toggleA1')[0].checked = false;
            $('#toggleA1').removeAttr('selected')
            $('#toggleA2')[0].checked = false;
            $('#toggleA2').removeAttr('selected')
            $('.check-A1').removeClass('check-pass--selected')
            $('.check-A2').removeClass('check-pass--selected')
        }
        else {
            $('.content-car').removeClass('d-none')
            $('.licences-cars').removeClass('d-none')
        }
    }
    else {
        confirm_t2 = false
        if (jQuery.inArray( confirm_l2, licences_car ) >= 0){
            $('.content-car').removeClass('d-none')
            $('.licences-cars').removeClass('d-none')
            $('.content-bike').addClass('d-none')
            $('.licences-bikes').addClass('d-none')
            deleteTramit('B1')
            deleteTramit('C1')
            deleteTramit('C2')
            deleteTramit('C3')
            $('#toggleB1')[0].checked = false;
            $('#toggleB1').removeAttr('selected')
            $('#toggleC1')[0].checked = false;
            $('#toggleC1').removeAttr('selected')
            $('#toggleC2')[0].checked = false;
            $('#toggleC2').removeAttr('selected')
            $('#toggleC3')[0].checked = false;
            $('#toggleC3').removeAttr('selected')
            $('.check-B1').removeClass('check-pass--selected')
            $('.check-C1').removeClass('check-pass--selected')
            $('.check-C2').removeClass('check-pass--selected')
            $('.check-C3').removeClass('check-pass--selected')
        }
        if (jQuery.inArray( confirm_l2, licences_bike) >= 0){
            $('.content-car').addClass('d-none')
            $('.licences-cars').addClass('d-none')
            deleteTramit('A1')
            deleteTramit('A2')
            $('#toggleA1')[0].checked = false;
            $('#toggleA1').removeAttr('selected')
            $('#toggleA2')[0].checked = false;
            $('#toggleA2').removeAttr('selected')
            $('.check-A1').removeClass('check-pass--selected')
            $('.check-A2').removeClass('check-pass--selected')
            $('.content-bike').removeClass('d-none')
            $('.licences-bikes').removeClass('d-none')
        }
    }
    if (actual_tramit == 'RC'){
        $('.element--licence-type').addClass('d-none')
        $('.element--second-licence').removeClass('d-none')
    }
    else {
        $('.element--licence-type').addClass('d-none')
        $('.element--vehicle-type').removeClass('d-none')
    }
})

$('.continue-licence-type').on('click', function(){
    if(( tramits['licence_1'] === "" && tramits['licence_2'] === '') || 
        (bike && car && (tramits['licence_1'] === "" || tramits['licence_2'] === ''))
        ){
            swal({
                title: 'Atención',
                text: 'Selecciona los tipos de licencia para tus vehículos para continuar',
                type: 'error',
                showCancelButton: false,
                confirmButtonText: 'Aceptar'
            })
    }
    else{
        $('.element--licence-type').addClass('d-none')
        if(tramit_type1 == 'FL'){
            confirm_t1 = true
            confirm_t2 = true
            confirm_l1 = tramits['licence_1']['licence']
            confirm_l2 = tramits['licence_2']['licence']
            $('.element--have-runt').removeClass('d-none')
        }
        else{
            if(tramits['licence_2'] === ''){
                confirm_t1 = true
                confirm_l1 = tramits['licence_1']['licence']
                $('.element--aditional-tramit').removeClass('d-none')
            }
            else {
                confirm_t2 = true
                confirm_l2 = tramits['licence_2']['licence']
                $('.element--have-runt').removeClass('d-none')
            }
        }
        
    }
})

$('.new-tramit').on('click', function(){
    if ($('.no-more-tramit').hasClass('choose--selected')){
        $('.no-more-tramit').removeClass('choose--selected')
    }
    aditional_tramit = true
    $('.new-tramit').addClass('choose--selected')
    $('li.option-'+tramit_type1).addClass('d-none')
    setTimeout(function(){ 
        $('.element--aditional-tramit').addClass('d-none')
        $('.element--second-licence').removeClass('d-none')
    }, 700);
})

$('.no-more-tramit').on('click', function(){
    if ($('.new-tramit').hasClass('choose--selected')){
        $('.new-tramit').removeClass('choose--selected')
    }
    $('.no-more-tramit').addClass('choose--selected')
    setTimeout(function(){ 
        $('.element--aditional-tramit').addClass('d-none')
        $('.element--have-runt').removeClass('d-none')
    }, 700);
})

$('.back-aditional-tramit').on('click', function(){
    confirm_t1 = false
    confirm_l1 = ''
    $('li.option-SL').removeClass('d-none')
    $('li.option-RN').removeClass('d-none')
    if (age >= 18){
        $('li.option-RC').removeClass('d-none')
    }
    $('.no-more-tramit').removeClass('choose--selected')
    $('.new-tramit').removeClass('choose--selected')
    $('.element--aditional-tramit').addClass('d-none')
    $('.element--licence-type').removeClass('d-none')
})

$('.back-have-runt').on('click', function(){
    $('.element--have-runt').addClass('d-none')
    $('.si-runt').removeClass('choose--selected')
    $('.no-runt').removeClass('choose--selected')
    if(tramit_type1 == 'FL'){
        confirm_t1 = false
        confirm_t2 = false
        confirm_l1 = ''
        confirm_l2 = ''
        $('.element--licence-type').removeClass('d-none')
    }
    else{
        if(tramits['licence_2'] === ''){
            $('.element--aditional-tramit').removeClass('d-none')
        }
        else{
            confirm_t2 = false
            confirm_l2 = ''
            $('.element--licence-type').removeClass('d-none')
        }
    }
})

$('.continue-personal-data').on('click', function(){
    if($('#first_name').val() === null || $('#first_name').val() === '' ||
    $('#last_name').val() === null || $('#last_name').val() === '' ||
    $('#doc_type').val() === null ||
    $('#document_id').val() === null || $('#document_id').val() === '' ||
    $('#day-1').val() === null || $('#day-1').val() === '' ||
    $('#month-1').val() === null || $('#month-1').val() === '' ||
    $('#year-1').val() === null || $('#year-1').val() === '' ||
    $('#cellphone').val() === null || $('#cellphone').val() === ''){
        toastr["error"]("Uno o más campos están mal diligenciados")
    }
    else{
        $('.element--personal-data').addClass('d-none')
        $('.element--auth-data').removeClass('d-none')
    }
})

$('.back-auth-data').on('click', function(){
    $('.element--auth-data').addClass('d-none')
    $('.element--personal-data').removeClass('d-none')
})

$('.send').on('click', function(e){
    
    if ($('.pick-up').hasClass('choose--selected')){
        $('.pick-up').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    paper = 'SEND'
    
    setTimeout(function(){ 
        $('.element--paper-data').addClass('d-none')
        $('.element--payment').removeClass('d-none')
    }, 700);

})

$('.pick-up').on('click', function(e){
    
    if ($('.send').hasClass('choose--selected')){
        $('.send').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    paper = 'PICK'
    
    setTimeout(function(){ 
        $('.element--paper-data').addClass('d-none')
        $('.element--payment').removeClass('d-none')
    }, 700);
})

$('.back-paper-data').on('click', function(){
    $('.element--paper-data').addClass('d-none')
    $('.element--auth-data').removeClass('d-none')
})

$('.back-payment').on('click', function(){
    $('.element--payment').addClass('d-none')
    $('.element--paper-data').removeClass('d-none')
})


function addTramit(licence){
    if (cea != "" || crc != "" || transit != ""){
        clearCart()
    }
    if (tramit_type1 != '' && tramit_type2 == ''){
        if (tramits['licence_1'] == ''){
            tramits['licence_1'] = {'tramit': tramit_type1, 'licence':licence}
        }
        else{
            tramits['licence_2'] = {'tramit': tramit_type1, 'licence':licence}
        }
    }
    else{
        if (tramits['licence_1'] == ''){
            tramits['licence_1'] = {'tramit': tramit_type2, 'licence':licence}
        }
        else{
            tramits['licence_2'] = {'tramit': tramit_type2, 'licence':licence}
        }
    }
}

function deleteTramit(licence){
    if(tramits['licence_1']['licence'] == licence){
        tramits['licence_1'] = tramits['licence_2']
        tramits['licence_2'] = ''
    }
    if(tramits['licence_2']['licence'] == licence){
        tramits['licence_2'] = ''
    }
}

// MOTOS
$('#toggleA1').on('click', function(e){
    if($(this).attr('selected')){
        delete licences['bike']
        deleteTramit($(this).data('name'))
        $(this).removeAttr('selected')
        $('.check-A1').removeClass('check-pass--selected')
    }
    else{
        if ($('#toggleA2').attr('selected')){
            $('#toggleA2').removeAttr('selected')
            $('#toggleA2')[0].checked = false;
            deleteTramit($('#toggleA2').data('name'))
            $('.check-A2').removeClass('check-pass--selected')
        }
        $(this).attr('selected', true)
        $('.check-A1').addClass('check-pass--selected')
        licences['bike'] = $(this).data('name')
        addTramit($(this).data('name'))
    }
})
$('#toggleA2').on('click', function(e){
    if($(this).attr('selected')){
        delete licences['bike']
        deleteTramit($(this).data('name'))
        $(this).removeAttr('selected')
        $('.check-A2').removeClass('check-pass--selected')
    }
    else{
        if ($('#toggleA1').attr('selected')){
            $('#toggleA1').removeAttr('selected')
            $('#toggleA1')[0].checked = false;
            deleteTramit($('#toggleA1').data('name'))
            $('.check-A1').removeClass('check-pass--selected')
        }
        $(this).attr('selected', true)
        $('.check-A2').addClass('check-pass--selected')
        licences['bike'] = $(this).data('name')
        addTramit($(this).data('name'))
    }
})

// CARROS
$('#toggleB1').on('click', function(e){
    if($(this).attr('selected')){
        delete licences['car']
        deleteTramit($(this).data('name'))
        $(this).removeAttr('selected')
        $('.check-B1').removeClass('check-pass--selected')
    }
    else{
        if ($('#toggleC1').attr('selected')){
            $('#toggleC1').removeAttr('selected')
            $('#toggleC1')[0].checked = false;
            deleteTramit($('#toggleC1').data('name'))
            $('.check-C1').removeClass('check-pass--selected')
        }
        if ($('#toggleC2').attr('selected')){
            $('#toggleC2').removeAttr('selected')
            $('#toggleC2')[0].checked = false;
            deleteTramit($('#toggleC2').data('name'))
            $('.check-C2').removeClass('check-pass--selected')
        }
        if ($('#toggleC3').attr('selected')){
            $('#toggleC3').removeAttr('selected')
            $('#toggleC3')[0].checked = false;
            deleteTramit($('#toggleC3').data('name'))
            $('.check-C3').removeClass('check-pass--selected')
        }
        $(this).attr('selected', true)
        $('.check-B1').addClass('check-pass--selected')
        licences['car'] = $(this).data('name')
        addTramit($(this).data('name'))
    }
})
$('#toggleC1').on('click', function(e){
    if($(this).attr('selected')){
        delete licences['car']
        deleteTramit($(this).data('name'))
        $(this).removeAttr('selected')
        $('.check-C1').removeClass('check-pass--selected')
    }
    else{
        if ($('#toggleB1').attr('selected')){
            $('#toggleB1').removeAttr('selected')
            $('#toggleB1')[0].checked = false;
            deleteTramit($('#toggleB1').data('name'))
            $('.check-B1').removeClass('check-pass--selected')
        }
        if ($('#toggleC2').attr('selected')){
            $('#toggleC2').removeAttr('selected')
            $('#toggleC2')[0].checked = false;
            deleteTramit($('#toggleC2').data('name'))
            $('.check-C2').removeClass('check-pass--selected')
        }
        if ($('#toggleC3').attr('selected')){
            $('#toggleC3').removeAttr('selected')
            $('#toggleC3')[0].checked = false;
            deleteTramit($('#toggleC3').data('name'))
            $('.check-C3').removeClass('check-pass--selected')
        }
        $(this).attr('selected', true)
        $('.check-C1').addClass('check-pass--selected')
        licences['car'] = $(this).data('name')
        addTramit($(this).data('name'))
    }
})
$('#toggleC2').on('click', function(e){
    if($(this).attr('selected')){
        delete licences['car']
        deleteTramit($(this).data('name'))
        $(this).removeAttr('selected')
        $('.check-C2').removeClass('check-pass--selected')
    }
    else{
        if ($('#toggleB1').attr('selected')){
            $('#toggleB1').removeAttr('selected')
            $('#toggleB1')[0].checked = false;
            deleteTramit($('#toggleB1').data('name'))
            $('.check-B1').removeClass('check-pass--selected')
        }
        if ($('#toggleC1').attr('selected')){
            $('#toggleC1').removeAttr('selected')
            $('#toggleC1')[0].checked = false;
            deleteTramit($('#toggleC1').data('name'))
            $('.check-C1').removeClass('check-pass--selected')
        }
        if ($('#toggleC3').attr('selected')){
            $('#toggleC3').removeAttr('selected')
            $('#toggleC3')[0].checked = false;
            deleteTramit($('#toggleC3').data('name'))
            $('.check-C3').removeClass('check-pass--selected')
        }
        $('.check-C2').addClass('check-pass--selected')
        $(this).attr('selected', true)
        licences['car'] = $(this).data('name')
        addTramit($(this).data('name'))
    }
})
$('#toggleC3').on('click', function(e){
    if($(this).attr('selected')){
        delete licences['car']
        deleteTramit($(this).data('name'))
        $(this).removeAttr('selected')
        $('.check-C3').removeClass('check-pass--selected')
    }
    else{
        if ($('#toggleB1').attr('selected')){
            $('#toggleB1').removeAttr('selected')
            $('#toggleB1')[0].checked = false;
            deleteTramit($('#toggleB1').data('name'))
            $('.check-B1').removeClass('check-pass--selected')
        }
        if ($('#toggleC1').attr('selected')){
            $('#toggleC1').removeAttr('selected')
            $('#toggleC1')[0].checked = false;
            deleteTramit($('#toggleC1').data('name'))
            $('.check-C1').removeClass('check-pass--selected')
        }
        if ($('#toggleC2').attr('selected')){
            $('#toggleC2').removeAttr('selected')
            $('#toggleC2')[0].checked = false;
            deleteTramit($('#toggleC2').data('name'))
            $('.check-C2').removeClass('check-pass--selected')
        }
        $(this).attr('selected', true)
        $('.check-C3').addClass('check-pass--selected')
        licences['car'] = $(this).data('name')
        addTramit($(this).data('name'))
    }
})

$('.si-runt').on('click', function(e){
    if ($('.no-runt').hasClass('choose--selected')){
        $('.no-runt').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    runt = 'si'
    
    setTimeout(function(){ 
        $('.element--have-runt').addClass('d-none')
        $('.btn-step-2').trigger('click')
    }, 700);
})

$('.no-runt').on('click', function(e){
    if ($('.si-runt').hasClass('choose--selected')){
        $('.si-runt').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    runt = 'no'
    
    setTimeout(function(){ 
        $('.element--have-runt').addClass('d-none')
        $('.element--runt').removeClass('d-none')
    }, 700);
})

$('.back-runt').on('click', function(){
    $('.element--runt').addClass('d-none')
    $('.element--have-runt').removeClass('d-none')
})

$('.continue-runt').on('click', function(){
    $('.element--runt').addClass('d-none')
    $('.btn-step-2').trigger('click')
})

$('.back-crc').on('click', function() {
    $('.element--have-runt').removeClass('d-none')
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
})


$('select.cities-crc').on('change', function(){
    selected = $(this)
    loadCRCSectorSelect(selected.val())
})

$('select.cities-crc-1').on('change', function(){
    selected = $(this)
    loadCRCSectorSelect1(selected.val())
})

$('select.cities-cea').on('change', function(){
    selected = $(this)
    loadCEASectorSelect(selected.val())
})

$('select.cities-cea-1').on('change', function(){
    selected = $(this)
    loadCEASectorSelect1(selected.val())
})

$('select.cities-transit').on('change', function(){
    selected = $(this)
    loadTransitSectorSelect(selected.val())
})

$('select.cities-transit-1').on('change', function(){
    selected = $(this)
    loadTransitSectorSelect1(selected.val())
})


var params_crc = {}
$('.sector-crc').on('change', function(e){
    params_crc['sector'] = $(this).val()
})
$('.rating-crc').on('change', function(){
    if ($(this).val() === '0'){
        delete params_crc['rating']
    }
    else{
        params_crc['rating'] = $(this).val()
    }
})

$('.sector-crc-1').on('change', function(e){
    params_crc['sector'] = $(this).val()
})
$('.rating-crc-1').on('change', function(){
    if ($(this).val() === '0'){
        delete params_crc['rating']
    }
    else{
        params_crc['rating'] = $(this).val()
    }
})

$('button.filter-crc').on('click', function(e){
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    if ($('.name-crc').val() != ''){
        params_crc['name']= $('.name-crc').val()
    }
    params_crc['state']= $('#states').val()
    params_crc['city']= $('.cities-crc').val()
    params_crc['age']= age
    params_crc['gender']= gender
    params_crc['licences']= licence
    crc_filter(params_crc)
})
$('button.filter-crc-1').on('click', function(e){
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    if ($('.name-crc-1').val() != ''){
        params_crc['name']= $('.name-crc-1').val()
    }
    params_crc['state']= $('#states').val()
    params_crc['city']= $('.cities-crc-1').val()
    params_crc['age']= age
    params_crc['gender']= gender
    params_crc['licences']= licence
    crc_filter(params_crc)
})

var licence = ""
$.each(licences, function(i, v){
    licence += (`${v},`)
})

var params_cea = {}
$('.vehicle-cea').on('change', function(e){
    params_cea['vehicles__vehicle__line'] = $(this).val()
})
$('.rating-cea').on('change', function(){
    if ($(this).val() === '0'){
        delete params_cea['rating']
    }
    else{
        params_cea['rating'] = $(this).val()
    }
})
$('.sector-cea').on('change', function(e){
    params_cea['sector'] = $(this).val()
})
$('.vehicle-cea-1').on('change', function(e){
    params_cea['vehicles__vehicle__line'] = $(this).val()
})
$('.rating-cea-1').on('change', function(){
    if ($(this).val() === '0'){
        delete params_cea['rating']
    }
    else{
        params_cea['rating'] = $(this).val()
    }
})

$('.sector-cea-1').on('change', function(e){
    params_cea['sector'] = $(this).val()
})

$('button.filter-cea').on('click', function(e){
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    if ($('.name-cea').val() != ''){
        params_cea['name']= $('.name-cea').val()
    }
    params_cea['state'] = $('#states').val()
    params_cea['city'] = $('.cities-cea').val()
    params_cea['age']= age
    params_cea['gender']= gender
    params_cea['licences']= licence
    params_cea['licences__licence__category__in'] = licence
    params_cea['tramit_1'] = tramit_type1
    params_cea['tramit_2'] = tramit_type2
    cea_filter(params_cea)
})

$('button.filter-cea-1').on('click', function(e){
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    if ($('.name-cea-1').val() != ''){
        params_cea['name']= $('.name-cea-1').val()
    }
    params_cea['state']= $('#states').val()
    params_cea['city']= $('.cities-cea-1').val()
    params_cea['age']= age
    params_cea['gender']= gender
    params_cea['licences']= licence
    params_cea['tramit_1'] = tramit_type1
    params_cea['tramit_2'] = tramit_type2
    cea_filter(params_cea)
})

var params_transit = {}
$('.rating-transit').on('change', function(){
    if ($(this).val() === '0'){
        delete params_transit['rating']
    }
    else{
        params_transit['rating'] = $(this).val()
    }
})
$('.sector-transit').on('change', function(e){
    params_transit['sector'] = $(this).val()
})

$('.rating-transit-1').on('change', function(){
    if ($(this).val() === '0'){
        delete params_transit['rating']
    }
    else{
        params_transit['rating'] = $(this).val()
    }
})
$('.sector-transit-1').on('change', function(e){
    params_transit['sector'] = $(this).val()
})
$('button.filter-transit').on('click', function(e){
    if ($('.name-transit').val() != ''){
        params_transit['name']= $('.name-transit').val()
    }
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    params_transit['state'] = $('#states').val(),
    params_transit['city'] = $('.cities-transit').val(),
    params_transit['tramit_1'] = tramit_type1,
    params_transit['tramit_2'] = tramit_type2,
    params_transit['licences'] = licence,
    transit_filter(params_transit)
})
$('button.filter-transit-1').on('click', function(e){
    if ($('.name-transit-1').val() != ''){
        params_transit['name']= $('.name-transit-1').val()
    }
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    params_transit['state'] = $('#states').val(),
    params_transit['city'] = $('.cities-transit').val(),
    params_transit['tramit_1'] = tramit_type1,
    params_transit['tramit_2'] = tramit_type2,
    params_transit['licences'] = licence,
    transit_filter(params_transit)
})

$('.no-licence').on('click', function(e){
    if (tramit == ""){
        tramit = "first_licence"
    }
    else {
        tramit = ""
    }
}) 

$('.online').on('click', function(e){
    $('btn-finish').removeClass('d-none')
    if($(this).hasClass('choose--selected')){
        payment_type = ""
        $(this).removeClass('choose--selected')
    }
    else{
        if ($('.credit').hasClass('choose--selected')){
            $('.credit').removeClass('choose--selected')
        }
        $(this).addClass('choose--selected')
        payment_type = 'CO'
    }
})
$('.credit').on('click', function(e){
    $('btn-finish').removeClass('d-none')
    if($(this).hasClass('choose--selected')){
        payment_type = ""
        $(this).removeClass('choose--selected')
    }
    else{
        if ($('.online').hasClass('choose--selected')){
            $('.online').removeClass('choose--selected')
        }
        $(this).addClass('choose--selected')
        payment_type = 'CR'
    }
})

$('#licence-request-form').on('submit', function(e){
    e.preventDefault();
    submit = true
    payment_value =  parseInt($('.total-price').last().unmask())
    payment_type2 = ''
    payment_value2 = 0
    if(payment_type == ""){
        submit = false
        swal({
            title: 'Atención',
            text: 'Selecciona tu medio de pago',
            type: 'error',
            showCancelButton: false,
            confirmButtonText: 'Ok'
        })
    }
    else if (payment_type == 'EXU'){
        total_exu = parseInt($('#payment-value-1').val()) + parseInt($('#payment-value-2').val())
        if (payment_value !== total_exu){
            submit = false
            swal({
                title: 'Atención',
                text: 'El valor total y el valor de los pagos no coincide. ',
                type: 'error',
                showCancelButton: false,
                confirmButtonText: 'Ok'
            })
        }
    }
    if (submit){
        console.log(payment_type)
        if (payment_type == "CR" || payment_type == 'EXU'){
            var lic = []
            $.each(licences, function(i, v){
                lic.push(v)
            })
            if (payment_type == 'EXU'){
                payment_type = $('#payment-type-1').val()
                payment_value = parseInt($('#payment-value-1').val())
                if ($('#payment-type-2').val() != ''){
                    payment_type2 = $('#payment-type-2').val()
                    payment_value2 = parseInt($('#payment-value-2').val())
                }
            }
            user = {
                "first_name": $('#first_name').val(),
                "last_name": $('#last_name').val(),
                "email": $('#email').val(),
                "password": $('#pass1').val(),
                "gender": gender,
                "document_type": $('#doc_type :selected').val(),
                "document_id": $('#doc_id').val(),
                "cellphone": $('#cellphone').val(),
                "phone_number": $('#phone_number').val(),
                "address": $('#address').val(),
                "state": $('#states').val(),
                "city": $('#city-user').val(),
                "birth_date": birth_date
            }
            form_data = {
                "user": user,
                "cea": cea,
                "crc": crc,
                "transit": transit,
                'payment_type': payment_type,
                'payment_value': payment_value,
                'payment_type2': payment_type2,
                'payment_value2': payment_value2,
                "licences": lic,
                "runt":runt,
                "paper":paper,
                "cea_price":cea_price,
                "crc_price": crc_price,
                "transit_price": transit_price,
                "tramits": tramits
            } 
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            var csrftoken = getCookie('csrftoken');
            axios.defaults.headers.common['X-CSRFToken'] = csrftoken;
            axios.post('/api/request/', form_data)
            .then(function (response) {
                data = response.data;
                swal({
                    title: 'Felicitaciones!',
                    html:
                        'Tu solicitud se ha creado exitosamente. Dirigete al punto de TuLicencia mas cercano para validar tu solicitud de crédito <br/><br/>' +
                        `Tu código de solicitud es <strong>${data.booking}</strong>`,
                    type: 'success',
                    showCancelButton: false,
                    confirmButtonText: 'Finalizar'
                }).then((result) => {
                    if (result.value) {
                        if ($('#pass1').val() === ''){
                            window.location.reload();
                        }
                        else {
                            window.location.replace(`/profile`);
                        }
                    }
                })
            })
            .catch(function (error) {
                console.log(error);
            })
        }
        else{
            $('.gender-input').val(gender)
            $('.birthday-input').val(birth_date)
            $('.runt-input').val(runt)
            $('.cea-input').val(cea)
            $('.crc-input').val(crc)
            $('.transit-input').val(transit)
            $('.cea-price-input').val(cea_price)
            $('.crc-price-input').val(crc_price)
            $('.transit-price-input').val(transit_price)
            $('.licence-1-input').val(tramits['licence_1']['licence'])
            $('.tramit-1-input').val(tramits['licence_1']['tramit'])
            $('.paper-input').val(paper)
            if (tramits['licence_2'] != ''){
                $('.licence-2-input').val(tramits['licence_2']['licence'])
                $('.tramit-2-input').val(tramits['licence_2']['tramit'])
            }

            $('#licence-request-form').off()
            $('#licence-request-form').submit()
        }

    }
    
})
