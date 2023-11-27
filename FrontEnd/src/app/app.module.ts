import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/shared/navbar/navbar.component';
import { HomeComponent } from './components/home/home.component';
import { HttpClientModule } from '@angular/common/http';
import { FooterComponent } from './components/shared/footer/footer.component';
import { ContactoComponent } from './components/contacto/contacto.component';
import { LoginComponent } from './components/login/login.component';
import { PalabrasComponent } from './components/palabras/palabras.component';
import { YoutubePipe } from './pipe/youtube.pipe';
import { AlfabetoComponent } from './components/alfabeto/alfabeto.component';
import { LeccionesComponent } from './components/lecciones/lecciones.component';
import { RegistroComponent } from './components/registro/registro.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    FooterComponent,
    ContactoComponent,
    LoginComponent,
    PalabrasComponent,
    YoutubePipe,
    AlfabetoComponent,
    LeccionesComponent,
    RegistroComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
