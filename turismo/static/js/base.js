$( "#buscar" ).click(function() {
    $("#excursion1 option").each(function() {
        $(this).remove();
    });

     $("#excursion2 option").each(function() {
        $(this).remove();
    });

      $("#excursion3 option").each(function() {
        $(this).remove();
    });

    $("#hotel option").each(function() {
        $(this).remove();
    });

    $("#vuelo_ida option").each(function() {
        $(this).remove();
    });

    $("#vuelo_vuelta option").each(function() {
        $(this).remove();
    });

    $.ajax({
        url : "http://127.0.0.1:8001/",     // Excursiones
        method: "GET",
        dataType: "json",
        data: {"fecha_inicio": $( "#fecha_inicio" ).val(),"fecha_fin": $( "#fecha_fin" ).val(),"destino": $( "#destino" ).val(),  "cantidad_p": $( "#cantidad_p" ).val()},
        success: function(data){
            $.each(data.excursiones, function (i, val) {
                $('#excursion1')
                         .append($("<option></option>")
                                    .attr("value", data.precios[i])
                                    .text(val)); 
                $('#excursion2')
                         .append($("<option></option>")
                                    .attr("value", data.precios[i])
                                    .text(val)); 
                $('#excursion3')
                         .append($("<option></option>")
                                    .attr("value", data.precios[i])
                                    .text(val));
            })
        }
    });

    $.ajax({
        url : "http://127.0.0.1:8002/", // Hoteles
        method: "GET",
        dataType: "json",
        data: {"fecha_inicio": $( "#fecha_inicio" ).val(), "fecha_fin": $( "#fecha_fin" ).val(), "destino": $( "#destino" ).val(),  "cantidad_p": $( "#cantidad_p" ).val()},
        success: function(data){
            console.log("llega a ajax hotel")
            $.each(data.hoteles, function (i, val) {
                $('#hotel')
                         .append($("<option></option>")
                                    .attr("value", data.estrellas[i])
                                    .attr("name", data.precios[i])
                                    .text(val));
            })
            $('#estrellas').val(data.estrellas[0]);
            console.log($( "#hotel option:selected" ).attr('name'))
        }
    });

    $.ajax({
        url : "http://127.0.0.1:8003/", // Vuelo ida
        method: "GET",
        dataType: "json",
        data: {"fecha_inicio": $( "#fecha_inicio" ).val(), "origen": $( "#origen" ).val(),"destino": $( "#destino" ).val(),  "cantidad_p": $( "#cantidad_p" ).val()},
        success: function(data){
            console.log("llega a ajax vuelos_ida")
            $.each(data.vuelos, function (i, val) {
                $('#vuelo_ida')
                         .append($("<option></option>")
                                    .attr("value", data.precios[i])
                                    .text(val));
            })
        }
    });

    $.ajax({
        url : "http://127.0.0.1:8003/", // Vuelo vuelta
        method: "GET",
        dataType: "json",
        data: {"fecha_inicio": $( "#fecha_fin" ).val(), "origen": $( "#destino" ).val(),"destino": $( "#origen" ).val(),  "cantidad_p": $( "#cantidad_p" ).val()},
        success: function(data){
            console.log("llega a ajax vuelos_vuelta")
            $.each(data.vuelos, function (i, val) {
                $('#vuelo_vuelta')
                         .append($("<option></option>")
                                    .attr("value", data.precios[i])
                                    .text(val));
            })
        }
    });
});

$( "#limpiar" ).click(function() {
    $('#nombre').val('')
    $('#fecha_inicio').val('')
    $('#fecha_fin').val('')
    $('#cantidad_p').val('')
    $('#origen').val('')
    $('#destino').val('')

    $("#excursion1 option").each(function() {
        $(this).remove();
    });

     $("#excursion2 option").each(function() {
        $(this).remove();
    });

      $("#excursion3 option").each(function() {
        $(this).remove();
    });

    $("#hotel option").each(function() {
        $(this).remove();
    });

    $("#vuelo_ida option").each(function() {
        $(this).remove();
    });

    $("#vuelo_vuelta option").each(function() {
        $(this).remove();
    });

});

$(document).on("click","button#generar",function(){
    $('#modal_id').modal('show');
});

$(document).on("click","button#reservar",function(){
    console.log("Toca el boton");
    $('#modal_reservar').show();
    $('#modal_reservar').modal('show');
});

