import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Environment
import { environment } from '../../environments/environment';

// Model
import { Category } from './category';

@Injectable()
export class CategoryService {

	private url = environment.apiEndPoint + 'category';

  	constructor(private http: HttpClient) { }

	get(): Observable<Category[]>{

		return this.http.get(this.url);
  	}
}
