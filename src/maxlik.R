#!/usr/bin/Rscript 
N=8 #number of elements
sqrt2=sqrt(2)
#load the comparison data as a matrix
file=file("data","r")
M = matrix(scan(file,quiet=TRUE),ncol=N,nrow=N,byrow=TRUE)
close(file)

#maximum likelihood function
likfun<-function(p,...){
	if(length(p)!=N-1) return("Error")
	range=seq(length(p)+1)
	p[N]=0
	F=0
	for(i in range){
		for(j in range){
			if(i==j) next
			F=F+M[i,j]*log(pnorm(p[i]-p[j],sd=sqrt2))
		}
	}	
	return (-F)
}

argv=commandArgs(TRUE)
argc=length(argv)
if(argc!=N-1) quit(status=1)
Ini=numeric(argc)
for(i in seq(argv)){
	Ini[i]=as.numeric(argv[i])
}

nlm<-nlm(likfun,Ini,print.level=0)
parameters=c(nlm$estimate,0)
cat("Parameters:",parameters,"\n")
rankings=c()

#Sample size S.  Samples based on parameters derived from maximum likelihood.
#Tallies proportion of each rank order which occurs.
S=1000
for(i in 1:S){
	ranking=order(sapply(parameters,rnorm,n=1))-1
	string=paste(ranking,collapse="<")
	if(string %in% names(rankings)){
		rankings[string]=rankings[string]+1
	}
	else{
		rankings=c(rankings,1)
		names(rankings)[length(rankings)]=string
	}
}
rankings=rankings/sum(rankings)
if(length(rankings)==1)
	cat(names(rankings)," : ",rankings,"\n") else
	for(i in seq(rankings))
 		cat(names(rankings)[i]," : ",rankings[i],"\n")
