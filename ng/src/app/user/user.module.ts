import { NgModule }  from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule }  from '@angular/forms';
import { RouterModule } from '@angular/router';

// Theme
import { NbCardModule, NbLayoutModule } from '@nebular/theme';

// Service
import { AuthService } from '../auth/auth.service';
import { UserService } from './user.service';

// Component 
import { 
    CreateUserComponent, 
    ShowUserComponent, 
    UpdateUserComponent 
} from './user.component';

// Route
import { UserRoutes } from './user.route';

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        RouterModule.forChild(UserRoutes),
        NbCardModule,
        NbLayoutModule,
    ],
    declarations: [
        CreateUserComponent, 
        ShowUserComponent, 
        UpdateUserComponent
    ],
    providers: [
        UserService
    ],
})
export class UserModule {}