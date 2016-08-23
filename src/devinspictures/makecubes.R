#!/usr/bin/Rscript
require("diagram")
argv=commandArgs(TRUE);
filter_true=length(argv)!=0 && argv[1]=="FILTER"
if(filter_true) setwd("special20") else setwd("all54")
pattern = if(filter_true) "mats" else "mat(?=[^s])"
count=1
for(f in grep(paste0("^",pattern),dir(),value=TRUE,perl=TRUE))
{
	if(length(grep("mats",dir("../special20")))==0){
		write("Please fill up \"special20\" with matrices, first",stderr())
		q(status=1)
	}
	s=filter_true || (sub("mat(?=[^s])","mats",f,perl=T)%in%dir("../special20"))
	if(s){
		cat(count," ",f," in special20\n")
		count <- count+1
	}
	A <- matrix(scan(f,quiet=T),ncol=8,nrow=8,byrow=FALSE,
			dimnames=list(c("000","001","010","011","100",
					"101","110","111"),
				c("000","001","010","011","100",
					"101","110","111")))
		A. <- matrix(c( 0.0,0.8,0.7,0.0,0.8,0.0,0.0,0.0,
					0.8,0.0,0.0,0.7,0.0,0.8,0.0,0.0,
					0.7,0.0,0.0,0.8,0.0,0.0,0.8,0.0,
					0.0,0.7,0.8,0.0,0.0,0.0,0.0,0.8,
					0.8,0.0,0.0,0.0,0.0,0.8,0.7,0.8,
					0.0,0.8,0.0,0.0,0.8,0.7,0.0,0.7,
					0.0,0.0,0.8,0.0,0.7,0.0,0.0,0.8,
					0.0,0.0,0.0,0.8,0.8,0.7,0.8,0.0),nrow=8,ncol=8,
				dimnames=list(c("000","001","010","011","100",
						"101","110","111"),
					c("000","001","010","011","100",
						"101","110","111")))
		name <-
		c("111","110","101","011","100","010","001","000")
		pos <-
		c(1, 3, 3, 1)
		file <- paste(sub(pattern,if(filter_true) "cubes" else "cube",f,perl=TRUE),".eps",sep="") 
		setEPS(horizontal=FALSE,onefile=FALSE,paper="special")
		postscript(file,height = 2.9, width = 2.9)
		op <- par(mar = rep(0,4))
		txt.col<-arr.lcol<-arr.col<-lcol<-if(s) "red" else "black"
		plotmat(A[name,name], pos, curve = 0, name,
				box.size = 0.07,segment.from=0.1,
				endhead=T,shadow.size = 0,arr.col=arr.col,
				arr.pos = A.[name,name],lcol=lcol,txt.col=txt.col,
				cex.txt = 0.1,box.cex=1.1,arr.length=0.8
			   )
		dev.off()
}
