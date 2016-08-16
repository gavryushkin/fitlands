#!/usr/bin/Rscript 
#options(digits=21)

argv=commandArgs(TRUE)
if(length(argv)!=2){
	write("Two files as arguments; empirical data and initial parameters.",stderr())
	q(status=1)
}

data=scan(argv[1],quiet=TRUE)
parameters=scan(argv[2],quiet=TRUE)

# N==number of genotypes
N=length(parameters)+1
if(length(data)!=N*N){
	write("Contradicting sizes of data and parameters",stderr())
	q(status=1)
}

data = matrix(data,ncol=N,nrow=N,byrow=TRUE)
sqrt2=sqrt(2)

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
			F=F+data[i,j]*log(pnorm(q[i]-q[j],sd=sqrt2))
		}
	}	
	#nlm _minimizes_, so we take negative of result.
	return (-F)
}

# print out _all_ warnings
options(warn=1)
optParameters=nlm(likfun,parameters,print.level=0)$estimate

# print out parameters in first line of output
optParameters=c(0,optParameters)
cat("Parameters:",optParameters,"\n")

# print out parameter rank order
cat(paste(order(optParameters)-1,collapse="<")," : ","Parameter rank order\n\n")

rankings=c()

#Sample size S.  Samples based on parameters derived from maximum likelihood.
#Tallies proportion of each rank order which occurs.
S=10000
for(i in 1:S){
	ranking=order(sapply(optParameters,rnorm,n=1))-1
	string=paste(ranking,collapse="<")
	if(string %in% names(rankings)){
		rankings[string]=rankings[string]+1
	}
	else{
		rankings=c(rankings,1)
		names(rankings)[length(rankings)]=string
	}
}

cat("Sampling based rankings\n")
rankings=sort(rankings,decreasing=TRUE)
rankings=rankings/sum(rankings)
if(length(rankings)==1)
	cat(names(rankings)," : ",rankings,"\n") else
	for(i in seq(rankings))
 		cat(names(rankings)[i]," : ",rankings[i],"\n")
