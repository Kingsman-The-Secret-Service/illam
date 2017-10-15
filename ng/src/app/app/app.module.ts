import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

// Theme
import {
    // Module
    NbActionsModule,
    NbCardModule,
    NbLayoutModule,
    NbSidebarModule,
    NbTabsetModule,
    NbThemeModule,
    NbUserModule,
    NbMenuModule,
    // Service
    NbSidebarService
} from '@nebular/theme';

// Util
import { ToasterModule } from 'angular2-toaster';


// Bootstrap
import { AppComponent, ChildComponent } from './app.component';
import { AuthInterceptor } from '../auth/auth.interceptor';

// Modules
import { AuthModule } from '../auth/auth.module';
import { UserModule } from '../user/user.module';
import { DashboardModule } from '../dashboard/dashboard.module';
import { CategoryModule } from '../category/category.module';

const AppRoutes: Routes = [];

@NgModule({
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        RouterModule.forRoot(         
            AppRoutes,
            // { enableTracing: true }
        ),
        
        // Theme
        NbThemeModule.forRoot({ name: 'default' }),
        NbLayoutModule,
        NbSidebarModule,
        NbActionsModule,
        NbUserModule,
        NbCardModule,
        NbMenuModule.forRoot(),

        // Util
        ToasterModule,

        // Application
        AuthModule,
        UserModule,
        DashboardModule,
        CategoryModule,
    ],
    declarations: [
        AppComponent,
        ChildComponent
    ],
    providers: [
        {
            provide: HTTP_INTERCEPTORS,
            useClass: AuthInterceptor,
            multi: true
        },
        NbSidebarService
    ],
    bootstrap: [
        AppComponent
    ]
})
export class AppModule { }
