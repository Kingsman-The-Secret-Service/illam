import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Router } from "@angular/router";

// Service
import { ToasterService } from 'angular2-toaster';
import { AuthService } from '../auth/auth.service';
import { UserService } from './user.service';

// Model
import { User } from './user';

class UserForm{

	errorMessage: string;
	userForm: FormGroup;
	family_name: FormControl;
	family_hexcolor: FormControl;
	name: FormControl;
	email: FormControl;
	phone: FormControl;
	password: FormControl;

	constructor(){

		this.family_name = new FormControl('',[]);
		this.family_hexcolor = new FormControl('',[]);
		this.name = new FormControl('', []);
		this.email = new FormControl('', []);
		this.phone = new FormControl('', []);
		this.password = new FormControl('',[]);

		this.userForm = new FormGroup({
			family_name: this.family_name,
			family_hexcolor: this.family_hexcolor,
			name: this.name,
			email: this.email,
			phone: this.phone,
			password: this.password
		});
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
  selector: 'user-create',
  templateUrl: './create.html'
})
export class CreateUserComponent extends UserForm implements OnInit{

	constructor(private auth:AuthService, private user:UserService){

		super();
	}

	ngOnInit(){}

	onSubmit(){

		if (this.userForm.valid) {

			this.user.post(this.userForm.value)
				.subscribe(
					dataResponse => this.handleData(dataResponse),
					errorResponse => this.handleError(errorResponse)
				);
		}
	}

	handleData(dataResponse){

		this.auth.preserveUser(dataResponse);
	}
	
}

@Component({
  selector: 'user-update',
  templateUrl: './update.html'
})
export class UpdateUserComponent extends UserForm implements OnInit{
	

	constructor(
		private auth:AuthService, 
		private user:UserService,
		private toasterService: ToasterService){

		super();
	}

	ngOnInit(){

		this.family_name.setValue(localStorage.getItem('family_name'));
		this.family_hexcolor.setValue(localStorage.getItem('family_hexcolor'));
		this.name.setValue(localStorage.getItem('name'));
		this.phone.setValue(localStorage.getItem('phone'));
	}

	onSubmit(){

		if (this.userForm.valid) {

			let userId = localStorage.getItem('id');
			let familyId = localStorage.getItem('family_id');
			let formData = this.userForm.value;
			formData['id'] = userId;
			formData['family_id'] = familyId;

			delete formData['email'];
			delete formData['password'];

			this.user.put(formData)
				.subscribe(
					dataResponse => this.handleData(dataResponse),
					errorResponse => this.handleError(errorResponse)
				);
		}
	}

	handleData(dataResponse){
		
		this.toasterService.pop('success', dataResponse['message']);
		this.auth.storeData(dataResponse['user']);
	}
}


@Component({
  selector: 'user-show',
  templateUrl: './show.html'
})
export class ShowUserComponent implements OnInit{

	userProfile;

	constructor(private user:UserService){}

	ngOnInit(){

		this.user.get().subscribe(profile => this.userProfile = profile);
	}
}

