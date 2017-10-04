import { Routes } from '@angular/router';

// Component
import { LoginFormComponent, LogoutComponent } from './auth.component';

export const AuthRoutes: Routes = [
    { path:'login', component:LoginFormComponent },
    { path:'logout', component:LogoutComponent}
];