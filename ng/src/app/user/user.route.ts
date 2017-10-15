import { Routes } from '@angular/router';

// Service
import { AuthService } from '../auth/auth.service';

// Component
import { ChildComponent } from '../app/app.component';
import { CreateUserComponent, ShowUserComponent, UpdateUserComponent } from './user.component';

export const UserRoutes: Routes = [
	{ path:'register', component:CreateUserComponent },
	{ 
		path:'profile', 
		component:ChildComponent, 
		canActivate: [AuthService],
		canActivateChild: [AuthService],
        children:[
            {path:'', component:ShowUserComponent },
            {path:'update', component:UpdateUserComponent }
        ]
	},
];