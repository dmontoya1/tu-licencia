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
            $('select#cities').empty()
            $(data).each(function(i, v){
                $('select#cities').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select#cities').prepend(
                `<option value="" disabled selected>Seleccione una ciudad</option>`
            )

            $('select.city-select').empty()
            $(data).each(function(i, v){
                $('select.city-select').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select.city-select').prepend(
                `<option value="" disabled selected>Filtro por ciudad</option>`
            )
        },
    });
        
}

function loadCRCSectorSelect(cityId){
    $.ajax({
        type: "GET",
        url:"/api/manager/sector/"+cityId+"/",
        success:function(data)
        {   
            $('select#sector-crc').empty()
            $(data).each(function(i, v){
                $('select#sector-crc').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select#sector-crc').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`
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
            $('select#sector-cea').empty()
            $(data).each(function(i, v){
                $('select#sector-cea').append(
                    `<option value="${v.id}">${v.name}</option>`
                )
            })
            $('select#sector-cea').prepend(
                `<option value="" selected disabled>Seleccione un sector</option>`
            )
        },
    });
        
}

loadStatesSelect();

function clearLicences(){
    console.log("Clear Licence")
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
                    console.log("Licence Bike ")
                    $('ul.bike-licences').addClass('d-none')
                    $('li.bikelicence span.imgCheckbox0').removeClass('imgChked');
                    $('li.carlicence').removeClass('disabled');
                }
                else{
                    if (car != -1){
                        console.log("Licence CAR ")
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
                    console.log("solo RC")
                    clearLicences()
            }
            else{
                console.log("Elseeee")
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
                        console.log("Licence Bike ")
                        $('ul.bike-licences').addClass('d-none')
                        $('li.bikelicence span.imgCheckbox0').removeClass('imgChked');
                        $('li.carlicence').removeClass('disabled');
                    }
                    else{
                        if (car != -1){
                            console.log("Licence CAR ")
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
    console.log("Tramits sale: ")
    console.warn(tramits)
}

$('select#cities-crc').on('change', function(){
    selected = $(this)
    loadCRCSectorSelect(selected.val())
})

$('select#cea-city').on('change', function(){
    selected = $(this)
    loadCEASectorSelect(selected.val())
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

function crc_filter(params){
    axios.get('/api/companies/crc', {
        params: params
    })
    .then(function (response) {
        console.log(response.data)
        data = response.data;
        if (data.length > 0){
            $('.crc-list').empty()
            $.each(data, function(i, v){
                if(v.logo == null){
                    logo = '/static/images/logo1.png'
                }
                else{
                    logo = v.logo
                }
                $('.crc-list').append(
                    `
                        <div class="col-12 col-xl-6">
                            <button type="button" class="company-detail" data-id="${v.id}" data-company="crc" data-toggle="modal" data-target=".crcDetailModal-${v.id}">
                                <div class="d-flex flex-row content-result rounded mb-2">
                                    <div class="thumbnail mr-2 mb-4">
                                        
                                        <img src="${logo}" width="90" height="90" alt="Logo Company">
                                        <div class="qualification">
                                            <span class="subtitle d-block">Calificación</span>
                                            <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>                            
                                        </div>
                                    </div>
                                    <div class="result-body">
                                        <h4 class="text-small"><span>${v.name}</span></h4>
                                        <div class="d-flex flex-row">
                                            <div class="price  pr-2">
                                                <span class="subtitle d-block">Precio</span>
                                                <p class="weigh-5">$${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                                <span class="subtitle d-block pb-3">Horarios</span>
                                                <div class="d-flex flex-row d-normal">
                                                    <div class="pr-2">
                                                        <span class="subtitle d-block">Luneas a viernes:</span>
                                                        <p class="text mb-1">08:00 AM - 12:00 PM y 2:00 PM - 6:00 PM</p>
                                                    </div>
                                                    <div class="saturday">
                                                        <span class="subtitle d-block">Sábado:</span>
                                                        <p class="text mb-0">08:00 AM - 12:00 PM </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <span class="subtitle d-block">Descripción:</span>
                                        <p class="p-text">Lorem ipsum dolor sit amet </p>
                                    </div>
                                </div>
                            </a>
                        </div>

                        <div class="modal fade crcDetailModal-${v.id}" tabindex="-1" role="dialog" aria-labelledby="companyDetailModalTitle" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
                                <div class="modal-content">
                                    <div class="modal-body">
                                        <div class="col-sm-12 col-md-12 col-lg-12 form-box">
                                            <div class="detail-crc">
                                                <h3 class="crc-big-title">Detalle</h3>
                                                <div class="row crc-info justify-content-around mb-4">
                                                    <div class="col-sm-12 col-md-c-4 justify-content-center mb-4">
                                                        <div class="image-crc">
                                                            <img class="company-logo mx-auto d-block mt-4 img-fluid" width=200 height=200 src="${logo}" alt="Logo Company">
                                                        </div>
                                                        <div class="select-button mt-3">
                                                            <button type="button" class="btn-select add-cart-crc" data-id="${v.id}" data-name='${v.name}' data-price='${v.final_price}' >Seleccionar</button>
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-12 col-md-c-8 info-crc mb-4">
                                                        <div class="row crc-title">
                                                            <div class="col-12">
                                                                <span>${v.name}</span>
                                                            </div>
                                                            
                                                        </div>
                                                        <div class="row details">
                                                            <div class="col-12 col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/ubicacion/res/mipmap-mdpi/ubicacion.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Dirección: <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            ${v.address}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-12 col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/ciudad/res/mipmap-mdpi/ciudad.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Sector: ${v.sector.name} <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            ${v.city.name}, ${v.city.state.name}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-12 col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/horario/res/mipmap-mdpi/horario.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Horario <br>
                                                                            Lunes a Viernes <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            08:00 AM - 12:00 PM <br>
                                                                            02:00 PM - 06:00 PM
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-12 col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/telefono/res/mipmap-mdpi/telefono.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Teléfono <br>
                                                                        </span>
                                                                        <span>
                                                                            ${v.cellphone}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-12 col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Calificación <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-12 col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/precio/res/mipmap-mdpi/precio.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Precios <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            $ ${v.final_price}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="row map">
                                                    <div class="col-12">
                                                        <div style="width: 100%">
                                                            <iframe 
                                                                width="100%"
                                                                height="400"
                                                                src="https://www.google.com/maps/embed/v1/directions
                                                                ?key=AIzaSyBVpHZAXJYLpgCIuXAvb4HZSo0cT4wklIY
                                                                &origin=Pereira+Risaralda+Colombia
                                                                &destination=${v.address}+Pereira+Risaralda+Colombia
                                                                &avoid=tolls|highways&output=embed"
                                                                frameborder="0" scrolling="no" marginheight="0" marginwidth="0">
                                                            </iframe>
                                                        </div>
                                                        <br />
                                                    </div>
                                                </div>
                                            </div>    
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                    `
                )
            })
            $('.add-cart-crc').on('click', function(){
                crc = $(this).data('id')
                crc_name = $(this).data('name')
                crc_price = $(this).data('price')

                function addCrc(){
                    $('li.cart-crc').empty()
                    $('li.cart-crc').append(
                        `
                            <div class="media w-100">
                                <img class="align-self-top mr-2" src="/static/assets/img/img-check.svg" width="35">
                                <div class="media-body">
                                    <h6 class="mt-0 mb-0 text-small">CRC</h6>
                                    <p class="mb-0 text-small">${crc_name}</p>
                                    <p class="mb-0 text-small">$${crc_price}</p>
                                </div>
                            </div>
                            <a href="#" class="align-self-center"><i class="material-icons">edit</i></a>
                        `
                    )
                    $('li.cart-crc').data('value', crc)
                    toastr["success"](`Se ha añadido ${crc_name} al carrito de compras`)
                    setTimeout(function(){ 
                        $('.modal').modal('hide')
                        $('.btn-step-3').trigger('click')
                    }, 2000);
                }
                if ($('li.cart-crc').data('value') == '0')
                {
                    addCrc();
                }
                else{
                    swal({
                        title: 'Momento',
                        text: "Ya tienes un CRC en el carrito. Deseas agregar este y eliminar el anterior?",
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#162d40',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Si, agregar',
                        reverseButtons: true
                    }).then((result) => {
                        if (result.value) {
                            addCrc();
                        }
                    })
                }
                
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
                            <button type="button" class="company-detail" data-id="${v.id}" data-company="cea" data-toggle="modal" data-target=".ceaDetailModal-${v.id}">
                                <div class="d-flex flex-row content-result rounded mb-2">
                                    <div class="thumbnail mr-2 mb-4">
                                        
                                        <img src="${logo}" width="90" height="90" alt="Logo Company">
                                        <div class="qualification">
                                            <span class="subtitle d-block">Calificación</span>
                                            <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>                            
                                        </div>
                                    </div>
                                    <div class="result-body">
                                        <h4 class="text-small"><span>${v.name}</span></h4>
                                        <div class="d-flex flex-row">
                                            <div class="price  pr-2">
                                                <span class="subtitle d-block">Precio</span>
                                                <p class="weigh-5">$${v.final_price}</p>
                                            </div>
                                            <div class="schedule pl-2 pr-2">
                                                <span class="subtitle d-block pb-3">Horarios</span>
                                                <div class="d-flex flex-row d-normal">
                                                    <div class="pr-2">
                                                        <span class="subtitle d-block">Luneas a viernes:</span>
                                                        <p class="text mb-1">08:00 AM - 12:00 PM y 2:00 PM - 6:00 PM</p>
                                                    </div>
                                                    <div class="saturday">
                                                        <span class="subtitle d-block">Sábado:</span>
                                                        <p class="text mb-0">08:00 AM - 12:00 PM </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <span class="subtitle d-block">Descripción:</span>
                                        <p class="p-text">Lorem ipsum dolor sit amet </p>
                                    </div>
                                </div>
                            </a>
                        </div>

                        <div class="modal fade ceaDetailModal-${v.id}" tabindex="-1" role="dialog" aria-labelledby="companyDetailModalTitle" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
                                <div class="modal-content">
                                    <div class="modal-body">
                                        <div class="col-sm-12 col-md-12 col-lg-12 form-box">
                                            <div class="detail-crc">
                                                <h3 class="crc-big-title">Detalle</h3>
                                                <div class="row crc-info justify-content-around mb-4">
                                                    <div class="col-sm-12 col-md-c-4 justify-content-center mb-4">
                                                        <div class="image-crc">
                                                            <img class="company-logo mx-auto d-block mt-4 img-fluid" width=200 height=200 src="${logo}" alt="Logo Company">
                                                        </div>
                                                        <div class="select-button mt-3">
                                                            <button type="button" class="btn-select add-cart-cea" data-id="${v.id}" data-name='${v.name}' data-price='${v.final_price}' >Seleccionar</button>
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-12 col-md-c-8 info-crc mb-4">
                                                        <div class="row crc-title">
                                                            <div class="col-12">
                                                                <span>${v.name}</span>
                                                            </div>
                                                            
                                                        </div>
                                                        <div class="row details">
                                                            <div class="col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/ubicacion/res/mipmap-mdpi/ubicacion.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Dirección: <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                        ${v.address}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/ciudad/res/mipmap-mdpi/ciudad.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Sector ${v.sector.name}<br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            ${v.city.name}, ${v.city.state.name}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/horario/res/mipmap-mdpi/horario.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Horario <br>
                                                                            Lunes a Viernes <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            08:00 AM - 12:00 PM <br>
                                                                            02:00 PM - 06:00 PM
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/telefono/res/mipmap-mdpi/telefono.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Teléfono <br>
                                                                        </span>
                                                                        <span>
                                                                            ${v.cellphone}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Calificación <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-lg-6">
                                                                <div class="row">
                                                                    <div class="col-3 img-location">
                                                                        <img src="/static/icons/precio/res/mipmap-mdpi/precio.png" width="30" height="30">
                                                                    </div>
                                                                    <div class="col-8 item">
                                                                        <span class="item-title">
                                                                            Precio <br>
                                                                        </span>
                                                                        <span class="item-detail">
                                                                            $ ${v.final_price}
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="row vehicles">
                                                    <div class="col-3 col-sm-2 col-md-1 img-location mt-3">
                                                        <img src="/static/icons/vehiculos/res/mipmap-mdpi/vehiculos .png" width="30" height="30">
                                                    </div>
                                                    <div class="col-8 item mt-3">
                                                        <span class="item-title">
                                                            Vehículos: <br>
                                                        </span>
                                                    </div>
                                                    <div class="col-12">
                                                        <div class="row justify-content-around mb-4 vehicle-list">
                                                            <!-- <div class="col-1 img-location mt-3">
                                                            </div> -->
                                                            <div class=" col-12 col-md-6 col-lg-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/bike1.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Honda pop 100</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class=" col-12 col-md-6 col-lg-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/car1.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Chevrolet cruze</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class=" col-12 col-md-6 col-lg-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/car2.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Chevrolet Onix</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class=" col-12 col-md-6 col-lg-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/van1.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Chevrolet Van</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class=" col-12 col-md-6 col-lg-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/bus1.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Bus</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class=" col-12 col-md-6 col-lg-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/car2.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Chevrolet Onix</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <!-- <div class="col-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/van1.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Chevrolet Van</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="col-2 vehicle-detail">
                                                                <div class="card">
                                                                    <div class="card-img">
                                                                        <img class="card-img-top" src="/static/vehicles/bus1.png" alt="Card image cap">
                                                                    </div>
                                                                    <div class="card-body">
                                                                        <p class="card-text">Bus</p>
                                                                    </div>
                                                                </div>
                                                            </div> -->
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="row map">
                                                    <div class="col-12">
                                                        <div style="width: 100%">
                                                            <iframe 
                                                                width="100%"
                                                                height="400"
                                                                src="https://www.google.com/maps/embed/v1/directions
                                                                ?key=AIzaSyBVpHZAXJYLpgCIuXAvb4HZSo0cT4wklIY
                                                                &origin=Oslo+Norway
                                                                &destination=Telemark+Norway
                                                                &avoid=tolls|highways"
                                                                frameborder="0" scrolling="no" marginheight="0" marginwidth="0">
                                                            </iframe>
                                                        </div>
                                                        <br />
                                                    </div>
                                                </div>
                                            </div>    
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    `
                )
            })
            $('.add-cart-cea').on('click', function(){
                cea = $(this).data('id')
                cea_name = $(this).data('name')
                cea_price = $(this).data('price')
                function addCea(){
                    $('li.cart-cea').empty()
                    $('li.cart-cea').append(
                        `
                            <div class="media w-100">
                            <img class="align-self-top mr-2" src="/static/assets/img/volante.svg" width="35">
                            <div class="media-body">
                                <h6 class="mt-0 mb-0 text-small">CEA</h6>
                                <p class="mb-0 text-small">${cea_name}</p>
                                <p class="mb-0 text-small">$${cea_price}</p>
                            </div>
                        </div>
                        <a href="#" class="align-self-center"><i class="material-icons">edit</i></a>
                        `
                    )
                    $('li.cart-cea').data('value', cea)
                    toastr["success"](`Se ha añadido ${$(this).data('name')} al carrito de compras`)
                    setTimeout(function(){ 
                        $('.modal').modal('hide')
                        $('.btn-step-4').trigger('click')
                    }, 2000);
                }
                if ($('li.cart-cea').data('value') == '0')
                {
                    addCea();
                }
                else{
                    swal({
                        title: 'Momento',
                        text: "Ya tienes un CEA en el carrito. Deseas agregar este y eliminar el anterior?",
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#162d40',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Si, agregar',
                        reverseButtons: true
                    }).then((result) => {
                        if (result.value) {
                            addCea();
                        }
                    })
                }
                
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
                    <button type="button" class="company-detail" data-id="${v.id}" data-company="transit" data-toggle="modal" data-target=".transitDetailModal-${v.id}">
                        <div class="d-flex flex-row content-result rounded mb-2">
                            <div class="thumbnail mr-2 mb-4">
                                
                                <img src="${logo}" width="90" height="90" alt="Logo Company">
                                <div class="qualification">
                                    <span class="subtitle d-block">Calificación</span>
                                    <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>                            
                                </div>
                            </div>
                            <div class="result-body">
                                <h4 class="text-small"><span>${v.name}</span></h4>
                                <div class="d-flex flex-row">
                                    <div class="price  pr-2">
                                        <span class="subtitle d-block">Precio</span>
                                        <p class="weigh-5">$${v.final_price}</p>
                                    </div>
                                    <div class="schedule pl-2 pr-2">
                                        <span class="subtitle d-block pb-3">Horarios</span>
                                        <div class="d-flex flex-row d-normal">
                                            <div class="pr-2">
                                                <span class="subtitle d-block">Luneas a viernes:</span>
                                                <p class="text mb-1">08:00 AM - 12:00 PM y 2:00 PM - 6:00 PM</p>
                                            </div>
                                            <div class="saturday">
                                                <span class="subtitle d-block">Sábado:</span>
                                                <p class="text mb-0">08:00 AM - 12:00 PM </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="subtitle d-block">Descripción:</span>
                                <p class="p-text">Lorem ipsum dolor sit amet </p>
                            </div>
                        </div>
                    </button>
                </div>

                <div class="modal fade transitDetailModal-${v.id}" tabindex="-1" role="dialog" aria-labelledby="companyDetailModalTitle" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
                        <div class="modal-content">
                            <div class="modal-body">
                                <div class="col-sm-12 col-md-12 col-lg-12 form-box">
                                    <div class="detail-transit">
                                        <h3 class="transit-big-title">Detalle</h3>
                                        <div class="row transit-info justify-content-around mb-4">
                                            <div class="col-sm-12 col-md-c-4 justify-content-center mb-4">
                                                <div class="image-transit">
                                                    <img class="company-logo mx-auto d-block mt-4 img-fluid" src="${logo}" alt="Logo Company">
                                                </div>
                                                <div class="select-button mt-3">
                                                    <button type="button" class="btn-select add-cart-transit" data-id="${v.id}" data-name='${v.name}' data-price='${v.final_price}' >Seleccionar</button>
                                                </div>
                                            </div>
                                            <div class="col-sm-12 col-md-c-8 info-transit mb-4">
                                                <div class="row transit-title">
                                                    <div class="col-12">
                                                        <span>${v.name}</span>
                                                    </div>
                                                    
                                                </div>
                                                <div class="row details">
                                                    <div class="col-12 col-lg-6">
                                                        <div class="row">
                                                            <div class="col-3 img-location">
                                                                <img src="/static/icons/ubicacion/res/mipmap-mdpi/ubicacion.png" width="30" height="30">
                                                            </div>
                                                            <div class="col-8 item">
                                                                <span class="item-title">
                                                                    Dirección: <br>
                                                                </span>
                                                                <span class="item-detail">
                                                                    ${v.address}
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-12 col-lg-6">
                                                        <div class="row">
                                                            <div class="col-3 img-location">
                                                                <img src="/static/icons/ciudad/res/mipmap-mdpi/ciudad.png" width="30" height="30">
                                                            </div>
                                                            <div class="col-8 item">
                                                                <span class="item-title">
                                                                    Sector: ${v.sector.name} <br>
                                                                </span>
                                                                <span class="item-detail">
                                                                    ${v.city.name}, ${v.city.state.name}
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-12 col-lg-6">
                                                        <div class="row">
                                                            <div class="col-3 img-location">
                                                                <img src="/static/icons/horario/res/mipmap-mdpi/horario.png" width="30" height="30">
                                                            </div>
                                                            <div class="col-8 item">
                                                                <span class="item-title">
                                                                    Horario <br>
                                                                    Lunes a Viernes <br>
                                                                </span>
                                                                <span class="item-detail">
                                                                    08:00 AM - 12:00 PM <br>
                                                                    02:00 PM - 06:00 PM
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-12 col-lg-6">
                                                        <div class="row">
                                                            <div class="col-3 img-location">
                                                                <img src="/static/icons/telefono/res/mipmap-mdpi/telefono.png" width="30" height="30">
                                                            </div>
                                                            <div class="col-8 item">
                                                                <span class="item-title">
                                                                    Teléfono <br>
                                                                </span>
                                                                <span>
                                                                    ${v.cellphone}
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-12 col-lg-6">
                                                        <div class="row">
                                                            <div class="col-3 img-location">
                                                            </div>
                                                            <div class="col-8 item">
                                                                <span class="item-title">
                                                                    Calificación <br>
                                                                </span>
                                                                <span class="item-detail">
                                                                    <p class="text"><span class="weigh-5">${v.rating} </span><i class="material-icons">grade</i> (${v.count_rating})</p>
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-12 col-lg-6">
                                                        <div class="row">
                                                            <div class="col-3 img-location">
                                                                <img src="/static/icons/precio/res/mipmap-mdpi/precio.png" width="30" height="30">
                                                            </div>
                                                            <div class="col-8 item">
                                                                <span class="item-title">
                                                                    Precios <br>
                                                                </span>
                                                                <span class="item-detail">
                                                                    $ ${v.final_price}
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="row map">
                                            <div class="col-12">
                                                <div style="width: 100%">
                                                    <iframe 
                                                        width="100%"
                                                        height="400"
                                                        src="https://maps.google.com/maps?width=100%&amp;height=600&amp;hl=en&amp;coord=4.8142912, -75.6946451&amp;q=Plaza%20de%20Bolivar+(Pereira%20Colombia)&amp;ie=UTF8&amp;t=&amp;z=16&amp;iwloc=B&amp;output=embed"
                                                        frameborder="0" scrolling="no" marginheight="0" marginwidth="0">
                                                    </iframe>
                                                </div>
                                                <br />
                                            </div>
                                        </div>
                                    </div>    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                    `
                )
            })
            $('.add-cart-transit').on('click', function(){
                transit = $(this).data('id')
                transit_name = $(this).data('name')
                transit_price = $(this).data('price')

                function addTransit(){
                    $('li.cart-transit').empty()
                    $('li.cart-transit').append(
                        `
                            <div class="media w-100">
                                <img class="align-self-top mr-2" src="/static/assets/img/img-check.svg" width="35">
                                <div class="media-body">
                                    <h6 class="mt-0 mb-0 text-small">Organismo de transito</h6>
                                    <p class="mb-0 text-small">${transit_name}</p>
                                    <p class="mb-0 text-small">$${transit_price}</p>
                                </div>
                            </div>
                            <a href="#" class="align-self-center"><i class="material-icons">edit</i></a>
                        `
                    )
                    $('li.cart-transit').data('value', transit)
                    toastr["success"](`Se ha añadido ${transit_name} al carrito de compras`)
                    setTimeout(function(){ 
                        $('.modal').modal('hide')
                        $('.btn-step-5').trigger('click')
                    }, 2000);
                }
                if ($('li.cart-transit').data('value') == '0')
                {
                    addTransit();
                }
                else{
                    swal({
                        title: 'Momento',
                        text: "Ya tienes un organismo de Tránsito en el carrito. Deseas agregar este y eliminar el anterior?",
                        type: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#162d40',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Si, agregar',
                        reverseButtons: true
                    }).then((result) => {
                        if (result.value) {
                            addTransit();
                        }
                    })
                }
                
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
})

$('.continue-location').on('click', function(){
    if($('select#states').val() === null){
        toastr["error"]("Debes seleccionar un departamento antes de continuar")
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
    
    $('.element--gender').addClass('d-none')
    $('.element--birth-date').addClass('animated fadeInRight')
    $('.element--birth-date').removeClass('d-none')

})
$('.female').on('click', function(e){
    
    if ($('.male').hasClass('choose--selected')){
        $('.male').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    gender = 'F'
    
    $('.element--gender').addClass('d-none')
    $('.element--birth-date').addClass('animated fadeInRight')
    $('.element--birth-date').removeClass('d-none')
})

$('.back-birth-date').on('click', function(){
    $('.element--birth-date').addClass('d-none')
    $('.element--gender').addClass('animated fadeInRight')
    $('.element--gender').removeClass('d-none')
    loadCitiesSelect(selected.val())

})
$('.continue-birth-date').click(() => {
    if($('#day').val() === '' || $('#month').val() === '' || $('#year').val() === '' ){
        toastr["error"]("Ingresa tu fecha de nacimiento para continuar")
    }
    else {

        birth_date = `${$('#month').val()}-${$('#day').val()}-${$('#year').val()}`
        dob = new Date(birth_date);
        var today = new Date();
        age = Math.floor((today-dob) / (365.25 * 24 * 60 * 60 * 1000));
        $('#day-1').val($('#day').val())
        $('#month-1').val($('#month').val())
        $('#year-1').val($('#year').val())
        $('.btn-step-1').trigger('click')
        
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

    $('.element--tramit-type').addClass('d-none')
    $('.element--vehicle-type').removeClass('d-none')
})

$('#licence-2').on('click', function(ev){
    clearLicences()
    tramit_type1 = ""
    $('#licence-2').addClass('choose--selected')
    if ($('#licence-1').hasClass('choose--selected')){
        $('#licence-1').removeClass('choose--selected')
    }
    $('.element--tramit-type').addClass('d-none')
    $('.element--second-licence').removeClass('d-none')
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
    $('.element--tramit-type').removeClass('d-none')
})

$('.element--second-licence input').on('click', function(ev){
    console.log('click')
    console.log(($(this).val()))
    if (!($('.option-' + tramit_type1).hasClass('option--selected'))){
        console.log('entro al if')
        $('.option-' + tramit_type1).addClass('option--selected')
        if($(this).val() != 'SL' ){
            $('.toggleC2').removeClass('d-none')
            $('.toggleC3').removeClass('d-none')
        }
        if($(this).val() == 'RC' ){
            if (!($('#bike-licence').hasClass('disabled'))){
                $('#bike-licence').addClass('disabled')
            }
            $('.toggleB1').addClass('d-none')
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
                confirmButtonText: 'Ok'
            })
        }
        
        if (tramit_type1 == ""){
            console.log("No hay tramite")
            tramit_type1 = $(this).val()
            $('.option-' + tramit_type1).addClass('option--selected');
            $('.element--second-licence').addClass('d-none');
            $('.element--vehicle-type').removeClass('d-none');
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
                $('.element--second-licence').addClass('d-none')
                $('.element--vehicle-type').removeClass('d-none')
            }
            
        }
    }
    else {
        console.log('else')
        $('.option-' + $(this).val()).removeClass('option--selected');
        clearTramit($(this).val())
    }
})

$('#bike-licence').on('click', function(ev){
    if(tramit_type1 == 'SL'){
        if ($('#car-licence').hasClass('choose--selected'))
        {
            $('#car-licence').removeClass('choose--selected')
        }
    }
    bike = !bike;
    if (!(bike)){
        $('#bike-licence').removeClass('choose--selected')
        if ('bike' in licences){
            delete licences['bike']
        }
        $('.title-car').addClass('d-none')
        $('.toggleA1').addClass('d-none')
        $('.toggleA2').addClass('d-none')
    }
    else{
        $('#bike-licence').addClass('choose--selected')
        $('.title-bike').removeClass('d-none')
        $('.toggleA1').removeClass('d-none')
        $('.toggleA2').removeClass('d-none')
    }
    
})

$('#car-licence').on('click', function(ev){
    if(tramit_type1 == 'SL'){
        if ($('#bike-licence').hasClass('choose--selected'))
        {
            $('#bike-licence').removeClass('choose--selected')
        }
    }
    car = !car;
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
    
})


$('.continue-vehicle-type').on('click', function(){
    $('.element--vehicle-type').addClass('d-none')
    $('.element--licence-type').removeClass('d-none')
})

$('.back-licence-type').on('click', function(){
    $('.element--licence-type').addClass('d-none')
    $('.element--vehicle-type').removeClass('d-none')
})

$('.continue-licence-type').on('click', function(){
    $('.element--licence-type').addClass('d-none')
    if(tramit_type1 == 'FL'){
        $('.element--have-runt').removeClass('d-none')
    }
    else{
        $('.element--aditional-tramit').removeClass('d-none')
    }
})


$('.back-have-runt').on('click', function(){
    $('.element--have-runt').addClass('d-none')
    if(tramit_type1 == 'FL'){
        $('.element--licence-type').removeClass('d-none')
    }
    else{
        $('.element--aditional-tramit').removeClass('d-none')
    }
})

$('.continue-personal-data').on('click', function(){
    if($('#first_name').val() === null || 
    $('#last_name').val() === null ||
    $('#doc_type').val() === null ||
    $('#document_id').val() === null ||
    $('#day-1').val() === null ||
    $('#month-1').val() === null ||
    $('#year-1').val() === null ||
    $('#cellphone').val() === null){
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

$('.continue-auth-data').on('click', function(){
    if(!($('.checkbox-terms').is(":checked"))){
        toastr["error"]("Debes aceptar los terminos y condiciones para continuar")
    }
    if($('#phone_number').val() === null || 
        $('#email').val() === null){
        toastr["error"]("Debes llenar todos los campos")
    }
    else if ($('#pass1').val() != null) {
        if ($('#pass1').val() != $('#pass2').val()){
            toastr["error"]("Las contraseñas no coinciden")
        }
        else{
            $('.element--auth-data').addClass('d-none')
            $('.element--paper-data').removeClass('d-none')
        }
    }
    else{
        $('.element--auth-data').addClass('d-none')
        $('.element--paper-data').removeClass('d-none')
    }
})

$('.send').on('click', function(e){
    
    if ($('.pick-up').hasClass('choose--selected')){
        $('.pick-up').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    paper = 'send'
    
    $('.element--paper-data').addClass('d-none')
    $('.element--payment').removeClass('d-none')

})
$('.pick-up').on('click', function(e){
    
    if ($('.send').hasClass('choose--selected')){
        $('.send').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    paper = 'pick-up'
    
    $('.element--paper-data').addClass('d-none')
    $('.element--payment').removeClass('d-none')
})

$('.back-paper-data').on('click', function(){
    $('.element--paper-data').addClass('d-none')
    $('.element--auth-data').removeClass('d-none')
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
    console.log(tramits)
}

function deleteTramit(licence){
    if(tramits['licence_1']['licence'] == licence){
        tramits['licence_1'] = tramits['licence_2']
        tramits['licence_2'] = ''
    }
    if(tramits['licence_2']['licence'] == licence){
        tramits['licence_2'] = ''
    }
    console.log(tramits)
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
    
    $('.element--have-runt').addClass('d-none')
    $('.btn-step-2').trigger('click')
})
$('.no-runt').on('click', function(e){
    if ($('.si-runt').hasClass('choose--selected')){
        $('.si-runt').removeClass('choose--selected')
    }
    $(this).addClass('choose--selected')
    runt = 'no'
    
    $('.element--have-runt').addClass('d-none')
    $('.element--runt').removeClass('d-none')
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
$('#sector-crc').on('change', function(e){
    params_crc['sector'] = $(this).val()
})
$('#rating-crc').on('change', function(){
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
    params_crc['city']= $('#cities-crc').val()
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
$('#vehicle-cea').on('change', function(e){
    params_cea['vehicles__vehicle__line'] = $(this).val()
})
$('#rating-cea').on('change', function(){
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
$('#sector-cea').on('change', function(e){
    params_cea['sector'] = $(this).val()
})

$('button.filter-cea').on('click', function(e){
    var licence = ""
    $.each(licences, function(i, v){
        licence += (`${v},`)
    })
    params_cea['state'] = $('#states').val()
    params_cea['city'] = $('#cea-city').val()
    params_cea['age']= age
    params_cea['gender']= gender
    params_cea['licences']= licence
    params_cea['licences__licence__category__in'] = licence
    cea_filter(params_cea)

})

var params_transit = {}
$('#rating-transit').on('change', function(){
    if ($(this).val() === '0'){
        delete params_transit['rating']
    }
    else{
        params_transit['rating'] = $(this).val()
    }
})
$('#price-transit').on('change', function(){
    if ($(this).val() === '0'){
        delete params_transit['price']
    }
    else{
        params_transit['price'] = $(this).val()
    }
})
$('button.filter-transit').on('click', function(e){
    params_transit['state'] = $('#states').val(),
    params_transit['city'] = $('#transit-city').val(),
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
            "cellphone": $('#phone_number').val(),
            "city": $('#cities').val(),
            "state": $('#states').val(),
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
                    text: 'Tu solicitud se ha creado exitosamente. Dirigete al punto de TuLicencia mas cercano para validar tu solicitud de crédito',
                    type: 'success',
                    showCancelButton: false,
                    confirmButtonText: 'Finalizar'
                }).then((result) => {
                    if (result.value) {
                        window.location.replace(`/profile/`);
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
            if (tramits['licence_2'] != ''){
                $('.licence-2-input').val(tramits['licence_2']['licence'])
                $('.tramit-2-input').val(tramits['licence_2']['tramit'])
            }

            $('#licence-request-form').off()
            $('#licence-request-form').submit()
        }

    }
    
})
