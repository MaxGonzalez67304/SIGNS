import { Component } from '@angular/core';

@Component({
  selector: 'app-lecciones',
  templateUrl: './lecciones.component.html',
  styleUrls: ['./lecciones.component.css']
})
export class LeccionesComponent {
  selectL : any
  leccionSeleccionada: any = null; // Variable para almacenar la lección seleccionada
  mostrarLeccion = false; // Bandera para mostrar la pantalla de la lección

  // Método para manejar el clic en la card
  mostrarPantallaLeccion(leccion: any) {
    this.leccionSeleccionada = leccion;
    this.mostrarLeccion = true;
  }

  // Método para volver a la vista de las cards
  volverALasCards() {
    this.leccionSeleccionada = null;
    this.mostrarLeccion = false;
  }
   lecciones = [
    {
      titulo: 'Expresiones',
      imagen: '../../../../assets/images/expresiones.jpg',
      progreso: 25,
      descripcion: 'En esta lección, aprenderás expresiones comunes y frases básicas utilizadas en situaciones cotidianas. Desde saludos hasta preguntas simples, será una introducción perfecta al idioma.',
      preguntas: [
        '¿Cómo te llamas?',
        '¿De dónde eres?',
        '¿Qué hora es?',
        '¿Puedes decir "hola" en este idioma?',
        '¿Qué expresión utilizas para agradecer en situaciones formales?'
      ]
    },
    {
      titulo: 'Días, semanas y meses',
      imagen: '../../../../assets/images/calendario.jpg',
      progreso: 50,
      descripcion: 'Explora el vocabulario relacionado con el tiempo, los días de la semana y los meses. Podrás hablar sobre fechas, planificar eventos y entender mejor el calendario.',
      preguntas: [
        '¿Cuál es tu día favorito de la semana?',
        '¿Qué meses tienen 31 días?',
        '¿Cuál es la fecha de hoy?',
        '¿Cuántos días tiene una semana?',
        '¿Puedes decir la fecha de tu cumpleaños en este idioma?'
      ]
    },
    {
      titulo: 'Colores',
      imagen: '../../../../assets/images/colores.jpg',
      progreso: 70,
      descripcion: 'Descubre una paleta de colores en el idioma. Desde los colores primarios hasta los tonos más complejos, esta lección te ayudará a identificar y nombrar los colores en diversas situaciones.',
      preguntas: [
        '¿Cómo se dice "rojo" en este idioma?',
        '¿Qué color se obtiene mezclando azul y amarillo?',
        '¿Cuál es tu color favorito y cómo se dice en este idioma?',
        'Menciona tres colores primarios en este idioma.',
        '¿Qué color es conocido como neutro en esta lengua?'
      ]
    },
    {
      titulo: 'Animales',
      imagen: '../../../../assets/images/animales.webp',
      progreso: 10,
      descripcion: 'Adéntrate en el mundo animal a través del idioma. Conocerás el vocabulario para describir una variedad de animales, desde mascotas hasta animales salvajes.',
      preguntas: [
        '¿Cómo se dice "perro" en este idioma?',
        '¿Qué animal es conocido por su gran tamaño y larga trompa?',
        '¿Cuál es tu animal favorito y cómo se dice en este idioma?',
        'Nombra tres animales que viven en la selva en este idioma.',
        '¿Puedes mencionar dos animales marinos en este idioma?'
      ]
    },
    {
      titulo: 'Medios de transporte',
      imagen: '../../../../assets/images/transportes.jpg',
      progreso: 77,
      descripcion: 'Aprende el vocabulario relacionado con diferentes medios de transporte. Desde automóviles hasta transporte público, podrás hablar sobre cómo te mueves de un lugar a otro.',
      preguntas: [
        '¿Cómo se dice "coche" en este idioma?',
        '¿Qué medio de transporte es comúnmente utilizado en ciudades para viajes cortos?',
        '¿Cuál es tu medio de transporte favorito y cómo se dice en este idioma?',
        'Nombra tres medios de transporte público en este idioma.',
        '¿Puedes mencionar dos medios de transporte que se utilicen en el agua?'
      ]
    }
    // Puedes agregar más objetos con títulos, imágenes, progreso, descripciones y preguntas
  ];
  

}
