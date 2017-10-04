import { NgModule }       from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule }    from '@angular/forms';
import { RouterModule } from '@angular/router';

// Service
import { AuthService } from './auth.service';

// Component 
import { LoginFormComponent, LogoutComponent } from './auth.component';

// Route
import { AuthRoutes } from './auth.route';

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