import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
	intercept (req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
		
		const token: string = localStorage.getItem('api_token');

		if (token) {
		    req = req.clone({ headers: req.headers.set('Authorization', token) });
		}

		if (!req.headers.has('Content-Type')) {
		    req = req.clone({ headers: req.headers.set('Content-Type', 'application/json') });
		}

		req = req.clone({ headers: req.headers.set('Accept', 'application/json') });

		return next.handle(req);
	}
}