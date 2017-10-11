import { Component } from '@angular/core';
import { 
	NbMediaBreakpoint,
  	NbMediaBreakpointsService,
  	NbThemeService,
	NbSidebarService 

} from '@nebular/theme';


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

  	name = localStorage.getItem('name');
    menu = mainMenu;
    userMenu = userMenu;
    

	constructor(private sidebarService: NbSidebarService) {}

	toggleSidebar(): boolean {
		this.sidebarService.toggle(true, 'menu-sidebar');
		return false;
	}

}


import { NbMenuItem } from '@nebular/theme';

const mainMenu: NbMenuItem[] = [
  {
    title: 'Dashboard',
    icon: 'nb-home',
    link: '/',
    home: true,
  },
  {
    title: 'Category',
    icon: 'nb-list',
    link: '/category',
    children: [
      {
        title: 'List',
        link: '/category/list',
      },
      {
        title: 'Create',
        link: '/category/create',
      },
    ],
  }
];

const userMenu: NbMenuItem[]  = [
	{ title: 'Profile', link: '/profile'},
	{ title: 'Log out', link: '/logout' }
];