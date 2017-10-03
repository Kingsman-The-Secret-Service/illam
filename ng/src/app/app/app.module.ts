import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent, ChildComponent } from './app.component';
import { AuthModule } from '../auth/auth.module';
import { DashboardModule } from '../dashboard/dashboard.module';
import { CategoryModule } from '../category/category.module';

const AppRoutes: Routes = [];

@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        RouterModule.forRoot(         
            AppRoutes,
            // { enableTracing: true }
        ),
        AuthModule,
        DashboardModule,
        CategoryModule,
    ],
    declarations: [
        AppComponent,
        ChildComponent
    ],
    bootstrap: [
        AppComponent
    ]
})
export class AppModule { }
