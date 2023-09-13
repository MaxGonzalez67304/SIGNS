import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ObjectId } from 'bson';
import {
  _URL_GET_ALL_PALABRAS,
  _URL_GET_PALABRA_BY_NOMBRE,
  _URL_POST_PALABRA,
  _URL_UPDATE_PALABRA_BY_ID,
  _URL_DELETE_PALABRA_BY_ID
} from '../config/config';
import {
  _URL_GET_ALL_USUARIOS,
  _URL_GET_USUARIO_BY_ID,
  _URL_POST_USUARIO,
  _URL_UPDATE_USUARIO_BY_ID,
  _URL_DELETE_USUARIO_BY_ID
} from '../config/config';

@Injectable({
  providedIn: 'root'
})
export class ConexionService {

  constructor(private http: HttpClient) { }

  getAllPalabras() {
    return this.http.get(_URL_GET_ALL_PALABRAS);
  }

  getPalabraByNombre(nombre: string) {
    return this.http.get(_URL_GET_PALABRA_BY_NOMBRE + '/' + nombre);
  }

  postPalabra(palabra: string, video: string) {

    const params = JSON.stringify({ "palabra": palabra, "video": video });

    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.post(_URL_POST_PALABRA, params, {
      headers: httpHeaders
    });
  }

  updatePalabraById(id: ObjectId, palabra: string, video: string) {

    const params = JSON.stringify({ "palabra": palabra, "video": video });

    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.put(_URL_UPDATE_PALABRA_BY_ID + '/' + id, params, {
      headers: httpHeaders
    });
  }

  deletePalabraById(id: ObjectId) {
    return this.http.delete(_URL_DELETE_PALABRA_BY_ID + '/' + id);
  }

  getAllUsuarios() {
    return this.http.get(_URL_GET_ALL_USUARIOS);
  }

  getUsuarioById(id: ObjectId) {
    return this.http.get(_URL_GET_USUARIO_BY_ID + '/' + id);
  }

  postUsuario(nombre: string, correo: string, username: string, password: string) {

    const params = JSON.stringify({ "nombre": nombre, "correo": correo, "username": username, "password": password });

    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.post(_URL_POST_USUARIO, params, {
      headers: httpHeaders
    });
  }

  updateUsuarioById(id: ObjectId, nombre: string, correo: string, username: string, password: string) {

    const params = JSON.stringify({ "nombre": nombre, "correo": correo, "username": username, "password": password });

    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.put(_URL_UPDATE_USUARIO_BY_ID + '/' + id, params, {
      headers: httpHeaders
    });
  }

  deleteUsuarioById(id: ObjectId) {
    return this.http.delete(_URL_DELETE_USUARIO_BY_ID + '/' + id);
  }

}
