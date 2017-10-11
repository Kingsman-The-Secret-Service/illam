import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Router } from "@angular/router";

// Service
import { AuthService } from '../auth/auth.service';
import { UserService } from './user.service';

// Model
import { User } from './user';

@Component({
  selector: 'user-register',
  templateUrl: './register.html'
})
export class UserFormComponent implements OnInit{

	errorMessage: string;
	registerForm: FormGroup;
	family_name: FormControl;
	family_hexcolor: FormControl;
	name: FormControl;
	email: FormControl;
	phone: FormControl;
	password: FormControl;

	constructor(private auth:AuthService, private user:UserService, private router: Router){}

	ngOnInit(){

		this.family_name = new FormControl('',[]);
		this.family_hexcolor = new FormControl('',[]);
		this.name = new FormControl('', []);
		this.email = new FormControl('', []);
		this.phone = new FormControl('', []);
		this.password = new FormControl('',[]);

		this.registerForm = new FormGroup({
			family_name: this.family_name,
			family_hexcolor: this.family_hexcolor,
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


@Component({
  selector: 'user-profile',
  templateUrl: './profile.html'
})
export class UserProfileComponent implements OnInit{

	userProfile;

	constructor(private user:UserService){}

	ngOnInit(){

		this.user.get().subscribe(profile => this.userProfile = profile);
	}
}