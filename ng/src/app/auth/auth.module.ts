import { NgModule }       from '@angular/core';
import { ReactiveFormsModule }    from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AuthService } from './auth.service';
import { LoginFormComponent } from './auth.component';

const AuthRoutes: Routes = [
    { path:'login', component:LoginFormComponent }
];

@NgModule({
    imports: [
        ReactiveFormsModule,
        RouterModule.forChild(AuthRoutes)
    ],
    declarations: [
        LoginFormComponent,
    ],
    providers: [
        AuthService
    ],
})
export class AuthModule {}