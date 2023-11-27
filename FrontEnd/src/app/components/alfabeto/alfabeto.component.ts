import { Component } from '@angular/core';

@Component({
  selector: 'app-alfabeto',
  templateUrl: './alfabeto.component.html',
  styleUrls: ['./alfabeto.component.css']
})
export class AlfabetoComponent {
  rutaBase = '../../../assets/images//alfabeto/';

  cardsAlfabeto: { src: string; letra: string }[] = [
    { src: this.rutaBase + 'A.jpg', letra: 'A' },
    { src: this.rutaBase + 'B.jpg', letra: 'B' },
    { src: this.rutaBase + 'C.jpg', letra: 'C' },
    { src: this.rutaBase + 'D.jpg', letra: 'D' },
    { src: this.rutaBase + 'E.jpg', letra: 'E' },
    { src: this.rutaBase + 'F.jpg', letra: 'F' },
    { src: this.rutaBase + 'G.jpg', letra: 'G' },
    { src: this.rutaBase + 'H.jpg', letra: 'H' },
    { src: this.rutaBase + 'I.jpg', letra: 'I' },
    { src: this.rutaBase + 'J.jpg', letra: 'J' },
    { src: this.rutaBase + 'K.jpg', letra: 'K' },
    { src: this.rutaBase + 'L.jpg', letra: 'L' },
    { src: this.rutaBase + 'M.jpg', letra: 'M' },
    { src: this.rutaBase + 'N.jpg', letra: 'N' },
    { src: this.rutaBase + 'Ñ.jpg', letra: 'Ñ' },
    { src: this.rutaBase + 'O.jpg', letra: 'O' },
    { src: this.rutaBase + 'P.jpg', letra: 'P' },
    { src: this.rutaBase + 'Q.jpg', letra: 'Q' },
    { src: this.rutaBase + 'R.jpg', letra: 'R' },
    { src: this.rutaBase + 'S.jpg', letra: 'S' },
    { src: this.rutaBase + 'T.jpg', letra: 'T' },
    { src: this.rutaBase + 'U.jpg', letra: 'U' },
    { src: this.rutaBase + 'V.jpg', letra: 'V' },
    { src: this.rutaBase + 'W.jpg', letra: 'W' },
    { src: this.rutaBase + 'X.jpg', letra: 'X' },
    { src: this.rutaBase + 'Y.jpg', letra: 'Y' },
    { src: this.rutaBase + 'Z.jpg', letra: 'Z' }
  ];
}
