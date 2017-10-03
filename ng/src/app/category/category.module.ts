import { NgModule }       from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthService } from '../auth/auth.service';
import { ChildComponent } from '../app/app.component';

import { CategoryService } from './category.service';
import { CategoryListComponent, CategoryFormComponent } from './category.component';

const CategoryRoutes: Routes = [
    {
        path:'category',
        component:ChildComponent,
        canActivate: [AuthService],
        canActivateChild: [AuthService],
        children:[
            {path:'', component:CategoryListComponent },
            {path:'create', component:CategoryFormComponent }
        ]
    }
];

@NgModule({
    imports: [
        RouterModule.forChild(CategoryRoutes)
    ],
    declarations: [
        CategoryListComponent,
        CategoryFormComponent,
    ],
    providers: [ 
    	CategoryService 
    ]
})

export class CategoryModule {}