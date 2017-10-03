import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators, AbstractControl } from '@angular/forms';

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

	loginForm: FormGroup;
	email: FormControl;
	password: FormControl;

	constructor(private auth: AuthService){

	}

	ngOnInit(){

		this.createFormControl();

		this.loginForm = new FormGroup({
			email: this.email,
			password: this.password
		});
	}

	createFormControl(){

		this.email = new FormControl('', [
			Validators.required,
			Validators.pattern("[^ @]*@[^ @]*")
		]);

		this.password = new FormControl('',[
			Validators.required,
			Validators.minLength(5)
		])
	}

	onSubmit() {
		if (this.loginForm.valid) {

			this.auth.getToken(this.loginForm.value)
			.then(
				res => console.log(res)
			)
			.catch(err => console.log(err));
			// this.loginForm.reset();
		}
	}

	// formErrors(): FormError[] {
 //    if (this.submitted && this.form.errors) {
 //      return this.getErrors(this.form);
 //    }
 //  }

 //  fieldErrors(name: string): FormError[] {
 //    let control = this.findFieldControl(name);
 //    if (control && (control.touched || this.submitted) && control.errors) {
 //      return this.getErrors(control);
 //    } else {
 //      return undefined;
 //    }
 //  }

 //  resetFieldErrors(name: string): void {
 //    this.form.get(name).setErrors(null);
 //  }

 //  protected handleSubmitSuccess(category: Category) {
 //    this.added.emit(category)
 //  }

 //  protected handleSubmitError(error: any) {
 //    if (error.status === 422) {
 //      const data = error.json();
 //      const fields = Object.keys(data || {});
 //      fields.forEach((field) => {
 //        const control = this.findFieldControl(field);
 //        const errors = this.fetchFieldErrors(data, field);
 //        control.setErrors(errors);
 //      });
 //    }
 //  }

 //  protected getErrors(control: AbstractControl): FormError[] {
 //    return Object.keys(control.errors)
 //      .filter((error) => control.errors[error])
 //      .map((error) => {
 //        let params = control.errors[error];
 //        return {
 //          error: error,
 //          params: params === true || params == {} ? null : params
 //        };
 //      });
 //  }

 //  protected findFieldControl(field: string): AbstractControl {
 //    let control: AbstractControl;
 //    if (field === 'base') {
 //      control = this.form;
 //    } else if (this.form.contains(field)) {
 //      control = this.form.get(field);
 //    } else if (field.match(/_id$/) && this.form.contains(field.substring(0, field.length - 3))) {
 //      control = this.form.get(field.substring(0, field.length - 3));
 //    } else if (field.indexOf('.') > 0) {
 //      let group = this.form;
 //      field.split('.').forEach((f) => {
 //        if (group.contains(f)) {
 //          control = group.get(f);
 //          if (control instanceof FormGroup) group = control;
 //        } else {
 //          control = group;
 //        }
 //      })
 //    } else {
 //      // Field is not defined in form but there is a validation error for it, set it globally
 //      control = this.form;
 //    }
 //    return control;
 //  }

 //  private fetchFieldErrors(data: any, field: string): any {
 //    const errors = {};
 //    data[field].forEach((e) => {
 //      let name: string = e.error;
 //      delete e.error;
 //      errors[name] = e;
 //    });
 //    return errors;
 //  }
}
