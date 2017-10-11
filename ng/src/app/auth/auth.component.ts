import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Router } from "@angular/router";

// Service
import { AuthService } from './auth.service';


@Component({
  selector: 'auth-login',
  templateUrl: './login.html'
})
export class LoginFormComponent implements OnInit {
		
	errorMessage: string;
	loginForm: FormGroup;
	email: FormControl;
	password: FormControl;

	constructor(private auth: AuthService, private router: Router){

		this.auth.isLoggedIn();
	}

	ngOnInit(){

		this.email = new FormControl('', []);
		this.password = new FormControl('',[]);

		this.loginForm = new FormGroup({
			email: this.email,
			password: this.password
		});
	}

	onSubmit() {
		if (this.loginForm.valid) {

			this.auth.authenticate(this.loginForm.value)
				.subscribe(
					dataResponse => this.handleData(dataResponse),
					errorResponse => this.handleError(errorResponse)
				);
		}
	}

	handleData(dataResponse){

		this.auth.preserveUser(dataResponse);
	}

	handleError(errorResponse) {
		let errors = JSON.parse(errorResponse['error']);
		this.password.setValue(null);
		for(let err in errors){
			if(['error', 'data'].indexOf(err) > -1){
				this.errorMessage = errors[err];
			}else{
				this[err].setErrors(errors[err]);
			}
		}
	}
}

@Component({
	template:""
})
export class LogoutComponent implements OnInit{

	constructor(private auth: AuthService, private router: Router){}

	ngOnInit(){

		this.auth.doLogout();
	}
}
