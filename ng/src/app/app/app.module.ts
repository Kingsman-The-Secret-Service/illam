import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { HttpClientModule, HTTP_INTERCEPTORS }    from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

// Bootstrap
import { AppComponent, ChildComponent } from './app.component';
import { AuthInterceptor } from '../auth/auth.interceptor';

// Modules
import { AuthModule } from '../auth/auth.module';
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
        AuthModule,
        DashboardModule,
        CategoryModule,
    ],
    declarations: [
        AppComponent,
        ChildComponent
    ],
    providers: [{
        provide: HTTP_INTERCEPTORS,
        useClass: AuthInterceptor,
        multi: true
    }],
    bootstrap: [
        AppComponent
    ]
})
export class AppModule { }
