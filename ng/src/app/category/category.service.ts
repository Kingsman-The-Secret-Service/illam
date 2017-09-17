import { Injectable } from '@angular/core';
import { Http }    from '@angular/http';
import { Category } from './category';
import 'rxjs/add/operator/toPromise';
import 'rxjs/add/operator/map'

@Injectable()
export class CategoryService {

	private url = 'http://192.168.33.10/api/category?api_token=UHRrNXN2SzUxMmlqc2ZNb3MxVjUyR1g3RTlEU3JSaFlFMndKb0ZNWA==';

  	constructor(private http: Http) { }

	getCategories(): Promise<Category[]>{

		return this.http.get(this.url)
				.toPromise()
				.then(response => response.json().category as Category[])
				.catch(this.handleError);

  	}

  	private handleError(error: any): Promise<any> {
		
		console.error('An error occurred', error); 
		return Promise.reject(error.message || error);
	}

}
