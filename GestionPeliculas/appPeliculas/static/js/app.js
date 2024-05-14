function eliminarPelicula(id){
    Swal.fire({
        title: "¿Está seguro de eliminar la pelicula?",
        showDenyButton:true,
        confirmButtonText:"Si",
        denyButtonText:"No"
    }).then((result)=>{
        if(result.isConfirmed){
            location.href = "/eliminarPelicula/" + id
        }
    })
}