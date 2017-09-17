import { Component, OnInit } from '@angular/core';
import { Category } from './category';
import { CategoryService } from './category.service';
import { ActivatedRoute }   from '@angular/router';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})

export class CategoryComponent implements OnInit {

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
