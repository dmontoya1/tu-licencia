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

loadStatesSelect();

function clearLicences(){
    $('#toggleA1')[0].checked = false;
    $('#toggleA2')[0].checked = false;
    $('#toggleB1')[0].checked = false;
    $('#toggleC1')[0].checked = false;
    $('#toggleC2')[0].checked = false;
    $('#toggleC3')[0].checked = false;
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
    licences = {}
    bike = false
    car = false
    tramit_type1 = ""
    tramit_type2 = ""
    tramits['licence_1'] = ""
    tramits['licence_2'] = ""
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

$('select.cities-crc').on('change', function(){
    selected = $(this)
    loadCRCSectorSelect(selected.val())
})

$('select.cities-cea').on('change', function(){
    selected = $(this)
    loadCEASectorSelect(selected.val())
})

$('select.cities-transit').on('change', function(){
    selected = $(this)
    loadTransitSectorSelect(selected.val())
})

function loadVehicleSelect(licences){
    vehicle_params: {
        
    }
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

function crc_filter(params){
    axios.get('/api/companies/crc', {
        params: params
    })
    .then(function (response) {
        data = response.data;
        if (data.length > 0){
            $('.crc-list').empty()
            $.each(data, function(i, v){
                if(data.logo == null){
                    logo = "../static/images/logo1.png"
                }
                else{
                    logo = data.logo
                }
                $('.crc-list').append(
                    `
                    <div class="col-12 col-xl-6">
                        <button type="button" class="company-detail-crc" data-id="${v.id}" data-company="crc">
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
                                                <p class="weigh-5">$${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                            <span class="subtitle d-block pb-3">Horarios de atención</span>
                                            <div class="d-flex flex-row d-normal">
                                                <div class="pr-2">
                                                <span class="subtitle d-block">Luneas a viernes:</span>
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
                        <button type="button" class="company-detail-cea" data-id="${v.id}" data-company="cea">
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
                                                <p class="weigh-5">$${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                            <span class="subtitle d-block pb-3">Horarios de atención</span>
                                            <div class="d-flex flex-row d-normal">
                                                <div class="pr-2">
                                                    <span class="subtitle d-block">Lunes a viernes:</span>
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
                        <button type="button" class="company-detail" data-id="${v.id}" data-company="transit">
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
                                                <p class="weigh-5">$${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                            <span class="subtitle d-block pb-3">Horarios</span>
                                            <div class="d-flex flex-row d-normal">
                                                <div class="pr-2">
                                                <span class="subtitle d-block">Luneas a viernes:</span>
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
            $('.company-detail').on('click', function(){
                var licence = ""
                $.each(licences, function(i, v){
                    licence += (`${v},`)
                })
                id = $(this).data('id')
                company = $(this).data('company')
                url = `api/companies/${company}/${id}`
                axios.get(url)
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
                    $('.add-cart').data('name', data.name);
                    $('.add-cart').data('price', data.final_price);
                    $('.add-cart').data('company', company);

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
            $(".toggleC1").addClass('disabled');
            $("input#toggleC1").attr('disabled', true);
            $(".toggleC2").addClass('disabled');
            $("input#toggleC2").attr('disabled', true);
            $("toggleC3").addClass('disabled');
            $("input#toggleC3").attr('disabled', true);
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

})


function get_age(){
    swal({
        title: 'Atención',
        text: 'Si cambias tu fecha de nacimiento, los precios mostrados de los servicios pueden cambiar',
        type: 'warning',
        showCancelButton: false,
        confirmButtonText: 'Ok'
    })
    birth_date = `${$('#month-1').val()}-${$('#day-1').val()}-${$('#year-1').val()}`
    dob = new Date(birth_date);
    var today = new Date();
    age = Math.floor((today-dob) / (365.25 * 24 * 60 * 60 * 1000));
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
        $(".toggleC1").addClass('disabled');
        $("input#toggleC1").attr('disabled', true);
        $(".toggleC2").addClass('disabled');
        $("input#toggleC2").attr('disabled', true);
        $("toggleC3").addClass('disabled');
        $("input#toggleC3").attr('disabled', true);
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

$('#day-1').on('change', function(e){
    get_age()
})
$('#month-1').on('change', function(e){
    get_age()
})
$('#year-1').on('change', function(e){
    get_age()
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
        
        if($(this).val() == 'RC' ){
            if (!($('.content-bike').hasClass('d-none'))){
                $('.content-bike').addClass('d-none')
            }
            $('.licences-bikes').addClass('d-none')
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
            })
        }
        
        if (tramit_type1 == ""){
            tramit_type1 = $(this).val()
            $('.option-' + tramit_type1).addClass('option--selected');
            setTimeout(function(){ 
                $('.element--second-licence').addClass('d-none');
                $('.element--vehicle-type').removeClass('d-none');
            }, 700);
        }
        else{
            if (jQuery.isEmptyObject(licences)){
                $(this)[0].checked = false;
                swal({
                    title: 'Atención',
                    text: 'Primero selecciona la licencia para tu primer categoría',
                    type: 'error',
                    showCancelButton: false,
                    confirmButtonText: 'Ok'
                })
            }
            else{
                $('.option-' + $(this).val()).addClass('option--selected')
                if ('bike' in licences){
                    $('.bike-licences').toggleClass('d-none')
                    $('.bikelicence').toggleClass('disabled')
                    if ($('.carlicence').hasClass('disabled')){
                        $('.carlicence').removeClass('disabled')
                    }
                }
                else{
                    $('.car-licences').toggleClass('d-none')
                    $('.carlicence').toggleClass('disabled')
                    if(!($(this).val() == 'RC' )){
                        $('.bikelicence').toggleClass('disabled')
                    }
                }
                tramit_type2 = $(this).val()
                $('.option-' + tramit_type1).addClass('option--selected');
                setTimeout(function(){ 
                    $('.element--second-licence').addClass('d-none')
                    $('.element--vehicle-type').removeClass('d-none')
                }, 700);
            }
            
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
    if(tramit_type1 == 'SL'){
        if ($('#car-licence').hasClass('choose--selected')){
            $('#car-licence').removeClass('choose--selected')
            car = false
        }
        if (!(bike)){
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
        if (!(bike)){
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
            $('.title-bike').removeClass('d-none')
            $('.toggleA1').removeClass('d-none')
            $('.toggleA2').removeClass('d-none')
            
        }
    }
    
})

$('#car-licence').on('click', function(ev){
    car = !car;
    if(tramit_type1 == 'SL'){
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
            $('.title-car').removeClass('d-none')
            $('.toggleB1').removeClass('d-none')
            $('.toggleC1').removeClass('d-none')
            $('.title-bike').addClass('d-none')
            $('.toggleA1').addClass('d-none')
            $('.toggleA2').addClass('d-none')
        }
    }
    else {
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
            $('.title-car').removeClass('d-none')
            $('.toggleB1').removeClass('d-none')
            $('.toggleC1').removeClass('d-none')
            if(tramit_type1 == 'RN'){
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
    else{
        $('.element--vehicle-type').addClass('d-none')
        $('.element--licence-type').removeClass('d-none')
    }
})

$('.back-licence-type').on('click', function(){
    $('.element--licence-type').addClass('d-none')
    $('.element--vehicle-type').removeClass('d-none')
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
            $('.element--have-runt').removeClass('d-none')
        }
        else{
            if(tramits['licence_2'] === ''){
                $('.element--aditional-tramit').removeClass('d-none')
            }
            else {
                $('.element--have-runt').removeClass('d-none')
            }
        }
        
    }
})

$('.new-tramit').on('click', function(){
    aditional_tramit = true
    $('li.option-'+tramit_type1).attr('disabled', true)
    setTimeout(function(){ 
        $('.element--aditional-tramit').addClass('d-none')
        $('.element--second-licence').removeClass('d-none')
    }, 700);
})

$('.no-more-tramit').on('click', function(){
    setTimeout(function(){ 
        $('.element--aditional-tramit').addClass('d-none')
        $('.element--have-runt').removeClass('d-none')
    }, 700);
})

$('.back-aditional-tramit').on('click', function(){
    $('.element--aditional-tramit').addClass('d-none')
    $('.element--licence-type').removeClass('d-none')
})


$('.back-have-runt').on('click', function(){
    $('.element--have-runt').addClass('d-none')
    if(tramit_type1 == 'FL'){
        $('.element--licence-type').removeClass('d-none')
    }
    else{
        if(tramits['licence_2'] === ''){
            $('.element--aditional-tramit').removeClass('d-none')
        }
        else{
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
        toastr["error"]("Debes llenar todos los campos")
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

$('button.filter-crc').on('click', function(e){
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
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
// $('#price-cea').on('change', function(){
//     if ($(this).val() === '0'){
//         delete params_cea['price']
//     }
//     else{
//         params_cea['price'] = $(this).val()
//     }
// })
$('.sector-cea').on('change', function(e){
    params_cea['sector'] = $(this).val()
})

$('button.filter-cea').on('click', function(e){
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    params_cea['state'] = $('#states').val()
    params_cea['city'] = $('.cea-city').val()
    params_cea['age']= age
    params_cea['gender']= gender
    params_cea['licences']= licence
    params_cea['licences__licence__category__in'] = licence
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
$('button.filter-transit').on('click', function(e){
    params_transit['state'] = $('#states').val(),
    params_transit['city'] = $('.transit-city').val(),
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
    if (submit){
        var lic = []
        $.each(licences, function(i, v){
            lic.push(v)
        })
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
        },

        form_data = {
            "user": user,
            "cea": cea,
            "crc": crc,
            "transit": transit,
            'payment_type': payment_type,
            "licences": lic,
            "runt":runt,
            "paper":paper,
            "cea_price":cea_price,
            "crc_price": crc_price,
            "transit_price": transit_price,
            "tramits": tramits
        }
        
        if (payment_type == "CR"){
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
                console.log("Error")
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
