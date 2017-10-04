import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Router } from "@angular/router";

// Service
import { AuthService } from './auth.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginFormComponent implements OnInit {
	
	loginForm: FormGroup;
	errorMessage: string;
	email: FormControl;
	password: FormControl;

	constructor(private auth: AuthService, private router: Router){

		let token = localStorage.getItem('token');

		if(token){
			this.router.navigate(["/"]);
		}
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

		let user = dataResponse['user'];
		let token = user['api_token'];
		
		localStorage.setItem('token', token);
		this.router.navigate(["/"]);
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

	constructor(private router: Router){}

	ngOnInit(){

		localStorage.removeItem('token');
		this.router.navigate(["/"]);
	}
}
