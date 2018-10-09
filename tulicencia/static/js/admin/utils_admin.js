;(function($) {
  
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

        $('select#id_state').on('change', function(ev){
            getCities($(this).val())
        })
    });

  })(django.jQuery);