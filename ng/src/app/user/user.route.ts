import { Routes } from '@angular/router';

// Service
import { AuthService } from '../auth/auth.service';

// Component
import { ChildComponent } from '../app/app.component';
import { UserFormComponent, UserProfileComponent } from './user.component';

export const UserRoutes: Routes = [
	{ path:'register', component:UserFormComponent },
	{ 
		path:'profile', 
		component:ChildComponent, 
		canActivate: [AuthService],
		canActivateChild: [AuthService],
        children:[
            {path:'', component:UserProfileComponent }
        ]
	},
];