import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthService } from '../auth/auth.service';
import { ChildComponent } from '../app/app.component';

import { DashboardComponent } from './dashboard.component';


const DashboardRoutes: Routes = [
    {
        path:'', 
        component:ChildComponent,
        canActivate: [AuthService],
        canActivateChild: [AuthService],
        children:[
            {path:'', component:DashboardComponent },
        ]
    }
]

@NgModule({
    imports: [
        RouterModule.forChild(DashboardRoutes)
    ],
    declarations: [
        DashboardComponent,
    ],
})
export class DashboardModule { }
