;(function($) {
    
    axios.defaults.headers.common['Api-Key'] = 'e98f0150a142eb04c4abf3f297adb965c3d8ff18';
    $(document).ready(function(){
        booking = $('.field-booking p').text()
        data = {}
        data['booking'] = booking
        $('#request_form').on('submit', function(ev){
            ev.preventDefault()
            swal({
                title: 'Atención!',
                text: "Ingresa el número de documento del cliente para verificar su solicitud antes de guardar",
                input: 'text',
                showCancelButton: true,
                confirmButtonText: 'Verificar',
                showLoaderOnConfirm: true,
                preConfirm: (document) => {
                    document = document
                },
                allowOutsideClick: () => !swal.isLoading()
            }).then((result) => {
                if (result.value) {
                    data['document'] = result.value
                    axios.get('/api/request/validate-document/', {
                        params: data
                    })
                    .then(function (response) {
                        data = response.data;
                        swal({
                            title: 'Verificado!',
                            text: 'el usuario se ha verificado correctamente',
                            type: 'success',
                            showCancelButton: false,
                            confirmButtonText: 'Guardar'
                        }).then((result) => {
                            $("#request_form").off();
                            $('#request_form').submit()
                        })
                    })
                    .catch(function (error) {
                        console.log(error.response)
                        swal({
                            title: 'No Verificado!',
                            text: 'No se ha podido verificar. Intenta nuevamente',
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
    });

})(django.jQuery);
