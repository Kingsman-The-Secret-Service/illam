import { NgModule }  from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule }  from '@angular/forms';
import { RouterModule } from '@angular/router';

// Service
import { AuthService } from '../auth/auth.service';
import { UserService } from './user.service';

// Component 
import { UserFormComponent } from './user.component';

// Route
import { UserRoutes } from './user.route';

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        RouterModule.forChild(UserRoutes)
    ],
    declarations: [
        UserFormComponent
    ],
    providers: [
        UserService
    ],
})
export class UserModule {}