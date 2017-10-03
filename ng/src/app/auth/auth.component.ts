import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators, AbstractControl } from '@angular/forms';
import { Router } from "@angular/router";
import { AuthService } from './auth.service';

export interface FormError {
  error: string;
  params: any;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginFormComponent implements OnInit {

	message: string;
	isValidFormSubmitted: boolean;
	loginForm: FormGroup;
	email: FormControl;
	password: FormControl;

	constructor(private auth: AuthService, private router: Router){

	}

	ngOnInit(){

		let token = localStorage.getItem('token');

		if(token){
			this.router.navigate(["/"]);
		}

		this.createFormControl();

		this.loginForm = new FormGroup({
			email: this.email,
			password: this.password
		});
	}

	createFormControl(){

		this.email = new FormControl('', [
			// Validators.required,
			// Validators.pattern("[^ @]*@[^ @]*")
		]);

		this.password = new FormControl('',[
			// Validators.required,
			// Validators.minLength(5)
		])
	}

	onSubmit() {
		if (this.loginForm.valid) {

			this.auth.getToken(this.loginForm.value)
				.subscribe(
					response => this.handleSuccess(response),
					error => this.handleError(error)
				);
			
			// this.loginForm.reset();
		}
	}

	handleSuccess(response){

		let data = response['data'];
		let token = data['api_token'];
		
		localStorage.setItem('token', token);
		this.router.navigate(["/"]);
	}

	handleError(errors) {

		for(let error in errors){

			if(['message', 'data'].indexOf(error) > -1){
				
				this.message = errors[error];
			}else{

				this[error].setErrors(errors[error]);
				console.log("Err Comp",error,errors[error]);
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
