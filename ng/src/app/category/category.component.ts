import { Component, OnInit } from '@angular/core';

import { Category } from './category';
import { CategoryService } from './category.service';



@Component({
    selector: 'app-category-list',
    templateUrl: './category-list.component.html',
})

export class CategoryListComponent implements OnInit {

    title = 'Category';
    categories: Category[];
      
    constructor(private categoryService: CategoryService) { }

    ngOnInit(): void {

       this.categoryService.get()
        .subscribe(categories => this.categories = categories['category']);
    }

}

@Component({
  selector: 'app-category-form',
  templateUrl: './category-form.component.html'
})
export class CategoryFormComponent implements OnInit {

    categories: Category[];
    category = new Category();

    constructor(private categoryService: CategoryService) { 

        categoryService.get()
        .subscribe(categories => this.categories = categories['category']);
    }


    ngOnInit() {
    }

    onSubmit() {
    }

}

