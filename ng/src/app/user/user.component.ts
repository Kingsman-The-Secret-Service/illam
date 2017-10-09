import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Router } from "@angular/router";

// Service
import { AuthService } from '../auth/auth.service';
import { UserService } from './user.service';


@Component({
  selector: 'user-register',
  templateUrl: './register.html',
  styleUrls: ['./register.css']
})
export class UserFormComponent implements OnInit{

	errorMessage: string;
	registerForm: FormGroup;
	name: FormControl;
	email: FormControl;
	phone: FormControl;
	password: FormControl;

	constructor(private auth:AuthService, private user:UserService, private router: Router){}

	ngOnInit(){

		this.name = new FormControl('', []);
		this.email = new FormControl('', []);
		this.phone = new FormControl('', []);
		this.password = new FormControl('',[]);

		this.registerForm = new FormGroup({
			name: this.name,
			email: this.email,
			phone: this.phone,
			password: this.password
		});
	}

	onSubmit(){

		if (this.registerForm.valid) {

			this.user.post(this.registerForm.value)
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