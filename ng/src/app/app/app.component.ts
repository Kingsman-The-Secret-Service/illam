import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: '<router-outlet></router-outlet>'
})

export class AppComponent {
  title = "Kananku Puthagam"
}

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html'
})

export class ChildComponent {
  title = "Child - Kananku Puthagam"
}