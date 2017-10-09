import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Environment
import { environment } from '../../environments/environment';

@Injectable()
export class UserService{
	
	private url = environment.apiEndPoint + 'user';

	constructor(private http: HttpClient) {}

	post(formData){
		return this.http.post(this.url, formData);
	}
}