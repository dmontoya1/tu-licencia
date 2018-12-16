;(function($) {

    $(document).ready(function(){
        // using jQuery
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
        axios.defaults.headers.common['X-CSRFToken'] = csrftoken
        axios.defaults.headers.common['Api-Key'] = '36f24428d8a940bcdbe996a01a98e10bfc7f2231'

        function disableCompany(nit){
            params = {}
            params ['nit'] = nit
            axios.post('/api/companies/disable-cea', params)
            .then(function (response) {
                data = response.data;
                swal({
                    title: 'Atención!',
                    text: 'Tu solicitud se ha enviado con éxito. El administrador de Tu Licencia se pondrá en contacto contigo pronto.',
                    type: 'success',
                    showCancelButton: false,
                    confirmButtonText: 'Cerrar'
                })
            })
            .catch(function (error) {
                console.log(error.response)
                swal({
                    title: 'Atención!',
                    text: 'Ha ocurrido un error, intenta nuevamente mas tarde',
                    type: 'error',
                    showCancelButton: false,
                    confirmButtonText: 'Cerrar'
                }).then((result) => {
                    console.log("reintentar")
                })
            })
        }

        function enableCompany(nit){
            params = {}
            params ['nit'] = nit
            axios.post('/api/companies/enable-cea', params)
            .then(function (response) {
                data = response.data;
                swal({
                    title: 'Atención!',
                    text: 'Tu solicitud se ha enviado con éxito. El administrador de Tu Licencia se pondrá en contacto contigo pronto.',
                    type: 'success',
                    showCancelButton: false,
                    confirmButtonText: 'Cerrar'
                })
            })
            .catch(function (error) {
                console.log(error.response)
                swal({
                    title: 'Atención!',
                    text: 'Ha ocurrido un error, intenta nuevamente mas tarde',
                    type: 'error',
                    showCancelButton: false,
                    confirmButtonText: 'Cerrar'
                }).then((result) => {
                    console.log("reintentar")
                })
            })
        }

        $('.request-soft').on('click', function(ev){
            ev.preventDefault()
            nit = $('#id_nit').val()
            swal({
                title: '¿Estas Seguro?',
                text: "¿Seguro quieres inhabilitar esta compañía?",
                type: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Si, Inhabilitar!',
                reverseButtons: true,
            }).then((result) => {
                if (result.value) {
                    axios.get('/api/request/cea-pending/', {
                        params: {
                            nit: nit
                        }
                    })
                    .then(function (response) {
                        data = response.data;
                        if (data.length > 0){
                            swal({
                                title: 'Atención!',
                                text: `Tienes ${data.length} solicitudes pendientes. Si inhabilitas tu compañía, igual debes de atender estas solicitudes.\n
                                Seguro deseas continuar? `,
                                type: 'info',
                                showCancelButton: true,
                                reverseButtons: true,
                                confirmButtonText: 'Solicitar inhabilitación',
                                showLoaderOnConfirm: true,
                                preConfirm: () => {
                                    console.log("loading")
                                },
                                allowOutsideClick: () => !swal.isLoading()
                            }).then((result) => {
                                if (result){
                                    disableCompany(nit)
                                }
                            })
                        }
                        else {
                            disableCompany(nit)
                        }
                    })
                    .catch(function (error) {
                        console.log(error.response)
                        swal({
                            title: 'Atención!',
                            text: 'Ha ocurrido un error, intenta nuevamente mas tarde',
                            type: 'error',
                            showCancelButton: false,
                            confirmButtonText: 'Cerrar'
                        }).then((result) => {
                            console.log("reintentar")
                        })
                    })
                }
            })
        })

        $('.request-revive').on('click', function(ev){
            ev.preventDefault()
            nit = $('#id_nit').val()
            swal({
                title: '¿Estas Seguro?',
                text: "¿Seguro quieres habilitar esta compañía?",
                type: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Si, habilitar!',
                reverseButtons: true
            }).then((result) => {
                if (result.value) {
                    enableCompany(nit)
                }
            })
        })
    });

    

  })(django.jQuery);