#include<stdlib.h>
#include<stdio.h>
#include<string.h>

#define uch unsigned char
#define ui unsigned int

static uch(*permblock)[8]; //holds all permutation of 8 elts
static uch(*xgraph)[8];
static uch(*mod_xgraph)[8];

void fillpermblock(uch *perm,int len)
	/* fill permblock with all permutations of eight elements.  
	   (recursive definition)  */
{
	if(len==1) 
	{
		memcpy(*permblock++,perm-7,8);
		return;
	}
	int i;
	char s;
	fillpermblock(perm+1,len-1);
	for(i=1;i<len;i++)
	{
		s=perm[0];
		perm[0]=perm[i];
		perm[i]=s;
		fillpermblock(perm+1,len-1);
		s=perm[0];
		perm[0]=perm[i];
		perm[i]=s;
	}
}	

/* cube symmetries */
ui symelt(uch n,uch sigma,uch tau,uch xoring){
	uch A,B;
	n &= 0x7; //mask just in case
	/* 3-cycle */ 
	for(A=0;A<sigma;A++){
		B=n&0x1;
		n &= 0x6;
		n >>= 1;
		n += (B<<2);
	}
	/* flip */
	if(tau){
		A=n&0x1;
		B=n&0x2;
		n &= 0x4;
		n += (A<<1) + (B>>1);
	}
	/* xor op */
	n ^= xoring;
	return n;
}

/* Makes a directed graph matrix from interger encoding of graph */
void int2graph(ui n,uch (*Xgraph)[8]){
	bzero(Xgraph,8*8*sizeof(char));
	uch pos,sect,A,B;
	for(pos=0;pos<3;pos++){
		for(sect=0;sect<4;sect++){
			A=((1<<pos)-1)&sect;
			B=sect-A;
			B <<= 1;
			if(n&0x1){
				Xgraph[B+(1<<pos)+A][B+A]=1;
			}
			else{
				Xgraph[B+A][B+A+(1<<pos)]=1;
			}
			n >>= 1;
		}
	}
}

/* Inverse of previous function */
ui graph2int(uch (*Xgraph)[8]){
	ui n=0,pos,sect,A,B,bit=1;
	for(pos=0;pos<3;pos++){
		for(sect=0;sect<4;sect++){
			A=((1<<pos)-1)&sect;
			B=sect-A;
			B <<= 1;
			if(Xgraph[B+(1<<pos)+A][B+A]==1){
				n+=bit;
			}
			bit <<= 1;
		}
	}
	return n;
}

/* Checks that graph (encoded by integer) is compatible with a given 
   linear order */
uch IsCompat(ui n,uch *perm){
	uch pos,sect,low,high,A,B;
	for(pos=0;pos<3;pos++)
		for(sect=0;sect<4;sect++){
			A = sect&((1<<pos)-1);
			B = sect - A;
			B <<= 1;
			if(n&1){
				low = B+(1<<pos)+A;
				high = B+A;
			}
			else{
				low = B+A;
				high=B+(1<<pos)+A;
			}
			for(A=0;perm[A]!=low;A++){
				if(perm[A]==high) return 0;
			}
			n >>= 1;
		}
	return 1;
}

/* Checks that a graph has no cycles (ie a partial order) */
uch IsPartialOrder(ui n){
	int i;
	uch (*permblock0)[8]=permblock;
	for(i=0;i<40320;i++){
		if(IsCompat(n,*permblock0++)) return 1;
	}
	return 0;
}

/* Write out a file with graphs adjacency matrix */
void matrixify(ui n)
{
	char name[8];
	char num[8];
#ifdef FILTER
	strcpy(name,"mats");
#else
	strcpy(name,"mat");
#endif
	sprintf(num,"%03x",n);
	FILE *stream = fopen(strcat(name,num),"w");
	uch mat[8][8],pos,sect,A,B;
	bzero(mat,64*sizeof(char));
	int i,j;
	for(pos=0;pos<3;pos++)
		for(sect=0;sect<4;sect++){
			A=sect&((1<<pos)-1);
			B=sect-A;
			B <<= 1;
			if(n&1)
				mat[B+(1<<pos)+A][B+A]=1;
			else mat[B+A][B+(1<<pos)+A]=1;	
			n >>= 1;
		}	
	for(i=0;i<8;i++)
	{
		for(j=0;j<7;j++)
			fprintf(stream,"%d ",mat[i][j]);
		fprintf(stream,"%d\n",mat[i][7]);
	}
	fclose(stream);
}

/* Check that dyck condition holds */
inline int dyck_check(uch* perm)
{
	/* Is the number evil or odious?
	 * ;-) */
	char *table="\0\1\1\0\1\0\0\1";
	int sum=0;
	int
		i,sign=(table[(ui)perm[0]])?1:-1;
	for(i=0;i<8;i++)
	{
		sum+=sign*((table[(ui)*perm++])?1:-1);
		if(sum
				<
				0)
			return
				0; 
		/* more of the wrong one than
		 * the other
		 so fail
		 */
	}	
	/* else passes test */
	return 1;
}

int main(void)
{
	int i,j,k,t;
	uch perm[8],sigma,tau,xoring;

	/*set permblock */
	permblock=(uch (*)[8])calloc(40320,8*sizeof(char));
	for(i=0;i<8;i++)
		perm[i]=i;
	fillpermblock(perm,8);
	permblock-=40320;

	/* Pick out one from each isomorphism class */ 
	ui * IsoRep = malloc(0x1000*sizeof(int));
	ui *IsoRep0 = IsoRep;
	uch *checkbox = calloc(0x1000,sizeof(char));
	xgraph = malloc(8*8*sizeof(char));
	mod_xgraph=malloc(8*8*sizeof(char));
	for(i=0;i<0x1000;i++){
		if(0x111&i || !IsPartialOrder(i))
			checkbox[i]=1;
		if(checkbox[i]==1) continue;
		*IsoRep0++ = i;
		int2graph(i,xgraph);
		for(sigma=0;sigma<3;sigma++)
			for(tau=0;tau<2;tau++)
				for(xoring=0;xoring<8;xoring++){
					for(j=0;j<8;j++)
						for(k=0;k<8;k++)
							mod_xgraph[symelt(j,sigma,tau,xoring)]
								[symelt(k,sigma,tau,xoring)] = 
								xgraph[j][k];
					t=graph2int(mod_xgraph);
					if(t!=i) checkbox[t]=1;
				}	
	}
	*IsoRep0=0xffffffff;
	/* Print out classes */
	for(;*IsoRep!=0xffffffff;IsoRep++){
#ifdef FILTER
		/* Print out special classes */
		for(i=0;i<40320;i++){
			if(IsCompat(*IsoRep,permblock[i]) &&
					!dyck_check(permblock[i]))
				goto End;	
		}
#endif
		matrixify(*IsoRep);
		printf("%03x\n",*IsoRep);
#ifdef FILTER
End:;
#endif
	}
	return 0;
}
