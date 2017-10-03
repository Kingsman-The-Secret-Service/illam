import { Component, OnInit } from '@angular/core';
import { ActivatedRoute }   from '@angular/router';

import { Category } from './category';
import { CategoryService } from './category.service';



@Component({
    selector: 'app-category-list',
    templateUrl: './category-list.component.html',
})

export class CategoryListComponent implements OnInit {

    title = 'Category';
    categories: Category[];
      
    constructor(private categoryService: CategoryService, private route: ActivatedRoute) { 

    // this.route.params.subscribe(params => {
    //    console.log(params);
    //  });
    }

    getCategories(): void {
        this.categoryService
        .getCategories()
        .then(categories => this.categories = categories);
    }

    ngOnInit(): void {

        this.getCategories();
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

        categoryService
        .getCategories()
        .then(categories => this.categories = categories);
    }


    ngOnInit() {
    }

    onSubmit() {
  //       if (this.category.valid) {
  //   console.log("Form Submitted!");
  // }
    }

}

