import { Routes } from '@angular/router';

// Service
import { AuthService } from '../auth/auth.service';

// Component
import { ChildComponent } from '../app/app.component';
import { CategoryListComponent, CategoryFormComponent } from './category.component';

export const CategoryRoutes: Routes = [
    {
        path:'category',
        component:ChildComponent,
        canActivate: [AuthService],
        canActivateChild: [AuthService],
        children:[
            {path:'', redirectTo:'/category/list', pathMatch:'full' },
            {path:'list', component:CategoryListComponent },
            {path:'create', component:CategoryFormComponent }
        ]
    }
];