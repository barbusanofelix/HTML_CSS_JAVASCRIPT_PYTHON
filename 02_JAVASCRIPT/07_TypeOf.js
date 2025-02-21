var libro = {
    titulo: 'Las Legiones Malditas',
    autor: 'Santiago Posterguillo',
    informacion: function (){ return this titulo + " escrito por " +
    this autor;}
    }
    
    console.log(typeof libro.informacion);
    
    