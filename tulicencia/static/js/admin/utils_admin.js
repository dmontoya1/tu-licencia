;(function($) {
    
    axios.defaults.headers.common['Api-Key'] = '98697b3f36dfaefb7f7f70e32be3dbde418c078b';7
    function getCities(idState) {
        $.ajax({
            type: "GET",
            url:"/api/manager/city/"+idState+"/",
            success:function(data)
            {   
                city = $('select#id_city option:selected').val()
                $('select#id_city').empty()
                $(data).each(function(i, v){
                    if (city === v.id){
                        $('select#id_city').append(
                            `<option selected value="${v.id}">${v.name}</option>`
                        )
                    }
                    else{
                        $('select#id_city').append(
                            `<option value="${v.id}">${v.name}</option>`
                        )
                    }
                    
                })
                $('select#id_city').prepend(
                    `<option value="" disabled selected>Seleccione una ciudad</option>`
                )
                $('select#id_city').val(city).trigger('change');
                $('select#id_city').select2("destroy");
                $('select#id_city').select2();
            },
        });
    }

    function getSectors(idCity) {
        $.ajax({
            type: "GET",
            url:"/api/manager/sector/"+idCity+"/",
            success:function(data)
            {   
                sector = $('select#id_sector option:selected').val()
                $('select#id_sector').empty()
                $(data).each(function(i, v){
                    if (sector === v.id){
                        $('select#id_sector').append(
                            `<option selected value="${v.id}">${v.name}</option>`
                        )
                    }
                    else{
                        $('select#id_sector').append(
                            `<option value="${v.id}">${v.name}</option>`
                        )
                    }
                    
                })
                $('select#id_sector').prepend(
                    `<option value="" disabled selected>Seleccione una ciudad</option>`
                )
                $('select#id_sector').val(sector).trigger('change');
                $('select#id_sector').select2("destroy");
                $('select#id_sector').select2();
            },
        });
    }

    $(document).ready(function(){
        if ($('select#id_state option:selected').val()){
            getCities($('select#id_state option:selected').val())
        }
        else {
            $('select#id_city').empty()
            $('select#id_city').append(
                '<option disabled value selected>Seleccione primero un departamento</option>'
            )
        }
        if ($('select#id_city option:selected').val()){
            getSectors($('select#id_city option:selected').val())
        }
        else {
            $('select#id_sector').empty()
            $('select#id_sector').append(
                '<option disabled value selected>Seleccione primero una ciudad</option>'
            )
        }

        $('select#id_state').on('change', function(ev){
            getCities($(this).val())
        })
        $('select#id_city').on('change', function(ev){
            getSectors($(this).val())
        })

        $('.softdeletelink').on('click', function(ev){
            ev.preventDefault()
            swal({
                title: '¿Estas Seguro?',
                text: "¿Seguro quieres inhabilitar esta compañía?",
                type: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Si, Inhabilitar!',
                reverseButtons: true
            }).then((result) => {
                if (result.value) {
                    $('.softdeletelink').off()
                    $('.softdeletelink').trigger('click')
                }
            })
        })

        $('.revivelink').on('click', function(ev){
            ev.preventDefault()
            swal({
                title: '¿Estas Seguro?',
                text: "¿Seguro quieres habilitar esta compañía?",
                type: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Si, habilitar!',
                reverseButtons: true
            }).then((result) => {
                if (result.value) {
                    $('.revivelink').off()
                    $('.revivelink').trigger('click')
                }
            })
        })
    });

    

  })(django.jQuery);