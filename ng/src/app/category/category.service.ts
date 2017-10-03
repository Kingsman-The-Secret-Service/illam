import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions }    from '@angular/http';
import 'rxjs/add/operator/toPromise';
import 'rxjs/add/operator/map'

import { environment } from '../../environments/environment';
import { Category } from './category';

@Injectable()
export class CategoryService {

	private url = environment.apiEndPoint + 'category';

  	constructor(private http: Http) { }

	getCategories(): Promise<Category[]>{

		let headers = new Headers({ 
			'Authorization':'UHRrNXN2SzUxMmlqc2ZNb3MxVjUyR1g3RTlEU3JSaFlFMndKb0ZNWA=='
		});
        let options = new RequestOptions({ headers: headers });

		return this.http.get(this.url, options)
				.toPromise()
				.then(response => response.json().category as Category[])
				.catch(this.handleError);

  	}

  	private handleError(error: any): Promise<any> {
		
		console.error('An error occurred', error); 
		return Promise.reject(error.message || error);
	}

}
