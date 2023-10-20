import { Component } from '@angular/core';

@Component({
  selector: 'app-alfabeto',
  templateUrl: './alfabeto.component.html',
  styleUrls: ['./alfabeto.component.css']
})
export class AlfabetoComponent {
  rutaBase = '../../../assets/images/';

  cardsAlfabeto: { src: string; letra: string }[] = [
    { src: this.rutaBase + 'logo.jpg', letra: 'A' },
    { src: this.rutaBase + 'logo.jpg', letra: 'B' },
    { src: this.rutaBase + 'logo.jpg', letra: 'C' },
    { src: this.rutaBase + 'logo.jpg', letra: 'D' },
    { src: this.rutaBase + 'logo.jpg', letra: 'E' },
    { src: this.rutaBase + 'logo.jpg', letra: 'F' },
    { src: this.rutaBase + 'logo.jpg', letra: 'G' },
    { src: this.rutaBase + 'logo.jpg', letra: 'H' },
    { src: this.rutaBase + 'logo.jpg', letra: 'I' },
    { src: this.rutaBase + 'logo.jpg', letra: 'J' },
    { src: this.rutaBase + 'logo.jpg', letra: 'K' },
    { src: this.rutaBase + 'logo.jpg', letra: 'L' },
    { src: this.rutaBase + 'logo.jpg', letra: 'M' },
    { src: this.rutaBase + 'logo.jpg', letra: 'N' },
    { src: this.rutaBase + 'logo.jpg', letra: 'Ñ' },
    { src: this.rutaBase + 'logo.jpg', letra: 'O' },
    { src: this.rutaBase + 'logo.jpg', letra: 'P' },
    { src: this.rutaBase + 'logo.jpg', letra: 'Q' },
    { src: this.rutaBase + 'logo.jpg', letra: 'R' },
    { src: this.rutaBase + 'logo.jpg', letra: 'S' },
    { src: this.rutaBase + 'logo.jpg', letra: 'T' },
    { src: this.rutaBase + 'logo.jpg', letra: 'U' },
    { src: this.rutaBase + 'logo.jpg', letra: 'V' },
    { src: this.rutaBase + 'logo.jpg', letra: 'W' },
    { src: this.rutaBase + 'logo.jpg', letra: 'X' },
    { src: this.rutaBase + 'logo.jpg', letra: 'Y' },
    { src: this.rutaBase + 'logo.jpg', letra: 'Z' }
  ];
}
