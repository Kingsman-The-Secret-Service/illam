export class User{
	id:number;
	family_id: number;
	name: string;
	email:string;
	phone:string;
	image:string;
	api_token:string;
}

export class Family{
	id:number;
	name: string;
	hexcolor:string;
	user: User[]
}