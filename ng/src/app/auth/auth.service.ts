import { Injectable } from '@angular/core';
import { Http, RequestOptions, Headers }    from '@angular/http';
import { Router, CanActivate, CanActivateChild,
		ActivatedRouteSnapshot, RouterStateSnapshot} from "@angular/router";

import 'rxjs/add/operator/toPromise';
import 'rxjs/add/operator/map'

import { environment } from '../../environments/environment';


@Injectable()
export class AuthService implements CanActivate, CanActivateChild {

	private url = environment.apiEndPoint + 'authenticate';

	constructor(private http: Http, private router: Router) {}

	canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {

		this.isLoggedIn();
		return true;
	}

	canActivateChild(){

		this.isLoggedIn();
		return true;
	}

	isLoggedIn(){

		let token = localStorage.getItem('token');

		if(token){

			return true;

		}else{

			this.router.navigate(['login']);
		}
	}

	getToken (formData:object){

		return this.http.post(this.url, formData)
				.toPromise()
				.then(response => response.json())
				.catch(error => error.json());
	}

}