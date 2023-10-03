function obtenerDatos(id){
    document.getElementById('formulario').action='/editar_persona/'+id
    document.getElementById('boton').innerHTML = 'Actualizar'
    nombreActual = document.getElementById('tabla_nombre'+id).innerHTML
    apellidoActual = document.getElementById('tabla_apellido'+id).innerHTML
    telefonoActual = document.getElementById('tabla_telefono'+id).innerHTML

    document.getElementById('nombre').value=nombreActual
    document.getElementById('apellido').value=apellidoActual
    document.getElementById('telefono').value=telefonoActual

}