#!/usr/bin/Rscript
file=file("stdin","r")
para=scan(file,quiet=TRUE)
close(file)

nelts=length(para)
results=matrix(0,ncol=nelts,nrow=nelts)

S=1000
for(i in 1:S){
	pair=sample(seq(para),size=2)
	if(rnorm(1,para[pair[1]])>rnorm(1,para[pair[2]])) results[pair[1],pair[2]]=results[pair[1],pair[2]]+1 else
	results[pair[2],pair[1]]=results[pair[2],pair[1]]+1
}

for(i in seq(nelts)){
	cat(results[i,],"\n")
}

write(t(results),file=stderr(),ncolumns=nrow(results)
