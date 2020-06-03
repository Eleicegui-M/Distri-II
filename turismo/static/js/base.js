$( "#destino" ).change(function() {
    $.ajax({
        url : "localhost:8001",     // Excursiones
        dataType: "json",
        data: {"fecha_inicio": $( "#fecha_inicio" ).val(), "fecha_fin": $( "#fecha_fin" ).val(), "lugar": $( "#destino" ).val(),  "disponibilidad": $( "#cantidad-p" ).val()},
        success: function(data){
            $.each(data, function (i, data) {
                $('#extursion1').append($('<option>', { 
                    value: data.value,
                    text : data.text 
                }));

                $('#extursion2').append($('<option>', { 
                    value: data.value,
                    text : data.text 
                }));

                $('#extursion3').append($('<option>', { 
                    value: data.value,
                    text : data.text 
                }));
            })
        }
    });


    $.ajax({
        url : "localhost:8002", // Hoteles
        dataType: "json",
        data: {"fecha_inicio": $( "#fecha_inicio" ).val(), "fecha_fin": $( "#fecha_fin" ).val(), "lugar": $( "#destino" ).val(),  "disponibilidad": $( "#cantidad-p" ).val()},
        success: function(data){
            $.each(data, function (i, data) {
                $('#hotel').append($('<option>', { 
                    value: data.value,
                    text : data.text 
                }));
            })
        }
    });


    $.ajax({
        url : "localhost:8003", // Vuelo ida
        dataType: "json",
        data: {"fecha_inicio": $( "#fecha_inicio" ).val(), "ciudad_origen": $( "#origen" ).val(),"ciudad_destino": $( "#destino" ).val(),  "disponibilidad": $( "#cantidad-p" ).val()},
        success: function(data){
            $.each(data, function (i, data) {
                $('#vuelo_ida').append($('<option>', { 
                    value: data.value,
                    text : data.text 
                }));
            })
        }
    });

    $.ajax({
        url : "localhost:8003", // Vuelo vuelta
        dataType: "json",
        data: {"fecha_fin": $( "#fecha_fin" ).val(), "ciudad_origen": $( "#destino" ).val(),"ciudad_destino": $( "#origen" ).val(),  "disponibilidad": $( "#cantidad-p" ).val()},
        success: function(data){
            $.each(data, function (i, data) {
                $('#vuelo_vuelta').append($('<option>', { 
                    value: data.value,
                    text : data.text 
                }));
            })
        }
    });
});

$( "#hotel" ).change(function() {
    $('#estrellas').text($( "#hotel option:selected" ).val())
});


