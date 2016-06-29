require("diagram")
for(f in grep("^mats",dir(),value=TRUE))
{
	A <- matrix(scan(f),ncol=8,nrow=8,byrow=FALSE,
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
		file <- paste(sub("mats","cubes",f),".ps",sep="") 
		setEPS(horizontal=FALSE,onefile=FALSE,paper="special")
		postscript(file,height = 2.9, width = 2.9)
		op <- par(mar = rep(0,4))
		on.exit(par(op))
		plotmat(A[name,name], pos, curve = 0, name,
				box.size = 0.07,segment.from=0.1,
				endhead=T,shadow.size = 0,
				arr.pos = A.[name,name],
				cex.txt = 0.1,box.cex=1.1,arr.length=0.8
			   )
		dev.off()
}
