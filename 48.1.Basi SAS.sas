/*DATA STEP*/
data myclass;
    set sashelp.class; /*seleziono una tabella (una di default di SAS*/
run;
/*PROC STEP*/
proc print data=myclass; /*mostro una tabella*/
run;

/*Nuova Tabella default di SAS*/
data mycars;
    set sashelp.cars; /*seleziono una tabella (una di default di SAS*/
	
	/*Calcola la media*/
	AvgMPG=mean(mpg_city,mpg_higway);
run;

/*Titolo della nuova tabella*/
title "Auto con media MPG superiore a 35";
proc print data=mycars; /*mostro una tabella*/
	var make model type avgmpg;
	/*Mostra solo chi ha ma media >35*/
	where AvgMPG >35;
run;

/*Raggruppa le auto per tipo*/
proc means data=mycars mean mini max maxdec=1
	var avgmpg;
	class type;
RUN;



