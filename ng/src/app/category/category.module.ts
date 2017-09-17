import { NgModule }       from '@angular/core';
import { CommonModule }   from '@angular/common';
import { FormsModule }    from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { CategoryService } from './category.service';
import { CategoryComponent } from './category.component';
import { CategoryFormComponent } from './category-form/category-form.component';

const categoryRoutes: Routes = [
  { path: 'category',  component: CategoryComponent },
  { path: 'category/create',  component: CategoryFormComponent }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    RouterModule.forChild(categoryRoutes)
  ],
  declarations: [
    CategoryComponent,
    CategoryFormComponent
  ],
  providers: [ 
  	CategoryService 
  ]
})

export class CategoryModule {}