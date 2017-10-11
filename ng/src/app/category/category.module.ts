import { NgModule }       from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NbCardModule } from '@nebular/theme';

// Service
import { CategoryService } from './category.service';

// Component
import { CategoryListComponent, CategoryFormComponent } from './category.component';

// Routes
import { CategoryRoutes } from './category.route';


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        RouterModule.forChild(CategoryRoutes),
        NbCardModule
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