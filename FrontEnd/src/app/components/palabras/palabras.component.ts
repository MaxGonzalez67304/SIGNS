import { Component } from '@angular/core';
import { YoutubeService } from 'src/app/services/youtube.service';

declare var $: (arg0: string) => { (): any; new(): any; modal: { (arg0: string): void; new(): any; }; };

@Component({
  selector: 'app-palabras',
  templateUrl: './palabras.component.html',
  styleUrls: ['./palabras.component.css']
})
export class PalabrasComponent {
  misVideos : any[] = [];
  videoId : string = '';

  constructor(private youtubeService: YoutubeService) {
    this.youtubeService.obtenerVideos().subscribe((resp : any) => {
      console.log(resp);
      this.misVideos = resp.items;
    });
  }

  ngOnInit() {

  }

  detalleVideo(detalle : string) {
    console.log(detalle);
    this.videoId = detalle;
    $('#exampleModal').modal('show');
  }

  cerrarModal() {
    this.videoId = '';
    $('#exampleModal').modal('hide');
  }

}
