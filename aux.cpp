void sacar(int persona,int termina,vector <intervalo> intervalos){

	if (!(persona==0 and termina!=0) and !(persona!=0 and termina ==0)){

		if(persona==0 and termina==0){
			todos.push_back(intervalos);

		}else{

			for(int i=1;i<=termina;i++){
				vector <intervalo> modIntervalos = intervalos;
				intervalo agregar;
				agregar.a=i;
				agregar.b=termina;
				modIntervalos.push_back(agregar);
				sacar(persona-1,i-1,modIntervalos);

			}
		}
	}
}
