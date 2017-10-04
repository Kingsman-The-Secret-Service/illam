import { NgModule }       from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { RouterModule } from '@angular/router';

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