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
		this.canLoggedIn();
		return true;
	}

	canActivateChild(){
		this.canLoggedIn();
		return true;
	}

	canLoggedIn(){

	 	let token = localStorage.getItem('api_token');

		if(token){
			return true;
		}else{
			this.router.navigate(['login']);
		}
	}

	isLoggedIn(){

		let token = localStorage.getItem('api_token');

		if(token){
			this.router.navigate(['/']);
		}else{
			this.router.navigate(['login']);
		}
	}

	authenticate (formData:any){

		return this.http.post(this.url, formData);
	}

	preserveUser(userData){

		let user = userData['user'];

		for(let key in user){

			localStorage.setItem(key, user[key]);
		}
		this.isLoggedIn();
	}

	doLogout(){

		localStorage.clear();
		this.isLoggedIn();
	}

	
}