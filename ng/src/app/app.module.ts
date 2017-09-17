import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule }   from '@angular/forms'; 
import { HttpModule }    from '@angular/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app/app.component';
import { CategoryModule } from './category/category.module';
import { PeopleComponent } from './people/people.component';



@NgModule({
  declarations: [
    AppComponent,
    PeopleComponent,   
  ],
  imports: [
    CategoryModule,
    BrowserModule,
    FormsModule,
    HttpModule,
    NgbModule.forRoot(),  
    RouterModule.forRoot([
     ])
    ],
  providers: [
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
