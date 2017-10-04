import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Authenticate Routes
import { Router, CanActivate, CanActivateChild,
		ActivatedRouteSnapshot, RouterStateSnapshot} from "@angular/router";

// Environment
import { environment } from '../../environments/environment';


@Injectable()
export class AuthService implements CanActivate, CanActivateChild {

	private url = environment.apiEndPoint + 'authenticate';

	constructor(private http: HttpClient, private router: Router) {}

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

	authenticate (formData:object){

		return this.http.post(this.url, formData);
	}
}