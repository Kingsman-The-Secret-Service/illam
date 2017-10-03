import { NgModule }       from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule }    from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AuthService } from './auth.service';
import { LoginFormComponent, LogoutComponent } from './auth.component';

const AuthRoutes: Routes = [
    { path:'login', component:LoginFormComponent },
    { path:'logout', component:LogoutComponent}
];

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        RouterModule.forChild(AuthRoutes)
    ],
    declarations: [
        LoginFormComponent,
        LogoutComponent
    ],
    providers: [
        AuthService
    ],
})
export class AuthModule {}