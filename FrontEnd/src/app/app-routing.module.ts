import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ContactoComponent } from './components/contacto/contacto.component';
import { LoginComponent } from './components/login/login.component';
import { PalabrasComponent } from './components/palabras/palabras.component';
import { AlfabetoComponent } from './components/alfabeto/alfabeto.component';
import { LeccionesComponent } from './components/lecciones/lecciones.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path:'contacto', component: ContactoComponent},
  { path:'login', component: LoginComponent},
  { path:'palabras', component: PalabrasComponent},
  { path:'alfabeto', component: AlfabetoComponent},
  { path :'lecciones', component:LeccionesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
