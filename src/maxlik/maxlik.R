#!/usr/bin/Rscript 
#options(digits=21)

#Command line args used as initial point in optimization below
argv=commandArgs(TRUE)
argc=length(argv)
N=argc+1 # number of elements
if(N==1){
	write("Error: No command line arguments?  Sure about that?",stderr())
	q(status=1)
}
sqrt2=sqrt(2)

#load the comparison data as a matrix
file=file("stdin","r")
data = scan(file,quiet=TRUE)
	# Correct number of command line arguments?
if(length(data) != N*N){
	write("Error: Command line arguments should be one less than number of genotypes",file=stderr())
	q(status=2)
}
M = matrix(data,ncol=N,nrow=N,byrow=TRUE)
close(file)

#maximum likelihood function
likfun<-function(p,...){
	if(length(p)!=N-1) q(status=2)
	range=seq(length(p)+1)
	#shift to include zero at start
	q=numeric(N)
	q[1]=0
	q[2:N]=p
	F=0
	for(i in range){
		for(j in range){
			if(i==j) next
			F=F+M[i,j]*log(pnorm(q[i]-q[j],sd=sqrt2))
		}
	}	
	#nlm _minimizes_, so we take negative of result
	return (-F)
}

Ini=as.numeric(argv)

# print out _all_ warnings
options(warn=1)
estimate=nlm(likfun,Ini,print.level=0)$estimate
# print out parameters in first line of output
parameters=c(0,estimate)
cat("Parameters:",parameters,"\n")

rankings=c()

#Sample size S.  Samples based on parameters derived from maximum likelihood.
#Tallies proportion of each rank order which occurs.
S=10000
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
rankings=sort(rankings,decreasing=TRUE)
rankings=rankings/sum(rankings)
if(length(rankings)==1)
	cat(names(rankings)," : ",rankings,"\n") else
	for(i in seq(rankings))
 		cat(names(rankings)[i]," : ",rankings[i],"\n")
