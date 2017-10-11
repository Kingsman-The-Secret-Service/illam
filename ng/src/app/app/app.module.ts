import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { HttpClientModule, HTTP_INTERCEPTORS }    from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';
import {
    NbActionsModule,
    NbCardModule,
    NbLayoutModule,
    NbSidebarModule,
    NbTabsetModule,
    NbThemeModule,
    NbUserModule,
    NbMenuModule
} from '@nebular/theme';


import { NbSidebarService } from '@nebular/theme';


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
        HttpModule,
        HttpClientModule,
        RouterModule.forRoot(         
            AppRoutes,
            // { enableTracing: true }
        ),
        NbThemeModule.forRoot({ name: 'default' }),
        NbLayoutModule,
        NbSidebarModule,
        NbActionsModule,
        NbUserModule,
        NbCardModule,
        NbMenuModule.forRoot(),
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