$(document).on("click","button#id_accion_si",function(){
    $.ajax({
        url : "paquetes/armar_paquete", // Vuelo vuelta
        dataType: "json",
        data: {"nombre": $( "#nombre" ).val(),
                "fecha_inicio": $( "#fecha_inicio" ).val(),
                "fecha_fin": $( "#fecha_fin" ).val(),
                "origen": $( "#origen" ).val(),
                "destino": $( "#destino" ).val(),
                "cantidad_p": $( "#cantidad_p" ).val(),
                "vuelo_ida": $( "#vuelo_ida option:selected" ).text(),
                "vuelo_vuelta": $( "#vuelo_vuelta option:selected" ).text(),
                "hotel": $( "#hotel option:selected" ).text(),
                "precio_hotel": $( "#hotel option:selected" ).attr('name'),
                "estrellas": $( "#hotel option:selected" ).val(),
                "excursion1": $( "#excursion1 option:selected" ).text(),
                "excursion2": $( "#excursion2 option:selected" ).text(),
                "excursion3": $( "#excursion3 option:selected" ).text(),
                "precio_vuelo_ida": $( "#vuelo_ida option:selected" ).val(),
                "precio_vuelo_vuelta": $( "#vuelo_vuelta option:selected" ).val(),
                "precio_excursion1": $( "#excursion1 option:selected" ).val(),
                "precio_excursion2": $( "#excursion2 option:selected" ).val(),
                "precio_excursion3": $( "#excursion3 option:selected" ).val(),

            },
        success: function(data){
            window.location.replace('/');
            console.log("volvio a pleno");
        }
    });
});

// $(document).on("change","#hotel",function(){
$(document).on('change', '#hotel', function() {
    console.log("Hasta aca llega perrito");
    $('#estrellas').val($( "#hotel option:selected" ).val());
});




// $(document).on("click","button#id_accion_si",function(){
//     $.ajax({
//         url : "generar_paquete",
//         dataType: "json",
//         data: {"nombre": $( "#nombre" ).val(),
//             "fecha_inicio": $( "#fecha_inicio" ).val(),
//             "fecha_fin": $( "#fecha_fin" ).val(),
//             "origen": $( "#origen" ).val(),
//             "destino": $( "#destino" ).val(),
//             "cantidad_p": $( "#cantidad_p" ).val(),
//             "vuelo_id": $( "#vuelo_ida option:selected" ).val(),
//             "vuelo_vuelta": $( "#vuelo_vuelta option:selected" ).val(),
//             "hotel": $( "#hotel option:selected" ).val(),
//             "excursion1": $( "#excursion1 option:selected" ).val(),
//             "excursion2": $( "#excursion2 option:selected" ).val(),
//             "excursion3": $( "#excursion3 option:selected" ).val()
//             },
//         success: function(data){
//             console.log("llega a ajax vuelos_vuelta")
//         }
//     });
// });

// $( "#hotel" ).change(function() {
//     $('#estrellas').val('2');
// });

// $( "#hotel option:selected" ).val()



/* RESERVAR PAQUETE */
$(document).on("click","button#reservar",function(){

    $.ajax({
        url : "reservar_paquete",     //
        dataType: "json",
        data: {"id_paquete": $(this).attr('name')},
        success: function(data){
            $('#modal_reserva').show();
            $('#modal_reserva').modal('show');    
        }
    });


    // $.ajax({
    //     url : "http://127.0.0.1:8001/reservar_excursion",     // URL encargada de reservar en API excursion
    //     method: "POST",
    //     dataType: "json",
    //     data: {},
    //     success: function(data){
    //     }
    // });

    // $.ajax({
    //     url : "http://127.0.0.1:8001/reservar_hotel",     // URL encargada de reservar en API excursion
    //     method: "POST",
    //     dataType: "json",
    //     data: {},
    //     success: function(data){
    //     }
    // });

    // $.ajax({
    //     url : "http://127.0.0.1:8001/reservar_vuelo_ida",     // URL encargada de reservar en API excursion
    //     method: "POST",
    //     dataType: "json",
    //     data: {},
    //     success: function(data){
    //     }
    // });

    //     $.ajax({
    //     url : "http://127.0.0.1:8001/reservar_vuelo_vuelta",     // URL encargada de reservar en API excursion
    //     method: "POST",
    //     dataType: "json",
    //     data: {},
    //     success: function(data){
    //     }
    // });
});